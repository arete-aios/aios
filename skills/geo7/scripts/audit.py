#!/usr/bin/env python3
"""GEO7 public HTTP crawl. PageParser adapted from Staksoft (MIT); see THIRD-PARTY.md.
Raw HTTP observations are not a rendered-browser test, CWV, index status or AI citations.
"""
import argparse,datetime,hashlib,ipaddress,json,re,socket,time,urllib.error,urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin,urlparse,urldefrag
from urllib.robotparser import RobotFileParser
from zoneinfo import ZoneInfo

USER_AGENT="Arete-GEO7/1.0 (+https://areteaios.com)"
MAX_BYTES=2_000_000
def public_url(url):
    p=urlparse(url)
    if p.scheme not in ("http","https") or not p.hostname or p.username or p.password or p.port not in (None,80,443):
        raise ValueError("Public HTTP(S) URL required")
    addresses=socket.getaddrinfo(p.hostname,p.port or (443 if p.scheme=="https" else 80),type=socket.SOCK_STREAM)
    if not addresses or any(not ipaddress.ip_address(a[4][0]).is_global for a in addresses):
        raise ValueError("Non-public destination refused")
    return url
class SafeRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        public_url(newurl)
        return super().redirect_request(req,fp,code,msg,headers,newurl)
def fetch_url(url):
    public_url(url);start=time.monotonic()
    request=urllib.request.Request(url,headers={"User-Agent":USER_AGENT,"Accept":"text/html,application/xml,text/plain"})
    try:
        response=urllib.request.build_opener(SafeRedirect()).open(request,timeout=20)
    except urllib.error.HTTPError as e:
        response=e
    with response:
        raw=response.read(MAX_BYTES+1)
        if len(raw)>MAX_BYTES:raise ValueError("Response exceeded 2 MB bound")
        charset=response.headers.get_content_charset() or "utf-8"
        text=raw.decode(charset,errors="replace")
        return {"url":url,"final_url":response.geturl(),"status":response.code,
          "content_type":response.headers.get("Content-Type",""),
          "x_robots_tag":response.headers.get("X-Robots-Tag",""),
          "http_elapsed_seconds":round(time.monotonic()-start,3),
          "bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"body":text}
class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = None
        self._in_title = False
        self.meta = {}            # name/property -> content
        self.headings = []        # (level, text)
        self._heading_level = None
        self._heading_buf = []
        self.canonical = None
        self.robots = None
        self.images = 0
        self.images_with_alt = 0
        self.links_internal = 0
        self.links_external = 0
        self.jsonld_blocks = []
        self._in_jsonld = False
        self._jsonld_buf = []
        self.text_parts = []
        self._skip_text = 0       # inside script/style
        self.og_tags = 0
        self.twitter_tags = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key.lower()] = a.get("content", "")
                if key.lower().startswith("og:"):
                    self.og_tags += 1
                if key.lower().startswith("twitter:"):
                    self.twitter_tags += 1
        elif tag == "link" and (a.get("rel", "").lower() == "canonical"):
            self.canonical = a.get("href")
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._heading_level = int(tag[1])
            self._heading_buf = []
        elif tag == "img":
            self.images += 1
            if a.get("alt", "").strip():
                self.images_with_alt += 1
        elif tag == "a" and a.get("href"):
            self._classify_link(a["href"])
        elif tag in ("script", "style"):
            self._skip_text += 1
            if tag == "script" and a.get("type", "").lower() == "application/ld+json":
                self._in_jsonld = True
                self._jsonld_buf = []

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self._heading_level:
            self.headings.append((self._heading_level, re.sub(r"\s+", " ", "".join(self._heading_buf)).strip()))
            self._heading_level = None
        elif tag in ("script", "style"):
            self._skip_text = max(0, self._skip_text - 1)
            if tag == "script" and self._in_jsonld:
                self.jsonld_blocks.append("".join(self._jsonld_buf).strip())
                self._in_jsonld = False

    def handle_data(self, data):
        if self._in_title:
            self.title = (self.title or "") + data
        if self._heading_level is not None:
            self._heading_buf.append(data)
        if self._in_jsonld:
            self._jsonld_buf.append(data)
        if self._skip_text == 0 and not self._in_title:
            stripped = data.strip()
            if stripped:
                self.text_parts.append(stripped)

    def _classify_link(self, href):
        if href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
            return
        netloc = urlparse(href).netloc
        if netloc:
            self.links_external += 1
        else:
            self.links_internal += 1


