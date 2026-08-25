import re, glob, os

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro') + \
             glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/tours/*.astro')

for fpath in tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    is_en = '/en/' in fpath

    # Clean subnav structure
    if is_en:
        clean_subnav = """    <!-- STICKY SUB-NAV WEROAD -->
    <div class="sticky top-[68px] sm:top-[76px] z-30 bg-white/95 backdrop-blur-md border-b border-slate-200 py-3 mb-8 sm:mb-10 shadow-sm">
      <div class="flex items-center gap-4 sm:gap-6 overflow-x-auto no-scrollbar text-xs sm:text-sm font-bold text-slate-600 px-1 py-0.5">
        <a href="#apercu" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Overview</a>
        <a href="#pour-moi" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Trip Profile</a>
        <a href="#programme" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Detailed Itinerary</a>
        <a href="#inclusions" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Included & Extras</a>
        <a href="#avis-voyageurs" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Reviews</a>
        <a href="#faq" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">FAQ</a>
      </div>
    </div>"""
    else:
        clean_subnav = """    <!-- STICKY SUB-NAV WEROAD -->
    <div class="sticky top-[68px] sm:top-[76px] z-30 bg-white/95 backdrop-blur-md border-b border-slate-200 py-3 mb-8 sm:mb-10 shadow-sm">
      <div class="flex items-center gap-4 sm:gap-6 overflow-x-auto no-scrollbar text-xs sm:text-sm font-bold text-slate-600 px-1 py-0.5">
        <a href="#apercu" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Aperçu</a>
        <a href="#pour-moi" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Profil Voyage</a>
        <a href="#programme" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Itinéraire détaillé</a>
        <a href="#inclusions" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Inclus & Extras</a>
        <a href="#avis-voyageurs" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">Avis</a>
        <a href="#faq" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354] whitespace-nowrap">FAQ</a>
      </div>
    </div>"""

    # Replace old subnav block
    c = re.sub(
        r'<!-- STICKY SUB-NAV.*?<!-- 2-COLUMN MAIN CONTENT GRID -->',
        clean_subnav + '\n\n    <!-- 2-COLUMN MAIN CONTENT GRID -->',
        c,
        flags=re.DOTALL
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print(f"Fixed sticky subnav HTML tags across all {len(tour_files)} tour pages!")
