#!/usr/bin/env python3
"""Create bounded DataForSEO query plans for keyword and competitor research.
Planner makes ZERO API calls. Location/language required; paid execution needs explicit provider permission and budget.
Domain-gap request adapted from ReScienceLab/opc-skills (Apache-2.0); see THIRD-PARTY.md.
"""
import argparse,json,re
from urllib.parse import urlparse
from audit import save_new

READ_TOOLS={"google_workspace__analytics_read","google_workspace__search_console_read",
 "marketing_legacy__keyword_ideas","dataforseo__api_request"}
BASELINE={"google_workspace__analytics_read","google_workspace__search_console_read"}
def validate(ops):
    if not isinstance(ops,list) or not 1<=len(ops)<=8:raise ValueError("1..8 bounded operations required")
    for op in ops:
        if op.get("tool") not in READ_TOOLS:raise ValueError("Only declared GEO7 readers supported")
        if not isinstance(op.get("arguments"),dict):raise ValueError("arguments object required")
        if op["tool"]=="dataforseo__api_request":
            a=op["arguments"];path=a.get("path","")
            allowed=["/v3/appendix/user_data","/v3/dataforseo_labs/google/ranked_keywords/live",
              "/v3/dataforseo_labs/google/competitors_domain/live","/v3/dataforseo_labs/google/domain_intersection/live",
              "/v3/serp/google/organic/live/regular"]
            if path not in allowed or a.get("url"):raise ValueError("Undeclared API path or transport override")
            if path!="/v3/appendix/user_data" and a.get("method")!="POST":raise ValueError("Query must be POST")
            if path=="/v3/appendix/user_data" and a.get("method")!="GET":raise ValueError("User-data GET only")

def domain(s):
    p=urlparse(s if "://" in s else "https://"+s)
    if p.username or p.password or p.port or p.query or not p.hostname or "." not in p.hostname:
        raise ValueError("Public domain required")
    return p.hostname.removeprefix("www.").lower()
def plan(site,keyword,location,language,competitor=None):
    if not isinstance(location,int) or location<=0 or not re.fullmatch(r"[a-z]{2}",language):raise ValueError("Valid market required")
    if not 1<=len(keyword)<=200 or re.search(r"\b(?:site|allinurl|allintitle|filetype):",keyword):raise ValueError("Plain bounded keyword required")
    host=domain(site);common={"location_code":location,"language_code":language}
    ops=[
      {"name":"ranked-keywords","tool":"dataforseo__api_request","arguments":{"method":"POST","path":"/v3/dataforseo_labs/google/ranked_keywords/live","data":[{"target":host,"limit":20,"item_types":["organic"],**common}]}},
      {"name":"search-competitors","tool":"dataforseo__api_request","arguments":{"method":"POST","path":"/v3/dataforseo_labs/google/competitors_domain/live","data":[{"target":host,"limit":5,"item_types":["organic"],**common}]}},
      {"name":"serp","tool":"dataforseo__api_request","arguments":{"method":"POST","path":"/v3/serp/google/organic/live/regular","data":[{"keyword":keyword,"depth":10,"device":"desktop",**common}]}}
    ]
    if competitor:
        ops.append({"name":"keyword-gap","tool":"dataforseo__api_request","arguments":{"method":"POST","path":"/v3/dataforseo_labs/google/domain_intersection/live","data":[{"target1":host,"target2":domain(competitor),"intersections":False,"limit":20,"item_types":["organic"],**common}]}})
    return {"schema":"geo7-research-plan/v1","site":host,"market":common,"status":"plan_not_executed","operations":ops,
        "api_calls_made":0,"maximum_results":65 if competitor else 45,"price":"operator review and task budget required before execution"}
def main():
    p=argparse.ArgumentParser();p.add_argument("site");p.add_argument("--keyword",required=True)
    p.add_argument("--location",type=int,required=True);p.add_argument("--language",required=True)
    p.add_argument("--competitor");p.add_argument("--out",required=True)
    a=p.parse_args()
    if not re.fullmatch(r"[a-z]{2}",a.language) or a.location<=0:p.error("Valid market required")
    if not 1<=len(a.keyword)<=200 or re.search(r"\b(?:site|allinurl|allintitle|filetype):",a.keyword):p.error("Plain bounded keyword required")
    save_new(a.out,plan(a.site,a.keyword,a.location,a.language,a.competitor))
    print(json.dumps({"out":a.out,"api_calls_made":0}))
if __name__=="__main__":main()
