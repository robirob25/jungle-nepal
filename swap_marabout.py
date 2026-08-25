import json

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Find tchitrec in top 20 and marabout in items
tchitrec_idx = None
marabout_idx = None

for idx, i in enumerate(items):
    if 'tchitrec' in i['file']:
        tchitrec_idx = idx
    if 'marabout_chevelu_pose_marais' in i['file'] or ('marabout' in i['file'] and 'pose' in i['file']) or ('marabout' in i['title'].lower() and 'affût' in i['title'].lower()):
        marabout_idx = idx

print(f"Tchitrec idx: {tchitrec_idx}, Marabout idx: {marabout_idx}")

if tchitrec_idx is not None and marabout_idx is not None:
    # Swap them
    items[tchitrec_idx], items[marabout_idx] = items[marabout_idx], items[tchitrec_idx]
    print(f"Successfully swapped! Position {tchitrec_idx+1} is now: {items[tchitrec_idx]['title']}")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, indent=2, ensure_ascii=False)

