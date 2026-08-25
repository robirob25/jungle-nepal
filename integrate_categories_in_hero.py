import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. We want to place the categories filter inside the Hero section, at the bottom of the Hero container, styled elegantly with glassmorphism or clean pill buttons.
# Let's inspect the current Hero section end and Categories section.

# Find the Hero search card and Hero closing tag:
old_hero_and_cat = r'(<!-- SEARCH CARD WEROAD LUXE.*?</div>\s*</form>\s*</div>)\s*</section>\s*<!-- ========================================================================= -->\s*<!-- 5\. CATEGORIES FILTER CAROUSEL -->\s*<!-- SECTION 3: FILTRES CATÉGORIES.*?-->\s*<section id="categories".*?</section>'

new_hero_with_cat = r"""\1

      <!-- INTEGRATED CATEGORY FILTER PILLS (DIRECTEMENT DANS LE HERO) -->
      <div id="categories" class="w-full max-w-5xl mt-12 pt-6 border-t border-white/15">
        <div class="flex items-center gap-2.5">
          <!-- Flèche Gauche < -->
          <button onclick="scrollCategories(-280)" class="hidden sm:flex w-9 h-9 rounded-full bg-slate-900/80 hover:bg-[#0e8354] border border-white/20 hover:border-emerald-400 text-white shadow-lg items-center justify-center transition-all duration-200 active:scale-95 shrink-0 cursor-pointer z-10" aria-label="Faire défiler vers la gauche">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
            </svg>
          </button>

          <!-- Conteneur des Catégories Scrollable (Pills Hero) -->
          <div id="categories-scroll-container" class="flex-1 flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1 scroll-smooth">
            <button type="button" onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-white text-slate-950 font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-lg hover:bg-slate-100 active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="all">
              <span>Tous les séjours</span>
              <span class="bg-[#0e8354] text-white text-[11px] px-2 py-0.5 rounded-full font-black">15</span>
            </button>
            <button type="button" onclick="filterTrips('safari')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-900/80 hover:bg-white/20 text-white font-bold text-xs sm:text-sm whitespace-nowrap border border-white/20 backdrop-blur-md shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="safari">
              <span>Safaris et grands félins (11)</span>
            </button>
            <button type="button" onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-900/80 hover:bg-white/20 text-white font-bold text-xs sm:text-sm whitespace-nowrap border border-white/20 backdrop-blur-md shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="bivouac">
              <span>Bivouacs et nuits sauvages (5)</span>
            </button>
            <button type="button" onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-900/80 hover:bg-white/20 text-white font-bold text-xs sm:text-sm whitespace-nowrap border border-white/20 backdrop-blur-md shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="chitwan">
              <span>Rhinocéros et Chitwan (3)</span>
            </button>
            <button type="button" onclick="filterTrips('rafting')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-900/80 hover:bg-white/20 text-white font-bold text-xs sm:text-sm whitespace-nowrap border border-white/20 backdrop-blur-md shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="rafting">
              <span>Rafting et expéditions rivières (3)</span>
            </button>
            <button type="button" onclick="filterTrips('mustang-himalaya')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-900/80 hover:bg-white/20 text-white font-bold text-xs sm:text-sm whitespace-nowrap border border-white/20 backdrop-blur-md shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="mustang-himalaya">
              <span>Himalaya, mustang et spiritualité (6)</span>
            </button>
            <button type="button" onclick="filterTrips('grand-tour')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-900/80 hover:bg-white/20 text-white font-bold text-xs sm:text-sm whitespace-nowrap border border-white/20 backdrop-blur-md shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="grand-tour">
              <span>Grands tours 360° (10)</span>
            </button>
          </div>

          <!-- Flèche Droite > -->
          <button onclick="scrollCategories(280)" class="hidden sm:flex w-9 h-9 rounded-full bg-slate-900/80 hover:bg-[#0e8354] border border-white/20 hover:border-emerald-400 text-white shadow-lg items-center justify-center transition-all duration-200 active:scale-95 shrink-0 cursor-pointer z-10" aria-label="Faire défiler vers la droite">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
            </svg>
          </button>
        </div>
      </div>

    </div>
  </section>"""

content = re.sub(old_hero_and_cat, new_hero_with_cat, content, flags=re.DOTALL)

# Update filterTrips JS in index.astro so active pill state matches the Hero dark/white style:
filter_trips_js_old = r'function filterTrips\(category\)\s*\{.*?pills\.forEach\(pill\s*=>\s*\{.*?\}\);'

filter_trips_js_new = """function filterTrips(category) {
      const cards = document.querySelectorAll('.trip-card');
      const pills = document.querySelectorAll('.category-pill');
      let visibleCount = 0;

      const catLower = (category || 'all').toLowerCase();

      pills.forEach(pill => {
        const filterVal = (pill.getAttribute('data-filter') || '').toLowerCase();
        if (filterVal === catLower) {
          pill.classList.add('bg-white', 'text-slate-950', 'active');
          pill.classList.remove('bg-slate-900/80', 'text-white', 'border-white/20');
        } else {
          pill.classList.remove('bg-white', 'text-slate-950', 'active');
          pill.classList.add('bg-slate-900/80', 'text-white', 'border-white/20');
        }
      });"""

content = re.sub(filter_trips_js_old, filter_trips_js_new, content, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Integrated categories directly inside the Hero section!")
