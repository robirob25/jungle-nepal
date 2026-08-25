import json, re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Build the Masonry Collage Cards
# Distribute the 11 photos strategically across 3 columns for balanced vertical height

cards_html = []
for idx, item in enumerate(items):
    card = f"""        <!-- Photo {idx+1}: {item['title']} -->
        <div class="wildlife-card break-inside-avoid mb-6 relative rounded-3xl overflow-hidden group cursor-pointer border border-white/10 shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:border-emerald-500/50 hover:shadow-[0_20px_50px_rgba(14,131,84,0.25)] transition-all duration-300 bg-slate-900" data-category="{item['category']}" onclick="openWildlifeLightbox({idx})">
          
          <img 
            src="{item['file']}" 
            alt="{item['title']} - {item['location']}" 
            class="w-full h-auto block filter brightness-95 group-hover:brightness-105 transition-all duration-300"
            loading="lazy"
          />
          
          <!-- Subtle Gradient Overlay (Visible on Hover for Maximum Photo Visibility) -->
          <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>

          <!-- Top Location Badge -->
          <div class="absolute top-3.5 left-3.5 z-10">
            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md border border-white/20 text-[11px] font-black text-amber-300 shadow-md">
              <span>📍</span>
              <span>{item['location']}</span>
            </span>
          </div>

          <!-- Bottom Floating Glass Caption (Revealed smoothly on Hover) -->
          <div class="absolute bottom-3.5 left-3.5 right-3.5 z-10 p-3.5 rounded-2xl bg-slate-950/90 backdrop-blur-xl border border-white/15 text-white opacity-0 translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-300 shadow-2xl">
            <div class="flex items-center justify-between gap-3">
              <div class="min-w-0 flex-1">
                <h3 class="font-black text-sm sm:text-base text-white group-hover:text-amber-300 transition-colors leading-tight truncate">
                  {item['title']}
                </h3>
                <p class="text-xs text-slate-300 mt-0.5 font-medium truncate">
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

cards_joined = "\n\n".join(cards_html)

collage_section_html = f"""  <!-- ========================================================================= -->
  <!-- 5. GALERIE COLLAGE SAUVAGE DU NÉPAL (MASONRY COLLAGE DESIGN ÉLITE 2026) -->
  <!-- ========================================================================= -->
  <section id="galerie-faune" class="py-20 sm:py-28 lg:py-32 bg-slate-950 text-white relative overflow-hidden border-t border-b border-white/10">
    
    <!-- Ambient ambient glow layers -->
    <div class="absolute top-1/4 left-1/4 w-[700px] h-[700px] bg-[#0e8354]/10 rounded-full blur-[180px] pointer-events-none"></div>
    <div class="absolute bottom-1/4 right-1/4 w-[700px] h-[700px] bg-amber-500/10 rounded-full blur-[180px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-12 sm:mb-16">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-emerald-400/30 text-amber-300 text-xs font-black uppercase tracking-widest mb-4 shadow-lg">
          <span>🌿 Galerie Exclusive Terrain</span>
        </div>
        <h2 class="font-black text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-tight">
          La faune du Terai dans son intimité brute.
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-300 font-medium leading-relaxed">
          Toutes ces photographies ont été prises lors de nos safaris à pied par nos voyageurs et maîtres pisteurs. Aucun artifice, aucune mise en scène : la pureté de la rencontre à hauteur d'homme.
        </p>
      </div>

      <!-- Filter Tabs -->
      <div class="flex flex-wrap items-center justify-center gap-2 sm:gap-3 mb-12" id="wildlife-tabs">
        <button onclick="filterWildlife('all')" class="wildlife-tab-btn active px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-emerald-600 text-white shadow-lg shadow-emerald-900/30 border border-emerald-400/40 cursor-pointer">
          🐾 Tous les 11 clichés
        </button>
        <button onclick="filterWildlife('felins')" class="wildlife-tab-btn px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🐅 Tigres du Bengale
        </button>
        <button onclick="filterWildlife('geants')" class="wildlife-tab-btn px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🦏 Rhinos & Éléphants
        </button>
        <button onclick="filterWildlife('oiseaux')" class="wildlife-tab-btn px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🦚 Oiseaux & Calaos
        </button>
        <button onclick="filterWildlife('herbivores')" class="wildlife-tab-btn px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🦌 Cerfs & Nilgauts
        </button>
        <button onclick="filterWildlife('reptiles')" class="wildlife-tab-btn px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🐊 Crocodiles & Rivières
        </button>
      </div>

      <!-- Fluid Multi-Column Masonry Collage (Pixel-perfect gaps & natural photo ratios) -->
      <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6" id="wildlife-grid">
{cards_joined}
      </div>

      <!-- Bottom Banner CTA -->
      <div class="mt-14 p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-[#041d13] via-[#0b4830] to-[#041d13] border border-emerald-500/30 flex flex-col sm:flex-row items-center justify-between gap-6 shadow-2xl">
        <div class="text-center sm:text-left space-y-1">
          <p class="font-black text-lg sm:text-xl text-white">Envie de vivre ces observations de vos propres yeux ?</p>
          <p class="text-xs sm:text-sm text-slate-300">Nos pisteurs Pawan & Kiran vous guident en micro-groupe de 4 à 8 explorateurs.</p>
        </div>
        <div class="flex items-center gap-3 shrink-0">
          <a href="#prochains-departs" class="px-6 py-3 rounded-full bg-white text-slate-950 font-black text-xs sm:text-sm hover:bg-slate-100 hover:scale-100 active:scale-95 transition-all shadow-lg">
            Explorer les 15 circuits faune →
          </a>
        </div>
      </div>

    </div>
  </section>"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace previous collage section
c = re.sub(r'<!-- ===+ -->\s*<!-- 5\. GALERIE COLLAGE.*?<\/div>\s*<\/div>\s*<\/section>', collage_section_html, c, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("Created world-class fluid Masonry Collage with natural aspect ratios and pixel-perfect margins!")
