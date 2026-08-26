import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/nepal-sauvage.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the badge 'Himalaya, Mustang et spiritualité' with 'Mixe jungle et montagne'
c = c.replace(
    'Himalaya, Mustang et spiritualité\n          </span>',
    'Mixe jungle et montagne\n          </span>'
)
c = c.replace(
    'Himalaya, Mustang et spiritualité</span>',
    'Mixe jungle et montagne</span>'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/nepal-sauvage.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Updated badge to 'Mixe jungle et montagne' in nepal-sauvage.astro!")
