#!/usr/bin/env python3
"""Aggregate observed AI answers. Absence of measurement is not absence of visibility."""
import argparse,collections,json
from pathlib import Path
from audit import save_new
def summarize(rows):
    seen=set();buckets=collections.defaultdict(list)
    for r in rows:
        required=["prompt_id","engine","model","market","observed_at","run_id","answer_source","status"]
        if any(not r.get(x) for x in required):raise ValueError("Every row needs prompt/engine/model/market/time/run/evidence/status")
        key=tuple(r[x] for x in ["prompt_id","engine","model","market","run_id"])
        if key in seen:raise ValueError("Duplicate observation")
        seen.add(key)
        if r["status"] not in ("observed","error","unknown"):raise ValueError("Invalid status")
        if r["status"]=="observed":
            for field in ("cited","mentioned","recommended"):
                if type(r.get(field)) is not bool:raise ValueError("Observed answer needs explicit boolean labels")
            if r["cited"] and not r.get("citations"):raise ValueError("Citation needs exact source URLs")
            if r["recommended"] and not r.get("recommendation_excerpt"):raise ValueError("Recommendation needs evidence excerpt")
        buckets[(r["engine"],r["model"],r["market"])].append(r)
    result=[]
    for (engine,model,market),group in sorted(buckets.items()):
        observed=[x for x in group if x["status"]=="observed"];n=len(observed)
        result.append({"engine":engine,"model":model,"market":market,"observed_answers":n,
            "unknown_or_error":len(group)-n,"unique_prompts":len({x["prompt_id"] for x in observed}),
            **{f+"_share":sum(x[f] for x in observed)/n if n else None for f in ["cited","mentioned","recommended"]}})
    return {"schema":"geo7-ai-observations/v1","groups":result,"scope":"Observed sample only; not a universal GEO score"}
def main():
    p=argparse.ArgumentParser();p.add_argument("input");p.add_argument("--out",required=True);a=p.parse_args()
    save_new(a.out,summarize(json.loads(Path(a.input).read_text())))
if __name__=="__main__":main()
