import glob, re

astro_pages = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/**/*.astro', recursive=True)

for fpath in astro_pages:
    fname = fpath.split('/')[-1]
    if fname == 'index.astro':
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    orig = c
    # Clean any old "L'esprit safari" from nav
    c = re.sub(r'<a href="[^"]*#concept"[^>]*>\s*L\'esprit safari\s*</a>', '', c)
    # Clean any old "Maîtres pisteurs" from nav
    c = re.sub(r'<a href="[^"]*#galerie-faune"[^>]*>\s*Maîtres pisteurs\s*</a>', '', c)
    
    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Cleaned legacy nav in {fname}")

print("Done verifying all headers across the site!")
