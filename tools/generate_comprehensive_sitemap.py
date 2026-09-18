import json, glob, os, datetime

today = datetime.datetime.now().strftime("%Y-%m-%d")

# 1. Load blog posts
with open('src/data/blog_posts.json', 'r', encoding='utf-8') as f:
    posts_fr = json.load(f)

with open('src/data/blog_posts.en.json', 'r', encoding='utf-8') as f:
    posts_en = json.load(f)

# 2. Load tours
with open('src/data/tours.json', 'r', encoding='utf-8') as f:
    tours_fr = json.load(f)

with open('src/data/tours.en.json', 'r', encoding='utf-8') as f:
    tours_en = json.load(f)

# 3. Load destinations
with open('src/data/destinations.json', 'r', encoding='utf-8') as f:
    destinations = json.load(f)

entries = []

def add_url(loc_fr, loc_en=None, priority=0.8, changefreq="weekly", lastmod=today):
    # FR entry
    entries.append({
        "loc": loc_fr,
        "lastmod": lastmod,
        "changefreq": changefreq,
        "priority": priority,
        "alt_fr": loc_fr,
        "alt_en": loc_en or loc_fr.replace("junglenepal.com/", "junglenepal.com/en/")
    })
    # EN entry if distinct
    if loc_en:
        entries.append({
            "loc": loc_en,
            "lastmod": lastmod,
            "changefreq": changefreq,
            "priority": priority,
            "alt_fr": loc_fr,
            "alt_en": loc_en
        })

# Home
add_url("https://junglenepal.com/", "https://junglenepal.com/en/", priority=1.0, changefreq="daily")

# Blog Index
add_url("https://junglenepal.com/blog/", "https://junglenepal.com/en/blog/", priority=0.9, changefreq="daily")

# Contact & About
add_url("https://junglenepal.com/contact/", "https://junglenepal.com/en/contact/", priority=0.8, changefreq="monthly")
add_url("https://junglenepal.com/a-propos/", "https://junglenepal.com/en/a-propos/", priority=0.8, changefreq="monthly")
add_url("https://junglenepal.com/mentions-legales/", "https://junglenepal.com/en/legal-mentions/", priority=0.3, changefreq="yearly")

# Destinations Index
add_url("https://junglenepal.com/destinations/", "https://junglenepal.com/en/destinations/", priority=0.9, changefreq="weekly")

# Individual Destinations
for d in destinations:
    slug = d.get('slug', '')
    if slug:
        add_url(f"https://junglenepal.com/destinations/{slug}/", f"https://junglenepal.com/en/destinations/{slug}/", priority=0.85)

# Individual Tours
for t in tours_fr:
    slug = t.get('slug', '')
    if slug:
        add_url(f"https://junglenepal.com/tours/{slug}/", f"https://junglenepal.com/en/tours/{slug}/", priority=0.9)

# All 41 Blog Posts
for p in posts_fr:
    slug = p.get('slug', '')
    if slug:
        # Check if top priority
        is_top = slug in [
            'voir-des-tigres-au-nepal',
            'guide-parc-national-de-bardia-safari-conseils',
            'bardia-ou-chitwan-guide-comparatif',
            'safari-nepal-ou-inde-comparatif-ranthambore-corbett-bardia',
            'sante-paludisme-vaccins-safari-nepal-conseils-medicaux',
            'oiseaux-bardia-calao-bicorne-rollier-indien-tchitrec-paradis',
            'safari-a-pied-au-nepal-guide-complet',
            'art-du-pistage-jungle-nepal-traces-cris-alarme'
        ]
        prio = 0.9 if is_top else 0.8
        date = p.get('date', today)
        add_url(f"https://junglenepal.com/blog/{slug}/", f"https://junglenepal.com/en/blog/{slug}/", priority=prio, changefreq="weekly", lastmod=date)

# Build XML
xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
    '        xmlns:xhtml="http://www.w3.org/1999/xhtml">'
]

for e in entries:
    xml_lines.append('  <url>')
    xml_lines.append(f'    <loc>{e["loc"]}</loc>')
    xml_lines.append(f'    <lastmod>{e["lastmod"]}</lastmod>')
    xml_lines.append(f'    <changefreq>{e["changefreq"]}</changefreq>')
    xml_lines.append(f'    <priority>{e["priority"]:.2f}</priority>')
    if e.get("alt_fr"):
        xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="fr" href="{e["alt_fr"]}"/>')
    if e.get("alt_en"):
        xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{e["alt_en"]}"/>')
        xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{e["alt_fr"]}"/>')
    xml_lines.append('  </url>')

xml_lines.append('</urlset>')

sitemap_content = '\n'.join(xml_lines)

with open('public/sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print(f"Generated comprehensive sitemap with {len(entries)} URLs and xhtml:link hreflangs!")
