import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

# Replace rounded-3xl with rounded-2xl or rounded-xl on dropdowns and sub-menus
# Also change the inner items rounded-2xl to rounded-xl

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # Destinations Dropdown container
    c = c.replace(
        'class="border border-white/10 rounded-3xl p-3 shadow-[0_25px_60px_rgba(0,0,0,0.8)] space-y-1 text-white"',
        'class="border border-white/10 rounded-2xl p-3 shadow-[0_25px_60px_rgba(0,0,0,0.8)] space-y-1 text-white"'
    )
    c = c.replace(
        'class="border border-white/15 rounded-3xl p-3 shadow-[0_25px_60px_rgba(0,0,0,0.8)] space-y-1 text-white"',
        'class="border border-white/15 rounded-2xl p-3 shadow-[0_25px_60px_rgba(0,0,0,0.8)] space-y-1 text-white"'
    )
    
    # Bottom button inside dropdown: rounded-2xl -> rounded-xl
    c = c.replace(
        'class="block w-full text-center py-2 rounded-2xl bg-[#0e5c3e]',
        'class="block w-full text-center py-2.5 rounded-xl bg-[#0e5c3e]'
    )
    c = c.replace(
        'class="block w-full text-center py-2 rounded-2xl bg-[#0e8354]',
        'class="block w-full text-center py-2.5 rounded-xl bg-[#0e5c3e]'
    )

    # Sub-item links inside dropdown
    c = c.replace(
        'class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item"',
        'class="flex items-center gap-3 p-2.5 rounded-xl hover:bg-white/10 transition-colors group/item"'
    )

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Adjusted dropdown border radius in {fpath.split('/')[-1]}")

print("Done adjusting dropdown border radius across all headers!")
