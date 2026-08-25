import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove the plain number rating badges (4.8, 4.9, 5.0) in the 4 tour cards in a-propos.astro
# Pattern: <span class="text-amber-500 font-bold">4.8</span> or <span class="bg-emerald-600...">4.9</span> etc.
c = re.sub(r'<span class="text-amber-500 font-bold">\s*\d+\.\d+\s*</span>', '', c)
c = re.sub(r'<span class="[^"]*">\s*4\.[89]\s*</span>', '', c)
c = re.sub(r'<span class="[^"]*">\s*5\.0\s*</span>', '', c)

# Also check for class containing 4.8 / 4.9 in the cards header flex
c = c.replace(
    '<div class="flex items-center justify-between gap-2 text-xs font-semibold text-slate-500 mb-1">\n                <span>Micro-groupe 4 à 10 pers.</span>\n                \n              </div>',
    '<div class="text-xs font-semibold text-slate-500 mb-1"><span>Micro-groupe 4 à 10 pers.</span></div>'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Removed isolated rating numbers from tour cards in a-propos.astro!")
