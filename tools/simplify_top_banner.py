import re, glob

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

new_banner_text = '<span>✨ <strong>Exceptionnellement -100€</strong> sur votre prochain tour en novembre 2027 avec le code <span class="bg-white/15 px-2 py-0.5 rounded text-amber-300 font-extrabold border border-amber-300/30 font-mono tracking-wider ml-1">JUNGLE100</span></span>'
new_tour_banner_text = 'Exceptionnellement -100€ sur votre prochain tour en novembre 2027 avec le code <span class="bg-white/10 px-1.5 py-0.5 rounded text-white border border-white/20 font-mono font-bold">JUNGLE100</span>'

updated = 0
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    is_tour = '/tours/' in fpath

    if is_tour:
        # Replace in tour top bar
        c = re.sub(
            r'-\d+€\s+code\s+<span[^>]*>JUNGLE100</span>',
            new_tour_banner_text,
            c
        )
    else:
        # Replace in top-bar aside
        c = re.sub(
            r'<span>(?:🐅\s*)?<strong>Saison\s+2026-2027</strong>.*?JUNGLE100</span></span>',
            new_banner_text,
            c,
            flags=re.DOTALL
        )

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated += 1

print(f"Updated and simplified top announcement banner across {updated} files!")
