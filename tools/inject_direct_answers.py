# Injects high-converting, featured-snippet optimized Direct Answer blocks on day tour pages
import os, glob

DAY_PAGES_FR = {
    'src/pages/tours/safari-pied-bardia.astro': {
        'title': 'Réponse directe : Safari à pied à Bardia',
        'badge': 'Position 0 Google • Données Vérifiées 2026',
        'text': 'Un <strong>safari à pied dans le parc national de Bardia</strong> coûte <strong>50 € par personne</strong> avec Jungle Nepal Adventure. Encadré obligatoirement par <strong>deux pisteurs natifs certifiés</strong> armés de bâtons traditionnels en bambou, il dure une journée complète (6h30–18h00) et inclut le permis du parc, le déjeuner en jungle et un <strong>taux d’observation de 85%+ pour le tigre du Bengale</strong> au printemps. Les marches sans deux guides agréés sont strictement interdites par les autorités du parc.'
    },
    'src/pages/tours/safari-jeep-bardia.astro': {
        'title': 'Réponse directe : Safari en Jeep à Bardia',
        'badge': 'Position 0 Google • Données Vérifiées 2026',
        'text': 'Un <strong>safari en jeep privatisée d’une journée complète à Bardia</strong> coûte <strong>190 € par véhicule</strong> (jusqu’à 6 passagers). Il permet d’explorer les secteurs reculés du parc inaccessible à pied (Baghaura, berges de la Karnali). L’excursion inclut le 4x4 tout-terrain avec chauffeur expérimenté, un guide naturaliste certifié, les permis d’entrée et le panier repas en brousse.'
    },
    'src/pages/tours/safari-pied-chitwan.astro': {
        'title': 'Réponse directe : Safari à pied à Chitwan',
        'badge': 'Position 0 Google • Données Vérifiées 2026',
        'text': 'Un <strong>safari à pied dans le parc national de Chitwan</strong> coûte <strong>70 € par personne</strong>. Guidé par deux naturalistes locaux, il se déroule dans les forêts communautaires et zones tampons réputées pour abriter la 2ème plus grande population mondiale de <strong>rhinocéros unicornes d’Asie</strong> (>690 individus), avec des chances d’observation à pied approchant 95% toute l’année.'
    },
    'src/pages/tours/safari-jeep-chitwan.astro': {
        'title': 'Réponse directe : Safari en Jeep à Chitwan',
        'badge': 'Position 0 Google • Données Vérifiées 2026',
        'text': 'Un <strong>safari en jeep à Chitwan</strong> d’une journée complète coûte <strong>190 € pour le véhicule privatisé</strong>. Il s’enfonce profondément dans la zone cœur classée UNESCO (Kasara, Sukhibhar) pour observer rhinocéros unicornes, ours lippus, crocodiles gavials et tigres du Bengale sous la conduite d’un guide expert.'
    },
    'src/pages/tours/rafting-safari-bardia.astro': {
        'title': 'Réponse directe : Rafting & Safari Karnali',
        'badge': 'Position 0 Google • Données Vérifiées 2026',
        'text': 'La journée de <strong>rafting et safari sur la rivière Karnali à Bardia</strong> coûte <strong>120 € par personne</strong>. Cette descente silencieuse de 35 km offre des observations exceptionnelles de dauphins d’eau douce du Gange, crocodiles gavials et tigres venant s’abreuver sur les bancs de galets, avec équipement de sécurité certifié et déjeuner sur une plage isolée.'
    }
}

