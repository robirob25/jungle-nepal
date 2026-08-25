import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

# Standardized Section Title Pattern:
# 1. Over-title: text-xs font-black tracking-widest uppercase mb-3 (text-[#0e8354] on light, text-slate-300 on dark)
# 2. Main Title (H2): font-black text-3xl sm:text-4xl lg:text-5xl tracking-tight leading-tight (text-slate-950 on light, text-white on dark)
# 3. Sub-title (P): text-base sm:text-lg text-slate-600 (on light) or text-slate-300 (on dark) leading-relaxed max-w-2xl mx-auto

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix all H2 section headers on index.astro to have identical font-black, tracking-tight, and sizing hierarchy:
# 1. Carte des destinations
c = re.sub(
    r'<h2 class="[^"]*text-2xl sm:text-4xl lg:text-5xl[^"]*">\s*Le Népal sauvage, <span class="[^"]*">d\'un sanctuaire à l\'autre</span>\.\s*</h2>',
    '<h2 class="font-black text-3xl sm:text-4xl lg:text-5xl text-white tracking-tight leading-tight">Le Népal sauvage, <span class="font-serif italic font-normal text-amber-100">d\'un sanctuaire à l\'autre</span>.</h2>',
    c
)

# 2. Galerie faune
c = re.sub(
    r'<h2 class="font-black text-3xl sm:text-5xl text-white tracking-tight leading-tight">\s*La faune du Terai dans son intimité brute\.\s*</h2>',
    '<h2 class="font-black text-3xl sm:text-4xl lg:text-5xl text-white tracking-tight leading-tight">La faune du Terai dans son intimité brute.</h2>',
    c
)

# 3. Concept / Esprit safari
c = re.sub(
    r'<h2 class="font-black text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-\[1\.1\]">\s*Vivre la jungle à hauteur d\'homme\.\s*</h2>',
    '<h2 class="font-black text-3xl sm:text-4xl lg:text-5xl text-white tracking-tight leading-tight">Vivre la jungle à hauteur d\'homme.</h2>',
    c
)

# 4. Pisteurs
c = re.sub(
    r'<h2 class="font-black text-3xl sm:text-5xl text-slate-900 tracking-tight">\s*Ceux qui vous ouvrent les portes <span class="[^"]*">du Népal</span>\s*</h2>',
    '<h2 class="font-black text-3xl sm:text-4xl lg:text-5xl text-slate-950 tracking-tight leading-tight">Ceux qui vous ouvrent les portes <span class="font-serif italic font-normal text-[#0e8354]">du Népal</span></h2>',
    c
)

# 5. Avis clients
c = re.sub(
    r'<h2 class="font-black text-3xl sm:text-5xl text-slate-900 tracking-tight">\s*Ceux qui ont vécu l\'immersion\.\s*</h2>',
    '<h2 class="font-black text-3xl sm:text-4xl lg:text-5xl text-slate-950 tracking-tight leading-tight">Ceux qui ont vécu l\'immersion.</h2>',
    c
)

# 6. FAQ
c = re.sub(
    r'<h2 class="font-black text-3xl sm:text-5xl text-slate-900 tracking-tight">\s*Questions fréquentes avant de partir\.\s*</h2>',
    '<h2 class="font-black text-3xl sm:text-4xl lg:text-5xl text-slate-950 tracking-tight leading-tight">Questions fréquentes avant de partir.</h2>',
    c
)

# 7. Surtitres standardisés
c = re.sub(
    r'<p class="text-xs font-black tracking-widest uppercase text-slate-200 mb-2 sm:mb-3">',
    '<p class="text-xs font-black tracking-widest uppercase text-slate-400 mb-3">',
    c
)
c = re.sub(
    r'<p class="text-xs font-black tracking-widest uppercase text-\[#0e8354\] mb-2 sm:mb-3">',
    '<p class="text-xs font-black tracking-widest uppercase text-[#0e8354] mb-3">',
    c
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Harmonized all section titles and subtitles across homepage!")
