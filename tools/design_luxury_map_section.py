import re

new_map_section = """  <!-- ========================================================================= -->
  <!-- 7.5 CARTE GÉOGRAPHIQUE INTÉGRÉE & SANCTUAIRES SAUVAGES (LUXURY EXPEDITION) -->
  <!-- ========================================================================= -->
  <section id="carte-territoires" class="scroll-mt-20 py-20 sm:py-28 lg:py-32 bg-[#f5f1ea] relative overflow-hidden border-t border-amber-950/10">
    
    <!-- Subtle Background Topographic Watermark -->
    <div class="absolute inset-0 opacity-25 pointer-events-none" style="background-image: radial-gradient(#b08958 0.75px, transparent 0.75px); background-size: 32px 32px;"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-12 sm:mb-16">
        <span class="inline-flex items-center gap-2 text-xs font-black uppercase tracking-widest text-[#0e8354] bg-emerald-950/5 border border-emerald-800/20 px-4 py-1.5 rounded-full mb-4 shadow-sm">
          <span>🧭</span>
          <span>Vos Terrains d'Aventure</span>
        </span>
        <h2 class="font-black text-3xl sm:text-5xl text-slate-900 tracking-tight leading-tight">
          Le Népal sauvage, grandeur nature.
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-600 font-medium leading-relaxed">
          De la jungle primaire de Bardia aux sanctuaires fluviaux de Chitwan et aux contreforts des Annapurnas : chaque expédition vous ancre dans un territoire préservé, loin des foules.
        </p>
      </div>

      <!-- Organic Seamless Map Stage -->
      <div class="relative max-w-5xl mx-auto">
        
        <!-- Ambient Radial Glow behind map -->
        <div class="absolute inset-0 bg-amber-500/5 rounded-full blur-3xl pointer-events-none"></div>

        <!-- The Map Illustration with Soft Seamless Feathering -->
        <div class="relative overflow-hidden rounded-3xl group">
          <img
            src="/nepal-map-illustrated.png"
            alt="Carte géographique illustrée du Népal - Bardia, Chitwan, Annapurna, Everest et Katmandou"
            width="1024"
            height="490"
            style="aspect-ratio: 1024/490; mix-blend-mode: multiply;"
            class="w-full h-auto object-contain block transition-transform duration-700 ease-out group-hover:scale-[1.01]"
            loading="lazy"
          />

          <!-- Interactive Hotspot 1: BARDIA NATIONAL PARK -->
          <a 
            href="/destinations/bardia.html" 
            class="absolute top-[52%] left-[28%] -translate-x-1/2 -translate-y-1/2 group/pin cursor-pointer z-20"
            aria-label="Explorer Bardia National Park"
          >
            <div class="relative flex items-center justify-center">
              <span class="absolute w-8 h-8 rounded-full bg-emerald-500/30 animate-ping pointer-events-none"></span>
              <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-[#0e8354] border-2 border-white text-white font-black text-xs flex items-center justify-center shadow-lg transition-transform group-hover/pin:scale-125">
                🐅
              </div>
              <!-- Floating Tooltip on Hover -->
              <div class="absolute bottom-full mb-2 left-1/2 -translate-x-1/2 opacity-0 group-hover/pin:opacity-100 transition-all duration-200 pointer-events-none z-30 whitespace-nowrap">
                <div class="bg-slate-950/95 backdrop-blur-md text-white px-3.5 py-1.5 rounded-xl text-xs font-bold shadow-xl border border-white/10 flex items-center gap-1.5">
                  <span class="text-amber-400 font-extrabold">Bardia :</span>
                  <span>Royaume des tigres & safaris à pied</span>
                  <span class="text-emerald-400">→</span>
                </div>
              </div>
            </div>
          </a>

          <!-- Interactive Hotspot 2: CHITWAN NATIONAL PARK -->
          <a 
            href="/destinations/chitwan.html" 
            class="absolute top-[72%] left-[50%] -translate-x-1/2 -translate-y-1/2 group/pin cursor-pointer z-20"
            aria-label="Explorer Chitwan National Park"
          >
            <div class="relative flex items-center justify-center">
              <span class="absolute w-8 h-8 rounded-full bg-emerald-500/30 animate-ping pointer-events-none"></span>
              <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-[#0e8354] border-2 border-white text-white font-black text-xs flex items-center justify-center shadow-lg transition-transform group-hover/pin:scale-125">
                🦏
              </div>
              <!-- Floating Tooltip on Hover -->
              <div class="absolute bottom-full mb-2 left-1/2 -translate-x-1/2 opacity-0 group-hover/pin:opacity-100 transition-all duration-200 pointer-events-none z-30 whitespace-nowrap">
                <div class="bg-slate-950/95 backdrop-blur-md text-white px-3.5 py-1.5 rounded-xl text-xs font-bold shadow-xl border border-white/10 flex items-center gap-1.5">
                  <span class="text-amber-400 font-extrabold">Chitwan :</span>
                  <span>Sanctuaire des rhinocéros & pirogues</span>
                  <span class="text-emerald-400">→</span>
                </div>
              </div>
            </div>
          </a>

          <!-- Interactive Hotspot 3: ANNAPURNAS & POKHARA -->
          <a 
            href="/destinations/annapurna.html" 
            class="absolute top-[54%] left-[45%] -translate-x-1/2 -translate-y-1/2 group/pin cursor-pointer z-20"
            aria-label="Explorer Pokhara et Annapurnas"
          >
            <div class="relative flex items-center justify-center">
              <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-slate-900 border-2 border-white text-white font-black text-xs flex items-center justify-center shadow-lg transition-transform group-hover/pin:scale-125">
                🏔️
              </div>
              <!-- Floating Tooltip on Hover -->
              <div class="absolute bottom-full mb-2 left-1/2 -translate-x-1/2 opacity-0 group-hover/pin:opacity-100 transition-all duration-200 pointer-events-none z-30 whitespace-nowrap">
                <div class="bg-slate-950/95 backdrop-blur-md text-white px-3.5 py-1.5 rounded-xl text-xs font-bold shadow-xl border border-white/10 flex items-center gap-1.5">
                  <span class="text-amber-400 font-extrabold">Pokhara & Annapurnas :</span>
                  <span>Lacs sacrés & balcons alpins</span>
                  <span class="text-emerald-400">→</span>
                </div>
              </div>
            </div>
          </a>

          <!-- Interactive Hotspot 4: KATHMANDU -->
          <a 
            href="/destinations/katmandou.html" 
            class="absolute top-[67%] left-[60%] -translate-x-1/2 -translate-y-1/2 group/pin cursor-pointer z-20"
            aria-label="Explorer Katmandou"
          >
            <div class="relative flex items-center justify-center">
              <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-amber-600 border-2 border-white text-white font-black text-xs flex items-center justify-center shadow-lg transition-transform group-hover/pin:scale-125">
                🕉️
              </div>
              <!-- Floating Tooltip on Hover -->
              <div class="absolute bottom-full mb-2 left-1/2 -translate-x-1/2 opacity-0 group-hover/pin:opacity-100 transition-all duration-200 pointer-events-none z-30 whitespace-nowrap">
                <div class="bg-slate-950/95 backdrop-blur-md text-white px-3.5 py-1.5 rounded-xl text-xs font-bold shadow-xl border border-white/10 flex items-center gap-1.5">
                  <span class="text-amber-400 font-extrabold">Katmandou :</span>
                  <span>Cités royales & temples séculaires</span>
                  <span class="text-emerald-400">→</span>
                </div>
              </div>
            </div>
          </a>

        </div>

      </div>

      <!-- Refined Interactive Territory Pills & Stats -->
      <div class="mt-10 sm:mt-12 max-w-4xl mx-auto flex flex-wrap items-center justify-center gap-3">
        <a 
          href="/destinations/bardia.html" 
          class="px-4 py-2 rounded-full bg-white/80 hover:bg-white text-slate-800 hover:text-[#0e8354] font-bold text-xs border border-amber-950/10 shadow-sm hover:shadow transition-all flex items-center gap-2 hover:scale-105"
        >
          <span>🐅</span>
          <span>Bardia (Tigres & Safaris à pied)</span>
        </a>
        <a 
          href="/destinations/chitwan.html" 
          class="px-4 py-2 rounded-full bg-white/80 hover:bg-white text-slate-800 hover:text-[#0e8354] font-bold text-xs border border-amber-950/10 shadow-sm hover:shadow transition-all flex items-center gap-2 hover:scale-105"
        >
          <span>🦏</span>
          <span>Chitwan (Rhinocéros & Pirogues)</span>
        </a>
        <a 
          href="/destinations/annapurna.html" 
          class="px-4 py-2 rounded-full bg-white/80 hover:bg-white text-slate-800 hover:text-[#0e8354] font-bold text-xs border border-amber-950/10 shadow-sm hover:shadow transition-all flex items-center gap-2 hover:scale-105"
        >
          <span>🏔️</span>
          <span>Annapurnas & Pokhara</span>
        </a>
        <a 
          href="/destinations/katmandou.html" 
          class="px-4 py-2 rounded-full bg-white/80 hover:bg-white text-slate-800 hover:text-[#0e8354] font-bold text-xs border border-amber-950/10 shadow-sm hover:shadow transition-all flex items-center gap-2 hover:scale-105"
        >
          <span>🕉️</span>
          <span>Katmandou & Cités Royales</span>
        </a>
      </div>

      <!-- Action Buttons -->
      <div class="mt-10 text-center flex flex-col sm:flex-row items-center justify-center gap-4">
        <a 
          href="#prochains-departs"
          class="inline-flex items-center gap-2.5 px-8 py-4 rounded-full bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-sm shadow-xl shadow-[#0e8354]/25 hover:scale-105 active:scale-95 transition-all"
        >
          <span>🐾</span>
          <span>Choisir mon circuit faune</span>
        </a>
        <a 
          href="/destinations.html"
          class="inline-flex items-center gap-2 px-6 py-4 rounded-full bg-white/80 hover:bg-white text-slate-700 hover:text-slate-950 font-bold text-xs sm:text-sm border border-slate-300/80 shadow-sm hover:shadow transition-all"
        >
          <span>Explorer les 5 guides de sanctuaires →</span>
        </a>
      </div>

    </div>
  </section>"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the previous map section with the luxury seamless edition
content = re.sub(
    r'\s*<!-- ========================================================================= -->\s*<!-- 7\.5 CARTE GÉOGRAPHIQUE.*?<!-- ========================================================================= -->\s*<!-- 8\. PISTEURS',
    '\n\n' + new_map_section + '\n\n  <!-- ========================================================================= -->\n  <!-- 8. PISTEURS',
    content,
    flags=re.DOTALL
)

# Also check if it had a different comment header:
if "<!-- 7.5 CARTE GÉOGRAPHIQUE" not in content:
    content = re.sub(
        r'\s*<section class="py-16 sm:py-24 bg-\[#faf8f5\].*?<!-- ========================================================================= -->\s*<!-- 8\. PISTEURS',
        '\n\n' + new_map_section + '\n\n  <!-- ========================================================================= -->\n  <!-- 8. PISTEURS',
        content,
        flags=re.DOTALL
    )

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("Luxury seamless map section injected successfully!")
