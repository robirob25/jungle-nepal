import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero section container:
# Make Hero section flex flex-col justify-between items-center relative min-h-[92vh] sm:min-h-screen pt-36 pb-6 sm:pb-8
content = content.replace(
    '<section class="relative min-h-[92vh] flex items-center justify-center pt-44 pb-28 px-4 sm:px-6 lg:px-8 overflow-hidden bg-slate-950">',
    '<section class="relative min-h-[92vh] sm:min-h-screen flex flex-col justify-between items-center pt-36 sm:pt-40 pb-6 sm:pb-8 px-4 sm:px-6 lg:px-8 overflow-hidden bg-slate-950">'
)

# 2. Extract and replace the section from search card down through categories section:
old_hero_bottom_and_cat = r'(\s*<!-- SEARCH CARD WEROAD LUXE.*?</div>\s*</form>\s*</div>\s*</div>)\s*</section>\s*<!-- ========================================================================= -->\s*<!-- 5\. CATEGORIES FILTER CAROUSEL -->\s*<!-- SECTION 3: FILTRES CATÉGORIES.*?-->\s*<section id="categories".*?</section>'

integrated_hero_bottom = r"""\1

      <!-- 5. CATEGORIES FILTER CAROUSEL DIRECTEMENT DANS LE BAS DU HERO -->
      <div id="categories" class="w-full max-w-7xl mx-auto mt-10 sm:mt-14 relative z-20">
        <div class="flex items-center justify-center gap-2 sm:gap-3 bg-slate-950/60 backdrop-blur-xl p-2 sm:p-2.5 rounded-full border border-white/15 shadow-[0_15px_35px_rgba(0,0,0,0.4)]">
          
          <!-- Flèche Gauche < -->
          <button onclick="scrollCategories(-280)" class="hidden sm:flex w-9 h-9 rounded-full bg-white/10 hover:bg-[#0e8354] border border-white/20 hover:border-emerald-400 text-white shadow items-center justify-center transition-all duration-200 active:scale-95 shrink-0 cursor-pointer z-10" aria-label="Faire défiler vers la gauche">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
            </svg>
          </button>

          <!-- Conteneur des Catégories Scrollable (Pills Hero) -->
          <div id="categories-scroll-container" class="flex-1 flex items-center gap-2 overflow-x-auto no-scrollbar py-0.5 scroll-smooth">
            <button type="button" onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-white text-slate-950 font-black text-xs sm:text-sm whitespace-nowrap shadow-md hover:bg-slate-100 active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="all">
              <span>Tous les séjours</span>
              <span class="bg-[#0e8354] text-white text-[11px] px-2 py-0.5 rounded-full font-black">15</span>
            </button>
            <button type="button" onclick="filterTrips('safari')" class="category-pill flex items-center gap-2 px-4 sm:px-5 py-2.5 rounded-full bg-white/10 hover:bg-white/20 text-white font-bold text-xs sm:text-sm whitespace-nowrap border border-white/10 hover:border-white/30 backdrop-blur-md shadow-sm active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="safari">
              <span>Safaris et grands félins (11)</span>
            </button>
            <button type="button" onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2 px-4 sm:px-5 py-2.5 rounded-full bg-white/10 hover:bg-white/20 text-white font-bold text-xs sm:text-sm whitespace-nowrap border border-white/10 hover:border-white/30 backdrop-blur-md shadow-sm active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="bivouac">
              <span>Bivouacs et nuits sauvages (5)</span>
            </button>
            <button type="button" onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2 px-4 sm:px-5 py-2.5 rounded-full bg-white/10 hover:bg-white/20 text-white font-bold text-xs sm:text-sm whitespace-nowrap border border-white/10 hover:border-white/30 backdrop-blur-md shadow-sm active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="chitwan">
              <span>Rhinocéros et Chitwan (3)</span>
            </button>
            <button type="button" onclick="filterTrips('rafting')" class="category-pill flex items-center gap-2 px-4 sm:px-5 py-2.5 rounded-full bg-white/10 hover:bg-white/20 text-white font-bold text-xs sm:text-sm whitespace-nowrap border border-white/10 hover:border-white/30 backdrop-blur-md shadow-sm active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="rafting">
              <span>Rafting et expéditions rivières (3)</span>
            </button>
            <button type="button" onclick="filterTrips('mustang-himalaya')" class="category-pill flex items-center gap-2 px-4 sm:px-5 py-2.5 rounded-full bg-white/10 hover:bg-white/20 text-white font-bold text-xs sm:text-sm whitespace-nowrap border border-white/10 hover:border-white/30 backdrop-blur-md shadow-sm active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="mustang-himalaya">
              <span>Himalaya, mustang et spiritualité (6)</span>
            </button>
            <button type="button" onclick="filterTrips('grand-tour')" class="category-pill flex items-center gap-2 px-4 sm:px-5 py-2.5 rounded-full bg-white/10 hover:bg-white/20 text-white font-bold text-xs sm:text-sm whitespace-nowrap border border-white/10 hover:border-white/30 backdrop-blur-md shadow-sm active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="grand-tour">
              <span>Grands tours 360° (10)</span>
            </button>
          </div>

          <!-- Flèche Droite > -->
          <button onclick="scrollCategories(280)" class="hidden sm:flex w-9 h-9 rounded-full bg-white/10 hover:bg-[#0e8354] border border-white/20 hover:border-emerald-400 text-white shadow items-center justify-center transition-all duration-200 active:scale-95 shrink-0 cursor-pointer z-10" aria-label="Faire défiler vers la droite">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
            </svg>
          </button>
        </div>
      </div>

    </section>"""

content = re.sub(old_hero_bottom_and_cat, integrated_hero_bottom, content, flags=re.DOTALL)

# Also update the JS filterTrips so active pill changes to bg-white text-slate-950
filter_js = """function filterTrips(category) {
      const cards = document.querySelectorAll('.trip-card');
      const pills = document.querySelectorAll('.category-pill');
      let visibleCount = 0;

      const catLower = (category || 'all').toLowerCase();

      pills.forEach(pill => {
        const filterVal = (pill.getAttribute('data-filter') || '').toLowerCase();
        if (filterVal === catLower) {
          pill.classList.add('bg-white', 'text-slate-950', 'active');
          pill.classList.remove('bg-white/10', 'text-white', 'border-white/10');
        } else {
          pill.classList.remove('bg-white', 'text-slate-950', 'active');
          pill.classList.add('bg-white/10', 'text-white', 'border-white/10');
        }
      });"""

content = re.sub(
    r'function filterTrips\(category\)\s*\{.*?pills\.forEach\(pill\s*=>\s*\{.*?\}\);',
    filter_js,
    content,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Categories cleanly embedded into Hero bottom!")
