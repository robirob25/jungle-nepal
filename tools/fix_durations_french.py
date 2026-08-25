import json, re, glob, os

# 1. Fix tours.json French duration field
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

for tour in tours:
    if 'duration' in tour:
        d = tour['duration']
        # Convert "5 Days" -> "5 jours", "18 Days" -> "18 jours", etc.
        d_fr = re.sub(r'(\d+)\s*Days?', r'\1 jours', d, flags=re.IGNORECASE)
        tour['duration'] = d_fr
    if 'daysCount' in tour and ('duration' not in tour or not tour['duration']):
        tour['duration'] = f"{tour['daysCount']} jours"

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'w', encoding='utf-8') as f:
    json.dump(tours, f, ensure_ascii=False, indent=2)

print("✓ Fixed durations in tours.json")

# 2. Fix all .astro files across src (index.astro, tours/*.astro)
all_astro = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in all_astro:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    orig = content

    # Replace hardcoded "X Days" in French spans
    # e.g., <span>5 Days</span>, <span>18 Days</span>, <span>17 Days</span>, etc.
    content = re.sub(r'<span>(\d+)\s*Days</span>', r'<span>\1 jours</span>', content, flags=re.IGNORECASE)
    content = re.sub(r'>(\d+)\s*Days<', r'>\1 jours<', content, flags=re.IGNORECASE)
    content = re.sub(r'\"(\d+)\s*Days\"', r'"\1 jours"', content, flags=re.IGNORECASE)

    # Clean up any bad mixes like "5 jours / pers." -> "5 jours"
    if content != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Fixed duration strings in {os.path.basename(fpath)}")

print("All durations successfully converted to clean French 'X jours'!")
