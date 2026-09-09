import glob, re

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

for fpath in tour_files:
    fname = fpath.split('/')[-1]
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # Pattern 1:
    # <li class="flex items-start gap-2.5">
    #   <span class="w-1.5 h-1.5 rounded-full bg-[#0e5c3e] mt-1.5 shrink-0"></span>
    #   <span><p class="pt-3">...</p></span>
    # </li>
    
    # We want a clean, well-padded text block:
    # Remove the awkward bullet dot and unnecessary nested p with pt-3, or align properly:
    # Replace `<span class="w-1.5 h-1.5 rounded-full bg-[#0e5c3e] mt-1.5 shrink-0"></span>\s*<span><p class="pt-3">` with `<p class="text-slate-700 leading-relaxed">`
    
    # Let's clean all variations of this accordion day body
    c = re.sub(
        r'<ul class="pt-3 space-y-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">\s*<li class="flex items-start gap-2\.5">\s*<span class="w-1\.5 h-1\.5 rounded-full bg-\[#0e5c3e\] mt-1\.5 shrink-0"></span>\s*<span><p class="pt-3">(.*?)</p></span>\s*</li>\s*</ul>',
        r'<div class="pt-4 pb-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">\1</div>',
        c,
        flags=re.DOTALL
    )
    
    # Also clean if p has no pt-3
    c = re.sub(
        r'<ul class="pt-3 space-y-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">\s*<li class="flex items-start gap-2\.5">\s*<span class="w-1\.5 h-1\.5 rounded-full bg-\[#0e5c3e\] mt-1\.5 shrink-0"></span>\s*<span><p>(.*?)</p></span>\s*</li>\s*</ul>',
        r'<div class="pt-4 pb-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">\1</div>',
        c,
        flags=re.DOTALL
    )

    # General catch-all for any `<p class="pt-3">` inside accordion body
    c = re.sub(r'<span><p class="pt-3">(.*?)</p></span>', r'<p>\1</p>', c, flags=re.DOTALL)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Cleaned and fixed itinerary alignment in {fname}")

print("All tour itinerary accordions perfected!")
