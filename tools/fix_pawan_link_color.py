with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the white text link class with readable emerald / dark link class in a-propos.astro
c = c.replace(
    'class="text-slate-200 hover:text-slate-200 underline decoration-emerald-500/30 underline-offset-2 transition-colors">Parc National de Bardia</a>',
    'class="text-[#0e8354] hover:text-[#0c6d46] font-bold underline decoration-emerald-500/30 underline-offset-2 transition-colors">Parc National de Bardia</a>'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Fixed 'Parc National de Bardia' link color in Pawan's bio card!")
