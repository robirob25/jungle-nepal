import re

tour_tags_map = {
    "tiji-mustang": "mustang-himalaya culture grand-tour",
    "immersion-spirituelle": "mustang-himalaya culture grand-tour",
    "nepal-sauvage": "safari mustang-himalaya culture grand-tour",
    "rara-lake-bardia": "safari mustang-himalaya aventure grand-tour",
    "carnet-de-voyage": "mustang-himalaya culture grand-tour",
    "rafting-safari": "rafting bivouac safari aventure grand-tour",
    "nepal-immersion-totale": "chitwan safari rafting aventure grand-tour",
    "chitwan-bardia-complete": "chitwan safari bivouac rafting aventure grand-tour",
    "bardia-nuit-sauvage": "safari bivouac",
    "bardia-babai-camping": "safari bivouac",
    "babai-special": "safari bivouac",
    "bardia-explorateur": "safari",
    "chitwan-culture": "chitwan",
    "jungle-extreme": "safari grand-tour"
}

def update_file(filepath, is_en=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Exact replacement of categories buttons container
    if not is_en:
        new_container = """      <!-- Conteneur des Catégories Scrollable -->
      <div id="categories-scroll-container" class="flex-1 flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1 scroll-smooth">
        <button type="button" onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-white font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-slate-900 hover:scale-105 active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="all">
          <span>🧭</span>
          <span>Tous les séjours</span>
          <span class="bg-white/20 text-white text-[11px] px-2 py-0.5 rounded-full font-black">14</span>
        </button>
        <button type="button" onclick="filterTrips('safari')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="safari">
          <span>🐅</span>
          <span>Safaris & Pistage Tigre (10)</span>
        </button>
        <button type="button" onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="bivouac">
          <span>⛺</span>
          <span>Bivouacs & Nuits Sauvages (5)</span>
        </button>
        <button type="button" onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="chitwan">
          <span>🦏</span>
          <span>Rhinocéros & Chitwan (3)</span>
        </button>
        <button type="button" onclick="filterTrips('rafting')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="rafting">
          <span>🚣</span>
          <span>Rafting & Expéditions Rivières (3)</span>
        </button>
        <button type="button" onclick="filterTrips('mustang-himalaya')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="mustang-himalaya">
          <span>🏔️</span>
          <span>Himalaya, Mustang & Spiritualité (5)</span>
        </button>
        <button type="button" onclick="filterTrips('grand-tour')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="grand-tour">
          <span>🇳🇵</span>
          <span>Grands Tours 360° (9)</span>
        </button>
      </div>"""
        new_select = """          <select id="search-dest" class="w-full bg-transparent text-slate-900 font-extrabold text-sm sm:text-base focus:outline-none cursor-pointer appearance-none">
            <option value="all">Tous les séjours (14)</option>
            <option value="safari">🐅 Safaris & Pistage Tigre (Bardia)</option>
            <option value="bivouac">⛺ Bivouacs & Nuits Sauvages en Jungle</option>
            <option value="chitwan">🦏 Rhinocéros & Parc de Chitwan</option>
            <option value="rafting">🚣 Rafting & Expéditions Rivières</option>
            <option value="mustang-himalaya">🏔️ Himalaya, Mustang & Spiritualité</option>
            <option value="grand-tour">🇳🇵 Grands Tours Immersion 360°</option>
          </select>"""
    else:
        new_container = """      <!-- Conteneur des Catégories Scrollable -->
      <div id="categories-scroll-container" class="flex-1 flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1 scroll-smooth">
        <button type="button" onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-white font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-slate-900 hover:scale-105 active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="all">
          <span>🧭</span>
          <span>All Expeditions</span>
          <span class="bg-white/20 text-white text-[11px] px-2 py-0.5 rounded-full font-black">14</span>
        </button>
        <button type="button" onclick="filterTrips('safari')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="safari">
          <span>🐅</span>
          <span>Safari & Tiger Tracking (10)</span>
        </button>
        <button type="button" onclick="filterTrips('bivouac')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="bivouac">
          <span>⛺</span>
          <span>Wild Jungle Camping (5)</span>
        </button>
        <button type="button" onclick="filterTrips('chitwan')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="chitwan">
          <span>🦏</span>
          <span>Rhinos & Chitwan Park (3)</span>
        </button>
        <button type="button" onclick="filterTrips('rafting')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="rafting">
          <span>🚣</span>
          <span>Rafting & River Trips (3)</span>
        </button>
        <button type="button" onclick="filterTrips('mustang-himalaya')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="mustang-himalaya">
          <span>🏔️</span>
          <span>Himalayas, Mustang & Spirituality (5)</span>
        </button>
        <button type="button" onclick="filterTrips('grand-tour')" class="category-pill flex items-center gap-2 px-5 py-2.5 rounded-full bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs sm:text-sm whitespace-nowrap border border-slate-200/90 shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0 transition-all duration-200 cursor-pointer shrink-0" data-filter="grand-tour">
          <span>🇳🇵</span>
          <span>Grand 360° Expeditions (9)</span>
        </button>
      </div>"""
        new_select = """          <select id="search-dest" class="w-full bg-transparent text-slate-900 font-extrabold text-sm sm:text-base focus:outline-none cursor-pointer appearance-none">
            <option value="all">All Expeditions (14)</option>
            <option value="safari">🐅 Safari & Tiger Tracking (Bardia)</option>
            <option value="bivouac">⛺ Wild Jungle Camping</option>
            <option value="chitwan">🦏 Rhinos & Chitwan National Park</option>
            <option value="rafting">🚣 Rafting & River Expeditions</option>
            <option value="mustang-himalaya">🏔️ Himalayas, Mustang & Spirituality</option>
            <option value="grand-tour">🇳🇵 Grand 360° Expeditions</option>
          </select>"""

    start_tag = '<!-- Conteneur des Catégories Scrollable -->'
    end_tag = '<!-- Flèche Droite > -->'
    if start_tag in content and end_tag in content:
        before = content.split(start_tag)[0]
        after = content.split(end_tag)[1]
        content = before + new_container + '\n\n      ' + end_tag + after

    select_start = '<select id="search-dest"'
    select_end = '</select>'
    if select_start in content and select_end in content:
        s_before = content.split(select_start)[0]
        s_after = content.split(select_end, 1)[1]
        content = s_before + new_select + s_after

    # 2. Update each of the 14 cards
    articles = content.split('<article class="trip-card')
    fixed_articles = [articles[0]]
    for art in articles[1:]:
        tour_slug = None
        for slug in tour_tags_map.keys():
            if f'{slug}.html' in art or f'/tours/{slug}' in art:
                tour_slug = slug
                break
        
        if tour_slug:
            tags = tour_tags_map[tour_slug]
            header, rest = art.split('>', 1)
            header = re.sub(r'data-category="[^"]*"', f'data-category="{tags}"', header)
            fixed_articles.append(header + '>' + rest)
        else:
            fixed_articles.append(art)
    
    content = '<article class="trip-card'.join(fixed_articles)

    # 3. Robust filterTrips function
    js_start = 'function filterTrips(category) {'
    js_end = 'function handleSearch(e) {'
    count_template = "Affichage de <strong>${visibleCount} circuit${visibleCount > 1 ? 's' : ''}</strong>" if not is_en else "Showing <strong>${visibleCount} tour${visibleCount > 1 ? 's' : ''}</strong>"

    new_js = f"""function filterTrips(category) {{
      const cards = document.querySelectorAll('.trip-card');
      const pills = document.querySelectorAll('.category-pill');
      let visibleCount = 0;

      const catLower = (category || 'all').toLowerCase();

      pills.forEach(pill => {{
        const filterVal = (pill.getAttribute('data-filter') || '').toLowerCase();
        if (filterVal === catLower) {{
          pill.classList.add('bg-slate-950', 'text-white', 'border-slate-900', 'scale-105', 'active');
          pill.classList.remove('bg-white', 'text-slate-900', 'text-slate-800');
        }} else {{
          pill.classList.remove('bg-slate-950', 'text-white', 'border-slate-900', 'scale-105', 'active');
          pill.classList.add('bg-white', 'text-slate-900');
        }}
      }});

      cards.forEach(card => {{
        const rawCats = card.getAttribute('data-category') || '';
        const cardCats = rawCats.toLowerCase().split(/\\s+/);
        
        let match = false;
        if (catLower === 'all') {{
          match = true;
        }} else if (catLower === 'mustang-himalaya' || catLower === 'mustang' || catLower === 'culture' || catLower === 'himalaya') {{
          match = cardCats.includes('mustang-himalaya') || cardCats.includes('culture') || cardCats.includes('mustang');
        }} else if (catLower === 'rafting' || catLower === 'aventure') {{
          match = cardCats.includes('rafting') || cardCats.includes('aventure');
        }} else {{
          match = cardCats.includes(catLower);
        }}

        if (match) {{
          card.style.display = 'flex';
          visibleCount++;
        }} else {{
          card.style.display = 'none';
        }}
      }});

      const badge = document.getElementById('trip-count-badge');
      if (badge) {{
        badge.innerHTML = `{count_template}`;
      }}
    }}

    """

    if js_start in content and js_end in content:
        j_before = content.split(js_start)[0]
        j_after = content.split(js_end)[1]
        content = j_before + new_js + 'function handleSearch(e) {' + j_after

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully rewritten and synced {filepath}!")

update_file('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', is_en=False)
update_file('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro', is_en=True)
