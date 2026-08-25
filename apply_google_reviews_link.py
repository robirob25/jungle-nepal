import re
import os

google_reviews_url = "https://www.google.com/search?q=Jungle+Nepal+Adventure+avis"

# 1. Update index.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update the main reviews button
html = re.sub(
    r'<a\s+href=\"https://wa\.me/[^\"]*\"\s+target=\"_blank\"\s+class=\"inline-flex items-center gap-2 px-6 py-3 rounded-full bg-white border border-slate-200 shadow-sm hover:shadow text-xs font-extrabold text-slate-800 hover:text-\[#0e8354\] transition-all\">.*?</a>',
    f'<a href="{google_reviews_url}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-6 py-3.5 rounded-full bg-white border border-slate-200 shadow-sm hover:shadow-md text-xs sm:text-sm font-extrabold text-slate-800 hover:text-[#0e8354] hover:border-[#0e8354]/40 transition-all group"><span class="w-2.5 h-2.5 rounded-full bg-[#00b67a] animate-pulse"></span><span>Lire les 19 avis vérifiés sur Google Reviews (5.0 / 5.0)</span><i data-lucide="arrow-up-right" class="w-4 h-4 text-slate-400 group-hover:text-[#0e8354] group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform"></i></a>',
    html,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update contact.html and a-propos.html
for p in ['/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/contact.html', '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/a-propos.html']:
    if not os.path.exists(p):
        continue
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('https://wa.me/33695413227', google_reviews_url) if 'avis' in c else c
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
    
    # Replace link in reviews section of tour
    tc = re.sub(
        r'<a\s+href=\"[^\"]*\"\s+class=\"inline-flex items-center gap-2 px-5 py-2\.5 rounded-full bg-white border border-slate-200[^\"]*\">.*?</a>',
        f'<a href="{google_reviews_url}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-white border border-slate-200 shadow-sm hover:shadow text-xs font-bold text-slate-800 hover:text-[#0e8354] transition-all"><span class="w-2 h-2 rounded-full bg-[#00b67a]"></span><span>Consulter les avis complets sur Google</span><i data-lucide="arrow-up-right" class="w-4 h-4"></i></a>',
        tc,
        flags=re.DOTALL
    )
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(tc)

print("Direct Google Reviews link applied across all pages successfully!")
