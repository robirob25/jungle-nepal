import re
import os

BASE_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'

# File 1: safari-chitwan-3-jours.astro (FR)
FILE_1 = f'{BASE_DIR}/src/pages/tours/safari-chitwan-3-jours.astro'
# File 2: chitwan-3-days-safari-post-trek.astro (EN)
FILE_2 = f'{BASE_DIR}/src/pages/en/tours/chitwan-3-days-safari-post-trek.astro'
# File 3: pokhara-chitwan-safari-transfert-katmandou.astro (FR)
FILE_3 = f'{BASE_DIR}/src/pages/tours/pokhara-chitwan-safari-transfert-katmandou.astro'
# File 4: pokhara-to-chitwan-safari-transfer-kathmandu.astro (EN)
FILE_4 = f'{BASE_DIR}/src/pages/en/tours/pokhara-to-chitwan-safari-transfer-kathmandu.astro'

ITIN_1 = """          <div class="space-y-3">
            
            <details open class="group bg-white rounded-2xl border border-slate-200/90 overflow-hidden shadow-sm transition-all">
              <summary class="flex items-center justify-between p-4 sm:p-5 cursor-pointer select-none hover:bg-slate-50 transition-colors">
                <div class="flex items-center gap-3.5">
                  <span class="w-8 h-8 rounded-xl bg-emerald-50 text-[#0e8354] font-black text-xs flex items-center justify-center shrink-0 border border-emerald-200">
                    J1
                  </span>
                  <h4 class="font-bold text-sm sm:text-base text-slate-900">
                    J1 – Transfert matinal vers Chitwan et visite du village Tharu l'après-midi
                  </h4>
                </div>
                <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 transition-transform group-open:rotate-180 shrink-0"></i>
              </summary>
              <div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">
                <div class="pt-4 pb-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">
                  <strong>Matin :</strong> Prise en charge matinale à votre hôtel à Pokhara ou à Katmandou. Trajet confortable en véhicule privé ou bus touristique le long des vallées fluviales vers la plaine tropicale du Terai.<br/>
                  <strong>Midi :</strong> Arrivée à Sauraha (Chitwan) vers 12h30. Accueil chaleureux par notre équipe locale avec rafraîchissement de bienvenue, installation dans votre éco-lodge au bord de l'eau et déjeuner savoureux aux saveurs népalaises.<br/>
                  <strong>Après-midi :</strong> Immersion guidée dans un village traditionnel Tharu pour découvrir l'architecture en terre crue et les traditions ancestrales. En fin d'après-midi, moment de détente face au coucher de soleil sur les berges de la rivière Rapti où les rhinocéros sauvages viennent fréquemment se baigner.<br/>
                  <strong>Soirée :</strong> Dîner au lodge et spectacle de danse traditionnelle des bâtons (Tharu Stick Dance). Première nuitée en éco-lodge (Nuit 1).
                </div>
              </div>
            </details>
        
            <details class="group bg-white rounded-2xl border border-slate-200/90 overflow-hidden shadow-sm transition-all">
              <summary class="flex items-center justify-between p-4 sm:p-5 cursor-pointer select-none hover:bg-slate-50 transition-colors">
                <div class="flex items-center gap-3.5">
                  <span class="w-8 h-8 rounded-xl bg-emerald-50 text-[#0e8354] font-black text-xs flex items-center justify-center shrink-0 border border-emerald-200">
                    J2
                  </span>
                  <h4 class="font-bold text-sm sm:text-base text-slate-900">
                    J2 – Journée complète de safari en jeep 4x4 dans le parc national de Chitwan
                  </h4>
                </div>
                <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 transition-transform group-open:rotate-180 shrink-0"></i>
              </summary>
              <div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">
                <div class="pt-4 pb-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">
                  <strong>Journée complète :</strong> Départ dès l'aube pour une grande journée d'exploration en jeep 4x4 privatisée au cœur de la zone centrale protégée du parc national de Chitwan.<br/>
                  <strong>Pistage animalier :</strong> Accompagnés de votre chauffeur tout-terrain, d'un guide naturaliste certifié et d'un maître pisteur, vous parcourez les forêts de sôles, les clairières marécageuses et les savanes pour observer les grands rhinocéros unicornes, cerfs axis, sangliers, singes et ours lippus, avec de réelles chances de croiser le discret tigre du Bengale. Safari 100% éthique et respectueux, sans aucune monte d'éléphant.<br/>
                  <strong>Midi :</strong> Déjeuner pique-nique chaud au cœur de la jungle, perché dans un mirador d'observation sécurisé au-dessus d'un point d'eau.<br/>
                  <strong>Soirée :</strong> Retour au lodge au crépuscule, débriefing des rencontres animalières, dîner convivial et deuxième nuitée en éco-lodge (Nuit 2).
                </div>
              </div>
            </details>
        
            <details class="group bg-white rounded-2xl border border-slate-200/90 overflow-hidden shadow-sm transition-all">
              <summary class="flex items-center justify-between p-4 sm:p-5 cursor-pointer select-none hover:bg-slate-50 transition-colors">
                <div class="flex items-center gap-3.5">
                  <span class="w-8 h-8 rounded-xl bg-emerald-50 text-[#0e8354] font-black text-xs flex items-center justify-center shrink-0 border border-emerald-200">
                    J3
                  </span>
                  <h4 class="font-bold text-sm sm:text-base text-slate-900">
                    J3 – Balade matinale en pirogue traditionnelle sur la Rapti et transfert vers Pokhara ou Katmandou
                  </h4>
                </div>
                <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 transition-transform group-open:rotate-180 shrink-0"></i>
              </summary>
              <div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">
                <div class="pt-4 pb-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">
                  <strong>Matin :</strong> Au lever du soleil, embarquement à bord d'une pirogue traditionnelle en bois creusée dans un tronc pour une glisse silencieuse et magique sur la rivière Rapti. Dans la brume matinale, approche rapprochée des crocodiles gavials du Gange, crocodiles des marais et d'une exceptionnelle variété d'oiseaux aquatiques (martins-pêcheurs, hérons, aigrettes).<br/>
                  <strong>Milieu de matinée :</strong> Petit-déjeuner complet face aux berges, derniers préparatifs et check-out du lodge.<br/>
                  <strong>Après-midi :</strong> Transfert retour vers Pokhara ou vers Katmandou (dépose à votre hôtel ou directement au terminal de l'aéroport international pour votre vol). Fin de votre escapade de 3 jours et 2 nuits en pleine jungle népalaise.
                </div>
              </div>
            </details>
        
          </div>"""

