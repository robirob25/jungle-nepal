import glob, re

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

for fpath in tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Remove empty green square / dot: <span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-emerald-50 text-[#0e8354] font-black text-xs shrink-0"></span>
    c = re.sub(
        r'<span class="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-emerald-50 text-\[#0e8354\] font-black text-xs shrink-0">\s*</span>',
        '',
        c
    )
    # Also handle w-8 h-8 or similar
    c = re.sub(
        r'<span class="[^"]*bg-emerald-50[^"]*shrink-0">\s*</span>',
        '',
        c
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print(f"✓ Removed empty green square container across {len(tour_files)} tour pages!")
