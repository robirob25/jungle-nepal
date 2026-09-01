with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    'Katmandou & Vallée de Babai',
    'Katmandou, Népal'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Updated Kiran location to 'Katmandou, Népal'")
