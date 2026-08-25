import os
import re

# 1. Update index.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(
    r'<a\s+href=\"#prochains-departs\"\s+class=\"hover:text-amber-300 transition-colors\">Destinations</a>',
    '<a href="destinations/index.html" class="hover:text-amber-300 transition-colors">Destinations</a>',
    html
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update a-propos.html and contact.html
for fname in ['a-propos.html', 'contact.html']:
    fpath = os.path.join('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal', fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('href="index.html#prochains-departs">Destinations</a>', 'href="destinations/index.html">Destinations</a>')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

# 3. Update all 14 tour pages
tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        tc = f.read()
    if 'href="../destinations/index.html"' not in tc:
        tc = tc.replace('href="../index.html#prochains-departs" class="hover:text-[#0e8354] transition-colors">Tous les 14 séjours</a>', 'href="../index.html#prochains-departs" class="hover:text-[#0e8354] transition-colors">Tous les 14 séjours</a>\n        <a href="../destinations/index.html" class="hover:text-[#0e8354] transition-colors">Destinations</a>')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(tc)

print("Linked destinations hub across all site pages successfully!")