class AuditParser(PageParser):
    def __init__(self,base):
        self.base=base;self.hrefs=[];self.hreflang=[];self.lang="";self.h1=[]
        super().__init__()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=="html":self.lang=a.get("lang","")
        if tag=="link" and "alternate" in a.get("rel","").lower().split() and a.get("hreflang"):
            self.hreflang.append({"lang":a["hreflang"],"url":urljoin(self.base,a.get("href",""))})
        super().handle_starttag(tag,attrs)
    def _classify_link(self,href):
        if href.startswith(("#","mailto:","tel:","javascript:")):return
        resolved=urldefrag(urljoin(self.base,href))[0]
        self.hrefs.append(resolved)
        if urlparse(resolved).netloc==urlparse(self.base).netloc:self.links_internal+=1
        else:self.links_external+=1
def schema_types(v):
    found=[]
    if isinstance(v,dict):
        t=v.get("@type",[])
        found.extend(t if isinstance(t,list) else [t])
        for val in v.values():found.extend(schema_types(val))
    elif isinstance(v,list):
        for val in v:found.extend(schema_types(val))
    return [x for x in found if isinstance(x,str) and x]
def inspect_page(row):
    p=AuditParser(row["final_url"]);p.feed(row["body"])
    types=[];invalid=[]
    for i,block in enumerate(p.jsonld_blocks):
        try:types.extend(schema_types(json.loads(block)))
        except (ValueError,TypeError) as e:invalid.append({"block":i,"error":str(e)[:120]})
    meta={k:v for k,v in p.meta.items() if k in ["description","robots","googlebot","og:title","og:description","og:image","viewport","author"]}
    robots=" ".join([meta.get("robots",""),meta.get("googlebot",""),row["x_robots_tag"]]).lower()
    return {k:v for k,v in row.items() if k!="body"}|{
        "title":(p.title or "").strip(),"meta":meta,"canonical":urljoin(row["final_url"],p.canonical) if p.canonical else None,
        "html_lang":p.lang,"hreflang":p.hreflang,"headings":[{"level":n,"text":t} for n,t in p.headings],
        "h1_count":sum(n==1 for n,_ in p.headings),
        "http_text_words":len(re.findall(r"\b\w+\b"," ".join(p.text_parts))),
        "text_excerpt":" ".join(p.text_parts)[:1400],
        "internal_links":p.links_internal,"external_links":p.links_external,"hrefs":p.hrefs,
        "schema_types":sorted(set(types)),"jsonld_blocks":len(p.jsonld_blocks),"jsonld_invalid":invalid,
        "noindex":bool(re.search(r"(?:^|[,\s])(?:noindex|none)(?:$|[,\s])",robots)),
        "images":p.images,"images_without_nonempty_alt":p.images-p.images_with_alt,
        "has_table":bool(re.search(r"<table\b",row["body"],re.I))}
def normal(url,origin):
    u=urlparse(urldefrag(urljoin(origin,url))[0])
    if u.scheme not in ("http","https") or u.netloc!=urlparse(origin).netloc or u.query:return None
    if any(u.path==s or u.path.startswith(s+"/") for s in ["/my","/my-panel","/kit","/checkout","/test","/testchat","/unsubscribe","/thank-you","/TEST-STORE"]):return None
    if re.search(r"\.(?:pdf|png|jpe?g|svg|woff2?|js|css|mp4|zip)$",u.path,re.I):return None
    return u._replace(path=u.path or "/").geturl()
