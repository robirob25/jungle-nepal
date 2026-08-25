import glob, re

# All pages (index, a-propos, contact, destinations, tours)
astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

# 1. Update Homepage Hero in index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx = f.read()

# Enhance hero gradient overlay to give deep contrast to navbar and text
# Make sure the top of the hero has a solid dark-gradient for navbar readability
idx = re.sub(
    r'<div class="absolute inset-0 bg-gradient-to-t[^"]*"></div>',
    '<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/60 to-black/75"></div>\n      <div class="absolute inset-0 bg-black/40"></div>',
    idx,
    count=1
)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx)

# 2. Update all destination pages (annapurna, bardia, chitwan, suklaphanta, katmandou)
dest_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/*.astro')
for fpath in dest_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Increase dark overlay & filter brightness
    c = c.replace('opacity-35 scale-105 filter brightness-85', 'opacity-40 scale-105 filter brightness-70 contrast-110')
    c = c.replace(
        '<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/60 to-black/40"></div>',
        '<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/75 to-black/80"></div>\n      <div class="absolute inset-0 bg-black/35"></div>'
    )
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

# 3. Update a-propos.astro Hero
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    ap = f.read()
ap = ap.replace('opacity-65 scale-105 transform filter brightness-95', 'opacity-50 scale-105 transform filter brightness-70 contrast-110')
ap = ap.replace(
    '<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/45 to-slate-950/70"></div>',
    '<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/65 to-black/85"></div>\n      <div class="absolute inset-0 bg-black/30"></div>'
)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(ap)

# 4. Update contact.astro Hero
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'r', encoding='utf-8') as f:
    ct = f.read()
ct = ct.replace('opacity-60 scale-105 filter brightness-90', 'opacity-45 scale-105 filter brightness-70 contrast-110')
ct = ct.replace(
    '<div class="absolute inset-0 bg-gradient-to-r from-slate-950/95 via-slate-950/75 to-slate-950/40"></div>',
    '<div class="absolute inset-0 bg-gradient-to-r from-slate-950/95 via-slate-950/80 to-slate-950/60"></div>\n      <div class="absolute inset-0 bg-black/30"></div>'
)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'w', encoding='utf-8') as f:
    f.write(ct)

# 5. Update all tour pages (src/pages/tours/*.astro)
tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')
for fpath in tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Darken tour hero background for contrast
    c = c.replace('brightness-85', 'brightness-65 contrast-110')
    c = c.replace('brightness-90', 'brightness-65 contrast-110')
    c = c.replace('brightness-95', 'brightness-65 contrast-110')
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("✓ Darkened hero background overlays across all pages for optimal menu and text legibility!")
