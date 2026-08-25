import glob, re

# Calibrate the homepage hero to a balanced, luminous yet legible setting
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx = f.read()

# Replace heavy dark overlays with a balanced, elegant, cinematic tint
old_idx_overlay = """      <!-- Deep Atmospheric Gradients & Dark Tint for Impeccable Text & Navbar Contrast -->
      <div class="absolute inset-0 z-10 bg-slate-950/60 pointer-events-none"></div>
      <div class="absolute inset-0 z-10 bg-gradient-to-b from-black/85 via-black/40 to-slate-950/95 pointer-events-none"></div>
      <div class="absolute inset-0 z-10 bg-gradient-to-t from-slate-950 via-transparent to-black/70 pointer-events-none"></div>"""

new_idx_overlay = """      <!-- Balanced Cinematic Gradient & Tint for Clarity & Warmth -->
      <div class="absolute inset-0 z-10 bg-slate-950/30 pointer-events-none"></div>
      <div class="absolute inset-0 z-10 bg-gradient-to-b from-black/60 via-transparent to-slate-950/70 pointer-events-none"></div>"""

idx = idx.replace(old_idx_overlay, new_idx_overlay)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx)

# Balance destination pages (annapurna, bardia, chitwan, suklaphanta, katmandou)
dest_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/*.astro')
for fpath in dest_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    c = re.sub(r'filter brightness-\d+ contrast-115', 'filter brightness-80 contrast-105', c)
    c = c.replace('opacity-35 scale-105', 'opacity-50 scale-105')
    c = re.sub(
        r'<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/85 to-black/95"></div>\s*<div class="absolute inset-0 bg-black/50"></div>',
        '<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/50 to-black/55"></div>',
        c
    )
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

# Balance a-propos.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    ap = f.read()
ap = re.sub(r'opacity-\d+ scale-105 transform filter brightness-\d+ contrast-115', 'opacity-55 scale-105 transform filter brightness-80 contrast-105', ap)
ap = re.sub(
    r'<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/80 to-black/95"></div>\s*<div class="absolute inset-0 bg-black/50"></div>',
    '<div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/45 to-black/60"></div>',
    ap
)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(ap)

# Balance contact.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'r', encoding='utf-8') as f:
    ct = f.read()
ct = re.sub(r'opacity-\d+ scale-105 filter brightness-\d+ contrast-115', 'opacity-55 scale-105 filter brightness-80 contrast-105', ct)
ct = re.sub(
    r'<div class="absolute inset-0 bg-gradient-to-r from-slate-950 via-slate-950/90 to-slate-950/75"></div>\s*<div class="absolute inset-0 bg-black/50"></div>',
    '<div class="absolute inset-0 bg-gradient-to-r from-slate-950/90 via-slate-950/65 to-slate-950/30"></div>',
    ct
)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/contact.astro', 'w', encoding='utf-8') as f:
    f.write(ct)

# Balance tour pages
tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')
for fpath in tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    c = c.replace('brightness-45 contrast-115', 'brightness-75 contrast-105')
    c = c.replace('opacity-30', 'opacity-50')
    c = c.replace('opacity-35', 'opacity-50')
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("✓ Rebalanced hero darkness across all pages to a balanced, luminous, and legible level!")
