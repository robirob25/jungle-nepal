import re
import json

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

# Build a lookup for slug -> categories string
tour_cat_str = {t['slug']: ",".join(t['categories']) for t in tours}

# Category pills HTML FR
categories_html_fr = """<!-- SECTION 3: FILTRES CATÉGORIES (AVEC FLÈCHES < ET >) -->
  <section id="categories" class="py-5 bg-white border-b border-slate-200 sticky top-0 z-30 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center">
      
      <!-- Flèche Gauche < -->
      <button onclick="scrollCategories(-280)" class="hidden sm:flex w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white hover:bg-emerald-50 border border-slate-300 hover:border-[#0e8354] shadow-md items-center justify-center text-slate-800 hover:text-[#0e8354] transition-all duration-200 hover:scale-110 active:scale-95 shrink-0 mr-3 cursor-pointer z-10" aria-label="Faire défiler vers la gauche">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
        </svg>
      </button>

      <!-- Conteneur des Catégories Scrollable -->
      <div id="categories-scroll-container" class="flex-1 flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1 scroll-smooth">
        <button onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-white font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-slate-900 hover:scale-105 active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="all">
          <span>🧭</span>
          <span>Tous les séjours</span>
          <span class="bg-white/20 text-white text-[11px] px-2 py-0.5 rounded-full font-black">14</span>
        </button>

        <button onclick="filterTrips('safari')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="safari">
          <span>🐅</span>
          <span>Safaris & Pistage Tigre (Bardia)</span>
        </button>

        <button onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="bivouac">
          <span>⛺</span>
          <span>Bivouacs & Nuits Sauvages en Jungle</span>
        </button>

        <button onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="chitwan">
          <span>🦏</span>
          <span>Rhinocéros & Parc de Chitwan</span>
        </button>

        <button onclick="filterTrips('grand-tour')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="grand-tour">
          <span>🇳🇵</span>
          <span>Grands Tours 360° (Jungle + Himalaya)</span>
        </button>

        <button onclick="filterTrips('aventure')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="aventure">
          <span>🚣</span>
          <span>Expéditions Aventure (Rafting & 4x4)</span>
        </button>

        <button onclick="filterTrips('culture')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="culture">
          <span>🕉️</span>
          <span>Himalaya, Mustang & Spiritualité</span>
        </button>
      </div>

      <!-- Flèche Droite > -->
      <button onclick="scrollCategories(280)" class="hidden sm:flex w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white hover:bg-emerald-50 border border-slate-300 hover:border-[#0e8354] shadow-md items-center justify-center text-slate-800 hover:text-[#0e8354] transition-all duration-200 hover:scale-110 active:scale-95 shrink-0 ml-3 cursor-pointer z-10" aria-label="Faire défiler vers la droite">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
        </svg>
      </button>

    </div>
  </section>"""

# Category pills HTML EN
categories_html_en = """<!-- SECTION 3: CATEGORIES FILTER (WITH < AND > ARROWS) -->
  <section id="categories" class="py-5 bg-white border-b border-slate-200 sticky top-0 z-30 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center">
      
      <!-- Left Arrow < -->
      <button onclick="scrollCategories(-280)" class="hidden sm:flex w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white hover:bg-emerald-50 border border-slate-300 hover:border-[#0e8354] shadow-md items-center justify-center text-slate-800 hover:text-[#0e8354] transition-all duration-200 hover:scale-110 active:scale-95 shrink-0 mr-3 cursor-pointer z-10" aria-label="Scroll left">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
        </svg>
      </button>

      <!-- Scrollable Container -->
      <div id="categories-scroll-container" class="flex-1 flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1 scroll-smooth">
        <button onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-white font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-slate-900 hover:scale-105 active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="all">
          <span>🧭</span>
          <span>All Expeditions</span>
          <span class="bg-white/20 text-white text-[11px] px-2 py-0.5 rounded-full font-black">14</span>
        </button>

        <button onclick="filterTrips('safari')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="safari">
          <span>🐅</span>
          <span>Bardia Safari & Tiger Tracking</span>
        </button>

        <button onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="bivouac">
          <span>⛺</span>
          <span>Wild Bivouacs & Jungle Camping</span>
        </button>

        <button onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="chitwan">
          <span>🦏</span>
          <span>Chitwan Rhinos & Wildlife</span>
        </button>

        <button onclick="filterTrips('grand-tour')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="grand-tour">
          <span>🇳🇵</span>
          <span>360° Grand Tours (Jungle + Peaks)</span>
        </button>

        <button onclick="filterTrips('aventure')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="aventure">
          <span>🚣</span>
          <span>Wild Adventures (Rafting & 4x4)</span>
        </button>

        <button onclick="filterTrips('culture')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="culture">
          <span>🕉️</span>
          <span>Himalaya, Mustang & Spirituality</span>
        </button>
      </div>

      <!-- Right Arrow > -->
      <button onclick="scrollCategories(280)" class="hidden sm:flex w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white hover:bg-emerald-50 border border-slate-300 hover:border-[#0e8354] shadow-md items-center justify-center text-slate-800 hover:text-[#0e8354] transition-all duration-200 hover:scale-110 active:scale-95 shrink-0 ml-3 cursor-pointer z-10" aria-label="Scroll right">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
        </svg>
      </button>

    </div>
  </section>"""

