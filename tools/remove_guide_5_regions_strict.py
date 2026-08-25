import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove the remaining guide des 5 régions block and extra closing tags cleanly
c = re.sub(
    r'<a href="/destinations\.html" class="text-slate-200 hover:text-white font-bold shrink-0 transition-colors">\s*Guide des 5 régions →\s*</a>\s*</div>',
    '',
    c
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Strictly removed Guide des 5 régions from index.astro!")
