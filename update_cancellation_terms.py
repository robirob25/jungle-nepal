import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

updated = 0
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    c = c.replace("Annulation flexible jusqu'à 30 jours", "Annulation flexible jusqu'à 45 jours")
    c = c.replace("jusqu'à 30 jours", "jusqu'à 45 jours")

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated += 1

print(f"Updated cancellation policy to 'jusqu'à 45 jours' across {updated} files!")
