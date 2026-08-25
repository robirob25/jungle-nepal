import json, re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Build the Artistic Collage Layout
# 11 curated photo cards with organic magazine collage spanning
# Grid of 12 columns for maximum layout flexibility

collage_cards = [
    # 0: Tiger Water (Main Hero Feature - 7 cols, tall)
    {
        "idx": 0, "col": "col-span-12 lg:col-span-7 h-[360px] sm:h-[480px] lg:h-[520px]",
        "badge": "🐅 Bardia • Rive du fleuve", "cat": "felins"
    },
    # 1: Rhino in Mist (5 cols, top right)
    {
        "idx": 1, "col": "col-span-12 sm:col-span-6 lg:col-span-5 h-[280px] sm:h-[320px] lg:h-[245px]",
        "badge": "🦏 Chitwan • Aube", "cat": "geants"
    },
    # 2: Peacock Wheel (5 cols, bottom right)
    {
        "idx": 10, "col": "col-span-12 sm:col-span-6 lg:col-span-5 h-[280px] sm:h-[320px] lg:h-[255px]",
        "badge": "🦚 Terai • Parade", "cat": "oiseaux"
    },
    # 3: Elephant Jungle (4 cols)
    {
        "idx": 5, "col": "col-span-12 sm:col-span-6 lg:col-span-4 h-[280px] sm:h-[340px]",
        "badge": "🐘 Forêt de Sal • Bardia", "cat": "geants"
    },
    # 4: Tiger Stalk (4 cols)
    {
        "idx": 6, "col": "col-span-12 sm:col-span-6 lg:col-span-4 h-[280px] sm:h-[340px]",
        "badge": "🐅 Babai • Approche", "cat": "felins"
    },
    # 5: Croco Water (4 cols)
    {
        "idx": 7, "col": "col-span-12 sm:col-span-12 lg:col-span-4 h-[280px] sm:h-[340px]",
        "badge": "🐊 Rivière Rapti • Affût", "cat": "reptiles"
    },
    # 6: Hornbill Calao (3 cols)
    {
        "idx": 8, "col": "col-span-12 sm:col-span-6 lg:col-span-3 h-[260px] sm:h-[300px]",
        "badge": "🦜 Canopée de Chitwan", "cat": "oiseaux"
    },
    # 7: Tiger Jungle Walk (6 cols)
    {
        "idx": 2, "col": "col-span-12 sm:col-span-6 lg:col-span-6 h-[260px] sm:h-[300px]",
        "badge": "🐅 Bardia • Sentier secret", "cat": "felins"
    },
    # 8: Marabout Flight (3 cols)
    {
        "idx": 9, "col": "col-span-12 sm:col-span-12 lg:col-span-3 h-[260px] sm:h-[300px]",
        "badge": "🦅 Zones humides • Envol", "cat": "oiseaux"
    },
    # 9: Deer Plain (6 cols)
    {
        "idx": 3, "col": "col-span-12 sm:col-span-6 lg:col-span-6 h-[260px] sm:h-[300px]",
        "badge": "🦌 Suklaphanta • Savane", "cat": "herbivores"
    },
    # 10: Nilgai Forest (6 cols)
    {
        "idx": 4, "col": "col-span-12 sm:col-span-6 lg:col-span-6 h-[260px] sm:h-[300px]",
        "badge": "🦌 Lisières de Bardia", "cat": "herbivores"
    },
]

cards_html = []
for c in collage_cards:
    item = items[c['idx']]
    card = f"""        <!-- Collage Card: {item['title']} -->
        <div class="wildlife-card {c['col']} relative rounded-3xl overflow-hidden group cursor-pointer border border-white/10 shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:border-emerald-500/50 transition-all duration-300" data-category="{c['cat']}" onclick="openWildlifeLightbox({c['idx']})">
          <img 
            src="{item['file']}" 
            alt="{item['title']} - {item['location']}" 
            class="w-full h-full object-cover filter brightness-95 group-hover:brightness-105 transition-all duration-500"
            loading="lazy"
          />
          <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/25 to-transparent opacity-85 group-hover:opacity-65 transition-opacity duration-300"></div>
          
          <!-- Top Badge: Location & Species -->
          <div class="absolute top-4 left-4 z-10">
            <span class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-slate-950/80 backdrop-blur-md border border-white/15 text-xs font-black text-amber-300 shadow-lg">
              <span>{c['badge']}</span>
            </span>
          </div>

          <!-- Bottom Floating Glass Caption -->
          <div class="absolute bottom-4 left-4 right-4 z-10 p-4 rounded-2xl bg-slate-950/85 backdrop-blur-md border border-white/15 text-white transition-transform duration-300">
            <div class="flex items-center justify-between gap-3">
              <div>
                <h3 class="font-black text-base sm:text-lg text-white group-hover:text-amber-300 transition-colors leading-tight">
                  {item['title']}
                </h3>
                <p class="text-xs text-slate-300 mt-0.5 font-medium line-clamp-1">
                  {item['desc']}
                </p>
              </div>
              <div class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center shrink-0 border border-emerald-500/30">
                <svg class="w-4 h-4 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"></path></svg>
              </div>
            </div>
          </div>
        </div>"""
    cards_html.append(card)

