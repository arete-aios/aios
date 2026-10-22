#!/usr/bin/env python3
"""One keyless PageSpeed API query; errors recorded, no automatic retry.
Lighthouse lab results are separate from field Core Web Vitals. No API key is read.
"""
import argparse,datetime,json,urllib.request,urllib.error
from urllib.parse import urlencode
from zoneinfo import ZoneInfo
from audit import public_url,save_new
def query(url,strategy):
    public_url(url)
    api="https://www.googleapis.com/pagespeedonline/v5/runPagespeed?"+urlencode({"url":url,"strategy":strategy,"category":"performance"})
    stamp=datetime.datetime.now(ZoneInfo("Europe/Riga")).isoformat()
    try:
        with urllib.request.urlopen(api,timeout=70) as r:
            raw=r.read(8_000_001)
            if len(raw)>8_000_000:raise ValueError("PageSpeed response exceeds bound")
            data=json.loads(raw)
        lh=data.get("lighthouseResult",{});audits=lh.get("audits",{})
        return {"schema":"geo7-performance/v1","status":"observed","timestamp_riga":stamp,"site":url,"strategy":strategy,
            "lab":{"lighthouse_version":lh.get("lighthouseVersion"),"fetch_time":lh.get("fetchTime"),"final_url":lh.get("finalUrl"),
            "performance_score":lh.get("categories",{}).get("performance",{}).get("score"),
            "metrics":{k:{f:audits.get(k,{}).get(f) for f in ["numericValue","numericUnit","displayValue"]}
              for k in ["largest-contentful-paint","cumulative-layout-shift","total-blocking-time","first-contentful-paint"]}},
            "field":data.get("loadingExperience"),"origin_field":data.get("originLoadingExperience"),
            "scope":"One lab sample; field metrics may be unavailable. TBT is not field INP."}
    except urllib.error.HTTPError as e:
        return {"schema":"geo7-performance/v1","status":"unavailable","timestamp_riga":stamp,"site":url,"strategy":strategy,
          "http_status":e.code,"error":"PageSpeed API refused request; no key or automatic retry","scope":"No performance measurement obtained"}
    except Exception as e:
        return {"schema":"geo7-performance/v1","status":"unavailable","timestamp_riga":stamp,"site":url,"strategy":strategy,
            "error":type(e).__name__,"scope":"No performance measurement obtained"}
def main():
    p=argparse.ArgumentParser();p.add_argument("url");p.add_argument("--strategy",choices=["mobile","desktop"],default="mobile")
    p.add_argument("--out",required=True);a=p.parse_args();value=query(a.url,a.strategy);save_new(a.out,value)
    print(json.dumps({"out":a.out,"status":value["status"],"http_status":value.get("http_status")}))
if __name__=="__main__":main()
