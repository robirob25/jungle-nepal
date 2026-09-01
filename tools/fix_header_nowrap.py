import glob, re

# Ensure strict single-line (whitespace-nowrap) on all nav elements and use standard responsive gap:
# Change "Contacte-nous" to "Contact" if needed or ensure whitespace-nowrap and gap-6 xl:gap-8

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # Make sure nav container has whitespace-nowrap and flex-nowrap
    c = c.replace(
        '<nav class="hidden lg:flex items-center gap-5 xl:gap-7 text-[13.5px] font-bold text-white/90 drop-shadow absolute left-1/2 -translate-x-1/2">',
        '<nav class="hidden lg:flex items-center gap-5 xl:gap-7 text-[13.5px] font-bold text-white/90 drop-shadow absolute left-1/2 -translate-x-1/2 whitespace-nowrap">'
    )
    c = c.replace(
        '<nav class="hidden lg:flex items-center gap-5 xl:gap-7 text-[13.5px] font-bold absolute left-1/2 -translate-x-1/2">',
        '<nav class="hidden lg:flex items-center gap-5 xl:gap-7 text-[13.5px] font-bold absolute left-1/2 -translate-x-1/2 whitespace-nowrap">'
    )

    # In index.astro and Header.astro: ensure all <a> tags have whitespace-nowrap and change Contacte-nous to Contact if desired
    c = c.replace('Contacte-nous</a>', 'Contact</a>')

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Fixed single-line nowrap in {fpath.split('/')[-1]}")

print("Done fixing header nowrap across all pages!")
