#!/usr/bin/env python3
"""Evidence-based audit report. Never converts unmeasured data into a GEO score."""
import argparse,collections,datetime,html,json,re,base64
from pathlib import Path
from zoneinfo import ZoneInfo
from audit import save_new
from report_detail import enrich,render_html,markdown_detail
def unwrap(reply):
    if not reply.get("ok",False):return {"_error":"broker refused or failed"}
    result=reply.get("result",{})
    if result.get("isError"):return {"_error":"provider returned error"}
    for block in result.get("content",[]):
        if block.get("type")=="text":
            try:
                v=json.loads(block["text"])
                if isinstance(v,dict):return v
            except (ValueError,TypeError):pass
    return {"_error":"no parseable provider payload"}
def table(data):
    dims=[x["name"] for x in data.get("dimensionHeaders",[])]
    mets=[x["name"] for x in data.get("metricHeaders",[])]
    out=[]
    for row in data.get("rows",[]):
        v={k:x.get("value") for k,x in zip(dims,row.get("dimensionValues",[]))}
        for k,x in zip(mets,row.get("metricValues",[])):
            try:v[k]=float(x["value"])
            except (KeyError,ValueError):v[k]=None
        out.append(v)
    return out
def analyze(crawl,native=None,performance=None):
    pages=crawl["pages"];findings=[];checks=[]
    def finding(id,priority,title,evidence,action,owner="Growth lead"):
        findings.append(dict(id=id,priority=priority,title=title,evidence=evidence,action=action,owner=owner))
    for p in pages:
        issues=[]
        if p["status"]!=200:issues.append("HTTP "+str(p["status"]))
        if p["noindex"]:issues.append("noindex")
        if not p["title"]:issues.append("title missing")
        if not p["meta"].get("description"):issues.append("description missing")
        if p["h1_count"]!=1:issues.append("H1 count "+str(p["h1_count"]))
        if not p["canonical"]:issues.append("canonical missing")
        if p["jsonld_invalid"]:issues.append("invalid JSON-LD")
        if issues:finding("page-"+str(len(findings)+1),"P1" if p["noindex"] or p["status"]!=200 else "P2",
            "Lapas tehniskā pārbaude",{"url":p["url"],"observed":issues},"Pārbaudīt un sagatavot labojumu konkrētajai lapai.","Web developer")
    duplicates=collections.defaultdict(list)
    for p in pages:duplicates[p["title"]].append(p["url"])
    for title,urls in duplicates.items():
        if title and len(urls)>1:finding("duplicate-title-"+str(len(findings)),"P2","Vienādi title pārbaudītajās lapās",{"title":title,"urls":urls},"Izvērtēt atšķirīgu meklēšanas nodomu un unikālus virsrakstus.")
    if pages and all(not p["schema_types"] for p in pages):
        finding("entity-schema","P2","Nav JSON-LD pārbaudītajās lapās",{"page_count":len(pages),"urls":[p["url"] for p in pages]},
          "Sagatavot Organization/Person/WebSite marķējuma projektu no redzamajiem faktiem. Tas nav obligāts AI redzamības nosacījums.","Web developer")
    for p in pages:
        levels=[h["level"] for h in p["headings"]]
        if any(b>a+1 for a,b in zip(levels,levels[1:])):
            finding("heading-order-"+str(len(findings)),"P3","Pārbaudīt virsrakstu hierarhiju",{"url":p["url"],"levels":levels},"Saskaņot sadaļu hierarhiju, saglabājot satura nozīmi.")
    connectors={};channels=[];events=[];keywords=[];period={}
    for op in (native or {}).get("operations",[]):
        v=unwrap(op["result"]);name=op["name"]
        if name=="gsc-sites":
            entries=v.get("data",{}).get("siteEntry",[])
            # Keep only the audited site's property; other account properties are not the report's scope.
            matching=[x for x in entries if x.get("siteUrl") in ("sc-domain:"+urlparse_host(crawl["site"]),crawl["site"],crawl["site"]+"/")]
            connectors["gsc-property"]={"status":"observed" if matching else "unknown","matching_property":matching}
        elif name.startswith("gsc-"):
            data=v.get("data",{});rows=data.get("rows",[])
            connectors[name]={"status":"unavailable" if "_error" in v else ("observed" if rows else "empty"),
                "returned_rows":len(rows),"rows":rows,"period":{k:op["arguments"].get(k) for k in ["start_date","end_date"]}}
        elif name.startswith("ga4-"):
            vals=table(v.get("data",{}))
            connectors[name]={"status":"unavailable" if "_error" in v else "observed","returned_rows":len(vals),"rows":vals}
            period={k:op["arguments"].get(k) for k in ["start_date","end_date"]}
            if name=="ga4-channels":channels=vals
            if name=="ga4-events":events=vals
        elif name=="keyword-ideas":
            keywords=[{k:row.get(k) for k in ["keyword","average_monthly_searches","competition"]} for row in v.get("rows",[])]
            connectors[name]={"status":"unavailable" if "_error" in v else "observed","returned_rows":len(keywords),
              "market":{"geo_target_ids":op["arguments"].get("geo_target_ids"),"language_id":op["arguments"].get("language_id")},"geo_target_ids":op["arguments"].get("geo_target_ids"),"language_id":op["arguments"].get("language_id"),
              "first_page_only":True,"has_more":v.get("has_more"),"api_fee":v.get("api_fee")}
    if any(x.get("status")=="empty" for k,x in connectors.items() if k.startswith("gsc-") and k!="gsc-property"):
        finding("gsc-baseline","P1","Search Console atbilde bez veiktspējas rindām",
          {k:x for k,x in connectors.items() if k in ["gsc-queries","gsc-pages"]},
          "Pēc datu apstrādes atkārtot tā paša perioda pārbaudi; tukša atbilde nepierāda nulles trafiku vai indeksācijas problēmu.")
    organic=sum(x.get("sessions",0) or 0 for x in channels if x.get("sessionSourceMedium")=="google / organic") if channels else None
    ai_paid=sum(x.get("sessions",0) or 0 for x in channels if x.get("sessionSourceMedium")=="chatgpt / paid") if channels else None
    if channels:
        finding("organic-baseline","P2","Organiskās piesaistes bāzes līnija",{"period":period,"google_organic_sessions":organic,"chatgpt_paid_sessions":ai_paid},
          "Mērīt organiskās sesijas atsevišķi no reklāmām; chatgpt / paid nav AI meklēšanas citējuma pierādījums.")
    if events:
        selected=[x for x in events if x.get("eventName") in ["generate_lead","sign_up","fit_call_click","whatsapp_clicked"]]
        finding("qualification-measurement","P1","Notikumi vēl nepierāda kvalificētas sarunas",
          {"period":period,"events":selected},"Savienot pieprasījumu ar vienu CRM sarunu un kvalifikācijas rezultātu; klikšķi/reģistrācijas nav sarunu skaits.")
    if keywords:
        relevant=keywords[:20]
        finding("keyword-intent","P2","Atslēgvārdu nodomu atlase",{"market":connectors.get("keyword-ideas",{}).get("market"),"first_page_only":True,"selected":relevant},
          "Atlasīt uzņēmēja problēmu un nodomu pirms satura radīšanas. Google Ads competition ir reklāmu konkurence, ne SEO difficulty.")
    if performance and performance.get("status")!="observed":
        finding("performance-unknown","P2","Lapas ātruma mērījums nav iegūts",performance,"Veikt atļautu PageSpeed/Lighthouse/CrUX mērījumu; HTTP atbildes laiku nesaukt par Core Web Vitals.","Web developer")
    checks=[
      {"name":"Publiskās lapas","result":str(len(pages)),"detail":"HTTP paraugs; nav visas vietnes rendera"},
      {"name":"Sitemap","result":str(len(crawl.get("sitemap_urls",[]))),"detail":"atrasto URL skaits"},
      {"name":"Title / H1 / canonical","result":str(sum(bool(p["title"]) and p["h1_count"]==1 and bool(p["canonical"]) for p in pages))+"/"+str(len(pages)),"detail":"tehnisko elementu klātbūtne"},
      {"name":"AI atbilžu novērojumi","result":"Nav mērīti","detail":"nav citējumu/rekomendāciju vērtējuma"}]
    result={"schema":"geo7-report/v1","site":crawl["site"],"timestamp_riga":datetime.datetime.now(ZoneInfo("Europe/Riga")).isoformat(),
      "goal":"Kvalificētas uzņēmēju sarunas no organiskās un AI meklēšanas.",
      "scope":crawl["scope"],"checks":checks,"pages":pages,"findings":findings,"connectors":connectors,
      "analytics":{"period":period,"channels":channels,"events":events,"google_organic_sessions":organic,"chatgpt_paid_sessions":ai_paid},
      "keyword_ideas":keywords,"performance":performance,"crawl_errors":crawl.get("errors",[]),
      "remaining":["Satura/konkurentu izvērtējums ar konkrētiem avotiem","AI atbilžu atkārtojami novērojumi","Vietnes izmaiņu ieviešana un pirms/pēc mērījums"],
      "source_files":[],"status":"INITIAL_AUDIT_COMPLETE; NOT_ALL_WORKFLOW_STAGES_EXECUTED" if pages else "AUDIT_BLOCKED_OR_EMPTY; NO_SUCCESSFUL_PAGE_SAMPLE"}
    return enrich(result,crawl)
