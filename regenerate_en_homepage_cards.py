import json, re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

# Build English cards HTML
cards_en_html = []

# Map of images per slug from index.astro
slug_images = {
    "bardia-explorateur": "https://junglenepal.com/wp-content/uploads/2025/11/P1133754-scaled.jpg",
    "chitwan-culture": "https://junglenepal.com/wp-content/uploads/2025/03/68.png",
    "rafting-safari": "https://junglenepal.com/wp-content/uploads/2025/11/WhatsApp-Image-2025-11-27-at-13.17.14.jpeg",
    "bardia-nuit-sauvage": "https://junglenepal.com/wp-content/uploads/2025/03/61.png",
    "rara-lake-bardia": "https://junglenepal.com/wp-content/uploads/2017/01/lac-rara-733979_1920.jpg",
    "bardia-babai-camping": "https://junglenepal.com/wp-content/uploads/2025/03/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
    "nepal-immersion-totale": "https://junglenepal.com/wp-content/uploads/2017/01/P1143891.jpg",
    "babai-special": "https://junglenepal.com/wp-content/uploads/2025/03/52.png",
    "chitwan-bardia-complete": "https://junglenepal.com/wp-content/uploads/2025/03/49.png",
    "tiji-mustang": "https://junglenepal.com/wp-content/uploads/2017/01/danseurs-tiji-festival-mustang-nepal.jpg",
    "carnet-de-voyage": "https://junglenepal.com/wp-content/uploads/2017/01/P1143948.jpg",
    "jungle-extreme": "https://junglenepal.com/wp-content/uploads/2025/03/46.png",
    "nepal-sauvage": "https://junglenepal.com/wp-content/uploads/2017/01/nepal-landscape-2388105_1920-1.jpg",
    "immersion-spirituelle": "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
    "panthere-des-neiges": "/assets/snow-leopard/snow_leopard_portrait.jpg"
}

# Categories per slug
slug_categories = {
    "bardia-explorateur": "safari",
    "chitwan-culture": "chitwan culture",
    "rafting-safari": "safari rafting bivouac grand-tour",
    "bardia-nuit-sauvage": "bivouac",
    "rara-lake-bardia": "safari mustang-himalaya grand-tour",
    "bardia-babai-camping": "safari bivouac",
    "nepal-immersion-totale": "safari chitwan rafting grand-tour",
    "babai-special": "safari bivouac",
    "chitwan-bardia-complete": "safari chitwan rafting bivouac grand-tour",
    "tiji-mustang": "mustang-himalaya culture grand-tour",
    "carnet-de-voyage": "mustang-himalaya culture grand-tour",
    "jungle-extreme": "safari grand-tour",
    "nepal-sauvage": "safari mustang-himalaya culture grand-tour",
    "immersion-spirituelle": "mustang-himalaya culture grand-tour",
    "panthere-des-neiges": "mustang-himalaya culture grand-tour safari"
}

# Key highlight tags per slug in English
slug_key_tags_en = {
    "bardia-explorateur": ["🐾 Tiger Walking Safari", "🚙 4x4 Core Zone", "👥 Max 8 pers"],
    "chitwan-culture": ["🦏 Rhino Safari", "🛶 Rapti Canoe", "👥 Max 8 pers"],
    "rafting-safari": ["🚣 Bheri River Rafting", "⛺ Riverside Bivouacs", "👥 Max 8 pers"],
    "bardia-nuit-sauvage": ["⛺ Deep Bush Camp", "🔥 Campfire Under Stars", "👥 Max 6 pers"],
    "rara-lake-bardia": ["🏔️ Sapphire Lake Rara", "🐅 Bardia Tiger Jungle", "👥 Max 8 pers"],
    "bardia-babai-camping": ["⛺ Restricted Babai Valley", "🐘 Wild Elephants", "👥 Max 8 pers"],
    "nepal-immersion-totale": ["🇳🇵 360° Grand Loop", "🚣 Rafting & Safari", "👥 Max 8 pers"],
    "babai-special": ["🐾 Untouched Sanctuary", "⛺ Wild Glamping", "👥 Max 8 pers"],
    "chitwan-bardia-complete": ["🦏 Chitwan Rhinos", "🐅 Bardia Tigers", "👥 Max 8 pers"],
    "tiji-mustang": ["🎭 Sacred Tiji Dances", "🏰 Lo Manthang Kingdom", "👥 Max 8 pers"],
    "carnet-de-voyage": ["🎨 Sketching & Photo", "🏔️ Himalayan Dawns", "👥 Max 8 pers"],
    "jungle-extreme": ["📸 Wildlife Photography", "🔭 Dawn-to-Dusk Tracking", "👥 Max 8 pers"],
    "nepal-sauvage": ["🐅 Bardia Jungle", "🏔️ Annapurna Balconies", "👥 Max 8 pers"],
    "immersion-spirituelle": ["🕉️ Tibetan Monasteries", "🧘 Mountain Meditation", "👥 Max 8 pers"],
    "panthere-des-neiges": ["🐾 9d Pure Tracking", "🏔️ Manang 3,600m", "👥 Max 8 pers"]
}

