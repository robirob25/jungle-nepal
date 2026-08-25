import re

tour_tags = {
    "bardia-explorateur": "safari",
    "chitwan-culture": "chitwan",
    "rafting-safari": "rafting bivouac safari grand-tour",
    "bardia-nuit-sauvage": "safari bivouac",
    "rara-lake-bardia": "mustang-himalaya safari grand-tour",
    "bardia-babai-camping": "safari bivouac",
    "nepal-immersion-totale": "chitwan safari rafting grand-tour",
    "babai-special": "safari bivouac",
    "chitwan-bardia-complete": "chitwan safari bivouac rafting grand-tour",
    "tiji-mustang": "mustang-himalaya grand-tour",
    "carnet-de-voyage": "mustang-himalaya grand-tour",
    "jungle-extreme": "safari grand-tour",
    "nepal-sauvage": "safari mustang-himalaya grand-tour",
    "immersion-spirituelle": "mustang-himalaya grand-tour"
}

def fix_page(filepath, is_en=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. New Category Pills markup
    if not is_en:
        pills_html = """      <div id="categories-scroll-container" class="flex-1 flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1 scroll-smooth">
        <button type="button" onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-white font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-slate-900 hover:scale-105 active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="all">
          <span>🧭</span>
          <span>Tous les séjours (14)</span>
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
        select_html = """          <select id="search-dest" class="w-full bg-transparent text-slate-900 font-extrabold text-sm sm:text-base focus:outline-none cursor-pointer appearance-none">
            <option value="all">Tous les séjours (14)</option>
            <option value="safari">🐅 Safaris & Pistage Tigre (Bardia)</option>
            <option value="bivouac">⛺ Bivouacs & Nuits Sauvages en Jungle</option>
            <option value="chitwan">🦏 Rhinocéros & Parc de Chitwan</option>
            <option value="rafting">🚣 Rafting & Expéditions Rivières</option>
            <option value="mustang-himalaya">🏔️ Himalaya, Mustang & Spiritualité</option>
            <option value="grand-tour">🇳🇵 Grands Tours Immersion 360°</option>
          </select>"""
    else:
        pills_html = """      <div id="categories-scroll-container" class="flex-1 flex items-center gap-2.5 overflow-x-auto no-scrollbar py-1 scroll-smooth">
        <button type="button" onclick="filterTrips('all')" class="category-pill active flex items-center gap-2 px-5 py-2.5 rounded-full bg-slate-950 text-white font-extrabold text-xs sm:text-sm whitespace-nowrap shadow-md border border-slate-900 hover:scale-105 active:scale-95 transition-all duration-200 cursor-pointer shrink-0" data-filter="all">
          <span>🧭</span>
          <span>All Expeditions (14)</span>
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
        select_html = """          <select id="search-dest" class="w-full bg-transparent text-slate-900 font-extrabold text-sm sm:text-base focus:outline-none cursor-pointer appearance-none">
            <option value="all">All Expeditions (14)</option>
            <option value="safari">🐅 Safari & Tiger Tracking (Bardia)</option>
            <option value="bivouac">⛺ Wild Jungle Camping</option>
            <option value="chitwan">🦏 Rhinos & Chitwan National Park</option>
            <option value="rafting">🚣 Rafting & River Expeditions</option>
            <option value="mustang-himalaya">🏔️ Himalayas, Mustang & Spirituality</option>
            <option value="grand-tour">🇳🇵 Grand 360° Expeditions</option>
          </select>"""

    # Replace category container
    content = re.sub(
        r'<div id="categories-scroll-container".*?</div>\s*(?=<button [^>]*scrollCategories)',
        lambda m: pills_html + '\n      ',
        content,
        flags=re.DOTALL
    )

    # Replace search-dest select
    content = re.sub(
        r'<select id="search-dest".*?</select>',
        lambda m: select_html,
        content,
        flags=re.DOTALL
    )

    # 2. Fix all 14 cards data-category attributes
    parts = content.split('<article class="trip-card')
    fixed_parts = [parts[0]]

    for part in parts[1:]:
        tour_slug = None
        for slug in tour_tags.keys():
            if f'{slug}.html' in part or f'/tours/{slug}' in part:
                tour_slug = slug
                break
        
        if tour_slug:
            tags = tour_tags[tour_slug]
            header, rest = part.split('>', 1)
            header = re.sub(r'data-category="[^"]*"', f'data-category="{tags}"', header)
            fixed_parts.append(header + '>' + rest)
        else:
            fixed_parts.append(part)

    content = '<article class="trip-card'.join(fixed_parts)

    # 3. Robust filterTrips JavaScript implementation
    count_text = "Affichage de <strong>${visibleCount} circuit${visibleCount > 1 ? 's' : ''}</strong>" if not is_en else "Showing <strong>${visibleCount} tour${visibleCount > 1 ? 's' : ''}</strong>"
    
    js_code = f"""    function filterTrips(category) {{
      const cards = document.querySelectorAll('.trip-card');
      const pills = document.querySelectorAll('.category-pill');
      let visibleCount = 0;

      pills.forEach(pill => {{
        const filterVal = pill.getAttribute('data-filter') || '';
        if (filterVal === category) {{
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
        if (category === 'all' || cardCats.indexOf(category.toLowerCase()) !== -1) {{
          card.style.display = 'flex';
          visibleCount++;
        }} else {{
          card.style.display = 'none';
        }}
      }});

      const badge = document.getElementById('trip-count-badge');
      if (badge) {{
        badge.innerHTML = `{count_text}`;
      }}
    }}"""

    content = re.sub(
        r'function filterTrips\(category\)\s*\{.*?\}\s*(?=function handleSearch)',
        lambda m: js_code + '\n\n    ',
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Completely fixed and synced {filepath}!")

fix_page('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', is_en=False)
fix_page('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro', is_en=True)
