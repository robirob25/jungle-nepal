with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    '<span>Mixe Jungle et Montagne (10)</span>',
    '<span>Mixe jungle et montagne (10)</span>'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Updated casing to 'Mixe jungle et montagne (10)' in index.astro!")
