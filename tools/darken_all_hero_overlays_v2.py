import glob, re

# All pages (index, a-propos, contact, destinations, tours)
astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

# 1. Update Homepage Hero in index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx = f.read()

# Enhance hero gradient overlay to give even deeper cinematic contrast
idx = re.sub(
    r'<div class="absolute inset-0 bg-gradient-to-t[^"]*"></div>(\s*<div class="absolute inset-0 bg-black/[^"]*"></div>)?',
    '<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/75 to-black/90"></div>\n      <div class="absolute inset-0 bg-black/55"></div>',
    idx,
    count=1
)
# Lower hero image opacity
idx = idx.replace('class="w-full h-full object-cover scale-105 transform filter brightness-95 opacity-60"', 'class="w-full h-full object-cover scale-105 transform filter brightness-60 opacity-45"')
idx = idx.replace('opacity-60 scale-105', 'opacity-45 scale-105')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx)

# 2. Update all destination pages (annapurna, bardia, chitwan, suklaphanta, katmandou)
dest_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/*.astro')
for fpath in dest_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Darker background photo & stronger overlay
    c = re.sub(r'opacity-\d+ scale-105 filter brightness-\d+ contrast-110', 'opacity-35 scale-105 filter brightness-50 contrast-115', c)
    c = re.sub(
        r'<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/75 to-black/80"></div>(\s*<div class="absolute inset-0 bg-black/[^"]*"></div>)?',
        '<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/85 to-black/95"></div>\n      <div class="absolute inset-0 bg-black/50"></div>',
        c
    )
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

# 3. Update a-propos.astro Hero
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    ap = f.read()
ap = re.sub(r'opacity-\d+ scale-105 transform filter brightness-\d+ contrast-110', 'opacity-40 scale-105 transform filter brightness-50 contrast-115', ap)
ap = re.sub(
    r'<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/65 to-black/85"></div>(\s*<div class="absolute inset-0 bg-black/[^"]*"></div>)?',
    '<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/80 to-black/95"></div>\n      <div class="absolute inset-0 bg-black/50"></div>',
    ap
)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(ap)

# 4. Update contact.astro Hero
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'r', encoding='utf-8') as f:
    ct = f.read()
ct = re.sub(r'opacity-\d+ scale-105 filter brightness-\d+ contrast-110', 'opacity-35 scale-105 filter brightness-50 contrast-115', ct)
ct = re.sub(
    r'<div class="absolute inset-0 bg-gradient-to-r from-slate-950/95 via-slate-950/80 to-slate-950/60"></div>(\s*<div class="absolute inset-0 bg-black/[^"]*"></div>)?',
    '<div class="absolute inset-0 bg-gradient-to-r from-slate-950 via-slate-950/90 to-slate-950/75"></div>\n      <div class="absolute inset-0 bg-black/50"></div>',
    ct
)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'w', encoding='utf-8') as f:
    f.write(ct)

# 5. Update all tour pages (src/pages/tours/*.astro)
tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')
for fpath in tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    c = c.replace('brightness-65 contrast-110', 'brightness-45 contrast-115')
    c = c.replace('opacity-40', 'opacity-30')
    c = c.replace('opacity-50', 'opacity-35')
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("✓ Strengthened dark overlay (bg-black/50 + brightness-50) across all heroes for maximum readability!")
