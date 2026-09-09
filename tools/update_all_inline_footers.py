import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/**/*.astro', recursive=True)

for fpath in astro_files:
    fname = fpath.split('/')[-1]
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # Pattern for footer legal links
    old_block = """        <span>•</span>
        <a href="/a-propos.html" class="hover:text-white transition-colors">À propos</a>"""
        
    new_block = """        <span>•</span>
        <a href="/mentions-legales" class="hover:text-white transition-colors">Mentions légales</a>
        <span>•</span>
        <a href="/a-propos.html" class="hover:text-white transition-colors">À propos</a>"""

    if old_block in c and "/mentions-legales" not in c:
        c = c.replace(old_block, new_block)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Added Mentions légales link in {fname}")

print("All footers updated!")
