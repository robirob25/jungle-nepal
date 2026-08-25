import glob, re

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

updated = 0
for tp in tour_files:
    with open(tp, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    # Replace sticky top-[...] with sticky top-[136px]
    c = re.sub(r'sticky\s+top-\[\d+px\]', 'sticky top-[136px]', c)

    if c != orig:
        with open(tp, 'w', encoding='utf-8') as f:
            f.write(c)
        updated += 1

print(f"Fixed sticky top offset to top-[136px] across {updated} tour detail pages!")
