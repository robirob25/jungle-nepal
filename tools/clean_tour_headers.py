import glob, re

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

for fpath in tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Remove the "Départs & Prix" button from the main header
    # Usually: <button onclick="scrollToBooking()" class="inline-flex items-center gap-2 bg-[#0e5c3e] ..."><span>Départs & Prix</span></button>
    c = re.sub(
        r'<button\s+onclick="scrollToBooking\(\)"\s+class="inline-flex items-center[^"]*">\s*<span>Départs & Prix</span>\s*</button>',
        '',
        c
    )
    c = re.sub(
        r'<a\s+href="[^"]*"\s+class="inline-flex items-center gap-2 bg-\[#0e5c3e\][^"]*">\s*<span>Départs & Prix</span>\s*</a>',
        '',
        c
    )

    # 2. Remove the "Réserver" button from the second sticky sub-nav bar
    # Usually: <div class="flex items-center gap-2 shrink-0">\s*<a href="/contact.html#formulaire-contact" ...>...<span>Réserver</span>...</a>\s*</div>
    c = re.sub(
        r'<div class="flex items-center gap-2 shrink-0">\s*<a\s+href="/contact\.html#formulaire-contact"[^>]*>[\s\S]*?<span>Réserver</span>[\s\S]*?</a>\s*</div>',
        '',
        c
    )

    # Also clean if plain button
    c = re.sub(
        r'<a\s+href="/contact\.html#formulaire-contact"\s+class="inline-flex items-center gap-1\.5[^"]*">\s*<span>Réserver</span>[\s\S]*?</a>',
        '',
        c
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print(f"✓ Successfully cleaned {len(tour_files)} tour pages!")
