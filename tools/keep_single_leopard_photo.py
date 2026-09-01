import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the 2 redundant leopard photos in gallery with high-value varied wildlife:
# 1. Replace Photo 52 (leopard_indien_camouflage.webp) with a majestic Fishing Cat or Jungle Cat or Sloth Bear (Ours lippu de Bardia)
ours_lippu = """        <!-- Photo 52: Ours lippu en recherche de termites -->
        <div class="wildlife-card break-inside-avoid mb-6 relative rounded-3xl overflow-hidden group cursor-pointer border border-white/10 shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:border-emerald-800/50 hover:shadow-[0_20px_50px_rgba(14,131,84,0.25)] transition-all duration-300 bg-slate-900" data-category="mammiferes" data-idx="51" onclick="openWildlifeLightbox(51)">
          
          <img 
            src="/assets/curated_gallery/ours_lippu_termitiere.webp" 
            alt="Ours lippu en recherche de termites - Parc national de Bardia" 
            width="1600"
            height="1067"
            style="aspect-ratio: 1600/1067;"
            class="w-full h-auto block filter brightness-95 group-hover:brightness-105 transition-all duration-300" loading="eager"
            decoding="async"
          />
          
          <!-- Top Location Badge -->
          <div class="absolute top-3.5 left-3.5 z-10 pointer-events-none">
            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md border border-white/20 text-[11px] font-black text-amber-100 shadow-md">
              <span>Parc national de Bardia</span>
            </span>
          </div>

          <!-- Bottom Floating Glass Caption -->
          <div class="absolute bottom-3.5 left-3.5 right-3.5 z-10 p-3.5 rounded-2xl bg-slate-950/90 backdrop-blur-xl border border-white/15 text-white opacity-0 translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-300 shadow-2xl pointer-events-none">
            <div class="flex items-center justify-between gap-3">
              <div class="min-w-0 flex-1">
                <h3 class="font-black text-sm sm:text-base text-white group-hover:text-amber-100 transition-colors leading-tight truncate">
                  Ours lippu (Sloth Bear)
                </h3>
                <p class="text-xs text-slate-300 mt-0.5 font-medium truncate">
                  Grand mammifère nocturne fouillant les termitières en forêt
                </p>
              </div>
              <div class="w-8 h-8 rounded-xl bg-white/10 text-slate-200 flex items-center justify-center shrink-0 border border-white/10">
                <svg class="w-4 h-4 text-slate-200" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"></path></svg>
              </div>
            </div>
          </div>

        </div>"""

# 2. Replace Photo 53 (leopard_sur_branche_maitresse.webp) with a Chaus (Chat de jungle / Jungle Cat)
chat_jungle = """        <!-- Photo 53: Chat de jungle (Jungle Cat) -->
        <div class="wildlife-card break-inside-avoid mb-6 relative rounded-3xl overflow-hidden group cursor-pointer border border-white/10 shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:border-emerald-800/50 hover:shadow-[0_20px_50px_rgba(14,131,84,0.25)] transition-all duration-300 bg-slate-900" data-category="felins" data-idx="52" onclick="openWildlifeLightbox(52)">
          
          <img 
            src="/assets/curated_gallery/chat_jungle_felin_sauvage.webp" 
            alt="Chat de jungle (Jungle Cat) - Parc national de Bardia" 
            width="900"
            height="1600"
            style="aspect-ratio: 900/1600;"
            class="w-full h-auto block filter brightness-95 group-hover:brightness-105 transition-all duration-300" loading="eager"
            decoding="async"
          />
          
          <!-- Top Location Badge -->
          <div class="absolute top-3.5 left-3.5 z-10 pointer-events-none">
            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md border border-white/20 text-[11px] font-black text-amber-100 shadow-md">
              <span>Parc national de Bardia</span>
            </span>
          </div>

          <!-- Bottom Floating Glass Caption -->
          <div class="absolute bottom-3.5 left-3.5 right-3.5 z-10 p-3.5 rounded-2xl bg-slate-950/90 backdrop-blur-xl border border-white/15 text-white opacity-0 translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-300 shadow-2xl pointer-events-none">
            <div class="flex items-center justify-between gap-3">
              <div class="min-w-0 flex-1">
                <h3 class="font-black text-sm sm:text-base text-white group-hover:text-amber-100 transition-colors leading-tight truncate">
                  Chat des marais (Jungle Cat)
                </h3>
                <p class="text-xs text-slate-300 mt-0.5 font-medium truncate">
                  Petit félin sauvage agile traquant dans les hautes herbes
                </p>
              </div>
              <div class="w-8 h-8 rounded-xl bg-white/10 text-slate-200 flex items-center justify-center shrink-0 border border-white/10">
                <svg class="w-4 h-4 text-slate-200" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"></path></svg>
              </div>
            </div>
          </div>

        </div>"""

# Replace in index.astro
# Search photo 52 chunk
photo52_pattern = r'<!-- Photo 52: Léopard indien dans les branchages -->.*?</div>\s*</div>\s*</div>'
c = re.sub(photo52_pattern, ours_lippu, c, flags=re.DOTALL)

# Search photo 53 chunk
photo53_pattern = r'<!-- Photo 53: Léopard sur branche maîtresse -->.*?</div>\s*</div>\s*</div>'
c = re.sub(photo53_pattern, chat_jungle, c, flags=re.DOTALL)

# Update the JS wildlifeData array as well
c = c.replace(
    '{"file": "/assets/curated_gallery/leopard_indien_camouflage.webp", "title": "Léopard indien dans les branchages", "desc": "Prédateur solitaire parfaitement dissimulé dans la canopée", "location": "Parc national de Bardia", "category": "felins", "aspect": 0.666875}',
    '{"file": "/assets/curated_gallery/ours_lippu_termitiere.webp", "title": "Ours lippu (Sloth Bear)", "desc": "Grand mammifère nocturne fouillant les termitières en forêt", "location": "Parc national de Bardia", "category": "mammiferes", "aspect": 0.666875}'
)

c = c.replace(
    '{"file": "/assets/curated_gallery/leopard_sur_branche_maitresse.webp", "title": "Léopard sur branche maîtresse", "desc": "Observation haute et sereine au-dessus des pistes sauvages", "location": "Parc national de Bardia", "category": "felins", "aspect": 1.7777777777777777}',
    '{"file": "/assets/curated_gallery/chat_jungle_felin_sauvage.webp", "title": "Chat des marais (Jungle Cat)", "desc": "Petit félin sauvage agile traquant dans les hautes herbes", "location": "Parc national de Bardia", "category": "felins", "aspect": 1.7777777777777777}'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Deduplicated leopards: exactly 1 majestic leopard kept in gallery!")
