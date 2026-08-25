import json, os, hashlib
from PIL import Image

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total items before deduplication: {len(items)}")

# 1. Exact file path deduplication
seen_paths = set()
# 2. Content hash deduplication
seen_hashes = set()
# 3. Small thumbnail pixel similarity deduplication
seen_pixel_hashes = set()

def get_pixel_hash(img_path):
    img = Image.open(img_path).convert('L').resize((16, 16), Image.Resampling.BILINEAR)
    pixels = list(img.getdata())
    avg = sum(pixels) / len(pixels)
    return "".join("1" if p > avg else "0" for p in pixels)

unique_items = []
duplicates_removed = 0

for item in items:
    rel_path = item['file']
    abs_path = "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public" + rel_path
    
    if not os.path.exists(abs_path):
        print(f"Skipping missing file: {abs_path}")
        continue
    
    # Path check
    if rel_path in seen_paths:
        print(f"Duplicate path removed: {rel_path}")
        duplicates_removed += 1
        continue
    
    # File content MD5 check
    with open(abs_path, 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    
    if file_hash in seen_hashes:
        print(f"Duplicate content MD5 removed: {rel_path} (matches existing)")
        duplicates_removed += 1
        continue
        
    # Visual perceptual hash check
    phash = get_pixel_hash(abs_path)
    
    # Check hamming distance to prevent almost identical burst shots
    is_duplicate = False
    for existing_phash in seen_pixel_hashes:
        hamming_dist = sum(c1 != c2 for c1, c2 in zip(phash, existing_phash))
        if hamming_dist <= 2: # extremely similar / same photo
            print(f"Visual near-duplicate removed: {rel_path} (hamming distance={hamming_dist})")
            duplicates_removed += 1
            is_duplicate = True
            break
            
    if is_duplicate:
        continue
        
    seen_paths.add(rel_path)
    seen_hashes.add(file_hash)
    seen_pixel_hashes.add(phash)
    unique_items.append(item)

print(f"\n================ DEDUPLICATION REPORT ================")
print(f"Removed {duplicates_removed} duplicate or visually identical photos.")
print(f"Remaining 100% strictly unique photos: {len(unique_items)}")

# Count per category
counts = {}
for i in unique_items:
    counts[i['category']] = counts.get(i['category'], 0) + 1

for c, count in sorted(counts.items()):
    print(f" - {c.upper()}: {count} unique photos")
print(f"======================================================\n")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(unique_items, f, indent=2, ensure_ascii=False)