ITIN_2 = """          <div class="space-y-3">
            
            <details open class="group bg-white rounded-2xl border border-slate-200/90 overflow-hidden shadow-sm transition-all">
              <summary class="flex items-center justify-between p-4 sm:p-5 cursor-pointer select-none hover:bg-slate-50 transition-colors">
                <div class="flex items-center gap-3.5">
                  <span class="w-8 h-8 rounded-xl bg-emerald-50 text-[#0e8354] font-black text-xs flex items-center justify-center shrink-0 border border-emerald-200">
                    D1
                  </span>
                  <h4 class="font-bold text-sm sm:text-base text-slate-900">
                    D1 – Morning Transfer to Chitwan & Afternoon Tharu Village Cultural Walk
                  </h4>
                </div>
                <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 transition-transform group-open:rotate-180 shrink-0"></i>
              </summary>
              <div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">
                <div class="pt-4 pb-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">
                  <strong>Morning:</strong> Early morning departure from your hotel in Pokhara or Kathmandu. Enjoy a comfortable drive through river valleys down to the subtropical lowlands of the Terai.<br/>
                  <strong>Midday:</strong> Arrive in Sauraha (Chitwan) around 12:30 PM. Warm welcome from our local team, welcome drinks, and check-in to your riverside eco-lodge followed by a freshly prepared Nepalese lunch.<br/>
                  <strong>Afternoon:</strong> Guided cultural walk through an authentic indigenous Tharu village to observe traditional mud architecture and farming traditions. Later, relax by the Rapti River banks at sunset, watching for Greater One-Horned Rhinos coming to bathe.<br/>
                  <strong>Evening:</strong> Dinner at the lodge and authentic Tharu stick dance performance. Night 1 at your riverside eco-lodge.
                </div>
              </div>
            </details>
        
            <details class="group bg-white rounded-2xl border border-slate-200/90 overflow-hidden shadow-sm transition-all">
              <summary class="flex items-center justify-between p-4 sm:p-5 cursor-pointer select-none hover:bg-slate-50 transition-colors">
                <div class="flex items-center gap-3.5">
                  <span class="w-8 h-8 rounded-xl bg-emerald-50 text-[#0e8354] font-black text-xs flex items-center justify-center shrink-0 border border-emerald-200">
                    D2
                  </span>
                  <h4 class="font-bold text-sm sm:text-base text-slate-900">
                    D2 – Full-Day 4x4 Jeep Safari in Chitwan National Park Core Zone
                  </h4>
                </div>
                <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 transition-transform group-open:rotate-180 shrink-0"></i>
              </summary>
              <div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">
                <div class="pt-4 pb-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">
                  <strong>Full-Day Core Safari:</strong> Dawn departure into the deep core zone of Chitwan National Park aboard a private open 4x4 safari jeep.<br/>
                  <strong>Wildlife Tracking:</strong> Accompanied by your experienced driver, certified naturalist guide, and veteran tracker, explore sal forests, marshlands, and elephant grass savannas. Track Greater One-Horned Rhinos, spotted deer, wild boars, sloth bears, and with patience, the Royal Bengal Tiger. 100% ethical and cruelty-free—strictly no elephant riding.<br/>
                  <strong>Midday:</strong> Warm picnic bush lunch in the heart of the jungle, perched in a protected observation watchtower overlooking a prime watering hole.<br/>
                  <strong>Evening:</strong> Return to your eco-lodge at dusk, evening wildlife debrief, dinner, and restful second night at the lodge (Night 2).
                </div>
              </div>
            </details>
        
            <details class="group bg-white rounded-2xl border border-slate-200/90 overflow-hidden shadow-sm transition-all">
              <summary class="flex items-center justify-between p-4 sm:p-5 cursor-pointer select-none hover:bg-slate-50 transition-colors">
                <div class="flex items-center gap-3.5">
                  <span class="w-8 h-8 rounded-xl bg-emerald-50 text-[#0e8354] font-black text-xs flex items-center justify-center shrink-0 border border-emerald-200">
                    D3
                  </span>
                  <h4 class="font-bold text-sm sm:text-base text-slate-900">
                    D3 – Sunrise Traditional Dugout Canoe Drift on the Rapti River & Afternoon Transfer
                  </h4>
                </div>
                <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 transition-transform group-open:rotate-180 shrink-0"></i>
              </summary>
              <div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">
                <div class="pt-4 pb-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">
                  <strong>Morning:</strong> At sunrise, board a traditional wooden dugout canoe carved from a single tree trunk for a silent, serene float down the calm Rapti River. Enjoy close views of fish-eating Gharial crocodiles, marsh muggers, and vibrant river birds (kingfishers, storks, egrets).<br/>
                  <strong>Late Morning:</strong> Generous breakfast overlooking the river, final packing, and check-out from the lodge.<br/>
                  <strong>Afternoon:</strong> Transfer onward to Pokhara or Kathmandu (drop-off directly at your hotel or Tribhuvan International Airport for your flight). Conclude your seamless 3-day / 2-night jungle recovery experience.
                </div>
              </div>
            </details>
        
          </div>"""

