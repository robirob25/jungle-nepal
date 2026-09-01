import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # 1. Desktop Nav in headers:
    c = re.sub(r'<a href="[^"]*#concept"[^>]*>L\'esprit safari</a>\s*', '', c)

    # 2. Mobile drawer items:
    c = re.sub(r'<!--\s*\d*\.?\s*L\'esprit safari\s*-->\s*<a href="[^"]*#concept"[^>]*>.*?<span>L\'esprit safari</span>.*?</a>\s*', '', c, flags=re.DOTALL)
    c = re.sub(r'<a href="[^"]*#concept"[^>]*>\s*<div[^>]*>.*?</div>\s*<span>L\'esprit safari</span>\s*</a>\s*', '', c, flags=re.DOTALL)

    # 3. Footer links:
    c = re.sub(r'<li>\s*<a href="[^"]*#concept"[^>]*>L\'esprit safari</a>\s*</li>\s*', '', c)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Removed L'esprit safari from menu in {fpath.split('/')[-1]}")

print("Done removing L'esprit safari across all navigation bars and footers!")
