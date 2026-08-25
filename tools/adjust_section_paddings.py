with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. #carte-nepal: reduce py-16 sm:py-24 lg:py-32 -> py-14 sm:py-20 lg:py-24
c = c.replace(
    'section id="carte-nepal" class="py-16 sm:py-24 lg:py-32 bg-slate-950 text-white relative overflow-hidden border-t border-white/10"',
    'section id="carte-nepal" class="py-12 sm:py-16 lg:py-20 bg-slate-950 text-white relative overflow-hidden border-t border-white/10"'
)

# 2. #galerie-faune: reduce py-20 sm:py-28 lg:py-32 -> py-12 sm:py-16 lg:py-20
c = c.replace(
    'section id="galerie-faune" class="scroll-mt-16 sm:scroll-mt-20 sm: py-20 sm:py-28 lg:py-32 bg-[#020617] text-white relative overflow-hidden"',
    'section id="galerie-faune" class="scroll-mt-16 sm:scroll-mt-20 py-12 sm:py-16 lg:py-20 bg-[#020617] text-white relative overflow-hidden border-t border-white/10"'
)

# 3. #concept: reduce py-20 sm:py-28 lg:py-32 -> py-12 sm:py-16 lg:py-20
c = c.replace(
    'section id="concept" class="scroll-mt-16 sm:scroll-mt-20 sm: py-20 sm:py-28 lg:py-32 bg-slate-950 text-white relative overflow-hidden border-t border-white/10"',
    'section id="concept" class="scroll-mt-16 sm:scroll-mt-20 py-12 sm:py-16 lg:py-20 bg-slate-950 text-white relative overflow-hidden border-t border-white/10"'
)

# 4. #pisteurs: reduce py-16 sm:py-24 lg:py-28 -> py-12 sm:py-16 lg:py-20
c = c.replace(
    'section id="pisteurs" class="scroll-mt-16 sm:scroll-mt-20 py-16 sm:py-24 lg:py-28 bg-white border-t border-slate-200"',
    'section id="pisteurs" class="scroll-mt-16 sm:scroll-mt-20 py-12 sm:py-16 lg:py-20 bg-white border-t border-slate-200"'
)

# 5. #avis: reduce py-20 sm:py-28 lg:py-32 -> py-12 sm:py-16 lg:py-20
c = c.replace(
    'section id="avis" class="scroll-mt-16 sm:scroll-mt-20 sm: py-20 sm:py-28 lg:py-32 bg-[#f4efe6]/50 border-t border-slate-200 relative overflow-hidden"',
    'section id="avis" class="scroll-mt-16 sm:scroll-mt-20 py-12 sm:py-16 lg:py-20 bg-[#f4efe6]/50 border-t border-slate-200 relative overflow-hidden"'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Spacing refined across all homepage sections!")
