import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/create_native_svg_map.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Extract svg_map_code
match = re.search(r'svg_map_code = """(.*?)"""', code, re.DOTALL)
if not match:
    print("Could not find svg_map_code")
    exit(1)

svg_map_html = match.group(1)

native_section_html = f"""  <!-- ========================================================================= -->
  <!-- 4.5 CARTE GÉOGRAPHIQUE VECTORIELLE DU NÉPAL SAUVAGE -->
  <!-- ========================================================================= -->
  <section id="carte-nepal" class="py-20 sm:py-28 bg-[#030b14] text-white relative overflow-hidden border-t border-white/5">
    <!-- Ambient backlights -->
    <div class="absolute top-1/2 left-1/4 -translate-y-1/2 w-96 h-96 bg-emerald-500/10 rounded-full blur-[120px] pointer-events-none"></div>
    <div class="absolute bottom-10 right-1/4 w-96 h-96 bg-amber-500/5 rounded-full blur-[140px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-12 sm:mb-16">
        <span class="inline-flex items-center gap-2 text-xs font-black uppercase tracking-widest text-amber-400 bg-amber-950/60 border border-amber-500/30 px-4 py-1.5 rounded-full mb-4 shadow-inner">
          <span>🗺️</span>
          <span>Géographie Sauvage & Sanctuaires</span>
        </span>
        <h2 class="font-black text-3xl sm:text-5xl text-white tracking-tight leading-tight">
          Où se déroulent nos expéditions ?
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-300 font-medium leading-relaxed">
          De la jungle primaire de Bardia aux sanctuaires fluviaux de Chitwan et aux géants de l'Himalaya. Explorez la carte vectorielle interactive du Népal.
        </p>
      </div>

      <!-- Main Map Container Card -->
      <div class="rounded-3xl bg-slate-900/90 border border-white/15 p-4 sm:p-8 lg:p-10 shadow-[0_25px_60px_rgba(0,0,0,0.7)] relative overflow-hidden backdrop-blur-xl">
        
        <!-- Native Interactive Vector SVG Map -->
        {svg_map_html}

        <!-- Dynamic Destination Card Below Map -->
        <div id="map-detail-card" class="mt-6 sm:mt-8 p-6 sm:p-7 rounded-2xl bg-slate-950/90 border border-emerald-500/30 flex flex-col md:flex-row items-start md:items-center justify-between gap-6 transition-all duration-300">
          <div class="space-y-1.5 flex-1">
            <div class="flex flex-wrap items-center gap-2.5">
              <span id="map-detail-badge" class="px-3 py-1 rounded-full text-xs font-black uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                Parc National de Bardia (Ouest Sauvage)
              </span>
              <span id="map-detail-fauna" class="text-xs font-semibold text-amber-300">
                🐅 Tigre du Bengale • 🐘 Éléphants sauvages • 🐆 Léopards
              </span>
            </div>
            <h3 id="map-detail-title" class="text-xl sm:text-2xl font-black text-white tracking-tight">
              Le sanctuaire ultime pour le safari à pied en forêt primaire
            </h3>
            <p id="map-detail-desc" class="text-xs sm:text-sm text-slate-300 leading-relaxed max-w-3xl">
              Immersion totale dans la plus vaste forêt préservée du Népal et la mystérieuse vallée de la Babai. Moins de 2% des touristes du Népal y accèdent, garantissant une observation animale exclusive et respectueuse.
            </p>
          </div>
          <div class="shrink-0 flex items-center gap-3 w-full md:w-auto">
            <a 
              id="map-detail-link" 
              href="/destinations/bardia" 
              class="w-full md:w-auto px-6 py-3.5 rounded-full bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold text-xs sm:text-sm text-center shadow-lg shadow-emerald-950/50 transition-all hover:scale-105 active:scale-95"
            >
              Explorer le guide Bardia →
            </a>
          </div>
        </div>

        <!-- Destination Selection Buttons / Pills -->
        <div class="mt-6 flex flex-wrap items-center justify-center gap-2 sm:gap-3">
          <button 
            onclick="selectMapLocation('bardia')" 
            class="map-pill-btn px-4 py-2 rounded-full text-xs font-black border transition-all duration-200 bg-emerald-600 text-white border-emerald-400/50 cursor-pointer shadow-md"
            data-loc="bardia"
          >
            🐅 Bardia National Park
          </button>
          <button 
            onclick="selectMapLocation('chitwan')" 
            class="map-pill-btn px-4 py-2 rounded-full text-xs font-black border transition-all duration-200 bg-white/10 text-slate-300 hover:bg-white/20 border-white/10 hover:text-white cursor-pointer"
            data-loc="chitwan"
          >
            🦏 Chitwan National Park
          </button>
          <button 
            onclick="selectMapLocation('katmandou')" 
            class="map-pill-btn px-4 py-2 rounded-full text-xs font-black border transition-all duration-200 bg-white/10 text-slate-300 hover:bg-white/20 border-white/10 hover:text-white cursor-pointer"
            data-loc="katmandou"
          >
            ⭐ Vallée de Katmandou
          </button>
          <button 
            onclick="selectMapLocation('annapurna')" 
            class="map-pill-btn px-4 py-2 rounded-full text-xs font-black border transition-all duration-200 bg-white/10 text-slate-300 hover:bg-white/20 border-white/10 hover:text-white cursor-pointer"
            data-loc="annapurna"
          >
            🏔️ Pokhara & Annapurnas
          </button>
          <button 
            onclick="selectMapLocation('rara')" 
            class="map-pill-btn px-4 py-2 rounded-full text-xs font-black border transition-all duration-200 bg-white/10 text-slate-300 hover:bg-white/20 border-white/10 hover:text-white cursor-pointer"
            data-loc="rara"
          >
            💧 Lac Rara & Hautes Terres
          </button>
        </div>

      </div>

    </div>
  </section>"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx = f.read()

idx = re.sub(
    r'<!-- ========================================================================= -->\s*<!-- 4\.5 CARTE GÉOGRAPHIQUE INTERACTIVE.*?<!-- ========================================================================= -->\s*<!-- 5\. GALERIE',
    native_section_html + '\n\n  <!-- ========================================================================= -->\n  <!-- 5. GALERIE',
    idx,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx)

print("Successfully injected 100% native vector SVG map of Nepal into index.astro!")
