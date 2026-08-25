with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the tabs containing 🦜 and 🐊
c = c.replace('🦜 Oiseaux rares (26)', 'Oiseaux rares (26)')
c = c.replace('🐊 Reptiles & rivières (10)', 'Reptiles et rivières (10)')
c = c.replace('🐊 Reptiles & rivieres (10)', 'Reptiles et rivières (10)')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Removed bird and reptile emojis from wildlife gallery filter buttons in index.astro!")
