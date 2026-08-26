import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # 1. Desktop Nav links in headers:
    c = c.replace('href="/index.html#pisteurs"', 'href="/index.html#galerie-faune"')
    c = c.replace('href="#pisteurs"', 'href="#galerie-faune"')
    c = c.replace('>Maîtres pisteurs<', '>Galerie<')
    c = c.replace('>Maîtres pisteurs (Pawan & Kiran)<', '>Galerie faune sauvage<')

    # 2. Mobile drawers:
    c = c.replace('<span>Maîtres pisteurs</span>', '<span>Galerie</span>')

    # 3. Footer links:
    c = c.replace('<li><a href="/index.html#pisteurs" class="hover:text-slate-200 transition-colors">Maîtres pisteurs</a></li>', '<li><a href="/index.html#galerie-faune" class="hover:text-slate-200 transition-colors">Galerie faune sauvage</a></li>')
    c = c.replace('<li><a href="/index.html#galerie-faune" class="hover:text-slate-200 transition-colors">Maîtres pisteurs</a></li>', '<li><a href="/index.html#galerie-faune" class="hover:text-slate-200 transition-colors">Galerie faune sauvage</a></li>')

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Replaced Maîtres pisteurs with Galerie in {fpath.split('/')[-1]}")

print("Done replacing Maîtres pisteurs with Galerie anchor across headers and footers!")
