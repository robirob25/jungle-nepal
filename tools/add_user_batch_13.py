import json, os, hashlib
from PIL import Image

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/curated_gallery'
os.makedirs(dest_dir, exist_ok=True)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Calculate hashes of existing images
existing_hashes = {}
for i in items:
    fpath = os.path.join('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public', i['file'].lstrip('/'))
    if os.path.exists(fpath):
        with open(fpath, 'rb') as img_f:
            existing_hashes[i['file']] = hashlib.md5(img_f.read()).hexdigest()

batch = [
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501782158.jpg",
        "fname": "rhino_dup.webp",
        "title": "Rhinocéros unicorne et martins",
        "desc": "",
        "location": "Chitwan",
        "category": "mammiferes"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501784469.jpg",
        "fname": "petit_duc_indien_creux_arbre.webp",
        "title": "Petit-duc indien (Chouette au creux de l'arbre)",
        "desc": "Camouflage parfait dans une cavité de tronc aux côtés d'une toile d'araignée",
        "location": "Forêts sauvages de Bardia",
        "category": "oiseaux"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501788909.jpg",
        "fname": "tchitrec_paradis_longues_rectrices.webp",
        "title": "Tchitrec de paradis d'Asie (Asian Paradise Flycatcher)",
        "desc": "Oiseau mythique paré de ses longues plumes caudales d'un blanc pur",
        "location": "Sous-bois préservés de Bardia",
        "category": "oiseaux"
    },
    {
        "src": "/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.user_uploaded/media_1787501791365.jpg",
        "fname": "tigre_dup.webp",
        "title": "Tigre vertical",
        "desc": "",
        "location": "Bardia",
        "category": "felins"
    }
]

added_count = 0
duplicates_found = []

for item in batch:
    src = item['src']
    with open(src, 'rb') as f:
        src_bytes = f.read()
    
    # Check if image visually matches any existing image via PIL comparison
    img = Image.open(src).convert('RGB')
    
    # Let's compare thumbnail hash with existing ones
    is_dup = False
    for existing_file in items:
        ex_path = os.path.join('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public', existing_file['file'].lstrip('/'))
        if os.path.exists(ex_path):
            ex_img = Image.open(ex_path).convert('RGB')
            # If aspect ratio and sizes are similar, check difference
            if abs(img.size[0]/img.size[1] - ex_img.size[0]/ex_img.size[1]) < 0.05:
                # Downsample and compare diff
                t1 = img.resize((32, 32))
                t2 = ex_img.resize((32, 32))
                diff = sum(abs(p1 - p2) for p1, p2 in zip(t1.tobytes(), t2.tobytes())) / (32 * 32 * 3)
                if diff < 15: # visually identical
                    is_dup = True
                    duplicates_found.append((item['src'], existing_file['title'], existing_file['file']))
                    break
    
    if is_dup:
        print(f"⚠️ Duplicate detected and skipped: {item['src']} matches {duplicates_found[-1][1]}")
        continue
    
    # Not duplicate, save!
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
