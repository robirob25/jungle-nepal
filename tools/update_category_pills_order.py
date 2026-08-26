with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace category pills container to place "Mixe Jungle et Montagne (10)" right after "Tous les séjours" (or as requested):
# 1. Tous les séjours (15)
# 2. Mixe Jungle et Montagne (10)
# 3. Safaris et grands félins (11)
# 4. Bivouacs et nuits sauvages (5)
# 5. Rhinocéros et Chitwan (3)
# 6. Rafting et expéditions rivières (3)
# 7. Himalaya, Mustang et spiritualité (6)

old_pills = """      <div id="categories-scroll-container" class="flex-1 flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1 scroll-smooth">
        <button type="button" onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-white font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-slate-900 hover:scale-100 active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="all">
          <span>Tous les séjours</span>
          <span class="bg-white/20 text-white text-[11px] px-2 py-0.5 rounded-full font-black">15</span>
        </button>
        <button type="button" onclick="filterTrips('safari')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="safari">
          <span>Safaris et grands félins (11)</span>
        </button>
        <button type="button" onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="bivouac">
          <span>Bivouacs et nuits sauvages (5)</span>
        </button>
        <button type="button" onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="chitwan">
          <span>Rhinocéros et Chitwan (3)</span>
        </button>
        <button type="button" onclick="filterTrips('rafting')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="rafting">
          <span>Rafting et expéditions rivières (3)</span>
        </button>
        <button type="button" onclick="filterTrips('mustang-himalaya')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="mustang-himalaya">
          <span>Himalaya, Mustang et spiritualité (6)</span>
        </button>
        <button type="button" onclick="filterTrips('grand-tour')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="grand-tour">
          <span>Grands tours 360° (10)</span>
        </button>
      </div>"""

new_pills = """      <div id="categories-scroll-container" class="flex-1 flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1 scroll-smooth">
        <button type="button" onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-white font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-slate-900 hover:scale-100 active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="all">
          <span>Tous les séjours</span>
          <span class="bg-white/20 text-white text-[11px] px-2 py-0.5 rounded-full font-black">15</span>
        </button>
        <button type="button" onclick="filterTrips('grand-tour')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="grand-tour">
          <span>Mixe Jungle et Montagne (10)</span>
        </button>
        <button type="button" onclick="filterTrips('safari')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="safari">
          <span>Safaris et grands félins (11)</span>
        </button>
        <button type="button" onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="bivouac">
          <span>Bivouacs et nuits sauvages (5)</span>
        </button>
        <button type="button" onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="chitwan">
          <span>Rhinocéros et Chitwan (3)</span>
        </button>
        <button type="button" onclick="filterTrips('rafting')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="rafting">
          <span>Rafting et expéditions rivières (3)</span>
        </button>
        <button type="button" onclick="filterTrips('mustang-himalaya')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="mustang-himalaya">
          <span>Himalaya, Mustang et spiritualité (6)</span>
        </button>
      </div>"""

c = c.replace(old_pills, new_pills)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Updated category filter pills: 'Mixe Jungle et Montagne (10)' placed first right after 'Tous les séjours'!")
