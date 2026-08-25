import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

updated = 0
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # Replace @domaine.com or other weird email placeholders with nom@email.com
    c = re.sub(r'placeholder=[\'"][^\'"]*@domaine\.com[\'"]', 'placeholder="nom@email.com"', c)
    c = re.sub(r'placeholder=[\'"]votre\.email@[^\'"]+[\'"]', 'placeholder="nom@email.com"', c)
    c = re.sub(r'placeholder=[\'"]Votre adresse e-mail[\'"]', 'placeholder="nom@email.com"', c)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated += 1

print(f"Updated email placeholder to 'nom@email.com' across {updated} files!")
