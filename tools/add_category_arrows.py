import re

# 1. New HTML for section#categories
categories_section_html = """  <!-- =========================================================================
       5. CATEGORIES FILTER CAROUSEL WITH NAVIGATION ARROWS
       ========================================================================= -->
  <section id="categories" class="py-4 sm:py-5 bg-white border-b border-slate-200/80 sticky top-0 z-30 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
      
      <!-- Left Arrow Desktop -->
      <button onclick="scrollCategories(-240)" class="hidden md:flex absolute -left-2 lg:-left-4 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full bg-white/95 backdrop-blur-md border border-slate-200 shadow-md items-center justify-center text-slate-700 hover:text-[#0e8354] hover:border-[#0e8354] hover:bg-white hover:scale-110 active:scale-95 transition-all z-10 cursor-pointer group" aria-label="Faire défiler à gauche">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-slate-600 group-hover:text-[#0e8354] transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
        </svg>
      </button>

      <!-- Scrollable Categories Container -->
      <div id="categories-scroll-container" class="flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1 scroll-smooth px-1 md:px-6">
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

      <!-- Right Arrow Desktop -->
      <button onclick="scrollCategories(240)" class="hidden md:flex absolute -right-2 lg:-right-4 top-1/2 -translate-y-1/2 w-8 h-8 rounded-full bg-white/95 backdrop-blur-md border border-slate-200 shadow-md items-center justify-center text-slate-700 hover:text-[#0e8354] hover:border-[#0e8354] hover:bg-white hover:scale-110 active:scale-95 transition-all z-10 cursor-pointer group" aria-label="Faire défiler à droite">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-slate-600 group-hover:text-[#0e8354] transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
        </svg>
      </button>

    </div>
  </section>"""

scroll_js = """
    function scrollCategories(amount) {
      const el = document.getElementById('categories-scroll-container');
      if (el) {
        el.scrollBy({ left: amount, behavior: 'smooth' });
      }
    }
"""

# Update index.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'<!-- =+\s*5\.\s*CATEGORIES.*?<!-- =+\s*6\.\s*LES 14 CIRCUITS'
html = re.sub(pattern, categories_section_html + '\n\n  <!-- =========================================================================\n       6. LES 14 CIRCUITS', html, flags=re.DOTALL)

if 'function scrollCategories' not in html:
    html = html.replace('function filterTrips(category) {', scroll_js + '\n    function filterTrips(category) {')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("1. Added navigation arrows to section#categories in index.html!")

# Update en/index.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/index.html', 'r', encoding='utf-8') as f:
    en_html = f.read()

en_categories_section = categories_section_html.replace('Tous les séjours', 'All Trips')
en_categories_section = en_categories_section.replace('Safaris et pistage Bardia', 'Bardia Safari & Tracking')
en_categories_section = en_categories_section.replace('Bivouacs et nuits sauvages', 'Wild Bivouac & Camping')
en_categories_section = en_categories_section.replace('Chitwan et rhinocéros', 'Chitwan & Rhinos')
en_categories_section = en_categories_section.replace('Treks et lac Rara', 'Treks & Rara Lake')
en_categories_section = en_categories_section.replace('Culture, yoga et carnet', 'Culture, Yoga & Art')
en_categories_section = en_categories_section.replace('Rafting Karnali', 'Karnali Rafting')

en_html = re.sub(pattern, en_categories_section + '\n\n  <!-- =========================================================================\n       6. LES 14 CIRCUITS', en_html, flags=re.DOTALL)

if 'function scrollCategories' not in en_html:
    en_html = en_html.replace('function filterTrips(category) {', scroll_js + '\n    function filterTrips(category) {')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/index.html', 'w', encoding='utf-8') as f:
    f.write(en_html)

print("2. Added navigation arrows to section#categories in en/index.html!")
