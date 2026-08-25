import re

fpath = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html'

with open(fpath, 'r', encoding='utf-8') as f:
    c = f.read()

map_section = """
  <!-- ========================================================================= -->
  <!-- MAP SECTION : LE NÉPAL EN UN COUP D'ŒIL -->
  <!-- ========================================================================= -->
  <section id="carte-nepal" class="py-20 sm:py-28 bg-[#f5f1ea] border-t border-slate-200/60 overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">

      <!-- Header -->
      <div class="text-center max-w-2xl mx-auto mb-12 sm:mb-16">
        <span class="inline-flex items-center gap-2 text-xs font-black uppercase tracking-widest text-[#0e8354] mb-4">
          <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
          </svg>
          Vos terrains d'aventure
        </span>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-950 tracking-tight leading-tight mb-4">
          Le Népal,<br class="hidden sm:block"/> grandeur nature
        </h2>
        <p class="text-base sm:text-lg text-slate-500 font-medium leading-relaxed">
          De la jungle de Bardia aux neiges éternelles de l'Everest — chaque séjour vous ancre dans un territoire unique, loin des circuits balisés.
        </p>
      </div>

      <!-- Map card -->
      <div class="relative rounded-3xl overflow-hidden shadow-2xl shadow-slate-900/20 border border-slate-200/80 group max-w-5xl mx-auto">

        <!-- Background texture layer -->
        <div class="absolute inset-0 bg-[#e8e0ce]/40 pointer-events-none z-10"></div>

        <!-- The map image -->
        <img
          src="assets/nepal-map-illustrated.png"
          alt="Carte illustrée du Népal avec Bardia, Chitwan, l'Annapurna, l'Everest et Katmandou"
          class="w-full h-auto object-contain transition-transform duration-700 ease-out group-hover:scale-[1.02]"
          loading="lazy"
        />

        <!-- Subtle vignette overlay -->
        <div class="absolute inset-0 pointer-events-none z-20"
             style="background: radial-gradient(ellipse at center, transparent 55%, rgba(30,20,10,0.18) 100%);">
        </div>

        <!-- Hotspot badges — Bardia -->
        <div class="absolute top-[38%] left-[10%] z-30 hidden md:flex flex-col items-center gap-1 cursor-default">
          <div class="bg-[#0e8354] text-white text-[11px] font-black uppercase tracking-wide px-3 py-1.5 rounded-full shadow-lg shadow-[#0e8354]/40 whitespace-nowrap hover:scale-105 transition-transform">
            🐘 Bardia — Jungle & Tigers
          </div>
        </div>

        <!-- Hotspot — Chitwan -->
        <div class="absolute top-[70%] left-[42%] z-30 hidden md:flex flex-col items-center gap-1 cursor-default">
          <div class="bg-[#0e8354] text-white text-[11px] font-black uppercase tracking-wide px-3 py-1.5 rounded-full shadow-lg shadow-[#0e8354]/40 whitespace-nowrap hover:scale-105 transition-transform">
            🦏 Chitwan — Faune sauvage
          </div>
        </div>

        <!-- Hotspot — Everest -->
        <div class="absolute top-[18%] right-[6%] z-30 hidden md:flex flex-col items-center gap-1 cursor-default">
          <div class="bg-slate-900 text-white text-[11px] font-black uppercase tracking-wide px-3 py-1.5 rounded-full shadow-lg whitespace-nowrap hover:scale-105 transition-transform">
            🏔️ Everest 8848m
          </div>
        </div>

      </div>

      <!-- CTA under map -->
      <div class="mt-10 sm:mt-14 flex flex-col sm:flex-row items-center justify-center gap-4">
        <a href="#prochains-departs"
           class="inline-flex items-center gap-2.5 px-7 py-4 rounded-full bg-[#0e8354] text-white font-extrabold text-sm shadow-xl shadow-[#0e8354]/30 hover:bg-[#0c7248] hover:scale-105 active:scale-95 transition-all">
          <svg class="w-4 h-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
          </svg>
          Choisir mon séjour
        </a>
        <a href="destinations/index.html"
           class="inline-flex items-center gap-2 text-sm font-bold text-slate-600 hover:text-slate-900 transition-colors">
          Explorer toutes les destinations
          <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"/></svg>
        </a>
      </div>

    </div>
  </section>

"""

# Insert just before the pisteurs section
marker = '  <!-- =========================================================================\n  <!-- 8. PISTEURS'
if marker not in c:
    # Try alternative marker
    marker = '  <section id="pisteurs"'

c_new = c.replace(marker, map_section + marker, 1)

if c_new == c:
    print("ERROR: Marker not found")
else:
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c_new)
    print("OK — map section inserted before #pisteurs")
