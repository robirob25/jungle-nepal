import re

card_fr = """        <!-- CARD 15 : PANTHÈRE DES NEIGES -->
        <article class="trip-card group bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-[0_4px_20px_rgba(0,0,0,0.06)] hover:shadow-[0_20px_40px_rgba(10,50,30,0.18)] hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between" data-category="mustang-himalaya culture grand-tour safari" data-title="expédition : panthère des neiges exclusive (17 jours)">
          <div>
            <div class="relative h-64 overflow-hidden">
              <img src="/assets/snow-leopard/snow_leopard_portrait.jpg" alt="Panthère des Neiges en liberté" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 filter brightness-95" loading="lazy" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
              
              <div class="absolute top-4 left-4 flex flex-wrap gap-2">
                <span class="px-3 py-1 rounded-full bg-slate-900/90 backdrop-blur-md text-amber-300 font-extrabold text-xs border border-amber-300/30">
                  🏔️ Himalaya & Faune Mythique
                </span>
              </div>

              <div class="absolute bottom-4 left-4 right-4 flex items-center justify-between text-white">
                <div class="flex items-center gap-1.5 text-xs font-bold bg-black/50 backdrop-blur-md px-3 py-1 rounded-full border border-white/20">
                  <svg class="w-3.5 h-3.5 text-amber-400 fill-amber-400" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                  <span>5.0 (10 avis)</span>
                </div>
                <div class="flex items-center gap-1.5 text-xs font-bold bg-black/50 backdrop-blur-md px-3 py-1 rounded-full border border-white/20">
                  <span>⏱️ 17 Jours</span>
                </div>
              </div>
            </div>

            <div class="p-6 space-y-4">
              <h3 class="font-black text-xl text-slate-900 group-hover:text-[#0e8354] transition-colors line-clamp-2">
                Expédition : Panthère des Neiges Exclusive (17 jours)
              </h3>
              <p class="text-xs text-slate-600 leading-relaxed line-clamp-3 font-normal">
                Neuf jours complets de suivi et de pistage intensif du Léopard des Neiges dans la haute vallée de Manang, avec acclimatation sécurisée et découverte de Braka Gompa.
              </p>

              <div class="pt-2 flex flex-wrap gap-1.5">
                <span class="text-[11px] font-bold px-2.5 py-0.5 rounded-md bg-emerald-50 text-emerald-800 border border-emerald-200">🐾 9j Pistage Pur</span>
                <span class="text-[11px] font-bold px-2.5 py-0.5 rounded-md bg-amber-50 text-amber-800 border border-amber-200">🏔️ Manang 3600m</span>
                <span class="text-[11px] font-bold px-2.5 py-0.5 rounded-md bg-slate-100 text-slate-700">👥 Max 8 pers</span>
              </div>
            </div>
          </div>

          <div class="p-6 pt-0 border-t border-slate-100 mt-4 flex items-center justify-between">
            <div>
              <span class="text-[11px] text-slate-500 font-bold block">À partir de</span>
              <span class="text-2xl font-black text-slate-950">4 300 €</span>
            </div>
            <a href="/tours/panthere-des-neiges.html" class="inline-flex items-center gap-1.5 px-5 py-2.5 rounded-full bg-[#0e8354] hover:bg-[#0c6d46] text-white text-xs font-black shadow-md hover:shadow-lg transition-all hover:scale-105">
              <span>Voir le séjour</span>
              <span>→</span>
            </a>
          </div>
        </article>
"""

card_en = card_fr.replace('Expédition : Panthère des Neiges Exclusive (17 jours)', 'Exclusive Snow Leopard Expedition (17 Days)')
card_en = card_en.replace('Panthère des Neiges en liberté', 'Wild Snow Leopard in Himalayas')
card_en = card_en.replace('🏔️ Himalaya & Faune Mythique', '🏔️ Himalayas & Mythic Wildlife')
card_en = card_en.replace('5.0 (10 avis)', '5.0 (10 reviews)')
card_en = card_en.replace('⏱️ 17 Jours', '⏱️ 17 Days')
card_en = card_en.replace("Neuf jours complets de suivi et de pistage intensif du Léopard des Neiges dans la haute vallée de Manang, avec acclimatation sécurisée et découverte de Braka Gompa.", "Nine full days of intensive tracking of the Snow Leopard in the high Manang valley, with safe acclimatization and Braka Gompa.")
card_en = card_en.replace('🐾 9j Pistage Pur', '🐾 9d Pure Tracking')
card_en = card_en.replace('À partir de', 'Starting from')
card_en = card_en.replace('Voir le séjour', 'View expedition')
card_en = card_en.replace('/tours/panthere-des-neiges.html', '/en/tours/panthere-des-neiges.html')

# 1. Update French index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    fr = f.read()

# Update counts
fr = fr.replace('<span>Tous les 14 séjours</span>', '<span>Tous les 15 séjours</span>')
fr = fr.replace('Tous les 14 séjours', 'Tous les 15 séjours')
fr = fr.replace('Tous les séjours (14)', 'Tous les séjours (15)')
fr = fr.replace('<span class="bg-white/20 text-white text-[11px] px-2 py-0.5 rounded-full font-black">14</span>', '<span class="bg-white/20 text-white text-[11px] px-2 py-0.5 rounded-full font-black">15</span>')
fr = fr.replace('<span>Himalaya, Mustang & Spiritualité (5)</span>', '<span>Himalaya, Mustang & Spiritualité (6)</span>')
fr = fr.replace('<span>Grands Tours 360° (9)</span>', '<span>Grands Tours 360° (10)</span>')

# Add card before closing </section> of prochains-departs or grid
if 'panthere-des-neiges' not in fr:
    fr = fr.replace(
        '<!-- CARD 14 : IMMERSION SPIRITUELLE -->',
        card_fr + '\n        <!-- CARD 14 : IMMERSION SPIRITUELLE -->'
    )

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(fr)

# 2. Update English index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro', 'r', encoding='utf-8') as f:
    en = f.read()

en = en.replace('<span>All 14 Expeditions</span>', '<span>All 15 Expeditions</span>')
en = en.replace('All 14 Expeditions', 'All 15 Expeditions')
en = en.replace('All Expeditions (14)', 'All Expeditions (15)')
en = en.replace('<span class="bg-white/20 text-white text-[11px] px-2 py-0.5 rounded-full font-black">14</span>', '<span class="bg-white/20 text-white text-[11px] px-2 py-0.5 rounded-full font-black">15</span>')
en = en.replace('<span>Himalayas, Mustang & Spirituality (5)</span>', '<span>Himalayas, Mustang & Spirituality (6)</span>')
en = en.replace('<span>Grand 360° Expeditions (9)</span>', '<span>Grand 360° Expeditions (10)</span>')

if 'panthere-des-neiges' not in en:
    en = en.replace(
        '<!-- CARD 14 : IMMERSION SPIRITUELLE -->',
        card_en + '\n        <!-- CARD 14 : IMMERSION SPIRITUELLE -->'
    )

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro', 'w', encoding='utf-8') as f:
    f.write(en)

print("Added Snow Leopard card and updated counts on FR & EN homepages!")
