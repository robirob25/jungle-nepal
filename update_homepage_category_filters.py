import re

# Update French index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    fr_code = f.read()

new_pills_fr = """      <div id="categories-scroll-container" class="flex-1 flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1 scroll-smooth">
        <button onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-white font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-slate-900 hover:scale-105 active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="all">
          <span>🧭</span>
          <span>Tous les séjours (14)</span>
        </button>
        <button onclick="filterTrips('safari')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="safari">
          <span>🐅</span>
          <span>Safaris & Pistage Tigre (10)</span>
        </button>
        <button onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="bivouac">
          <span>⛺</span>
          <span>Bivouacs & Nuits Sauvages (5)</span>
        </button>
        <button onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="chitwan">
          <span>🦏</span>
          <span>Rhinocéros & Chitwan (3)</span>
        </button>
        <button onclick="filterTrips('rafting')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="rafting">
          <span>🚣</span>
          <span>Rafting & Expéditions Rivières (3)</span>
        </button>
        <button onclick="filterTrips('mustang-himalaya')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="mustang-himalaya">
          <span>🏔️</span>
          <span>Haut Mustang & Himalaya (5)</span>
        </button>
        <button onclick="filterTrips('grand-tour')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="grand-tour">
          <span>🇳🇵</span>
          <span>Grands Tours 360° (9)</span>
        </button>
      </div>"""

# Replace categories scroll container
fr_code = re.sub(
    r'<div id="categories-scroll-container".*?</div>\s*<button onclick="scrollCategories\(260\)"',
    new_pills_fr + '\n      <button onclick="scrollCategories(260)"',
    fr_code,
    flags=re.DOTALL
)

# Make sure Hero search select options also match
new_select_fr = """          <select id="search-dest" class="w-full bg-transparent text-slate-900 font-extrabold text-sm sm:text-base focus:outline-none cursor-pointer appearance-none">
            <option value="all">Tous les séjours (14)</option>
            <option value="safari">🐅 Safaris & Pistage Tigre (Bardia)</option>
            <option value="bivouac">⛺ Bivouacs & Nuits Sauvages en Jungle</option>
            <option value="chitwan">🦏 Rhinocéros & Parc de Chitwan</option>
            <option value="rafting">🚣 Rafting & Expéditions Rivières</option>
            <option value="mustang-himalaya">🏔️ Haut Mustang & Himalaya</option>
            <option value="grand-tour">🇳🇵 Grands Tours Immersion 360°</option>
          </select>"""

fr_code = re.sub(
    r'<select id="search-dest".*?</select>',
    new_select_fr,
    fr_code,
    flags=re.DOTALL
)

# Ensure data-category attribute is cleanly formatted on each card
fr_code = re.sub(
    r'data-category=\{[^\}]*\}',
    r'data-category={tour.categories ? tour.categories.join(",") : ""}',
    fr_code
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(fr_code)

print("Updated French homepage category filters & search options!")

# English index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro', 'r', encoding='utf-8') as f:
    en_code = f.read()

new_pills_en = """      <div id="categories-scroll-container" class="flex-1 flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1 scroll-smooth">
        <button onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-white font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-slate-900 hover:scale-105 active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="all">
          <span>🧭</span>
          <span>All Expeditions (14)</span>
        </button>
        <button onclick="filterTrips('safari')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="safari">
          <span>🐅</span>
          <span>Safari & Tiger Tracking (10)</span>
        </button>
        <button onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="bivouac">
          <span>⛺</span>
          <span>Wild Jungle Camping (5)</span>
        </button>
        <button onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="chitwan">
          <span>🦏</span>
          <span>Rhinos & Chitwan Park (3)</span>
        </button>
        <button onclick="filterTrips('rafting')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="rafting">
          <span>🚣</span>
          <span>Rafting & River Trips (3)</span>
        </button>
        <button onclick="filterTrips('mustang-himalaya')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="mustang-himalaya">
          <span>🏔️</span>
          <span>Upper Mustang & Himalayas (5)</span>
        </button>
        <button onclick="filterTrips('grand-tour')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="grand-tour">
          <span>🇳🇵</span>
          <span>Grand 360° Expeditions (9)</span>
        </button>
      </div>"""

en_code = re.sub(
    r'<div id="categories-scroll-container".*?</div>\s*<button onclick="scrollCategories\(260\)"',
    new_pills_en + '\n      <button onclick="scrollCategories(260)"',
    en_code,
    flags=re.DOTALL
)

new_select_en = """          <select id="search-dest" class="w-full bg-transparent text-slate-900 font-extrabold text-sm sm:text-base focus:outline-none cursor-pointer appearance-none">
            <option value="all">All Expeditions (14)</option>
            <option value="safari">🐅 Safari & Tiger Tracking (Bardia)</option>
            <option value="bivouac">⛺ Wild Jungle Camping</option>
            <option value="chitwan">🦏 Rhinos & Chitwan National Park</option>
            <option value="rafting">🚣 Rafting & River Expeditions</option>
            <option value="mustang-himalaya">🏔️ Upper Mustang & Himalayas</option>
            <option value="grand-tour">🇳🇵 Grand 360° Expeditions</option>
          </select>"""

en_code = re.sub(
    r'<select id="search-dest".*?</select>',
    new_select_en,
    en_code,
    flags=re.DOTALL
)

en_code = re.sub(
    r'data-category=\{[^\}]*\}',
    r'data-category={tour.categories ? tour.categories.join(",") : ""}',
    en_code
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro', 'w', encoding='utf-8') as f:
    f.write(en_code)

print("Updated English homepage category filters & search options!")

