import json

# 1. Update src/data/tours.json with accurate multi-tag categories
tour_categories_map = {
    "bardia-explorateur": ["safari"],
    "chitwan-culture": ["chitwan"],
    "rafting-safari": ["rafting", "bivouac", "safari", "grand-tour"],
    "bardia-nuit-sauvage": ["safari", "bivouac"],
    "rara-lake-bardia": ["mustang-himalaya", "safari", "grand-tour"],
    "bardia-babai-camping": ["safari", "bivouac"],
    "nepal-immersion-totale": ["chitwan", "safari", "rafting", "grand-tour"],
    "babai-special": ["safari", "bivouac"],
    "chitwan-bardia-complete": ["chitwan", "safari", "bivouac", "rafting", "grand-tour"],
    "tiji-mustang": ["mustang-himalaya", "grand-tour"],
    "carnet-de-voyage": ["mustang-himalaya", "grand-tour"],
    "jungle-extreme": ["safari", "grand-tour"],
    "nepal-sauvage": ["safari", "mustang-himalaya", "grand-tour"],
    "immersion-spirituelle": ["mustang-himalaya", "grand-tour"]
}

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

for t in tours:
    slug = t['slug']
    if slug in tour_categories_map:
        t['categories'] = tour_categories_map[slug]

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'w', encoding='utf-8') as f:
    json.dump(tours, f, indent=2, ensure_ascii=False)

print("Updated src/data/tours.json with precise multi-tag categories!")

# Summary of counts
from collections import Counter
counts = Counter()
for t in tours:
    for cat in t['categories']:
        counts[cat] += 1

print("\nTour counts per category:")
for cat, count in counts.items():
    print(f"- {cat}: {count} tours")

