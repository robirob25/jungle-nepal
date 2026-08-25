import json
import re

# 1. Update src/data/tours.json with rich accurate multi-categories
categories_mapping = {
    "bardia-explorateur": ["safari"],
    "babai-special": ["safari", "bivouac"],
    "bardia-babai-camping": ["safari", "bivouac"],
    "bardia-nuit-sauvage": ["safari", "bivouac"],
    "jungle-extreme": ["safari"],
    "chitwan-culture": ["chitwan"],
    "chitwan-bardia-complete": ["safari", "chitwan", "grand-tour"],
    "nepal-sauvage": ["safari", "grand-tour"],
    "nepal-immersion-totale": ["safari", "grand-tour"],
    "rafting-safari": ["bivouac", "aventure", "safari"],
    "rara-lake-bardia": ["aventure", "safari"],
    "tiji-mustang": ["culture"],
    "carnet-de-voyage": ["culture"],
    "immersion-spirituelle": ["culture"]
}

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

for t in tours:
    slug = t['slug']
    t['categories'] = categories_mapping.get(slug, ["safari"])
    t['category'] = t['categories'][0] # fallback

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'w', encoding='utf-8') as f:
    json.dump(tours, f, ensure_ascii=False, indent=2)

print("Updated src/data/tours.json with accurate multi-categories tags!")
