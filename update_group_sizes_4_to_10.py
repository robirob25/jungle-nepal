import json, re, glob, os

# 1. Update tours.json
tours_path = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json'
with open(tours_path, 'r', encoding='utf-8') as f:
    tours = json.load(f)

for tour in tours:
    if 'group_size' in tour:
        tour['group_size'] = tour['group_size'].replace('4 à 8', '4 à 10').replace('4-8', '4-10')
    if 'group_size_en' in tour:
        tour['group_size_en'] = tour['group_size_en'].replace('4 to 8', '4 to 10').replace('4-8', '4-10')

with open(tours_path, 'w', encoding='utf-8') as f:
    json.dump(tours, f, ensure_ascii=False, indent=2)
print("✓ Updated tours.json")

# 2. Update destinations.json
dest_path = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/destinations.json'
with open(dest_path, 'r', encoding='utf-8') as f:
    dests = json.load(f)

def recurse_replace(obj):
    if isinstance(obj, dict):
        return {k: recurse_replace(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [recurse_replace(item) for item in obj]
    elif isinstance(obj, str):
        return obj.replace('4 à 8', '4 à 10').replace('4 to 8', '4 to 10').replace('4-8', '4-10')
    return obj

dests = recurse_replace(dests)
with open(dest_path, 'w', encoding='utf-8') as f:
    json.dump(dests, f, ensure_ascii=False, indent=2)
print("✓ Updated destinations.json")

# 3. Update all .astro, .ts, .js, .json, .md files in src and layouts
all_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*', recursive=True)

for fpath in all_files:
    if os.path.isfile(fpath) and (fpath.endswith('.astro') or fpath.endswith('.json') or fpath.endswith('.js') or fpath.endswith('.ts')):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        orig = content
        # Standard replacements
        content = content.replace('4 à 8', '4 à 10')
        content = content.replace('4 to 8', '4 to 10')
        content = content.replace('4-8 pers.', '4-10 pers.')
        content = content.replace('4-8 pers', '4-10 pers')
        content = content.replace('4-8 personnes', '4-10 personnes')
        content = content.replace('4 à 8 explorateurs', '4 à 10 explorateurs')
        content = content.replace('4 à 8 voyageurs', '4 à 10 voyageurs')
        content = content.replace('4 to 8 explorers', '4 to 10 explorers')
        content = content.replace('4 à 8 participants', '4 à 10 participants')
        content = content.replace('4 à 8 pers', '4 à 10 pers')

        if content != orig:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated group size in {os.path.basename(fpath)}")

print("All group sizes successfully changed to 4 à 10 across the entire project!")
