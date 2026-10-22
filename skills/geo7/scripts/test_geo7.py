#!/usr/bin/env python3
"""Offline behavioral acceptance checks. No provider/API calls or installed dependencies."""
import unittest,json
from unittest.mock import patch
from audit import inspect_page,schema_types,normal,crawl,save_new
from ai_visibility import summarize
from research_plan import plan,domain
from research_plan import validate
from report import analyze,unwrap
def page(body):
 return inspect_page({"url":"https://example.com/","final_url":"https://example.com/","status":200,
 "x_robots_tag":"","body":body})
class ParseTests(unittest.TestCase):
 def test_html_and_nested_graph(self):
  p=page('<html lang="lv"><head><title>Business</title><meta content="Desc" name="description"><link rel="canonical" href="/aios"></head><body><h1>Build <em>your</em> system</h1><a href="https://example.com/x">same</a><a href="https://other.example/x">other</a><script type="application/ld+json">{"@graph":[{"@type":"Organization"},{"@type":["WebSite","Person"]}]}</script><script>wrong hidden words</script></body></html>')
  self.assertEqual(p["title"],"Business");self.assertEqual(p["headings"],[{"level":1,"text":"Build your system"}])
  self.assertEqual(p["canonical"],"https://example.com/aios")
  self.assertEqual(p["schema_types"],["Organization","Person","WebSite"])
  self.assertEqual((p["internal_links"],p["external_links"]),(1,1))
  self.assertNotIn("wrong",p["text_excerpt"]);self.assertNotIn("Business",p["text_excerpt"])
 def test_invalid_schema_and_none(self):
  p=page('<meta name="robots" content="none"><h1>H</h1><script type="application/ld+json">{bad}</script>')
  self.assertTrue(p["noindex"]);self.assertEqual(len(p["jsonld_invalid"]),1);self.assertEqual(p["schema_types"],[])
 def test_routes(self):
  self.assertIsNone(normal("/checkout/card","https://example.com"))
  self.assertIsNone(normal("https://other.example/","https://example.com"))
  self.assertIsNone(normal("/x?q=private","https://example.com"))
 def test_unknown_robots_stops(self):
  with patch("audit.public_url",lambda u:u),patch("audit.fetch_url",side_effect=TimeoutError("network unavailable")) as fetch:
   v=crawl("https://example.com",15)
  self.assertEqual(fetch.call_count,1);self.assertEqual(v["pages"],[]);self.assertIn("blocked",v["scope"])
 def test_outside_output_refused(self):
  with self.assertRaises(ValueError):save_new("/etc/geo7-forbidden-test.json",{})
class ObservationTests(unittest.TestCase):
 def observation(self,status="observed"):
  return dict(prompt_id="p1",engine="Search A",model="dated",market="UK/en",observed_at="2026-10-11",
    run_id="r1",answer_source="saved-evidence.html",status=status,cited=True,mentioned=True,recommended=False,citations=["https://example.com"])
 def test_unknown_not_zero(self):
  a=self.observation();b=self.observation("unknown");b["run_id"]="r2"
  s=summarize([a,b])["groups"][0]
  self.assertEqual(s["observed_answers"],1);self.assertEqual(s["unknown_or_error"],1);self.assertEqual(s["cited_share"],1)
  self.assertIsNone(summarize([b])["groups"][0]["cited_share"])
 def test_missing_and_duplicate_proof(self):
  a=self.observation();a.pop("citations")
  with self.assertRaises(ValueError):summarize([a])
  a=self.observation()
  with self.assertRaises(ValueError):summarize([a,a])
