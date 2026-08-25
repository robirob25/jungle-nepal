import re, glob, os

# 1. Clean Layout.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

# Replace ✨ in footer / reassurance
layout = layout.replace('✨ Micro-groupes', 'Micro-groupes')
layout = layout.replace('✨ {isEn', '{isEn')

# Clean custom tour modal: remove decorative emojis from headings & badges, use premium mat styling
layout = layout.replace('<span>🌿</span> <span>Projet sur-mesure & Privatisé</span>', '<span>Projet sur-mesure & privatisé</span>')
layout = layout.replace('bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354]', 'bg-[#0e5c3e] hover:bg-[#09422b]')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)
print("✓ Cleaned Layout.astro")

# 2. Clean Header.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Header.astro', 'r', encoding='utf-8') as f:
    hdr = f.read()

hdr = hdr.replace('bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354]', 'bg-[#0e5c3e] hover:bg-[#09422b]')
hdr = hdr.replace('✨ Exceptionnellement', 'Exceptionnellement')
hdr = hdr.replace('✨ -100€', '-100€')
hdr = hdr.replace('✨ Créer', 'Créer')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/components/Header.astro', 'w', encoding='utf-8') as f:
    f.write(hdr)
print("✓ Cleaned Header.astro")

# 3. Clean index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx = f.read()

# Top banner
idx = idx.replace('<span>✨ <strong>-100€</strong>', '<span><strong>-100€</strong>')

# Clean section over-title pills into clean typography
# Carte section
idx = idx.replace(
    """        <span class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-950/80 border border-emerald-500/30 text-emerald-400 text-xs font-bold uppercase tracking-widest mb-3 sm:mb-4">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
          Géographie de vos expéditions
        </span>""",
    """        <p class="text-xs font-black tracking-widest uppercase text-emerald-400 mb-2 sm:mb-3">
          Géographie des expéditions
        </p>"""
)

# Galerie section
idx = idx.replace(
    """        <span class="inline-flex items-center gap-2 text-xs font-black uppercase tracking-widest text-emerald-400 bg-emerald-950/80 border border-emerald-500/30 px-4 py-1.5 rounded-full mb-4 shadow-inner">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
          Observations 100% Sauvages
        </span>""",
    """        <p class="text-xs font-black tracking-widest uppercase text-emerald-400 mb-2 sm:mb-3">
          Observations sur le terrain
        </p>"""
)

# Concept section
idx = idx.replace(
    """<div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-emerald-400/30 text-[#10b981] text-xs font-black uppercase tracking-widest mb-4"><i data-lucide="film" class="w-4 h-4 text-[#109363]"></i><span>Immersion sur le terrain</span></div>""",
    """<p class="text-xs font-black tracking-widest uppercase text-emerald-400 mb-2 sm:mb-3">Immersion sur le terrain</p>"""
)

# Pisteurs section
idx = idx.replace(
    """        <span class="inline-block text-xs font-bold uppercase tracking-widest text-[#0e8354] bg-emerald-50 border border-emerald-200 px-4 py-1.5 rounded-full mb-3">
          Sur le terrain depuis 20 ans
        </span>""",
    """        <p class="text-xs font-black tracking-widest uppercase text-[#0e8354] mb-2 sm:mb-3">
          Sur le terrain depuis 20 ans
        </p>"""
)

# 15 séjours header pill
idx = idx.replace(
    """          <div class="inline-flex items-center gap-2 text-xs font-black uppercase tracking-wider text-emerald-900 bg-emerald-100 px-3 py-1 rounded-full mb-3">
            <i data-lucide="sparkles" class="w-3.5 h-3.5 text-[#0e8354]"></i>
            <span>Départs garantis • Petits groupes de 4 à 10 explorateurs</span>
          </div>""",
    """          <p class="text-xs font-black tracking-widest uppercase text-[#0e8354] mb-2">
            Départs garantis • Petits groupes de 4 à 10 explorateurs
          </p>"""
)

# Clean button CTA gradients into deep forest mat green
idx = idx.replace('bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:bg-right bg-[length:200%_auto]', 'bg-[#0e5c3e] hover:bg-[#09422b]')
idx = idx.replace('bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354]', 'bg-[#0e5c3e] hover:bg-[#09422b]')
idx = idx.replace('bg-gradient-to-r from-[#0e8354] to-[#109363]', 'bg-[#0e5c3e] hover:bg-[#09422b]')

# Remove sparkles from custom tour CTA
idx = idx.replace('<span>✨</span>\n            <span>Créer un séjour sur-mesure</span>', '<span>Créer un séjour sur-mesure →</span>')
idx = idx.replace('<span>✨</span>\n        <span>Créer un séjour sur-mesure</span>', '<span>Créer un séjour sur-mesure</span>')

# Clean card badge stars e.g. "⭐ Best-seller" -> "Best-seller", "⭐ 100% Sauvage" -> "100% Sauvage"
idx = idx.replace('<span>⭐ Best-seller</span>', '<span>Best-seller</span>')
idx = idx.replace('<span>⭐ Grand classique</span>', '<span>Grand classique</span>')
idx = idx.replace('⭐ Best-seller', 'Best-seller')

# Clean card photo overlays: simplify top-left badge to a single elegant badge
# Remove redundant 4-10 pers pill overlaid on the photo since it's present in the card info
idx = re.sub(
    r'<span class="bg-black/40 backdrop-blur-md text-slate-200 text-xs px-2.5 py-1 rounded-full border border-white/15 font-semibold">\s*4-10 pers\.\s*</span>',
    '',
    idx
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx)
print("✓ Cleaned index.astro")

# 4. Clean all tour pages and other pages
all_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in all_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        tc = f.read()
    orig = tc

    tc = tc.replace('✨ Exceptionnellement', 'Exceptionnellement')
    tc = tc.replace('✨ -100€', '-100€')
    tc = tc.replace('✨ Micro-groupes', 'Micro-groupes')
    tc = tc.replace('✨ Sur-mesure', 'Sur-mesure')
    tc = tc.replace('bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:bg-right bg-[length:200%_auto]', 'bg-[#0e5c3e] hover:bg-[#09422b]')
    tc = tc.replace('bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354]', 'bg-[#0e5c3e] hover:bg-[#09422b]')
    tc = tc.replace('bg-gradient-to-r from-[#0e8354] to-[#109363]', 'bg-[#0e5c3e] hover:bg-[#09422b]')

    if tc != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(tc)
        print(f"✓ Cleaned {os.path.basename(fpath)}")

print("All AI artifacts & slop cleaned successfully across the entire site!")
