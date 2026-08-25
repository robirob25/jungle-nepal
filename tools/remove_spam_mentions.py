import re, glob

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

updated = 0
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    c = c.replace('🔒 Zéro spam. Vos données restent strictement confidentielles.', '🔒 Vos données restent strictement confidentielles.')
    c = c.replace('🔒 Vos données restent strictement confidentielles. Zéro spam garanti.', '🔒 Vos données restent strictement confidentielles.')
    c = c.replace('Zéro spam garanti.', '')
    c = c.replace('Zéro spam.', '')

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated += 1

print(f"Removed all mentions of spam across {updated} files!")