def urlparse_host(url):
    from urllib.parse import urlparse
    return urlparse(url).hostname
def markdown(v):
    return markdown_detail(v)
def html_report(v):
    return render_html(v,Path(__file__).resolve().parents[1])
def main():
    p=argparse.ArgumentParser();p.add_argument("--crawl",required=True);p.add_argument("--native");p.add_argument("--performance");p.add_argument("--keyword-source");p.add_argument("--out-prefix",required=True);a=p.parse_args()
    source_paths=[x for x in [a.crawl,a.native,a.performance,a.keyword_source] if x]
    prefix=Path(a.out_prefix)
    for ext in [".json",".md",".html"]:
        if Path(str(prefix)+ext).exists():p.error("Existing report will not be overwritten")
    crawl_data=json.loads(Path(a.crawl).read_text())
    native_data=json.loads(Path(a.native).read_text()) if a.native else None
    keyword_data=json.loads(Path(a.keyword_source).read_text()) if a.keyword_source else None
    if keyword_data:
        if native_data is None:native_data={"operations":[]}
        for op in keyword_data.get("operations",[]):
            if op.get("name")=="keyword-ideas" and not any(x.get("name")=="keyword-ideas" for x in native_data["operations"]):native_data["operations"].append(op)
    v=analyze(crawl_data,native_data,json.loads(Path(a.performance).read_text()) if a.performance else None)
    v["native_observed_at"]=native_data.get("timestamp_riga") if native_data else None
    v["keyword_observed_at"]=keyword_data.get("timestamp_riga") if keyword_data else (native_data.get("timestamp_riga") if native_data else None)
    v["report_version"]="1.1.0"
    v["source_files"]=source_paths
    save_new(str(prefix)+".json",v)
    for ext,text in [(".md",markdown(v)),(".html",html_report(v))]:
        with Path(str(prefix)+ext).open("x") as f:f.write(text)
    print(json.dumps({"report":str(prefix),"findings":len(v["findings"]),"status":v["status"]}))
if __name__=="__main__":main()