def crawl(url,max_pages=15):
    if not 1<=max_pages<=30:raise ValueError("max_pages must be 1..30")
    public_url(url);base=urlparse(url);origin=base.scheme+"://"+base.netloc
    stamp=datetime.datetime.now(ZoneInfo("Europe/Riga")).isoformat()
    errors=[];observations=[];raw=[]
    robots=None;rp=None
    try:
        robots=fetch_url(origin+"/robots.txt");raw.append(robots)
        if robots["status"]==200:
            rp=RobotFileParser();rp.parse(robots["body"].splitlines())
    except Exception as e:errors.append({"url":origin+"/robots.txt","error":str(e)})
    # Unknown/non-404 robot state does not authorize a crawl.
    if robots is None or robots["status"] not in (200,404):
        return {"schema":"geo7-crawl/v1","site":origin,"timestamp_riga":stamp,"pages":[],"errors":errors,
          "raw":raw,"scope":"blocked: robots unavailable","sitemap_urls":[],"robots":robots}
    sitemaps=[origin+"/sitemap.xml"]
    if robots["status"]==200:
        sitemaps=re.findall(r"(?im)^sitemap:\s*(\S+)",robots["body"]) or sitemaps
    site_urls=[];sitemap_evidence=[]
    for sm in list(dict.fromkeys(sitemaps))[:3]:
        if normal(sm,origin) is None:continue
        try:
            response=fetch_url(sm);raw.append(response)
            if response["status"]!=200:raise ValueError("sitemap HTTP "+str(response["status"]))
            root=ET.fromstring(response["body"])
            locations=[el.text.strip() for el in root.iter() if el.tag.rsplit("}",1)[-1]=="loc" and el.text]
            if root.tag.rsplit("}",1)[-1]=="sitemapindex":
                # Bounded nested sitemap discovery, never unlimited recursion.
                for nested in locations[:2]:
                    if normal(nested,origin) is None:continue
                    child=fetch_url(nested);raw.append(child)
                    croot=ET.fromstring(child["body"])
                    site_urls.extend(el.text.strip() for el in croot.iter() if el.tag.rsplit("}",1)[-1]=="loc" and el.text)
            else:site_urls.extend(locations)
            sitemap_evidence.append({k:v for k,v in response.items() if k!="body"})
        except Exception as e:errors.append({"url":sm,"error":str(e)})
    queue=list(dict.fromkeys([normal(url,origin)]+[normal(x,origin) for x in site_urls]))
    queue=[x for x in queue if x];seen=set();skipped=[]
    while queue and len(observations)<max_pages and len(seen)<max_pages*3:
        page=queue.pop(0)
        if page in seen:continue
        seen.add(page)
        if rp and not rp.can_fetch(USER_AGENT,page):
            skipped.append({"url":page,"reason":"robots disallow"});continue
        try:
            response=fetch_url(page);raw.append(response)
            if normal(response["final_url"],origin) is None:
                errors.append({"url":page,"error":"Redirect left permitted site or entered excluded route"});continue
            if "text/html" not in response["content_type"]:
                errors.append({"url":page,"error":"Non-HTML response","status":response["status"]});continue
            observation=inspect_page(response);observations.append(observation)
            for link in observation["hrefs"]:
                child=normal(link,origin)
                if child and child not in seen and child not in queue:queue.append(child)
        except Exception as e:errors.append({"url":page,"error":str(e)})
        time.sleep(.2)
    robot_access={}
    for bot in ["Googlebot","Bingbot","OAI-SearchBot","GPTBot","PerplexityBot","ClaudeBot"]:
        robot_access[bot]=rp.can_fetch(bot,url) if rp else None
    return {"schema":"geo7-crawl/v1","site":origin,"timestamp_riga":stamp,
        "pages":observations,"errors":errors,"skipped":skipped,"robots":{k:v for k,v in robots.items() if k!="body"},
        "robot_advisory":robot_access,"sitemap_urls":list(dict.fromkeys(site_urls)),"sitemaps":sitemap_evidence,
        "raw":raw,"scope":"public raw HTTP sample; no browser render, CWV, index or AI answer test"}
def save_new(path,value):
    p=Path(path).resolve()
    root=Path.cwd().resolve()
    if not p.is_relative_to(root):raise ValueError("Output must remain inside the explicitly selected current working directory")
    if p.exists():raise ValueError("Existing evidence will not be overwritten")
    if not p.parent.is_dir():raise ValueError("Create the output directory before writing")
    with p.open("x") as f:json.dump(value,f,ensure_ascii=False,indent=2);f.write("\n")
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("url");ap.add_argument("--max-pages",type=int,default=15);ap.add_argument("--out",required=True)
    a=ap.parse_args();value=crawl(a.url,a.max_pages);save_new(a.out,value)
    print(json.dumps({"out":a.out,"pages":len(value["pages"]),"errors":len(value["errors"]),"scope":value["scope"]}))
if __name__=="__main__":main()
