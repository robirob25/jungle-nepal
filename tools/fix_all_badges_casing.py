import json, re, glob, os

# 1. Update tours.json
tours_json_path = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json'
with open(tours_json_path, 'r', encoding='utf-8') as f:
    tours = json.load(f)

# Conversion map for badges: exactly 1 capital letter (the first one)
badge_replacements = {
    # Full with emojis or without
    "⭐ Best-Seller": "⭐ Best-seller",
    "Best-Seller": "Best-seller",
    "🦏 Rhinos & Tharu": "🦏 Rhinos & tharu",
    "Rhinos & Tharu": "Rhinos & tharu",
    "🚣 Rafting & Safari": "🚣 Rafting & safari",
    "Rafting & Safari": "Rafting & safari",
    "🌙 Micro-Aventure": "🌙 Micro-aventure",
    "Micro-Aventure": "Micro-aventure",
    "🏔️ Expédition 4x4 & Lac Sacré": "🏔️ Expédition 4x4 & lac sacré",
    "Expédition 4x4 & Lac Sacré": "Expédition 4x4 & lac sacré",
    "Expédition 4×4 & Lac Sacré": "Expédition 4x4 & lac sacré",
    "⛺ Bivouac Sauvage": "⛺ Bivouac sauvage",
    "Bivouac Sauvage": "Bivouac sauvage",
    "🔥 Promo -300€": "🔥 Promo -300€",
    "Promo -300€": "Promo -300€",
    "⚡ Aventure ++": "⚡ Aventure ++",
    "Aventure ++": "Aventure ++",
    "🌿 Double Safari Parcs": "🌿 Double safari parcs",
    "Double Safari Parcs": "Double safari parcs",
    "🕉️ Spécial Culture": "🕉️ Spécial culture",
    "Spécial Culture": "Spécial culture",
    "🎨 Spécial Dessin & Carnet": "🎨 Spécial dessin & carnet",
    "Spécial Dessin & Carnet": "Spécial dessin & carnet",
    "🐅 Passion Faune Pro": "🐅 Passion faune pro",
    "Passion Faune Pro": "Passion faune pro",
    "❤️ Coup de cœur": "❤️ Coup de cœur",
    "Coup de cœur": "Coup de cœur",
    "🧘 Retraite & Méditation": "🧘 Retraite & méditation",
    "Retraite & Méditation": "Retraite & méditation",
    "🏔️ Himalaya, Mustang & Spiritualité": "🏔️ Himalaya, mustang & spiritualité",
    "Himalaya, Mustang & Spiritualité": "Himalaya, mustang & spiritualité",
}

for tour in tours:
    if 'badge' in tour and tour['badge']:
        b = tour['badge']
        if b in badge_replacements:
            tour['badge'] = badge_replacements[b]
        else:
            # Fallback lowercase after first letter
            # Keep emoji at start if any
            m = re.match(r'^(\S+\s+)?(.*)$', b)
            if m:
                prefix = m.group(1) or ''
                rest = m.group(2)
                if rest:
                    tour['badge'] = prefix + rest[0].upper() + rest[1:].lower()

with open(tours_json_path, 'w', encoding='utf-8') as f:
    json.dump(tours, f, ensure_ascii=False, indent=2)
print("✓ tours.json badges updated")

# 2. Update all .astro files across the project
astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    orig = content
    for old_b, new_b in badge_replacements.items():
        content = content.replace(old_b, new_b)
    
    # Extra check for common patterns like 'Expédition 4x4 & Lac Sacré'
    content = re.sub(r'Expédition 4[x×]4 & Lac Sacré', 'Expédition 4x4 & lac sacré', content)
    content = re.sub(r'Best-Seller', 'Best-seller', content)
    content = re.sub(r'Micro-Aventure', 'Micro-aventure', content)
    content = re.sub(r'Bivouac Sauvage', 'Bivouac sauvage', content)
    content = re.sub(r'Double Safari Parcs', 'Double safari parcs', content)
    content = re.sub(r'Spécial Culture', 'Spécial culture', content)
    content = re.sub(r'Spécial Dessin & Carnet', 'Spécial dessin & carnet', content)
    content = re.sub(r'Passion Faune Pro', 'Passion faune pro', content)
    content = re.sub(r'Retraite & Méditation', 'Retraite & méditation', content)
    content = re.sub(r'Rafting & Safari', 'Rafting & safari', content)
    content = re.sub(r'Rhinos & Tharu', 'Rhinos & tharu', content)

    if content != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Updated badges in {os.path.basename(fpath)}")

print("All badges converted to sentence case (one single capital letter)!")
