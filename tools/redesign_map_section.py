import re

new_map_section = """  <!-- ========================================================================= -->
  <!-- 7. CARTE DES DESTINATIONS & EXPÉDITIONS (INTERACTIVE SPLIT LAYOUT 2026) -->
  <!-- ========================================================================= -->
  <section id="carte-nepal" class="py-20 sm:py-28 lg:py-32 bg-slate-950 text-white relative overflow-hidden border-t border-white/10">
    <!-- Ambient glowing light spots -->
    <div class="absolute -top-32 left-1/4 w-[600px] h-[600px] bg-emerald-500/10 rounded-full blur-[160px] pointer-events-none"></div>
    <div class="absolute -bottom-32 right-1/4 w-[500px] h-[500px] bg-amber-500/5 rounded-full blur-[140px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">

      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-16 sm:mb-20">
        <span class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-950/80 border border-emerald-500/30 text-emerald-400 text-xs font-bold uppercase tracking-widest mb-4">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
          Géographie de vos expéditions
        </span>
        <h2 class="text-3xl sm:text-5xl lg:text-6xl font-black text-white tracking-tight leading-tight">
          Le Népal sauvage, <span class="font-serif italic font-normal text-amber-300">d'un sanctuaire à l'autre</span>.
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-300 font-medium leading-relaxed">
          De la jungle millénaire du Teraï aux sommets de l'Himalaya. Chaque région abrite un écosystème unique, exploré à pied en micro-groupe.
        </p>
      </div>

      <!-- Split Layout: Interactive Sanctuary Cards (Left) + Visual Map Canvas (Right) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
        
        <!-- Left: Destination Sanctuary Interactive Cards (5 cols) -->
        <div class="lg:col-span-5 space-y-4">
          
          <!-- 1. Bardia -->
          <div class="map-region-card p-5 sm:p-6 rounded-3xl bg-slate-900/90 border border-white/10 hover:border-emerald-500/50 hover:bg-slate-900 transition-all duration-300 cursor-pointer group shadow-xl" onclick="highlightMapPin('bardia')">
            <div class="flex items-start justify-between gap-3">
              <div class="space-y-1">
                <div class="flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                  <h3 class="font-black text-lg text-white group-hover:text-amber-300 transition-colors">Parc national de Bardia</h3>
                </div>
                <p class="text-xs text-slate-300 font-medium leading-relaxed">
                  Le sanctuaire secret des tigres du Bengale, éléphants et dauphins du Gange. Safaris silencieux à pied &amp; bivouacs en bord de rivière.
                </p>
              </div>
              <span class="text-[11px] font-mono font-bold text-emerald-400 bg-emerald-950/80 px-2.5 py-1 rounded-full border border-emerald-500/30 shrink-0">
                10 séjours
              </span>
            </div>
            <div class="mt-3 pt-3 border-t border-white/5 flex items-center justify-between text-xs">
              <span class="text-slate-400 font-medium">Faune : Tigres, éléphants, gavials</span>
              <a href="/destinations/bardia.html" class="text-emerald-400 hover:text-emerald-300 font-bold flex items-center gap-1 group-hover:translate-x-0.5 transition-transform">
                Explorer →
              </a>
            </div>
          </div>

          <!-- 2. Chitwan -->
          <div class="map-region-card p-5 sm:p-6 rounded-3xl bg-slate-900/60 border border-white/10 hover:border-emerald-500/50 hover:bg-slate-900 transition-all duration-300 cursor-pointer group shadow-xl" onclick="highlightMapPin('chitwan')">
            <div class="flex items-start justify-between gap-3">
              <div class="space-y-1">
                <div class="flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                  <h3 class="font-black text-lg text-white group-hover:text-amber-300 transition-colors">Parc national de Chitwan</h3>
                </div>
                <p class="text-xs text-slate-300 font-medium leading-relaxed">
                  Terre ancestrale des rhinocéros unicornes et du peuple Tharu. Pirogues traditionnelles sur la Rapti et forêts subtropicales denses.
                </p>
              </div>
              <span class="text-[11px] font-mono font-bold text-emerald-400 bg-emerald-950/80 px-2.5 py-1 rounded-full border border-emerald-500/30 shrink-0">
                3 séjours
              </span>
            </div>
            <div class="mt-3 pt-3 border-t border-white/5 flex items-center justify-between text-xs">
              <span class="text-slate-400 font-medium">Faune : Rhinocéros unicornes, oiseaux</span>
              <a href="/destinations/chitwan.html" class="text-emerald-400 hover:text-emerald-300 font-bold flex items-center gap-1 group-hover:translate-x-0.5 transition-transform">
                Explorer →
              </a>
            </div>
          </div>

          <!-- 3. Annapurnas & Pokhara -->
          <div class="map-region-card p-5 sm:p-6 rounded-3xl bg-slate-900/60 border border-white/10 hover:border-emerald-500/50 hover:bg-slate-900 transition-all duration-300 cursor-pointer group shadow-xl" onclick="highlightMapPin('annapurna')">
            <div class="flex items-start justify-between gap-3">
              <div class="space-y-1">
                <div class="flex items-center gap-2">
                  <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
                  <h3 class="font-black text-lg text-white group-hover:text-amber-300 transition-colors">Annapurnas &amp; Mustang</h3>
                </div>
                <p class="text-xs text-slate-300 font-medium leading-relaxed">
                  Trésors de haute altitude : tracking de la panthère des neiges (4 700 m), festivals bouddhistes secrets et balcons himalayens.
                </p>
              </div>
              <span class="text-[11px] font-mono font-bold text-emerald-400 bg-emerald-950/80 px-2.5 py-1 rounded-full border border-emerald-500/30 shrink-0">
                4 séjours
              </span>
            </div>
            <div class="mt-3 pt-3 border-t border-white/5 flex items-center justify-between text-xs">
              <span class="text-slate-400 font-medium">Altitude : 4 700 m max • Panthère des neiges</span>
              <a href="/destinations/annapurna.html" class="text-emerald-400 hover:text-emerald-300 font-bold flex items-center gap-1 group-hover:translate-x-0.5 transition-transform">
                Explorer →
              </a>
            </div>
          </div>

        </div>

        <!-- Right: Map Canvas with Interactive Hotspots (7 cols) -->
        <div class="lg:col-span-7">
          <div class="relative rounded-3xl overflow-hidden border border-white/15 bg-gradient-to-b from-[#141e17] via-[#0d1610] to-[#080d0a] shadow-2xl p-4 sm:p-6 lg:p-8">
            
            <!-- Map Container with Parchment Rendering -->
            <div class="relative rounded-2xl overflow-hidden bg-[#f0ebd9] shadow-inner border border-[#d4c9aa]">
              <img
                src="/nepal-map-illustrated.png"
                alt="Carte illustrée du Népal - Bardia, Chitwan, Annapurna, Katmandou"
                class="w-full h-auto object-contain filter contrast-[1.03] saturate-[0.95]"
                loading="lazy"
              />

              <!-- Interactive Pulse Hotspots on the Map -->
              <!-- Hotspot 1: Bardia (West Jungle) -->
              <div id="pin-bardia" class="absolute top-[38%] left-[24%] -translate-x-1/2 -translate-y-1/2 group/pin cursor-pointer" onclick="window.location.href='/destinations/bardia.html'">
                <span class="relative flex h-8 w-8 items-center justify-center">
                  <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-amber-400 opacity-60"></span>
                  <span class="relative inline-flex rounded-full h-5 w-5 bg-amber-500 text-slate-950 font-black text-[10px] items-center justify-center shadow-lg border-2 border-white">
                    🐅
                  </span>
                </span>
                <!-- Tooltip -->
                <div class="absolute -top-9 left-1/2 -translate-x-1/2 bg-slate-950/95 text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full whitespace-nowrap shadow-xl border border-amber-400/30 opacity-90 group-hover/pin:opacity-100 transition-opacity">
                  Bardia (Tigres &amp; Jungle)
                </div>
              </div>

              <!-- Hotspot 2: Chitwan (South Jungle) -->
              <div id="pin-chitwan" class="absolute top-[65%] left-[50%] -translate-x-1/2 -translate-y-1/2 group/pin cursor-pointer" onclick="window.location.href='/destinations/chitwan.html'">
                <span class="relative flex h-8 w-8 items-center justify-center">
                  <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-60"></span>
                  <span class="relative inline-flex rounded-full h-5 w-5 bg-emerald-500 text-white font-black text-[10px] items-center justify-center shadow-lg border-2 border-white">
                    🦏
                  </span>
                </span>
                <div class="absolute -top-9 left-1/2 -translate-x-1/2 bg-slate-950/95 text-emerald-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full whitespace-nowrap shadow-xl border border-emerald-400/30 opacity-90 group-hover/pin:opacity-100 transition-opacity">
                  Chitwan (Rhinocéros)
                </div>
              </div>

              <!-- Hotspot 3: Annapurnas / Pokhara (Center North) -->
              <div id="pin-annapurna" class="absolute top-[42%] left-[45%] -translate-x-1/2 -translate-y-1/2 group/pin cursor-pointer" onclick="window.location.href='/destinations/annapurna.html'">
                <span class="relative flex h-7 w-7 items-center justify-center">
                  <span class="relative inline-flex rounded-full h-4 w-4 bg-cyan-500 text-white font-black text-[8px] items-center justify-center shadow border-2 border-white"></span>
                </span>
                <div class="absolute -top-8 left-1/2 -translate-x-1/2 bg-slate-950/90 text-cyan-200 text-[9px] font-extrabold px-2 py-0.5 rounded-full whitespace-nowrap shadow border border-cyan-400/20">
                  Annapurnas
                </div>
              </div>

              <!-- Hotspot 4: Kathmandu (East Valley) -->
              <div id="pin-kathmandu" class="absolute top-[58%] left-[62%] -translate-x-1/2 -translate-y-1/2 group/pin cursor-pointer" onclick="window.location.href='/destinations/katmandou.html'">
                <span class="relative flex h-7 w-7 items-center justify-center">
                  <span class="relative inline-flex rounded-full h-4 w-4 bg-orange-500 text-white font-black text-[8px] items-center justify-center shadow border-2 border-white"></span>
                </span>
                <div class="absolute -top-8 left-1/2 -translate-x-1/2 bg-slate-950/90 text-orange-200 text-[9px] font-extrabold px-2 py-0.5 rounded-full whitespace-nowrap shadow border border-orange-400/20">
                  Katmandou
                </div>
              </div>

            </div>

            <!-- Bottom Badges Bar -->
            <div class="mt-4 flex flex-wrap items-center justify-between gap-3 text-xs text-slate-300 pt-2 border-t border-white/10">
              <div class="flex items-center gap-4">
                <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-amber-400"></span> Bardia &amp; Ouest sauvage</span>
                <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-emerald-400"></span> Teraï &amp; Chitwan</span>
                <span class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-cyan-400"></span> Himalaya</span>
              </div>
              <a href="/destinations.html" class="text-emerald-400 hover:text-emerald-300 font-bold flex items-center gap-1 transition-colors">
                Guide complet des 5 régions →
              </a>
            </div>

          </div>
        </div>

      </div>

      <!-- Action Button Centered -->
      <div class="mt-14 sm:mt-16 text-center">
        <a href="#prochains-departs" class="inline-flex items-center gap-3 px-8 py-4 rounded-full bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:bg-right bg-[length:200%_auto] text-white font-extrabold text-sm shadow-xl shadow-emerald-950/50 hover:scale-105 active:scale-95 transition-all duration-300">
          <span>Choisir un circuit par territoire</span>
          <span>→</span>
        </a>
      </div>

    </div>
  </section>"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the map section in index.astro
old_map_pattern = r'<!-- ========================================================================= -->\s*<!-- MAP : LE NÉPAL EN UN COUP D\'ŒIL.*?<!-- ========================================================================= -->\s*<!-- 8\. PISTEURS'

content = re.sub(
    old_map_pattern,
    new_map_section + '\n\n  <!-- ========================================================================= -->\n  <!-- 8. PISTEURS',
    content,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Replaced map section with high-end split layout 2026!")
