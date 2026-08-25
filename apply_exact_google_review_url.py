import re
import os

exact_google_url = "https://www.google.com/search?sca_esv=a1a5ed640a4c7c37&cs=0&sxsrf=APpeQntnDL5GNsUQ_hIZE3WXkqPaN3biMw:1787312489201&q=Jungle+Nepal+Adventure+Avis&rflfq=1&num=20&stick=H4sIAAAAAAAAAONgkxK2MDA0NLY0MLYwNjUxMzMwMzMy3sDI-IpR2qs0Lz0nVcEvtSAxR8ExpSw1r6S0KFXBsSyzeBErPlkAWhIrKFYAAAA&rldimm=8011390383546606623&tbm=lcl&hl=fr-FR&sa=X&ved=2ahUKEwjW85Pw0bGWAxVfTaQEHX8wKpkQ9fQKegQIERAG&biw=1470&bih=798&dpr=2#lkt=LocalPoiReviews"

# 1. Update index.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace previous search query with exact URL
html = html.replace("https://www.google.com/search?q=Jungle+Nepal+Adventure+avis", exact_google_url)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update a-propos.html and contact.html
for p in ['/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/contact.html', '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/a-propos.html']:
    if not os.path.exists(p):
        continue
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace("https://www.google.com/search?q=Jungle+Nepal+Adventure+avis", exact_google_url)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)

# 3. Update all 14 tour pages
tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        tc = f.read()
    tc = tc.replace("https://www.google.com/search?q=Jungle+Nepal+Adventure+avis", exact_google_url)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(tc)

print("Exact Google Reviews URL applied across the entire website!")