ITIN_3 = """          <div class="space-y-3">
            
            <details open class="group bg-white rounded-2xl border border-slate-200/90 overflow-hidden shadow-sm transition-all">
              <summary class="flex items-center justify-between p-4 sm:p-5 cursor-pointer select-none hover:bg-slate-50 transition-colors">
                <div class="flex items-center gap-3.5">
                  <span class="w-8 h-8 rounded-xl bg-emerald-50 text-[#0e8354] font-black text-xs flex items-center justify-center shrink-0 border border-emerald-200">
                    J1
                  </span>
                  <h4 class="font-bold text-sm sm:text-base text-slate-900">
                    J1 – Prise en charge à Pokhara le matin, route vers Chitwan et village Tharu
                  </h4>
                </div>
                <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 transition-transform group-open:rotate-180 shrink-0"></i>
              </summary>
              <div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">
                <div class="pt-4 pb-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">
                  <strong>Matin (7h30) :</strong> Votre chauffeur privé vient vous chercher directement à la réception de votre hôtel à Pokhara (Lakeside). Descente panoramique le long des vallées fluviales jusqu'aux plaines subtropicales de Chitwan.<br/>
                  <strong>Midi :</strong> Arrivée à Sauraha vers 12h30. Accueil chaleureux par notre équipe locale, installation dans votre éco-lodge au bord de l'eau et déjeuner réconfortant après vos journées de marche en montagne.<br/>
                  <strong>Après-midi :</strong> Découverte guidée à pied d'un village traditionnel Tharu, suivie d'un moment de détente face au coucher de soleil sur les berges de la rivière Rapti (zone où les rhinocéros aiment venir se baigner au crépuscule).<br/>
                  <strong>Soirée :</strong> Dîner au lodge et spectacle de danse traditionnelle des bâtons de la communauté Tharu. Première nuitée en éco-lodge (Nuit 1).
                </div>
              </div>
            </details>
        
            <details class="group bg-white rounded-2xl border border-slate-200/90 overflow-hidden shadow-sm transition-all">
              <summary class="flex items-center justify-between p-4 sm:p-5 cursor-pointer select-none hover:bg-slate-50 transition-colors">
                <div class="flex items-center gap-3.5">
                  <span class="w-8 h-8 rounded-xl bg-emerald-50 text-[#0e8354] font-black text-xs flex items-center justify-center shrink-0 border border-emerald-200">
                    J2
                  </span>
                  <h4 class="font-bold text-sm sm:text-base text-slate-900">
                    J2 – Journée complète de safari en jeep 4x4 dans le parc national de Chitwan
                  </h4>
                </div>
                <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 transition-transform group-open:rotate-180 shrink-0"></i>
              </summary>
              <div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">
                <div class="pt-4 pb-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">
                  <strong>Journée complète :</strong> Départ matinal en jeep 4x4 ouverte et privatisée pour explorer la zone centrale sauvage du parc national de Chitwan.<br/>
                  <strong>Pistage animalier :</strong> Accompagnés de votre chauffeur, guide naturaliste et pisteur expérimenté, pénétrez les forêts de sôles et marécages. Observation rapprochée des rhinocéros unicornes, cerfs, sangliers, singes et ours lippus, avec de belles chances d'apercevoir le tigre du Bengale. Safari 100% éthique, sans monte d'éléphant.<br/>
                  <strong>Midi :</strong> Déjeuner pique-nique chaud au cœur de la jungle, perché dans un mirador d'observation sécurisé.<br/>
                  <strong>Soirée :</strong> Dîner au lodge sous les étoiles du Terai et deuxième nuitée paisible en éco-lodge (Nuit 2).
                </div>
              </div>
            </details>
        
            <details class="group bg-white rounded-2xl border border-slate-200/90 overflow-hidden shadow-sm transition-all">
              <summary class="flex items-center justify-between p-4 sm:p-5 cursor-pointer select-none hover:bg-slate-50 transition-colors">
                <div class="flex items-center gap-3.5">
                  <span class="w-8 h-8 rounded-xl bg-emerald-50 text-[#0e8354] font-black text-xs flex items-center justify-center shrink-0 border border-emerald-200">
                    J3
                  </span>
                  <h4 class="font-bold text-sm sm:text-base text-slate-900">
                    J3 – Balade matinale en pirogue traditionnelle sur la Rapti et transfert vers Katmandou
                  </h4>
                </div>
                <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 transition-transform group-open:rotate-180 shrink-0"></i>
              </summary>
              <div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">
                <div class="pt-4 pb-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">
                  <strong>Aube :</strong> Descente silencieuse en pirogue traditionnelle taillée dans un tronc d'arbre sur les eaux calmes de la Rapti. Rencontre magique au ras de l'eau avec les crocodiles gavials du Gange et une grande variété d'oiseaux aquatiques.<br/>
                  <strong>Matinée :</strong> Copieux petit-déjeuner face à la rivière, derniers préparatifs et check-out du lodge.<br/>
                  <strong>Après-midi :</strong> Départ à bord de votre véhicule tout confort vers Katmandou. Prise en charge intégrale de vos bagages.<br/>
                  <strong>Arrivée :</strong> Dépose directe en fin d'après-midi à votre hôtel à Katmandou (Thamel) ou directement au terminal de l'aéroport international Tribhuvan. Fin du combiné sans aucun stress logistique.
                </div>
              </div>
            </details>
        
          </div>"""

