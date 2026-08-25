import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)
json_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.json', recursive=True)

emojis_to_remove = [
    '🧘', '⚡', '⛺', '🚣', '🦜', '🐊', '🐅', '🦏', '🦌', '🏔️', '🐘', '👣', '👥', '🏡', '🐾', '🧭', '📖', '✉️', '⭐', '✨'
]

count = 0
for fpath in astro_files + json_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    for em in emojis_to_remove:
        if em in c:
            c = c.replace(em + ' ', '')
            c = c.replace(em, '')
            
    # Also clean phrases
    c = c.replace('Retraite & méditation', 'Retraite et méditation')
    c = c.replace('Aventure ++', 'Aventure')
    
    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        count += 1
        print(f"Cleaned remaining emojis in {fpath.split('/')[-1]}")

print(f"✓ Cleaned remaining emojis across {count} files!")
