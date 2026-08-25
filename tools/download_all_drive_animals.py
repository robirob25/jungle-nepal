import re, os, glob, urllib.request
from PIL import Image

dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/assets/drive_wildlife'
os.makedirs(dest_dir, exist_ok=True)

# Step output files
step_files = glob.glob('/Users/robinrozier/.gemini/antigravity/brain/406afa48-f747-44c2-9fe0-716195ab2c87/.system_generated/steps/*/output.txt')

all_found_files = []

for sf in step_files:
    with open(sf, 'r', encoding='utf-8') as f:
        txt = f.read()
    
    matches = re.findall(r'\[Fichier\]\s+([^(\n]+?)\s*\(ID:\s*([^)]+)\)', txt)
    for name, fid in matches:
        name = name.strip()
        fid = fid.strip()
        all_found_files.append((name, fid))

print(f"Total files found in drive listings: {len(all_found_files)}")

# Filter for animal photos (exclude city/people/landscapes without animals)
# Words indicating non-animals to exclude:
exclude_words = ['chambre', 'salle de bain', 'batiment', 'coin canape', 'brainstorming', 'contrat', 'carte de visite', 'satisfaction', 'prospections', 'katmandou', 'lever de soleil', 'groupe de femmes', 'femmes', 'temple', 'village', 'bhaktapur']

animal_files = []
seen_ids = set()

for name, fid in all_found_files:
    if fid in seen_ids:
        continue
    seen_ids.add(fid)
    
    name_lower = name.lower()
    if any(ex in name_lower for ex in exclude_words):
        continue
    
    if any(name_lower.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp']):
        animal_files.append((name, fid))

print(f"Identified {len(animal_files)} candidate animal photos from Drive folders!")

downloaded_count = 0
for name, fid in animal_files:
    # sanitize filename
    clean_name = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', name)
    target_jpg = os.path.join(dest_dir, clean_name)
    target_webp = os.path.splitext(target_jpg)[0] + '.webp'
    
    if os.path.exists(target_webp) and os.path.getsize(target_webp) > 5000:
        downloaded_count += 1
        continue
    
    url = f"https://lh3.googleusercontent.com/d/{fid}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            if len(data) > 5000:
                with open(target_jpg, 'wb') as f:
                    f.write(data)
                
                # Convert to WebP
                img = Image.open(target_jpg).convert('RGB')
                max_w = 2048
                if img.size[0] > max_w:
                    ratio = max_w / float(img.size[0])
                    new_h = int(float(img.size[1]) * ratio)
                    img = img.resize((max_w, new_h), Image.Resampling.LANCZOS)
                img.save(target_webp, 'WEBP', quality=88, method=6)
                if os.path.exists(target_jpg) and target_jpg != target_webp:
                    os.remove(target_jpg)
                
                downloaded_count += 1
                print(f"✓ Downloaded & Converted: {name} -> {os.path.basename(target_webp)} ({img.size})")
    except Exception as e:
        print(f"✗ Failed {name} ({fid}): {e}")

print(f"\nSuccessfully downloaded and processed {downloaded_count} wildlife photos into public/assets/drive_wildlife/!")
