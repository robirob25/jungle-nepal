import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove emojis from Layout.astro custom-tour-modal:
c = c.replace('<span>🐆 Expédition panthère des neiges</span>', '<span>Expédition panthère des neiges</span>')
c = c.replace('<span>🥾 Trekking</span>', '<span>Trekking</span>')
c = c.replace('<span>🤝 Rencontre avec des locaux</span>', '<span>Rencontre avec des locaux</span>')
c = c.replace('<span>📸 Photo animalière</span>', '<span>Photo animalière</span>')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Removed all emojis from custom tour modal in Layout.astro!")
