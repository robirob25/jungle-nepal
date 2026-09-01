with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Add cachebuster ?v=2 to img_3.webp so the browser instantly loads Robin's real photo
c = c.replace('/assets/img_3.webp', '/assets/img_3.webp?v=2')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Added cachebuster to Robin's photo in index.astro!")
