with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove the aggressive drop-shadow filter on the logo in index.astro
c = c.replace(
    'class="h-14 sm:h-16 w-auto object-contain filter drop-shadow-[0_4px_10px_rgba(0,0,0,0.5)] group-hover:scale-100 transition-transform"',
    'class="h-12 sm:h-14 w-auto object-contain drop-shadow-md group-hover:scale-105 transition-transform duration-300"'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Refined logo sizing and shadow in index.astro!")
