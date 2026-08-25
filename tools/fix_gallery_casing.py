import json, re

# 1. Update wildlife_gallery.json
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    gallery = json.load(f)

for item in gallery:
    if 'location' in item and item['location']:
        loc = item['location']
        # Convert to sentence case: exactly first letter capital, rest lowercase
        # e.g. "Parc National de Bardia" -> "Parc national de Bardia"
        # "Canopée de Bardia" -> "Canopée de Bardia"
        # "Forêt dense de Bardia" -> "Forêt dense de Bardia"
        # "Plaines inondables de Bardia" -> "Plaines inondables de Bardia"
        loc = loc.replace("Parc National de Bardia", "Parc national de Bardia")
        loc = loc.replace("Parc National de Chitwan", "Parc national de Chitwan")
        loc = loc.replace("Parc National de Suklaphanta", "Parc national de Suklaphanta")
        item['location'] = loc

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(gallery, f, ensure_ascii=False, indent=2)

# 2. Update index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Filter buttons in gallery:
# 🧭 Tous les clichés (68)
# 🐅 Grands félins (12)
# 🦏 Grands mammifères (20)
# 🦜 Oiseaux rares (26)
# 🐊 Reptiles & rivières (10)
content = content.replace("Grands Félins (12)", "Grands félins (12)")
content = content.replace("Grands Mammifères (20)", "Grands mammifères (20)")
content = content.replace("Oiseaux Rares (26)", "Oiseaux rares (26)")
content = content.replace("Reptiles & Rivières (10)", "Reptiles & rivières (10)")

# Badges inside gallery cards:
content = content.replace("Parc National de Bardia", "Parc national de Bardia")
content = content.replace("Parc National de Chitwan", "Parc national de Chitwan")
content = content.replace("Parc National de Suklaphanta", "Parc national de Suklaphanta")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Wildlife gallery buttons and badges updated to sentence case!")
