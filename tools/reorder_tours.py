import json

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

# Priority order requested by user:
# 1. Jungle extrême – spécial faune sauvage (slug: jungle-extreme)
# 2. Népal sauvage – de la jungle aux montagnes sacrées (slug: nepal-sauvage)
# 3. Chitwan + Bardia – l’aventure jungle complète (slug: chitwan-bardia-complete)

priority_slugs = [
    'jungle-extreme',
    'nepal-sauvage',
    'chitwan-bardia-complete'
]

# Extract prioritized tours
priority_tours = []
for slug in priority_slugs:
    for t in tours:
        if t['slug'] == slug:
            priority_tours.append(t)
            break

# Remaining tours in their current relative order
remaining_tours = [t for t in tours if t['slug'] not in priority_slugs]

# Reordered list
reordered_tours = priority_tours + remaining_tours

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'w', encoding='utf-8') as f:
    json.dump(reordered_tours, f, ensure_ascii=False, indent=2)

print("✓ Updated src/data/tours.json with top 3 priority tours!")
