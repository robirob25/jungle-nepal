import json, os
from PIL import Image

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/curated_gallery'
os.makedirs(dest_dir, exist_ok=True)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

batch = [
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501851823.jpg",
        "fname": "tigre_marquage_arbre_check.webp",
        "title": "Tigre du Bengale (Marquage)",
        "desc": "Marquage olfactif",
        "location": "Bardia",
        "category": "felins"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501857222.jpg",
        "fname": "gavial_gange_nage_riviere.webp",
        "title": "Gavial du Gange en nage",
        "desc": "Crocodilien préhistorique au museau effilé fendant le courant",
        "location": "Rivière Karnali • Bardia",
        "category": "reptiles"
    }
]

added_count = 0
for item in batch:
    src = item['src']
    img = Image.open(src).convert('RGB')
    
    # Check visual duplicate
    is_dup = False
    dup_match = ""
    for existing_file in items:
        ex_path = os.path.join('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public', existing_file['file'].lstrip('/'))
        if os.path.exists(ex_path):
            ex_img = Image.open(ex_path).convert('RGB')
            if abs(img.size[0]/img.size[1] - ex_img.size[0]/ex_img.size[1]) < 0.05:
                t1 = img.resize((32, 32))
                t2 = ex_img.resize((32, 32))
                diff = sum(abs(p1 - p2) for p1, p2 in zip(t1.tobytes(), t2.tobytes())) / (32 * 32 * 3)
                if diff < 15:
                    is_dup = True
                    dup_match = existing_file['title']
                    break
    
    if is_dup:
        print(f"⚠️ Duplicate detected and skipped: {src} matches '{dup_match}'")
        continue
    
    target_path = os.path.join(dest_dir, item['fname'])
    rel_path = f"/assets/curated_gallery/{item['fname']}"
    max_w = 2048
    if img.size[0] > max_w:
        ratio = max_w / float(img.size[0])
        new_h = int(float(img.size[1]) * ratio)
        img = img.resize((max_w, new_h), Image.Resampling.LANCZOS)
    img.save(target_path, 'WEBP', quality=90, method=6)
    print(f"✓ Processed new photo: {item['fname']} ({img.size})")
    
    items.append({
        "file": rel_path,
        "title": item['title'],
        "desc": item['desc'],
        "location": item['location'],
        "category": item['category']
    })
    added_count += 1

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, indent=2, ensure_ascii=False)

print(f"\nAdded {added_count} new unique photos. Total curated now: {len(items)}")
