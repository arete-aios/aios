"""Serve the fictional CC7 example locally. Python 3.9+, no dependencies or writes."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote,urlsplit
import argparse,json,re
ROOT=Path(__file__).resolve().parent
VIEWS=set(json.loads((ROOT/'views.json').read_text()))
ALIASES=json.loads((ROOT/'aliases.json').read_text())
CSP="default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data:; font-src 'self'; connect-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'"
class Handler(BaseHTTPRequestHandler):
 def reply(self,status,body=b'',kind='text/plain; charset=utf-8',location=None):
  self.send_response(status);self.send_header('content-type',kind);self.send_header('content-length',str(len(body)));self.send_header('content-security-policy',CSP);self.send_header('x-content-type-options','nosniff')
  if location:self.send_header('location',location)
  self.end_headers()
  if self.command!='HEAD':self.wfile.write(body)
 def do_GET(self):
  path=unquote(urlsplit(self.path).path).rstrip('/')or'/'
  if path=='/':return self.reply(303,location='/my/cc-demo')
  if path=='/START.md':return self.reply(200,(ROOT/'START.md').read_bytes())
  if path.startswith('/fonts/'):
   name=path[len('/fonts/'):]
   if name not in {p.name for p in(ROOT/'fonts').glob('*.woff2')}:return self.reply(404,b'Not found')
   return self.reply(200,(ROOT/'fonts'/name).read_bytes(),'font/woff2')
  locale='lv'if path.startswith('/lv/')else'en';base=('/lv'if locale=='lv'else'')+'/my/cc-demo'
  if path!=base and not path.startswith(base+'/'):return self.reply(404,b'Not found')
  view=path[len(base):].strip('/')or'today'
  if view in ALIASES:return self.reply(308,location=base+'/'+ALIASES[view])
  if view not in VIEWS:return self.reply(404,b'Not found')
  source=(ROOT/('command-center.lv.html'if locale=='lv'else'command-center.en.html')).read_text();parts=view.split('/');panel='skill-'+parts[1]if parts[0]=='skills'and len(parts)>1 else parts[0]
  source=re.sub(r'<section class="panel" id="([^"]+)"',lambda m:m[0]+(''if m[1]==panel else' hidden'),source)
  return self.reply(200,source.encode(),'text/html; charset=utf-8')
 do_HEAD=do_GET
 def log_message(self,*args):pass
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--port',type=int,default=8765);args=parser.parse_args()
 print('CC7 example: http://127.0.0.1:'+str(args.port)+'/my/cc-demo',flush=True)
 print('Latviski: http://127.0.0.1:'+str(args.port)+'/lv/my/cc-demo',flush=True)
 print('Fictional data only. Stop with Ctrl+C.',flush=True)
 ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()
