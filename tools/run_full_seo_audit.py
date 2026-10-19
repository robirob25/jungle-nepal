import os, glob, re, json
from html.parser import HTMLParser

class SuperSEOAuditor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ''
        self.in_title = False
        self.meta_desc = ''
        self.canonical = ''
        self.h1_texts = []
        self.in_h1 = False
        self.h2_count = 0
        self.h3_count = 0
        self.images_total = 0
        self.images_no_alt = 0
        self.internal_links = []
        self.hreflangs = {}
        self.schemas = []
        self.in_script_ld = False
        self.curr_script = ''
        self.og_title = ''
        self.og_desc = ''
        self.og_image = ''
        self.twitter_card = ''
        self.direct_answer = False
        self.in_script = False
        self.in_style = False
        self.text_tokens = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag in ['script', 'style']: self.in_script = True
        if tag == 'title': self.in_title = True
        elif tag == 'meta':
            name = attrs_dict.get('name', '').lower()
            prop = attrs_dict.get('property', '').lower()
            content = attrs_dict.get('content', '')
            if name == 'description': self.meta_desc = content
            elif prop == 'og:title': self.og_title = content
            elif prop == 'og:description': self.og_desc = content
            elif prop == 'og:image': self.og_image = content
            elif name == 'twitter:card': self.twitter_card = content
        elif tag == 'link':
            rel = attrs_dict.get('rel', '').lower()
            href = attrs_dict.get('href', '')
            if rel == 'canonical': self.canonical = href
            elif rel == 'alternate' and 'hreflang' in attrs_dict:
                self.hreflangs[attrs_dict['hreflang']] = href
        elif tag == 'h1': self.in_h1 = True
        elif tag == 'h2': self.h2_count += 1
        elif tag == 'h3': self.h3_count += 1
        elif tag == 'img':
            self.images_total += 1
            alt = attrs_dict.get('alt', '')
            if not alt or not alt.strip(): self.images_no_alt += 1
        elif tag == 'a':
            href = attrs_dict.get('href', '')
            if href: self.internal_links.append(href)
        elif tag == 'div' and 'direct-answer-snippet' in attrs_dict.get('class', ''):
            self.direct_answer = True
        elif tag == 'script' and attrs_dict.get('type') == 'application/ld+json':
            self.in_script_ld = True
            self.curr_script = ''

    def handle_endtag(self, tag):
        if tag in ['script', 'style']: self.in_script = False
        if tag == 'title': self.in_title = False
        elif tag == 'h1': self.in_h1 = False
        elif tag == 'script' and self.in_script_ld:
            self.in_script_ld = False
            try: self.schemas.append(json.loads(self.curr_script))
            except Exception: pass

    def handle_data(self, data):
        if self.in_title: self.title += data
        elif self.in_h1: self.h1_texts.append(data.strip())
        elif self.in_script_ld: self.curr_script += data
        elif not self.in_script and not self.in_style:
            t = data.strip()
            if t: self.text_tokens.append(t)

all_routes = set()
for f in glob.glob('dist/**/*.html', recursive=True):
    rel = os.path.relpath(f, 'dist')
    r = '/' + rel.replace('index.html', '').rstrip('/')
    if not r: r = '/'
    all_routes.add(r)
    all_routes.add(r + ('/' if not r.endswith('/') else ''))

content_pages = []
for f in glob.glob('dist/**/*.html', recursive=True):
    if 'googlee561a81130a4e7b5' in f: continue
    with open(f, 'r', encoding='utf-8') as fp: c = fp.read()
    if 'http-equiv="refresh"' in c: continue
    aud = SuperSEOAuditor()
    aud.feed(c)
    rel = os.path.relpath(f, 'dist')
    content_pages.append((rel, aud))

broken_links = {}
for p, aud in content_pages:
    for link in aud.internal_links:
        clean = link.split('#')[0].split('?')[0]
        if not clean or any(clean.startswith(x) for x in ['mailto:', 'tel:', 'javascript:', 'whatsapp:']): continue
        if clean.startswith('https://junglenepal.com'): clean = clean.replace('https://junglenepal.com', '')
        if not clean: clean = '/'
        if clean.startswith('http'): continue
        if clean not in all_routes and not clean.startswith('/assets/') and not clean.startswith('/_astro/'):
            if clean not in broken_links: broken_links[clean] = set()
            broken_links[clean].add(p)

no_canonical = [p for p, a in content_pages if not a.canonical]
no_h1 = [p for p, a in content_pages if len(a.h1_texts) == 0]
multi_h1 = [p for p, a in content_pages if len(a.h1_texts) > 1]
no_desc = [p for p, a in content_pages if not a.meta_desc]
no_title = [p for p, a in content_pages if not a.title]
no_og_image = [p for p, a in content_pages if not a.og_image]
no_twitter = [p for p, a in content_pages if not a.twitter_card]
missing_alts = [p for p, a in content_pages if a.images_no_alt > 0]
no_hreflang = [p for p, a in content_pages if len(a.hreflangs) < 2]
no_schema = [p for p, a in content_pages if not a.schemas]
thin_pages = [(p, len(' '.join(a.text_tokens).split())) for p, a in content_pages if len(' '.join(a.text_tokens).split()) < 400]
direct_answer_pages = [p for p, a in content_pages if a.direct_answer]

schema_dist = {}
for p, a in content_pages:
    for s in a.schemas:
        if isinstance(s, dict):
            st = s.get('@type', 'Unknown')
            schema_dist[st] = schema_dist.get(st, 0) + 1

print(f"Total live content pages: {len(content_pages)}")
print(f"1. Broken internal links (404): {len(broken_links)}")
print(f"2. Missing canonical tags: {len(no_canonical)}")
print(f"3. Missing H1: {len(no_h1)}")
print(f"4. Multiple H1 tags: {len(multi_h1)}")
print(f"5. Missing meta description: {len(no_desc)}")
print(f"6. Missing title tag: {len(no_title)}")
print(f"7. Missing OpenGraph image: {len(no_og_image)}")
print(f"8. Missing Twitter Card: {len(no_twitter)}")
print(f"9. Images missing ALT text: {len(missing_alts)}")
print(f"10. Missing hreflang pairs: {len(no_hreflang)}")
print(f"11. Missing Schema.org JSON-LD: {len(no_schema)}")
print(f"12. Thin content pages (<400 words): {len(thin_pages)}")
print(f"13. Day activities with Direct Answer (Position 0): {len(direct_answer_pages)}")
print(f"14. Schema.org distribution: {schema_dist}")
