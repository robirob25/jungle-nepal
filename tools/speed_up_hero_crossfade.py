with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace slow transition duration-1000 with ultra-smooth fast crossfade duration-500 or duration-400:
c = c.replace('transition-all duration-1000 ease-in-out', 'transition-opacity duration-400 ease-out')
c = c.replace('transition-all duration-700 ease-in-out', 'transition-opacity duration-400 ease-out')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Accelerated hero slide crossfade transition to 400ms ease-out for immediate, snappy image switching!")
