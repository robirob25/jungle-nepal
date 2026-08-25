with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    "Quatre façons d'éprouver le Népal",
    "Quatre façons de ressentir le Népal"
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Replaced 'éprouver' by 'de ressentir' in a-propos.astro!")
