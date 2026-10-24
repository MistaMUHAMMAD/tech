#!/usr/bin/env python3
"""Check local HTML links, anchors, favicon resources and required downloads."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, sys, re

ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=[];self.h1=0;self.labels=set();self.fields=[];self.images=[];self.form_actions=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag in ['a','link'] and a.get('href'):self.refs.append(a['href'])
  if tag in ['script','img'] and a.get('src'):self.refs.append(a['src'])
  if tag=='label' and a.get('for'):self.labels.add(a['for'])
  if tag in ['input','textarea']:self.fields.append(a.get('id'))
  if tag=='img':self.images.append(a)
  if tag=='form':self.form_actions.append(a.get('action',''))
  if a.get('formaction'):self.form_actions.append(a['formaction'])

pages={};errors=[];warnings=[]
for f in ROOT.glob('*.html'):
 page=Page();page.feed(f.read_text());pages[f.name]=page
 if page.h1!=1:errors.append(f'{f.name}: expected one h1')
 if len(page.ids)!=len(set(page.ids)):errors.append(f'{f.name}: duplicate IDs')
 for field in page.fields:
  if field not in page.labels:errors.append(f'{f.name}: missing label for {field}')
 for image in page.images:
  if 'alt' not in image:errors.append(f'{f.name}: image without alt text')
 for action in page.form_actions:
  if urlsplit(action).scheme.lower() in {'http','mailto'}:
   errors.append(f'{f.name}: insecure form target can trigger a Chrome warning: {action}')
for filename,page in pages.items():
 for ref in page.refs:
  parts=urlsplit(ref)
  if parts.scheme or parts.netloc:continue
  target=(ROOT/unquote(parts.path or filename)).resolve()
  if not target.is_relative_to(ROOT):errors.append(f'{filename}: link leaves repository: {ref}');continue
  if not target.is_file():errors.append(f'{filename}: missing resource: {ref}');continue
  if target.suffix=='.html' and parts.fragment:
   dest=pages.get(target.name)
   if dest and unquote(parts.fragment) not in dest.ids:errors.append(f'{filename}: missing anchor: {ref}')
for name in ['favicon.ico','assets/icons/favicon.svg','assets/icons/apple-touch-icon.png','site.webmanifest','assets/Muhammad_Musa_IT_CV.pdf','assets/documents/IT_Support_Sample_Workbook.xlsx','assets/documents/IT_Support_Field_Guide.pdf']:
 if not (ROOT/name).is_file():errors.append('Missing '+name)
manifest=json.loads((ROOT/'site.webmanifest').read_text())
for icon in manifest['icons']:
 if not (ROOT/icon['src']).is_file():errors.append('Missing manifest icon '+icon['src'])
config=json.loads((ROOT/'site-config.json').read_text())
if not config.get('github_username'):warnings.append('GitHub username is not configured. Run tools/configure.py before publication.')
if not config.get('site_url'):warnings.append('Canonical URL and absolute social-preview URLs need deployment configuration.')
for name in ['index.html','projects.html','samples.html']:
 text=(ROOT/name).read_text()
 if re.search(r'\b(?:192\.168\.|10\.0\.0\.|amaecomglobal\.com)',text,re.I):errors.append(name+': private environment detail detected')
for w in warnings:print('NOTE:',w)
for error in errors:print('ERROR:',error)
print(f'Checked {len(pages)} pages. {len(errors)} errors.')
sys.exit(1 if errors else 0)
