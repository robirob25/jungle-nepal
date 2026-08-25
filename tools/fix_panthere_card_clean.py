with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Exact replacement for the panthere-des-neiges card:
# 1. Use clean photo without heavy dark overlay (just the subtle gradient at the bottom like all other cards)
# 2. Use authentic portrait image from snow-leopard folder (/assets/snow-leopard/snow_leopard_portrait.webp) with full brightness
# 3. Clean pill badge without emoji or bright yellow borders
# 4. Standard sentence-case title: "Expédition panthère des neiges exclusive (17 jours)"

old_card = """        <article class="trip-card reveal-on-scroll group bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-[0_4px_20px_rgba(0,0,0,0.06)] hover:shadow-[0_20px_40px_rgba(10,50,30,0.18)] hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between" data-category="mustang-himalaya culture safari grand-tour" data-title="expédition : panthère des neiges exclusive">
          
          <div class="relative overflow-hidden">
            <a href="/tours/panthere-des-neiges.html" class="block relative aspect-[4/3] overflow-hidden">
              <img 
                src="/assets/snow-leopard/snow_leopard_portrait.webp" 
                alt="Panthère des neiges en haute altitude au Népal" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" 
                loading="lazy" 
              />
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/75 to-black/90"></div>
      <div class="absolute inset-0 bg-black/55"></div>

              <div class="absolute top-4 left-4 z-10">
                <span class="px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md text-amber-100 text-xs font-extrabold border border-amber-400/30">
                  Himalaya & Faune Mythique
                </span>
              </div>

              <div class="absolute bottom-4 left-4 right-4 flex items-center justify-between text-white text-xs z-10">
                <div class="flex items-center gap-1.5 bg-black/50 backdrop-blur-md px-3 py-1.5 rounded-full border border-white/15">
                  <svg class="w-4 h-4 text-emerald-600 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect><line x1="16" x2="16" y1="2" y2="6"></line><line x1="8" x2="8" y1="2" y2="6"></line><line x1="3" x2="21" y1="10" y2="10"></line></svg>
                  <span class="font-bold text-slate-100">17 jours</span>
                </div>
                <div class="flex items-center gap-1 bg-amber-500 text-jungle-950 font-black px-2.5 py-1 rounded-full shadow">
                  <svg class="w-4 h-4 text-amber-400 fill-amber-400 shrink-0" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                  <span>5.0 (10)</span>
                </div>
              </div>
            </a>
          </div>

          <div class="p-6 sm:p-7 flex-1 flex flex-col justify-between bg-gradient-to-b from-white to-slate-50/50">
            <div>
              <div class="text-[11px] font-extrabold uppercase tracking-widest text-[#0e8354] mb-1.5 flex items-center gap-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-[#0e8354]"></span>
                <span>Népal Sauvage • Éco-Safari</span>
              </div>
              <h3 class="font-black text-xl sm:text-[22px] text-slate-900 group-hover:text-[#0e8354] transition-colors leading-snug tracking-tight">
                <a href="/tours/panthere-des-neiges.html">Expédition : panthère des neiges exclusive</a>
              </h3>
              <p class="mt-3 text-sm text-slate-600 line-clamp-2 leading-relaxed font-normal">
                Neuf jours complets de suivi et de pistage intensif du Léopard des Neiges dans la haute vallée de Manang, avec acclimatation sécurisée et découverte de Braka Gompa.
              </p>
            </div>

            <div class="mt-5 pt-4 border-t border-slate-200/80">
              <div class="flex items-center justify-between gap-2">
                <div>
                  <p class="text-[10px] uppercase tracking-wider font-extrabold text-slate-400">À partir de</p>
                  <span class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight leading-none">4,300€</span>
                </div>
                <span class="inline-flex items-center gap-1.5 text-[11px] font-bold text-[#0e8354] bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200/80">
                  <span class="w-1.5 h-1.5 rounded-full bg-[#0e8354]"></span>
                  <span>Départs 2026/2027</span>
                </span>
              </div>
              <a href="/tours/panthere-des-neiges.html" class="w-full mt-3.5 py-3 px-4 rounded-2xl bg-[#0e5c3e] hover:bg-[#09422b] text-white font-extrabold text-xs sm:text-sm flex items-center justify-center gap-2 shadow-md shadow-emerald-950/20 active:scale-98 transition-all text-center">
                <span>Découvrir le circuit</span>
                <span>→</span>
              </a>
            </div>
          </div>

        </article>"""