ITIN_4 = """          <div class="space-y-3">
            
            <details open class="group bg-white rounded-2xl border border-slate-200/90 overflow-hidden shadow-sm transition-all">
              <summary class="flex items-center justify-between p-4 sm:p-5 cursor-pointer select-none hover:bg-slate-50 transition-colors">
                <div class="flex items-center gap-3.5">
                  <span class="w-8 h-8 rounded-xl bg-emerald-50 text-[#0e8354] font-black text-xs flex items-center justify-center shrink-0 border border-emerald-200">
                    D1
                  </span>
                  <h4 class="font-bold text-sm sm:text-base text-slate-900">
                    D1 – Morning Pickup in Pokhara, Transfer to Chitwan & Tharu Village Walk
                  </h4>
                </div>
                <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 transition-transform group-open:rotate-180 shrink-0"></i>
              </summary>
              <div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">
                <div class="pt-4 pb-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">
                  <strong>Morning (7:30 AM):</strong> Private driver pickup directly from your hotel lobby in Pokhara (Lakeside). Relaxing scenic road journey along mountain river valleys down to Chitwan's subtropical plains.<br/>
                  <strong>Midday:</strong> Arrive in Sauraha around 12:30 PM. Warm welcome by our local team, check-in at your riverside eco-lodge, and hearty lunch to recharge after mountain trekking.<br/>
                  <strong>Afternoon:</strong> Guided stroll through an authentic indigenous Tharu village, followed by a sunset relaxation session along the Rapti River banks where wild rhinos often come out to bathe.<br/>
                  <strong>Evening:</strong> Fresh dinner at the lodge and traditional Tharu stick dance performance. Night 1 at your riverside eco-lodge.
                </div>
              </div>
            </details>
        
            <details class="group bg-white rounded-2xl border border-slate-200/90 overflow-hidden shadow-sm transition-all">
              <summary class="flex items-center justify-between p-4 sm:p-5 cursor-pointer select-none hover:bg-slate-50 transition-colors">
                <div class="flex items-center gap-3.5">
                  <span class="w-8 h-8 rounded-xl bg-emerald-50 text-[#0e8354] font-black text-xs flex items-center justify-center shrink-0 border border-emerald-200">
                    D2
                  </span>
                  <h4 class="font-bold text-sm sm:text-base text-slate-900">
                    D2 – Full-Day 4x4 Jeep Safari in Chitwan National Park Core Zone
                  </h4>
                </div>
                <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 transition-transform group-open:rotate-180 shrink-0"></i>
              </summary>
              <div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">
                <div class="pt-4 pb-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">
                  <strong>Full-Day Core Safari:</strong> Early morning departure in your private open 4x4 safari jeep into the protected core jungle of Chitwan National Park.<br/>
                  <strong>Wildlife Tracking:</strong> With your driver, certified naturalist guide, and expert tracker, navigate deep sal forests and riverine wetlands. Close encounters with Greater One-Horned Rhinoceroses, deer, sloth bears, and birdlife, with genuine chances of spotting the Bengal tiger. 100% cruelty-free ethical safari without elephant riding.<br/>
                  <strong>Midday:</strong> Hot picnic lunch inside the jungle perched atop an elevated observation machan (watchtower).<br/>
                  <strong>Evening:</strong> Return to the lodge at sunset, dinner, and peaceful second night at the eco-lodge (Night 2).
                </div>
              </div>
            </details>
        
            <details class="group bg-white rounded-2xl border border-slate-200/90 overflow-hidden shadow-sm transition-all">
              <summary class="flex items-center justify-between p-4 sm:p-5 cursor-pointer select-none hover:bg-slate-50 transition-colors">
                <div class="flex items-center gap-3.5">
                  <span class="w-8 h-8 rounded-xl bg-emerald-50 text-[#0e8354] font-black text-xs flex items-center justify-center shrink-0 border border-emerald-200">
                    D3
                  </span>
                  <h4 class="font-bold text-sm sm:text-base text-slate-900">
                    D3 – Sunrise Traditional Dugout Canoe Drift & Seamless Kathmandu Transfer
                  </h4>
                </div>
                <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 transition-transform group-open:rotate-180 shrink-0"></i>
              </summary>
              <div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">
                <div class="pt-4 pb-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">
                  <strong>Sunrise:</strong> Silent drift down the Rapti River in a traditional handcrafted wooden dugout canoe. Spot endangered fish-eating Gharial crocodiles, marsh muggers, and vibrant river birds in the morning mist.<br/>
                  <strong>Mid-Morning:</strong> Full riverside breakfast at the lodge, pack your bags and check out.<br/>
                  <strong>Afternoon:</strong> Comfortable road transfer onward to Kathmandu with full luggage handling.<br/>
                  <strong>Arrival:</strong> Direct late-afternoon drop-off at your hotel in Kathmandu (Thamel) or at Tribhuvan International Airport terminal for your homeward flight. Zero logistics stress.
                </div>
              </div>
            </details>
        
          </div>"""

