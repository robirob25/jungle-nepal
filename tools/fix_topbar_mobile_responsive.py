import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

# Replace long top bar texts with clean, responsive, short text on mobile and complete text on desktop
# Mobile text: -100€ séjour nov. 2027 code JUNGLE100
# Desktop text: -100€ sur votre prochain séjour en novembre 2027 avec le code JUNGLE100

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # Clean top-bar banner texts
    c = re.sub(
        r'<span><strong>Exceptionnellement -100€</strong> sur votre prochain tour en novembre 2027 avec le code <span class="bg-white/15[^"]*">JUNGLE100</span></span>',
        '<span><strong class="text-amber-300">-100€</strong> sur votre séjour nov. 2027 <span class="hidden sm:inline">avec le code</span> <span class="bg-white/15 px-1.5 py-0.5 rounded text-amber-100 font-extrabold border border-amber-300/30 font-mono tracking-wider ml-1">JUNGLE100</span></span>',
        c
    )
    c = re.sub(
        r'<span><strong>-100€</strong> sur votre séjour nov 2027 avec le code <span class="bg-white/15[^"]*">JUNGLE100</span></span>',
        '<span><strong class="text-amber-300">-100€</strong> sur votre séjour nov. 2027 <span class="hidden sm:inline">avec le code</span> <span class="bg-white/15 px-1.5 py-0.5 rounded text-amber-100 font-extrabold border border-amber-300/30 font-mono tracking-wider ml-1">JUNGLE100</span></span>',
        c
    )

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Shortened top-bar banner for mobile in {fpath.split('/')[-1]}")

print("Done updating top-bar across all pages!")
