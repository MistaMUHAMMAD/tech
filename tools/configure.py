#!/usr/bin/env python3
"""Configure deployment metadata without adding a build step to GitHub Pages."""
from pathlib import Path
import argparse, json, re, html
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--username',help='Your confirmed GitHub username')
p.add_argument('--site-url',help='Optional HTTPS custom-domain URL')
p.add_argument('--photo',help='Existing local photo path relative to the site root')
args=p.parse_args()
config=json.loads((ROOT/'site-config.json').read_text())
if args.username:
 if not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?',args.username) or '--' in args.username:
  p.error('Enter a valid GitHub username without @, spaces or a URL.')
 config['github_username']=args.username.lower()
 if not args.site_url: config['site_url']=f'https://{args.username.lower()}.github.io/'
if args.site_url:
 u=urlparse(args.site_url)
 if u.scheme!='https' or not u.netloc or u.query or u.fragment or u.username or u.password:
  p.error('--site-url must be an HTTPS URL without query, fragment or credentials.')
 config['site_url']=args.site_url.rstrip('/')+'/'
if args.photo:
 photo=(ROOT/args.photo).resolve()
 if not photo.is_relative_to(ROOT) or not photo.is_file():p.error('--photo must point to an existing image inside this site folder.')
 if photo.suffix.lower() not in ['.jpg','.jpeg','.png','.webp']:p.error('Use a JPG, PNG or WebP photo.')
 config['photo_path']=photo.relative_to(ROOT).as_posix()
username=config.get('github_username','');url=config.get('site_url','')
for f in ROOT.glob('*.html'):
 content=f.read_text()
 if url:
  page=url if f.name=='index.html' else url+f.name
  metadata=f'<link rel="canonical" href="{html.escape(page,quote=True)}"><meta property="og:url" content="{html.escape(page,quote=True)}">'
  if f.name=='index.html':
   person={'@context':'https://schema.org','@type':'Person','name':'Muhammad Musa','jobTitle':config['headline'],'url':url,'email':'mailto:muhammad.musa4rl@gmail.com','telephone':'+2348148057035','address':{'@type':'PostalAddress','addressLocality':'Abuja','addressCountry':'NG'},'sameAs':['https://www.linkedin.com/in/muhammadmusa']}
   if username:person['sameAs'].append('https://github.com/'+username)
   metadata+='<script type="application/ld+json">'+json.dumps(person,separators=(',',':'))+'</script>'
  content=re.sub(r'<!-- DEPLOYMENT_META_START -->.*?<!-- DEPLOYMENT_META_END -->','<!-- DEPLOYMENT_META_START -->'+metadata+'<!-- DEPLOYMENT_META_END -->',content,flags=re.S)
  imageurl=html.escape(url+'assets/images/social-preview.png',quote=True)
  content=re.sub(r'(<meta property="og:image" content=")[^"]*(">)',lambda m:m[1]+imageurl+m[2],content)
  content=re.sub(r'(<meta name="twitter:image" content=")[^"]*(">)',lambda m:m[1]+imageurl+m[2],content)
 if username:
  contact=f'<a href="https://github.com/{username}" target="_blank" rel="noopener noreferrer">github.com/{username}</a>'
  content=re.sub(r'<!-- GITHUB_CONTACT_START -->.*?<!-- GITHUB_CONTACT_END -->','<!-- GITHUB_CONTACT_START -->'+contact+'<!-- GITHUB_CONTACT_END -->',content,flags=re.S)
 if config.get('photo_path') and f.name=='index.html':
  photo=html.escape(config['photo_path'],quote=True)
  content=re.sub(r'(<div class="portrait-shell" id="profile-image">).*?(</div><div class="panel-bottom">)',lambda m:m[1]+f'<img class="profile-photo" src="{photo}" alt="Muhammad Musa" width="600" height="600" fetchpriority="high">'+m[2],content,flags=re.S)
 f.write_text(content)
if url:
 pages=['','projects.html','samples.html']
 sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+html.escape(url+x)+'</loc></url>' for x in pages)+'</urlset>\n'
 (ROOT/'sitemap.xml').write_text(sitemap)
 (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+url+'sitemap.xml\n')
(ROOT/'site-config.json').write_text(json.dumps(config,indent=2)+'\n')
print('Configuration updated.' if username or url or config.get('photo_path') else 'No username configured. Site remains usable locally.')
print('Run: python tools/validate.py')