collage_grid_html = "\n\n".join(cards_html)

full_section_html = f"""  <!-- ========================================================================= -->
  <!-- 5. GALERIE COLLAGE SAUVAGE DU NÉPAL (POSITIONNÉE JUSTE AVANT LES PISTEURS) -->
  <!-- ========================================================================= -->
  <section id="galerie-faune" class="py-20 sm:py-28 lg:py-32 bg-slate-950 text-white relative overflow-hidden border-t border-b border-white/10">
    
    <!-- Ambient emerald and amber glows -->
    <div class="absolute top-1/4 left-1/4 w-[600px] h-[600px] bg-[#0e8354]/12 rounded-full blur-[160px] pointer-events-none"></div>
    <div class="absolute bottom-1/4 right-1/4 w-[600px] h-[600px] bg-amber-500/10 rounded-full blur-[160px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-12 sm:mb-16">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-emerald-400/30 text-amber-300 text-xs font-black uppercase tracking-widest mb-4">
          <span>🌿 Instants Sauvages & Expéditions Terrain</span>
        </div>
        <h2 class="font-black text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-tight">
          La faune du Terai dans son intimité brute.
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-300 font-medium leading-relaxed">
          Toutes ces photographies ont été capturées sur le vif lors de nos safaris à pied par nos voyageurs et maîtres pisteurs.
        </p>
      </div>

      <!-- Category Filter Pills -->
      <div class="flex flex-wrap items-center justify-center gap-2 sm:gap-3 mb-12" id="wildlife-tabs">
        <button onclick="filterWildlife('all')" class="wildlife-tab-btn active px-4 sm:px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-emerald-600 text-white shadow-lg shadow-emerald-900/30 border border-emerald-400/40 cursor-pointer">
          🐾 Tous les 11 clichés
        </button>
        <button onclick="filterWildlife('felins')" class="wildlife-tab-btn px-4 sm:px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🐅 Tigres du Bengale
        </button>
        <button onclick="filterWildlife('geants')" class="wildlife-tab-btn px-4 sm:px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🦏 Rhinos & Éléphants
        </button>
        <button onclick="filterWildlife('oiseaux')" class="wildlife-tab-btn px-4 sm:px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🦚 Oiseaux & Calaos
        </button>
        <button onclick="filterWildlife('herbivores')" class="wildlife-tab-btn px-4 sm:px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🦌 Cerfs & Nilgauts
        </button>
        <button onclick="filterWildlife('reptiles')" class="wildlife-tab-btn px-4 sm:px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🐊 Crocodiles & Rivières
        </button>
      </div>

      <!-- Organic 12-Column Art Collage Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-12 gap-4 sm:gap-6" id="wildlife-grid">
{collage_grid_html}
      </div>

    </div>
  </section>"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Remove previous instance of galerie-faune if any
c = re.sub(r'<!-- ===+ -->\s*<!-- \d+\. GALERIE ÉLITE.*?<\/div>\s*<\/div>\s*<\/section>', '', c, flags=re.DOTALL)
c = re.sub(r'<!-- ===+ -->\s*<!-- 5\. GALERIE COLLAGE.*?<\/div>\s*<\/div>\s*<\/section>', '', c, flags=re.DOTALL)

# 2. Insert the Collage section RIGHT BEFORE <!-- 8. PISTEURS & ÉQUIPE --> (id="pisteurs")
pisteurs_marker = '<!-- ========================================================================= -->\n  <!-- 8. PISTEURS & ÉQUIPE -->'
if pisteurs_marker in c:
    c = c.replace(pisteurs_marker, f'{full_section_html}\n\n  {pisteurs_marker}')
else:
    # fallback to before <section id="pisteurs"
    c = re.sub(r'(<section[^>]*id=[\'"]pisteurs[\'"])', f'{full_section_html}\n\n  \\1', c)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("Placed the luxury Wildlife Collage Gallery directly ABOVE the 'Nos maîtres pisteurs' section!")
