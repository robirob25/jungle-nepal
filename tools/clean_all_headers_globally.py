import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in astro_files:
    fname = fpath.split('/')[-1]
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    
    # Clean L'esprit safari
    c = re.sub(r'<a[^>]*href="[^"]*#concept"[^>]*>\s*L\'esprit safari\s*</a>', '', c)
    # Clean Maîtres pisteurs
    c = re.sub(r'<a[^>]*href="[^"]*#galerie-faune"[^>]*>\s*Maîtres pisteurs\s*</a>', '', c)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Cleaned legacy nav links in {fname}")

print("Global header cleaning completed!")
