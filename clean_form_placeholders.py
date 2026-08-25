import re, glob

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

updated = 0
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # Remove or clean personal name placeholders
    c = re.sub(r'placeholder=[\'"]Ex:\s*(?:Robin|Thomas|Jean)[\'"]', 'placeholder="Votre prénom"', c)
    c = re.sub(r'placeholder=[\'"]Ex:\s*(?:Rozier|Dupont|Martin)[\'"]', 'placeholder="Votre nom"', c)
    c = re.sub(r'placeholder=[\'"](?:robin|nom)@exemple\.com[\'"]', 'placeholder="votre.email@domaine.com"', c)
    c = re.sub(r'placeholder=[\'"]\+33\s*6\s*95\s*41\s*32\s*27[\'"]', 'placeholder="+33 6 12 34 56 78"', c)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated += 1

print(f"Cleaned generic placeholders across {updated} files!")