# Mosaic replacement with the traditional canoe photo
MOSAIC_OLD = """      <div class="hidden md:block md:col-span-1 h-full overflow-hidden">
        <img loading="lazy" decoding="async" src="/assets/drive_photos/adrien_tigre3.webp" alt="Expédition Népal Sauvage" class="w-full h-full object-cover transition-opacity duration-300 cursor-pointer" onclick="openLightbox(1)"/>
      </div>"""

MOSAIC_NEW = """      <div class="hidden md:block md:col-span-1 h-full overflow-hidden">
        <img loading="lazy" decoding="async" src="/assets/tours_thumbs/safari_pirogue_traditionnelle_chitwan.webp" alt="Pirogue traditionnelle sur la rivière Rapti à Chitwan" class="w-full h-full object-cover transition-opacity duration-300 cursor-pointer" onclick="openLightbox(1)"/>
      </div>"""

MOSAIC_NEW_EN = """      <div class="hidden md:block md:col-span-1 h-full overflow-hidden">
        <img loading="lazy" decoding="async" src="/assets/tours_thumbs/safari_pirogue_traditionnelle_chitwan.webp" alt="Traditional dugout canoe safari on the Rapti river in Chitwan" class="w-full h-full object-cover transition-opacity duration-300 cursor-pointer" onclick="openLightbox(1)"/>
      </div>"""