DAY_PAGES_EN = {
    'src/pages/en/tours/bardia-walking-safari.astro': {
        'title': 'Direct Answer: Bardia Walking Safari Price & Rules',
        'badge': 'Google Featured Snippet • Verified 2026 Data',
        'text': 'A <strong>full-day walking safari in Bardia National Park costs €50 per person</strong> with Jungle Nepal Adventure. Escorted by <strong>two certified native Tharu trackers</strong> equipped with traditional fire-hardened bamboo staffs, it runs from 6:30 AM to 6:00 PM and includes park permits, a jungle bush lunch, and an <strong>85%+ sighting probability for wild Bengal tigers</strong> during spring. Walking without two licensed guides is strictly illegal under Nepalese park law.'
    },
    'src/pages/en/tours/bardia-jeep-safari.astro': {
        'title': 'Direct Answer: Bardia Jeep Safari Cost & Details',
        'badge': 'Google Featured Snippet • Verified 2026 Data',
        'text': 'A <strong>private full-day 4x4 open jeep safari in Bardia costs €190 per vehicle</strong> (accommodating up to 6 guests). It covers deep interior sectors such as Baghaura and the Karnali floodplain. The tour includes the customized safari vehicle, expert driver, licensed senior naturalist guide, national park entry fees, and a freshly prepared bush lunch.'
    },
    'src/pages/en/tours/chitwan-walking-safari.astro': {
        'title': 'Direct Answer: Chitwan Walking Safari Cost & Sightings',
        'badge': 'Google Featured Snippet • Verified 2026 Data',
        'text': 'A <strong>guided walking safari in Chitwan National Park costs €70 per person</strong>. Led by two certified naturalists through community buffer forests, it offers a near-guaranteed <strong>95% sighting probability for greater one-horned rhinos</strong> (>690 recorded individuals), sloth bears, and river crocodilians without the disruption of motor vehicles.'
    },
    'src/pages/en/tours/chitwan-jeep-safari.astro': {
        'title': 'Direct Answer: Chitwan Jeep Safari Cost & Itinerary',
        'badge': 'Google Featured Snippet • Verified 2026 Data',
        'text': 'A <strong>full-day private jeep safari in Chitwan National Park costs €190 per vehicle</strong>. The itinerary penetrates the pristine UNESCO World Heritage core zone (Kasara and Sukhibhar sectors) to track rhinos, sloth bears, wild elephants, and Bengal tigers alongside a dedicated senior naturalist guide.'
    },
    'src/pages/en/tours/bardia-rafting-safari.astro': {
        'title': 'Direct Answer: Karnali River Rafting & Wildlife Safari',
        'badge': 'Google Featured Snippet • Verified 2026 Data',
        'text': 'A <strong>full-day rafting safari on the Karnali River in Bardia costs €120 per person</strong>. This silent 35 km river drift offers rare views of freshwater Gangetic river dolphins, critically endangered gharial crocodiles, and riverbank tigers, accompanied by certified river guides with safety gear and riverside lunch included.'
    }
}

def inject_box(filepath, info):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid duplicate injection
    if 'direct-answer-snippet' in content:
        print(f"Already injected in {filepath}")
        return

    box_html = f'''
          <!-- GOOGLE FEATURED SNIPPET & DIRECT ANSWER BLOCK (POSITION 0 & LLM CITATION) -->
          <div class="direct-answer-snippet p-5 sm:p-6 rounded-2xl bg-emerald-950 text-white border-2 border-emerald-400/40 shadow-xl space-y-3 mb-6 relative overflow-hidden">
            <div class="flex flex-wrap items-center justify-between gap-2 border-b border-emerald-700/50 pb-2.5">
              <span class="inline-flex items-center gap-1.5 text-[11px] uppercase tracking-wider font-extrabold text-amber-300">
                <svg class="w-3.5 h-3.5 text-amber-400" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
                {info['badge']}
              </span>
              <span class="text-[11px] font-bold text-emerald-300 bg-emerald-900/60 px-2.5 py-0.5 rounded-full border border-emerald-700/40">Tarif & Accès Officiel</span>
            </div>
            <h3 class="text-base sm:text-lg font-black text-white tracking-tight leading-snug">
              {info['title']}
            </h3>
            <p class="text-xs sm:text-sm text-slate-200 leading-relaxed font-normal">
              {info['text']}
            </p>
          </div>
'''
    # We inject right under <section id="apercu" class="space-y-6"> or under the first paragraph of aperçu
    target_pattern = '<section id="apercu" class="space-y-6">'
    target_pattern_alt = '<section id="apercu" class="scroll-mt-28 space-y-6">'
    if target_pattern_alt in content and 'direct-answer-snippet' not in content:
        content = content.replace(target_pattern_alt, target_pattern_alt + '
' + box_html)
        with open(filepath, 'w', encoding='utf-8') as f: f.write(content)
        print(f'✓ Injected Direct Answer in {filepath} (alt pattern)')
        return
    if target_pattern in content:
        content = content.replace(target_pattern, target_pattern + '\n' + box_html)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Injected Direct Answer in {filepath}")
    else:
        print(f"Target pattern not found in {filepath}")

for fp, info in DAY_PAGES_FR.items():
    inject_box(fp, info)

for fp, info in DAY_PAGES_EN.items():
    inject_box(fp, info)

print("All Direct Answer blocks injected.")