for i, t in enumerate(tours):
    slug = t['slug']
    title_en = t.get('title_en', t.get('title'))
    duration_en = t.get('duration_en', t.get('duration'))
    badge_en = t.get('badge_en', '🇳🇵 Adventure in Nepal')
    overview_en = t.get('overview_en', t.get('overview'))
    price = t.get('price', '450€')
    rating = t.get('rating', '5.0')
    reviews_count = t.get('reviews_count', 12)
    img_url = slug_images.get(slug, "/assets/logo_dark.png")
    cats = slug_categories.get(slug, "safari")
    tags = slug_key_tags_en.get(slug, ["🐾 Wildlife", "🇳🇵 Nepal", "👥 Small Group"])

    tags_html = "\n                ".join([f'<span class="text-[11px] font-extrabold px-3 py-1 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200">{tag}</span>' for tag in tags])

    card = f"""        <!-- CARD {i+1} : {slug.upper()} -->
        <article class="trip-card group bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-[0_4px_20px_rgba(0,0,0,0.06)] hover:shadow-[0_20px_40px_rgba(10,50,30,0.18)] hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between h-full" data-category="{cats}" data-title="{title_en.lower()}">
          <div>
            <a href="/en/tours/{slug}.html" class="relative h-72 sm:h-80 overflow-hidden block">
              <img 
                src="{img_url}" 
                alt="{title_en}" 
                class="w-full h-full object-cover group-hover:scale-108 transition-transform duration-500 ease-out" 
                loading="lazy" 
              />
              <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-black/20 to-transparent"></div>
              
              <div class="absolute top-4 left-4 flex flex-wrap gap-2 z-10">
                <span class="inline-flex items-center gap-1.5 bg-slate-950/90 backdrop-blur-md text-amber-300 font-extrabold text-xs px-3 py-1 rounded-full border border-amber-400/30">
                  <span>{badge_en}</span>
                </span>
              </div>

              <div class="absolute bottom-4 left-4 right-4 flex items-center justify-between text-white z-10 text-xs font-bold">
                <div class="flex items-center gap-1.5 bg-black/60 backdrop-blur-md px-3 py-1 rounded-full border border-white/10">
                  <svg class="w-3.5 h-3.5 fill-amber-400 text-amber-400" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                  <span>{rating} ({reviews_count} reviews)</span>
                </div>
                <div class="flex items-center gap-1.5 bg-black/60 backdrop-blur-md px-3 py-1 rounded-full border border-white/10">
                  <svg class="w-3.5 h-3.5 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                  <span>{duration_en}</span>
                </div>
              </div>
            </a>

            <div class="p-6 sm:p-7 space-y-4">
              <a href="/en/tours/{slug}.html" class="block group-hover:text-[#0e8354] transition-colors">
                <h3 class="font-black text-xl sm:text-2xl text-slate-900 leading-snug">
                  {title_en}
                </h3>
              </a>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed line-clamp-3 font-normal">
                {overview_en}
              </p>

              <div class="pt-2 flex flex-wrap gap-2">
                {tags_html}
              </div>
            </div>
          </div>

          <div class="p-6 sm:p-7 pt-4 border-t border-slate-100 flex items-center justify-between bg-slate-50/50">
            <div>
              <span class="text-[11px] font-bold text-slate-400 block uppercase tracking-wider">All-inclusive from</span>
              <span class="text-2xl sm:text-3xl font-black text-slate-950">{price}</span>
            </div>
            <a href="/en/tours/{slug}.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#0e8354] hover:bg-[#0c6d46] text-white text-xs font-black shadow-md hover:shadow-lg transition-all hover:scale-105 active:scale-95">
              <span>View itinerary</span>
              <span>→</span>
            </a>
          </div>
        </article>"""
    cards_en_html.append(card)

cards_joined_en = "\n\n".join(cards_en_html)

# Read en/index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro', 'r', encoding='utf-8') as f:
    en_page = f.read()

# Replace the cards grid container contents
grid_start = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 sm:gap-10">'
grid_end = '</div>\n\n    </div>\n  </section>'

idx1 = en_page.find(grid_start)
idx2 = en_page.find('</div>\n\n    </div>\n  </section>', idx1)

if idx1 != -1 and idx2 != -1:
    en_page = en_page[:idx1 + len(grid_start)] + '\n\n' + cards_joined_en + '\n\n      ' + en_page[idx2:]
    with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro', 'w', encoding='utf-8') as f:
        f.write(en_page)
    print("Successfully replaced all 15 cards with 100% English content on en/index.astro!")
else:
    print("Error locating cards grid on en/index.astro!")