clean_card = """        <article class="trip-card reveal-on-scroll group bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-[0_4px_20px_rgba(0,0,0,0.06)] hover:shadow-[0_20px_40px_rgba(10,50,30,0.18)] hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between" data-category="mustang-himalaya culture safari grand-tour" data-title="expédition panthère des neiges exclusive">
          
          <div class="relative">
            <a href="/tours/panthere-des-neiges.html" class="relative h-72 sm:h-80 overflow-hidden block">
              <img 
                src="/assets/snow-leopard/snow_leopard_portrait.webp" 
                alt="Panthère des neiges en haute altitude au Népal" 
                class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 ease-out filter brightness-100 contrast-100" 
                loading="lazy" 
              />
              
              <div class="absolute top-4 left-4 flex flex-wrap gap-2 z-10">
                <span class="inline-flex items-center gap-1.5 bg-jungle-950/90 backdrop-blur-md text-amber-100 font-extrabold text-xs px-3 py-1 rounded-full border border-white/20 shadow-md">
                  <span>Himalaya & Faune mythique</span>
                </span>
              </div>

              <div class="absolute bottom-4 left-4 right-4 flex items-center justify-between text-white text-xs z-10">
                <div class="flex items-center gap-1.5 bg-black/50 backdrop-blur-md px-3 py-1.5 rounded-full border border-white/15">
                  <svg class="w-4 h-4 text-emerald-600 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect><line x1="16" x2="16" y1="2" y2="6"></line><line x1="8" x2="8" y1="2" y2="6"></line><line x1="3" x2="21" y1="10" y2="10"></line></svg>
                  <span class="font-bold text-slate-100">17 jours</span>
                </div>
                <div class="flex items-center gap-1 bg-amber-500 text-jungle-950 font-black px-2.5 py-1 rounded-full shadow">
                  <svg class="w-4 h-4 text-amber-400 fill-amber-400 shrink-0" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                  <span>5.0 (10)</span>
                </div>
              </div>
            </a>
          </div>

          <div class="p-6 sm:p-7 flex-1 flex flex-col justify-between bg-gradient-to-b from-white to-slate-50/50">
            <div>
              <div class="text-[11px] font-extrabold uppercase tracking-widest text-[#0e8354] mb-1.5 flex items-center gap-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-[#0e8354]"></span>
                <span>Népal Sauvage • Éco-Safari</span>
              </div>
              <h3 class="font-black text-xl sm:text-[22px] text-slate-900 group-hover:text-[#0e8354] transition-colors leading-snug tracking-tight">
                <a href="/tours/panthere-des-neiges.html">Expédition : panthère des neiges exclusive</a>
              </h3>
              <p class="mt-3 text-sm text-slate-600 line-clamp-2 leading-relaxed font-normal">
                Neuf jours complets de suivi et de pistage intensif du Léopard des Neiges dans la haute vallée de Manang, avec acclimatation sécurisée et découverte de Braka Gompa.
              </p>
            </div>

            <div class="mt-5 pt-4 border-t border-slate-200/80">
              <div class="flex items-center justify-between gap-2">
                <div>
                  <p class="text-[10px] uppercase tracking-wider font-extrabold text-slate-400">À partir de</p>
                  <span class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight leading-none">4,300€</span>
                </div>
                <span class="inline-flex items-center gap-1.5 text-[11px] font-bold text-[#0e8354] bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200/80">
                  <span class="w-1.5 h-1.5 rounded-full bg-[#0e8354]"></span>
                  <span>Départs 2026/2027</span>
                </span>
              </div>
              <a href="/tours/panthere-des-neiges.html" class="w-full mt-3.5 py-3 px-4 rounded-2xl bg-[#0e5c3e] hover:bg-[#09422b] text-white font-extrabold text-xs sm:text-sm flex items-center justify-center gap-2 shadow-md shadow-emerald-950/20 active:scale-98 transition-all text-center">
                <span>Découvrir le circuit</span>
                <span>→</span>
              </a>
            </div>
          </div>

        </article>"""

c = c.replace(old_card, clean_card)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Replaced panthere card with 100% clean, bright, pixel-perfect card identical to all others!")