class PlannerTests(unittest.TestCase):
 def test_budget_free_bounded_plan(self):
  p=plan("https://example.com","business ai",2826,"en","other.example")
  self.assertEqual(p["api_calls_made"],0);self.assertEqual(len(p["operations"]),4);validate(p["operations"])
  self.assertEqual(p["operations"][-1]["arguments"]["data"][0]["limit"],20)
 def test_credentials_and_market_refused(self):
  with self.assertRaises(ValueError):domain("https://name:pass@example.com")
  with self.assertRaises(ValueError):plan("example.com","business ai",0,"en")
  with self.assertRaises(ValueError):validate([{"tool":"email_send","arguments":{}}])
class ReportTests(unittest.TestCase):
 def reply(self,v):return {"ok":True,"result":{"content":[{"type":"text","text":json.dumps(v)}]}}
 def test_empty_gsc_and_paid_ai_are_not_visibility(self):
  c={"site":"https://example.com","scope":"sample","pages":[page('<title>A</title><h1>A</h1><link rel="canonical" href="/">')],"sitemap_urls":[]}
  n={"operations":[{"name":"gsc-queries","arguments":{},"result":self.reply({"data":{}})},
  {"name":"ga4-channels","arguments":{},"result":self.reply({"data":{"dimensionHeaders":[{"name":"sessionSourceMedium"}],"metricHeaders":[{"name":"sessions"}],"rows":[{"dimensionValues":[{"value":"chatgpt / paid"}],"metricValues":[{"value":"8"}]}]}})}]}
  v=analyze(c,n);self.assertEqual(v["connectors"]["gsc-queries"]["status"],"empty")
  self.assertEqual(v["analytics"]["chatgpt_paid_sessions"],8)
  f=next(f for f in v["findings"] if f["id"]=="organic-baseline")
  self.assertIn("nav AI",f["action"]);self.assertNotIn("geo_score",v)
 def test_absent_sample_and_analytics_remain_unknown(self):
  v=analyze({"site":"https://example.com","scope":"blocked","pages":[],"sitemap_urls":[]})
  self.assertIn("BLOCKED_OR_EMPTY",v["status"]);self.assertIsNone(v["analytics"]["google_organic_sessions"])
 def test_failed_provider_stays_error(self):
  self.assertIn("_error",unwrap({"ok":False}))

class DetailedReportTests(unittest.TestCase):
 def test_root_alias_normalized(self):
  self.assertEqual(normal("https://example.com","https://example.com"),"https://example.com/")
 def test_duplicate_http_body_is_evidence_not_citation(self):
  body='<title>Test</title><h1>Same content</h1><p>Business answer</p>'
  rows=[]
  for url in ["https://example.com/a","https://example.com/b"]:
   rows.append({"url":url,"final_url":url,"status":200,"x_robots_tag":"","body":body,"content_type":"text/html"})
  c={"site":"https://example.com","scope":"sample","pages":[inspect_page(x) for x in rows],"raw":rows,"sitemap_urls":[x["url"] for x in rows]}
  v=analyze(c);self.assertEqual(len(v["content_duplicates"]),1);self.assertEqual(len(v["content_duplicates"][0]["parsed_http_text_sha256"]),64)
  self.assertEqual(v["ai_visibility"]["status"],"not_measured")
 def test_schema_presence_not_conflated_with_syntax(self):
  p=page('<title>A</title><h1>A</h1><script type="application/ld+json">{"@type":"Article"}</script>')
  v=analyze({"site":"https://example.com","scope":"sample","pages":[p],"raw":[],"sitemap_urls":[]})
  self.assertEqual(v["content_summary"]["schema_pages"],1)
  self.assertNotIn("entity-schema",[f["id"] for f in v["findings"]])
 def test_wrong_hreflang_self_target(self):
  p=page('<html lang="en"><title>A</title><h1>A</h1><link rel="alternate" hreflang="en" href="/other"></html>')
  v=analyze({"site":"https://example.com","scope":"sample","pages":[p],"raw":[],"sitemap_urls":[]})
  self.assertIn("hreflang-self",[f["id"] for f in v["findings"]])

if __name__=="__main__":unittest.main(verbosity=2)
