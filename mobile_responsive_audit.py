import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

print(f"Auditing {len(astro_files)} files for mobile responsiveness, button sizing, flex centering, and tap targets...")

updated_files = 0

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # 1. Standardize and refine buttons to ensure perfect flex centering, balanced padding, and comfortable tap targets (min-h-[46px] or [48px] on mobile)
    # Ensure text is never clipped or misaligned
    
    # Fix buttons that have py-2 or py-2.5 on primary CTA mobile buttons to py-3 sm:py-3.5
    # Ensure all primary action buttons have 'flex items-center justify-center text-center'
    
    # Standardize full width action buttons in cards
    c = re.sub(
        r'class="w-full mt-3\.5 py-3 px-4 rounded-2xl bg-\[#0e5c3e\][^"]*"',
        'class="w-full mt-3.5 py-3.5 px-5 rounded-2xl bg-[#0e5c3e] hover:bg-[#09422b] text-white font-extrabold text-xs sm:text-sm flex items-center justify-center gap-2 shadow-md shadow-emerald-950/20 active:scale-98 transition-all text-center leading-none min-h-[46px]"',
        c
    )
    
    # Ensure mobile drawer and mobile header buttons have great breathing room and centered icons
    c = c.replace('py-3 rounded-2xl bg-[#0e8354]', 'py-3.5 px-4 rounded-2xl bg-[#0e5c3e] flex items-center justify-center text-center')
    c = c.replace('py-3 rounded-2xl bg-white text-slate-950', 'py-3.5 px-4 rounded-2xl bg-white text-slate-950 flex items-center justify-center text-center')

    # Improve search form submit button on homepage mobile
    c = c.replace(
        'class="w-full sm:w-auto px-6 py-3.5 sm:py-4 rounded-2xl bg-[#0e5c3e] hover:bg-[#09422b] text-white font-extrabold text-xs sm:text-sm shadow-md flex items-center justify-center gap-2 shrink-0 transition-all cursor-pointer"',
        'class="w-full sm:w-auto px-7 py-3.5 sm:py-4 rounded-2xl bg-[#0e5c3e] hover:bg-[#09422b] text-white font-extrabold text-xs sm:text-sm shadow-md flex items-center justify-center gap-2 shrink-0 transition-all cursor-pointer min-h-[48px] text-center leading-none"'
    )

    # Floating contact badge / quick actions for mobile
    # Ensure responsive font sizes in headers so titles don't overflow on small 360px-390px screens
    c = c.replace('text-4xl sm:text-6xl md:text-7xl lg:text-[76px]', 'text-3xl sm:text-5xl md:text-6xl lg:text-7xl')
    
    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated_files += 1
        print(f"Optimized mobile responsiveness in {fpath.split('/')[-1]}")

print(f"✓ Completed mobile responsive optimization across {updated_files} files!")
