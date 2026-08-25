import re, glob, os

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours/*.html') + \
             glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/tours/*.html') + \
             glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro') + \
             glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/tours/*.astro')

for fpath in tour_files:
    if not os.path.exists(fpath): continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    is_en = '/en/' in fpath

    if is_en:
        new_subnav = """    <!-- STICKY SUB-NAV WEROAD -->
    <div class="sticky top-[68px] sm:top-[76px] z-30 py-4 sm:py-5 mb-8 sm:mb-10 before:content-[''] before:absolute before:top-0 before:left-1/2 before:-translate-x-1/2 before:w-[100vw] before:h-full before:bg-white/95 before:backdrop-blur-md before:border-b before:border-slate-200 before:-z-10 before:shadow-sm">
      <div class="flex items-center gap-6 sm:gap-10 overflow-x-auto no-scrollbar text-sm font-bold text-slate-600 px-4 sm:px-6 lg:px-8 py-0.5">
        <a href="#apercu" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Overview</a>
        <a href="#pour-moi" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Trip Profile</a>
        <a href="#programme" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Detailed Itinerary</a>
        <a href="#inclusions" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Included & Extras</a>
        <a href="#avis-voyageurs" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Reviews</a>
        <a href="#faq" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">FAQ</a>
      </div>
    </div>"""
    else:
        new_subnav = """    <!-- STICKY SUB-NAV WEROAD -->
    <div class="sticky top-[68px] sm:top-[76px] z-30 py-4 sm:py-5 mb-8 sm:mb-10 before:content-[''] before:absolute before:top-0 before:left-1/2 before:-translate-x-1/2 before:w-[100vw] before:h-full before:bg-white/95 before:backdrop-blur-md before:border-b before:border-slate-200 before:-z-10 before:shadow-sm">
      <div class="flex items-center gap-6 sm:gap-10 overflow-x-auto no-scrollbar text-sm font-bold text-slate-600 px-4 sm:px-6 lg:px-8 py-0.5">
        <a href="#apercu" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Aperçu</a>
        <a href="#pour-moi" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Profil Voyage</a>
        <a href="#programme" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Itinéraire détaillé</a>
        <a href="#inclusions" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Inclus & Extras</a>
        <a href="#avis-voyageurs" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Avis</a>
        <a href="#faq" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">FAQ</a>
      </div>
    </div>"""

    c_new = re.sub(
        r'<!-- STICKY SUB-NAV WEROAD -->.*?<!-- 2-COLUMN MAIN CONTENT GRID -->',
        new_subnav + '\n\n    <!-- 2-COLUMN MAIN CONTENT GRID -->',
        c,
        flags=re.DOTALL
    )

    if c_new != c:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c_new)
        print(f"Updated {os.path.basename(fpath)}")

print("Done.")
