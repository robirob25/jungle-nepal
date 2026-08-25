import re

new_categories_section_fr = """  <!-- =========================================================================
       5. CATEGORIES FILTER CAROUSEL (AVEC FLÈCHES VISIBLES < ET >)
       ========================================================================= -->
  <section id="categories" class="py-4 bg-white border-b border-slate-200 sticky top-0 z-30 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center">
      
      <!-- Flèche Gauche < -->
      <button id="cat-btn-left" onclick="scrollCategories(-280)" class="hidden sm:flex w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white hover:bg-emerald-50 border border-slate-300 hover:border-[#0e8354] shadow-md items-center justify-center text-slate-800 hover:text-[#0e8354] transition-all duration-200 hover:scale-110 active:scale-95 shrink-0 mr-3 cursor-pointer z-10" aria-label="Faire défiler vers la gauche">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
        </svg>
      </button>

      <!-- Conteneur des Catégories Scrollable -->
      <div id="categories-scroll-container" class="flex-1 flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1 scroll-smooth">
        <button onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-white font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-slate-900 hover:scale-105 active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="all">
          <i data-lucide="compass" class="w-4 h-4"></i>
          <span>Tous les séjours</span>
          <span class="bg-white/20 text-white text-[11px] px-2 py-0.5 rounded-full font-black">14</span>
        </button>

        <button onclick="filterTrips('safari')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="safari">
          <i data-lucide="binoculars" class="w-4 h-4 text-slate-900"></i>
          <span>Safaris et pistage Bardia</span>
        </button>

        <button onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="bivouac">
          <i data-lucide="tent" class="w-4 h-4 text-slate-900"></i>
          <span>Bivouacs et nuits sauvages</span>
        </button>

        <button onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="chitwan">
          <i data-lucide="trees" class="w-4 h-4 text-slate-900"></i>
          <span>Chitwan et rhinocéros</span>
        </button>

        <button onclick="filterTrips('trek')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="trek">
          <i data-lucide="mountain" class="w-4 h-4 text-slate-900"></i>
          <span>Treks et lac Rara</span>
        </button>

        <button onclick="filterTrips('culture')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="culture">
          <i data-lucide="palette" class="w-4 h-4 text-slate-900"></i>
          <span>Culture, yoga et carnet</span>
        </button>

        <button onclick="filterTrips('rafting')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="rafting">
          <i data-lucide="waves" class="w-4 h-4 text-slate-900"></i>
          <span>Rafting Karnali</span>
        </button>
      </div>

      <!-- Flèche Droite > -->
      <button id="cat-btn-right" onclick="scrollCategories(280)" class="hidden sm:flex w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white hover:bg-emerald-50 border border-slate-300 hover:border-[#0e8354] shadow-md items-center justify-center text-slate-800 hover:text-[#0e8354] transition-all duration-200 hover:scale-110 active:scale-95 shrink-0 ml-3 cursor-pointer z-10" aria-label="Faire défiler vers la droite">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
        </svg>
      </button>

    </div>
  </section>"""

# 1. Update index.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'<!-- =+\s*5\.\s*CATEGORIES.*?<!-- =+\s*6\.\s*LES 14 CIRCUITS'
html = re.sub(pattern, new_categories_section_fr + '\n\n  <!-- =========================================================================\n       6. LES 14 CIRCUITS', html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("1. Applied visible arrows < and > to index.html!")

# 2. Update en/index.html
new_categories_section_en = new_categories_section_fr.replace('Tous les séjours', 'All Trips')
new_categories_section_en = new_categories_section_en.replace('Safaris et pistage Bardia', 'Bardia Safari & Tracking')
new_categories_section_en = new_categories_section_en.replace('Bivouacs et nuits sauvages', 'Wild Bivouac & Camping')
new_categories_section_en = new_categories_section_en.replace('Chitwan et rhinocéros', 'Chitwan & Rhinos')
new_categories_section_en = new_categories_section_en.replace('Treks et lac Rara', 'Treks & Rara Lake')
new_categories_section_en = new_categories_section_en.replace('Culture, yoga et carnet', 'Culture, Yoga & Art')
new_categories_section_en = new_categories_section_en.replace('Rafting Karnali', 'Karnali Rafting')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/index.html', 'r', encoding='utf-8') as f:
    en_html = f.read()

en_html = re.sub(pattern, new_categories_section_en + '\n\n  <!-- =========================================================================\n       6. LES 14 CIRCUITS', en_html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/index.html', 'w', encoding='utf-8') as f:
    f.write(en_html)

print("2. Applied visible arrows < and > to en/index.html!")