def replace_itinerary(filepath, new_itin, mosaic_new):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace <div class="space-y-3">...</div> under #programme
    itin_pattern = re.compile(r'<div class="space-y-3">[\s\S]*?</div>\s*</section>', re.MULTILINE)
    match = itin_pattern.search(content)
    if match:
        content = content[:match.start()] + new_itin + "\n        </section>" + content[match.end():]
        print(f"Replaced itinerary in {filepath}")
    else:
        print(f"Could not find itinerary in {filepath}")

    # Replace mosaic image
    if MOSAIC_OLD in content:
        content = content.replace(MOSAIC_OLD, mosaic_new)
        print(f"Updated mosaic in {filepath}")
    elif "/assets/tours_thumbs/safari_pirogue_traditionnelle_chitwan.webp" not in content:
        # Check alternative image in slot 1
        slot1_pattern = re.compile(r'<div class="hidden md:block md:col-span-1 h-full overflow-hidden">\s*<img[^>]+onclick="openLightbox\(1\)"\s*/>\s*</div>')
        content = slot1_pattern.sub(mosaic_new, content)
        print(f"Updated slot 1 mosaic via regex in {filepath}")

    # Add pirogue to galleryImages array if not present
    if "/assets/tours_thumbs/safari_pirogue_traditionnelle_chitwan.webp" not in content:
        gallery_needle = 'window.galleryImages = [\n'
        if gallery_needle in content:
            content = content.replace(gallery_needle, gallery_needle + '      "/assets/tours_thumbs/safari_pirogue_traditionnelle_chitwan.webp",\n')
            print(f"Added pirogue to galleryImages in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

replace_itinerary(FILE_1, ITIN_1, MOSAIC_NEW)
replace_itinerary(FILE_2, ITIN_2, MOSAIC_NEW_EN)
replace_itinerary(FILE_3, ITIN_3, MOSAIC_NEW)
replace_itinerary(FILE_4, ITIN_4, MOSAIC_NEW_EN)

print("Finished updating all 4 tours!")