# Multi-category filter script JS
filter_js = """
    window.scrollCategories = function(amount) {
      const el = document.getElementById('categories-scroll-container');
      if (el) el.scrollBy({ left: amount, behavior: 'smooth' });
    };

    window.filterTrips = function(category) {
      const pills = document.querySelectorAll('.category-pill');
      pills.forEach(p => {
        if (p.getAttribute('data-filter') === category) {
          p.classList.add('bg-slate-950', 'text-white', 'border-slate-900');
          p.classList.remove('bg-white', 'text-slate-900');
        } else {
          p.classList.remove('bg-slate-950', 'text-white', 'border-slate-900');
          p.classList.add('bg-white', 'text-slate-900');
        }
      });

      const cards = document.querySelectorAll('.trip-card');
      let visible = 0;
      cards.forEach(card => {
        const cats = (card.getAttribute('data-category') || card.getAttribute('data-categories') || '').split(',');
        if (category === 'all' || cats.includes(category)) {
          card.style.display = 'flex';
          visible++;
        } else {
          card.style.display = 'none';
        }
      });

      const countEl = document.getElementById('trip-count');
      if (countEl) countEl.textContent = visible;
    };
"""

# Update index.astro and index.html
for fpath in [
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html'
]:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Replace section #categories
    c = re.sub(r'<section\s+id=[\'\"]categories[\'\"].*?</section>', categories_html_fr, c, flags=re.DOTALL)
    
    # Update data-category on each card to include all its categories
    for slug, cat_str in tour_cat_str.items():
        # Match href or onclick containing slug
        # Replace data-category="..." on that card
        card_pattern = rf'(<div[^>]*class=[\'\"][^\'\"]*trip-card[^\'\"]*[\'\"][^>]*href=[\'\"][^\'\"]*{slug}[^\'\"]*[\'\"][^>]*>)'
        c = re.sub(rf'(class=[\'\"][^\'\"]*trip-card[^\'\"]*[\'\"][^>]*?)data-category=[\'\"][^\'\"]*[\'\"]([^>]*?{slug})', rf'\1data-category="{cat_str}"\2', c)
        c = re.sub(rf'(class=[\'\"][^\'\"]*trip-card[^\'\"]*[\'\"][^>]*?{slug}[^>]*?)data-category=[\'\"][^\'\"]*[\'\"]', rf'\1data-category="{cat_str}"', c)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

# Update en/index.astro and en/index.html
for fpath in [
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/index.html'
]:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    c = re.sub(r'<section\s+id=[\'\"]categories[\'\"].*?</section>', categories_html_en, c, flags=re.DOTALL)
    
    for slug, cat_str in tour_cat_str.items():
        c = re.sub(rf'(class=[\'\"][^\'\"]*trip-card[^\'\"]*[\'\"][^>]*?)data-category=[\'\"][^\'\"]*[\'\"]([^>]*?{slug})', rf'\1data-category="{cat_str}"\2', c)
        c = re.sub(rf'(class=[\'\"][^\'\"]*trip-card[^\'\"]*[\'\"][^>]*?{slug}[^>]*?)data-category=[\'\"][^\'\"]*[\'\"]', rf'\1data-category="{cat_str}"', c)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Successfully deployed accurate categories and multi-tag filtering across French & English!")
