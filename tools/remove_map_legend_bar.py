import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove the Mobile-Friendly Legend Bar under the map:
pattern = r'<!-- Mobile-Friendly Legend Bar -->\s*<div class="mt-3 sm:mt-4 flex items-center justify-between gap-2 text-\[11px\] sm:text-xs text-slate-300 pt-2 border-t border-white/10">.*?</div>\s*'
c = re.sub(pattern, '', c, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Removed legend bar (Bardia Chitwan... / Guide des 5 régions) from under the map in index.astro!")
