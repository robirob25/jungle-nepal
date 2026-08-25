import re, glob, os

# 1. Standardize Header & Container alignment on Homepage (index.astro & en/index.astro)
for hp in ['/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro',
           '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro']:
    with open(hp, 'r', encoding='utf-8') as f:
        c = f.read()

    # Make top-bar static (not sticky) so sticky category filter bar sticks cleanly at top-0
    c = c.replace('class="bg-slate-950 text-slate-300 text-xs py-2 px-4 sticky top-0 z-50 border-b border-white/10 shadow-sm"',
                  'class="bg-slate-950 text-slate-300 text-xs py-2.5 px-4 border-b border-white/10 shadow-sm relative z-50"')
    
    # Align hero header inside max-w-7xl
    c = re.sub(
        r'<header class="absolute top-\[\d+px\] left-0 right-0 z-40 px-6 sm:px-12 lg:px-16 py-4 flex items-center justify-between text-white">',
        '<header class="absolute top-[42px] left-0 right-0 z-40 py-4 text-white">\n    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">',
        c
    )
    # Ensure closing div for header container
    if '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">' in c and '    </div>\n  </header>' not in c:
        c = c.replace('  </header>', '    </div>\n  </header>')

    # Sticky Filter bar sticks at top-0 cleanly with nice shadow and backdrop-blur
    c = c.replace('class="py-5 bg-white border-b border-slate-200 sticky top-0 z-30 shadow-sm"',
                  'class="py-4 sm:py-5 bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-0 z-30 shadow-[0_4px_20px_rgba(0,0,0,0.04)]"')

    # Section spacing harmony
    c = c.replace('py-16 sm:py-24 bg-safari-50', 'py-16 sm:py-24 lg:py-28 bg-[#faf8f5]')
    c = c.replace('py-24 sm:py-32 bg-slate-950', 'py-20 sm:py-28 lg:py-32 bg-slate-950')
    c = c.replace('py-20 sm:py-28 bg-white', 'py-20 sm:py-28 lg:py-32 bg-white')
    c = c.replace('py-24 bg-safari-100/70', 'py-20 sm:py-28 lg:py-32 bg-[#f4efe6]/50')

    with open(hp, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"✓ Perfected desktop spacing on {os.path.basename(hp)}")

# 2. Standardize all Tour Detail Pages (15 FR & 15 EN)
tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro') + \
             glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/tours/*.astro')

for tp in tour_files:
    with open(tp, 'r', encoding='utf-8') as f:
        c = f.read()

    # Top-bar is static at top, so main header sticks at top-0 seamlessly
    c = re.sub(
        r'<aside aria-label="Bannière d\'information" class="bg-slate-950 text-slate-300 text-xs py-2 px-4 sticky top-0 z-50 border-b border-white/10 shadow-sm">',
        '<aside aria-label="Bannière d\'information" class="bg-slate-950 text-slate-300 text-xs py-2 px-4 border-b border-white/10 shadow-sm relative z-50">',
        c
    )
    
    # Header sticks cleanly at top-0
    c = re.sub(
        r'<header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-8 z-40',
        '<header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-0 z-40',
        c
    )

    # Sub-nav sticks cleanly directly under header at top-[69px] sm:top-[77px] with max-w-7xl container
    c = re.sub(
        r'<div class="sticky top-\[\d+px\][^>]*z-30 bg-white/95 backdrop-blur-md border-b border-slate-200 py-[\d\.]+ sm:py-[\d\.]+ mb-[\d\.]+ sm:mb-[\d\.]+ shadow-sm">',
        '<div class="sticky top-[68px] sm:top-[76px] z-30 bg-white/95 backdrop-blur-md border-b border-slate-200 py-3 mb-8 sm:mb-10 shadow-sm">',
        c
    )

    # Main Grid spacing: lg:col-span-8 and lg:col-span-4 with gap-8 lg:gap-12
    c = c.replace('class="grid grid-cols-1 lg:grid-cols-12 gap-10"', 'class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12"')
    c = c.replace('class="grid grid-cols-1 lg:grid-cols-12 gap-8"', 'class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12"')

    # Left Column section spacing: space-y-12 lg:space-y-14
    c = c.replace('class="lg:col-span-8 space-y-12"', 'class="lg:col-span-8 space-y-12 lg:space-y-14"')

    # Right Column Sticky Booking card: top-32 lg:top-36
    c = c.replace('class="sticky top-28', 'class="sticky top-[130px]')

    # Day by Day timeline vertical line position & length
    c = c.replace(
        'before:absolute before:inset-0 before:left-4 before:w-0.5 before:bg-slate-200',
        'before:absolute before:top-6 before:bottom-6 before:left-4 before:w-0.5 before:bg-emerald-200/80'
    )
    c = c.replace(
        'before:absolute before:inset-0 before:left-4 before:w-0.5 before:bg-emerald-200',
        'before:absolute before:top-6 before:bottom-6 before:left-4 before:w-0.5 before:bg-emerald-200/80'
    )

    with open(tp, 'w', encoding='utf-8') as f:
        f.write(c)

print(f"✓ Perfected desktop layout and sticky stacking on all {len(tour_files)} tour pages!")

# 3. Standardize About & Destination pages
about_files = ['/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro',
               '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/a-propos.astro']

for ap in about_files:
    with open(ap, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('class="bg-slate-950 text-slate-300 text-xs py-2 px-4 sticky top-0 z-50 border-b border-white/10 shadow-sm"',
                  'class="bg-slate-950 text-slate-300 text-xs py-2.5 px-4 border-b border-white/10 shadow-sm relative z-50"')
    c = re.sub(
        r'<header class="absolute top-\[\d+px\] left-0 right-0 z-40 px-6 sm:px-12 lg:px-16 py-4 flex items-center justify-between text-white">',
        '<header class="absolute top-[42px] left-0 right-0 z-40 py-4 text-white">\n    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">',
        c
    )
    if '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between">' in c and '    </div>\n  </header>' not in c:
        c = c.replace('  </header>', '    </div>\n  </header>')
    with open(ap, 'w', encoding='utf-8') as f:
        f.write(c)

print("✓ Perfected desktop layout on About pages!")
