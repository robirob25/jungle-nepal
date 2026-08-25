import json, os, hashlib
from PIL import Image

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Add unique extra mammal if needed to round up to 20
mammiferes_count = sum(1 for i in items if i['category'] == 'mammiferes')
if mammiferes_count < 20:
    candidate = {
        "file": "/assets/drive_wildlife/Chital_1.webp",
        "title": "Cerf Axis en harde",
        "desc": "Cervidé tacheté emblématique des clairières de Bardia",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    }
    if not any(i['file'] == candidate['file'] for i in items):
        items.append(candidate)

print(f"Total unique photographs: {len(items)}")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, indent=2, ensure_ascii=False)

