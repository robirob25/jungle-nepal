import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect the entire map section replacement:
old_map_section_pattern = r'<!-- ========================================================================= -->\s*<!-- 7\. CARTE DES DESTINATIONS & EXPÉDITIONS.*?<!-- ========================================================================= -->\s*<!-- 8\. PISTEURS'

new_mobile_optimized_map = """<!-- ========================================================================= -->
  <!-- 7. CARTE DES DESTINATIONS & EXPÉDITIONS (RESPONSIVE & CLEAN MOBILE) -->
  <!-- ========================================================================= -->
  <section id="carte-nepal" class="py-16 sm:py-24 lg:py-32 bg-slate-950 text-white relative overflow-hidden border-t border-white/10">
    <!-- Ambient glowing light spots -->
    <div class="absolute -top-32 left-1/4 w-[600px] h-[600px] bg-emerald-500/10 rounded-full blur-[160px] pointer-events-none"></div>
    <div class="absolute -bottom-32 right-1/4 w-[500px] h-[500px] bg-amber-500/5 rounded-full blur-[140px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">

      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-10 sm:mb-16">
        <span class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-950/80 border border-emerald-500/30 text-emerald-400 text-xs font-bold uppercase tracking-widest mb-3 sm:mb-4">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
          Géographie de vos expéditions
        </span>
        <h2 class="text-2xl sm:text-4xl lg:text-5xl font-black text-white tracking-tight leading-tight">
          Le Népal sauvage, <span class="font-serif italic font-normal text-amber-300">d'un sanctuaire à l'autre</span>.
        </h2>
        <p class="mt-3 text-sm sm:text-base text-slate-300 font-medium leading-relaxed max-w-2xl mx-auto">
          De la jungle millénaire du Teraï aux sommets de l'Himalaya. Chaque région abrite un écosystème unique, exploré à pied en micro-groupe.
        </p>
      </div>

      <!-- Main Layout: Map Canvas FIRST on Mobile, Side by Side on Desktop -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-10 items-center">
        
        <!-- Map Canvas (Placed on top on mobile for immediate visual impact) -->
        <div class="lg:col-span-7 order-1 lg:order-2">
          <div class="relative rounded-3xl overflow-hidden border border-white/15 bg-gradient-to-b from-[#141e17] via-[#0d1610] to-[#080d0a] shadow-2xl p-3 sm:p-5 lg:p-7">
            
            <!-- Map Container with Parchment Rendering -->
            <div class="relative rounded-2xl overflow-hidden bg-[#f0ebd9] shadow-inner border border-[#d4c9aa]">
              <img
                src="/nepal-map-illustrated.png"
                alt="Carte illustrée du Népal - Bardia, Chitwan, Annapurna, Katmandou"
                class="w-full h-auto object-contain filter contrast-[1.03] saturate-[0.95]"
                loading="lazy"
              />

              <!-- Interactive Pulse Hotspots on the Map (Clean, scaled for mobile) -->
              <!-- Hotspot 1: Bardia -->
              <a href="/destinations/bardia.html" class="absolute top-[38%] left-[24%] -translate-x-1/2 -translate-y-1/2 group cursor-pointer" aria-label="Bardia National Park">
                <span class="relative flex h-6 w-6 sm:h-8 sm:w-8 items-center justify-center">
                  <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-amber-400 opacity-60"></span>
                  <span class="relative inline-flex rounded-full h-4 w-4 sm:h-5 sm:w-5 bg-amber-500 text-slate-950 font-black text-[9px] sm:text-[10px] items-center justify-center shadow-lg border sm:border-2 border-white">
                    🐅
                  </span>
                </span>
                <div class="hidden sm:block absolute -top-8 left-1/2 -translate-x-1/2 bg-slate-950/95 text-amber-300 text-[10px] font-extrabold px-2 py-0.5 rounded-full whitespace-nowrap shadow-xl border border-amber-400/30">
                  Bardia
                </div>
              </a>

              <!-- Hotspot 2: Chitwan -->
              <a href="/destinations/chitwan.html" class="absolute top-[65%] left-[50%] -translate-x-1/2 -translate-y-1/2 group cursor-pointer" aria-label="Chitwan National Park">
                <span class="relative flex h-6 w-6 sm:h-8 sm:w-8 items-center justify-center">
                  <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-60"></span>
                  <span class="relative inline-flex rounded-full h-4 w-4 sm:h-5 sm:w-5 bg-emerald-500 text-white font-black text-[9px] sm:text-[10px] items-center justify-center shadow-lg border sm:border-2 border-white">
                    🦏
                  </span>
                </span>
                <div class="hidden sm:block absolute -top-8 left-1/2 -translate-x-1/2 bg-slate-950/95 text-emerald-300 text-[10px] font-extrabold px-2 py-0.5 rounded-full whitespace-nowrap shadow-xl border border-emerald-400/30">
                  Chitwan
                </div>
              </a>

              <!-- Hotspot 3: Annapurna -->
              <a href="/destinations/annapurna.html" class="absolute top-[42%] left-[45%] -translate-x-1/2 -translate-y-1/2 group cursor-pointer" aria-label="Annapurna & Pokhara">
                <span class="relative flex h-5 w-5 sm:h-7 sm:w-7 items-center justify-center">
                  <span class="relative inline-flex rounded-full h-3 w-3 sm:h-4 sm:w-4 bg-cyan-500 text-white font-black text-[8px] items-center justify-center shadow border sm:border-2 border-white"></span>
                </span>
                <div class="hidden sm:block absolute -top-7 left-1/2 -translate-x-1/2 bg-slate-950/90 text-cyan-200 text-[9px] font-extrabold px-1.5 py-0.5 rounded-full whitespace-nowrap shadow border border-cyan-400/20">
                  Annapurnas
                </div>
              </a>

              <!-- Hotspot 4: Kathmandu -->
              <a href="/destinations/katmandou.html" class="absolute top-[58%] left-[62%] -translate-x-1/2 -translate-y-1/2 group cursor-pointer" aria-label="Kathmandu Valley">
                <span class="relative flex h-5 w-5 sm:h-7 sm:w-7 items-center justify-center">
                  <span class="relative inline-flex rounded-full h-3 w-3 sm:h-4 sm:w-4 bg-orange-500 text-white font-black text-[8px] items-center justify-center shadow border sm:border-2 border-white"></span>
                </span>
                <div class="hidden sm:block absolute -top-7 left-1/2 -translate-x-1/2 bg-slate-950/90 text-orange-200 text-[9px] font-extrabold px-1.5 py-0.5 rounded-full whitespace-nowrap shadow border border-orange-400/20">
                  Katmandou
                </div>
              </a>

            </div>

            <!-- Mobile-Friendly Legend Bar -->
            <div class="mt-3 sm:mt-4 flex items-center justify-between gap-2 text-[11px] sm:text-xs text-slate-300 pt-2 border-t border-white/10">
              <div class="flex items-center gap-3 overflow-x-auto no-scrollbar">
                <span class="flex items-center gap-1 shrink-0"><span class="w-2 h-2 rounded-full bg-amber-400"></span> Bardia</span>
                <span class="flex items-center gap-1 shrink-0"><span class="w-2 h-2 rounded-full bg-emerald-400"></span> Chitwan</span>
                <span class="flex items-center gap-1 shrink-0"><span class="w-2 h-2 rounded-full bg-cyan-400"></span> Himalaya</span>
              </div>
              <a href="/destinations.html" class="text-emerald-400 hover:text-emerald-300 font-bold shrink-0 transition-colors">
                Guide des 5 régions →
              </a>
            </div>

          </div>
        </div>

        <!-- Destination Sanctuary Cards (Left / Below Map on Mobile) -->
        <div class="lg:col-span-5 space-y-3 sm:space-y-4 order-2 lg:order-1">
          
          <!-- 1. Bardia -->
          <a href="/destinations/bardia.html" class="block p-4 sm:p-5 rounded-2xl sm:rounded-3xl bg-slate-900/90 border border-white/10 hover:border-emerald-500/50 hover:bg-slate-900 transition-all duration-300 group shadow-lg">
            <div class="flex items-start justify-between gap-2">
              <div>
                <div class="flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                  <h3 class="font-black text-base sm:text-lg text-white group-hover:text-amber-300 transition-colors">Parc national de Bardia</h3>
                </div>
                <p class="text-xs text-slate-300 font-medium leading-relaxed mt-1">
                  Sanctuaire des tigres du Bengale, éléphants et dauphins du Gange. Safaris silencieux à pied &amp; bivouacs sauvages.
                </p>
              </div>
              <span class="text-[10px] sm:text-[11px] font-mono font-bold text-emerald-400 bg-emerald-950/80 px-2 py-0.5 rounded-full border border-emerald-500/30 shrink-0">
                10 séjours
              </span>
            </div>
            <div class="mt-2.5 pt-2.5 border-t border-white/5 flex items-center justify-between text-xs">
              <span class="text-slate-400 text-[11px]">Faune : Tigres, éléphants, gavials</span>
              <span class="text-emerald-400 font-bold flex items-center gap-1 group-hover:translate-x-0.5 transition-transform text-xs">
                Explorer →
              </span>
            </div>
          </a>

          <!-- 2. Chitwan -->
          <a href="/destinations/chitwan.html" class="block p-4 sm:p-5 rounded-2xl sm:rounded-3xl bg-slate-900/60 border border-white/10 hover:border-emerald-500/50 hover:bg-slate-900 transition-all duration-300 group shadow-lg">
            <div class="flex items-start justify-between gap-2">
              <div>
                <div class="flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                  <h3 class="font-black text-base sm:text-lg text-white group-hover:text-amber-300 transition-colors">Parc national de Chitwan</h3>
                </div>
                <p class="text-xs text-slate-300 font-medium leading-relaxed mt-1">
                  Terre ancestrale des rhinocéros unicornes et du peuple Tharu. Pirogues traditionnelles et jungle subtropicale.
                </p>
              </div>
              <span class="text-[10px] sm:text-[11px] font-mono font-bold text-emerald-400 bg-emerald-950/80 px-2 py-0.5 rounded-full border border-emerald-500/30 shrink-0">
                3 séjours
              </span>
            </div>
            <div class="mt-2.5 pt-2.5 border-t border-white/5 flex items-center justify-between text-xs">
              <span class="text-slate-400 text-[11px]">Faune : Rhinocéros unicornes</span>
              <span class="text-emerald-400 font-bold flex items-center gap-1 group-hover:translate-x-0.5 transition-transform text-xs">
                Explorer →
              </span>
            </div>
          </a>

          <!-- 3. Annapurna & Mustang -->
          <a href="/destinations/annapurna.html" class="block p-4 sm:p-5 rounded-2xl sm:rounded-3xl bg-slate-900/60 border border-white/10 hover:border-emerald-500/50 hover:bg-slate-900 transition-all duration-300 group shadow-lg">
            <div class="flex items-start justify-between gap-2">
              <div>
                <div class="flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                  <h3 class="font-black text-base sm:text-lg text-white group-hover:text-amber-300 transition-colors">Annapurnas &amp; Mustang</h3>
                </div>
                <p class="text-xs text-slate-300 font-medium leading-relaxed mt-1">
                  Haute altitude : tracking de la panthère des neiges (4 700 m), spiritualité tibétaine et balcons alpins.
                </p>
              </div>
              <span class="text-[10px] sm:text-[11px] font-mono font-bold text-emerald-400 bg-emerald-950/80 px-2 py-0.5 rounded-full border border-emerald-500/30 shrink-0">
                4 séjours
              </span>
            </div>
            <div class="mt-2.5 pt-2.5 border-t border-white/5 flex items-center justify-between text-xs">
              <span class="text-slate-400 text-[11px]">Altitude : 4 700 m • Panthère</span>
              <span class="text-emerald-400 font-bold flex items-center gap-1 group-hover:translate-x-0.5 transition-transform text-xs">
                Explorer →
              </span>
            </div>
          </a>

        </div>

      </div>

      <!-- Action Button Centered -->
      <div class="mt-10 sm:mt-14 text-center">
        <a href="#prochains-departs" class="inline-flex items-center gap-2.5 px-7 py-3.5 sm:px-8 sm:py-4 rounded-full bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:bg-right bg-[length:200%_auto] text-white font-extrabold text-xs sm:text-sm shadow-xl shadow-emerald-950/50 hover:scale-105 active:scale-95 transition-all duration-300">
          <span>Choisir un circuit par territoire</span>
          <span>→</span>
        </a>
      </div>

    </div>
  </section>"""

content = re.sub(
    old_map_section_pattern,
    new_mobile_optimized_map + '\n\n  <!-- ========================================================================= -->\n  <!-- 8. PISTEURS',
    content,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Replaced with fully responsive, mobile-first map section!")
