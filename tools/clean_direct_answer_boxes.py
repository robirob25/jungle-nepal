import re
import os

files_map = {
    # French files
    'src/pages/tours/safari-jeep-bardia.astro': (
        """Un <strong>safari en jeep privatisée d’une journée complète à Bardia</strong> coûte <strong>190 € par véhicule</strong> (jusqu’à 6 passagers). Il permet d’explorer les secteurs reculés du parc inaccessibles à pied (Baghaura, berges de la Karnali). L’excursion inclut le 4x4 tout-terrain avec chauffeur expérimenté, un guide naturaliste certifié, les permis d’entrée et le panier repas en brousse."""
    ),
    'src/pages/tours/safari-pied-bardia.astro': (
        """Un <strong>safari à pied dans le parc national de Bardia</strong> coûte <strong>50 € par personne</strong> avec Jungle Nepal Adventure. Encadré obligatoirement par <strong>deux pisteurs natifs certifiés</strong> armés de bâtons traditionnels en bambou, il dure une journée complète (6h30–18h00) et inclut le permis du parc, le déjeuner en jungle et un <strong>taux d’observation de 85%+ pour le tigre du Bengale</strong> au printemps. Les marches sans deux guides agréés sont strictement interdites par les autorités du parc."""
    ),
    'src/pages/tours/rafting-safari-bardia.astro': (
        """La journée de <strong>rafting et safari sur la rivière Karnali à Bardia</strong> coûte <strong>120 € par personne</strong>. Cette descente silencieuse de 35 km offre des observations exceptionnelles de dauphins d’eau douce du Gange, crocodiles gavials et tigres venant s’abreuver sur les bancs de galets, avec équipement de sécurité certifié et déjeuner sur une plage isolée."""
    ),
    'src/pages/tours/safari-pied-chitwan.astro': (
        """Un <strong>safari à pied dans le parc national de Chitwan</strong> coûte <strong>70 € par personne</strong>. Guidé par deux naturalistes locaux, il se déroule dans les forêts communautaires et zones tampons réputées pour abriter la 2ème plus grande population mondiale de <strong>rhinocéros unicornes d’Asie</strong> (>690 individus), avec des chances d’observation à pied approchant 95% toute l’année."""
    ),
    'src/pages/tours/safari-jeep-chitwan.astro': (
        """Un <strong>safari en jeep à Chitwan</strong> d’une journée complète coûte <strong>190 € pour le véhicule privatisé</strong> (jusqu’à 6 personnes). Il s’enfonce profondément dans la zone cœur classée UNESCO (Kasara, Sukhibhar) pour observer rhinocéros unicornes, ours lippus, crocodiles gavials et tigres du Bengale sous la conduite d’un guide naturaliste agréé."""
    ),

    # English files
    'src/pages/en/tours/bardia-jeep-safari.astro': (
        """A <strong>private full-day 4x4 open jeep safari in Bardia costs €190 per vehicle</strong> (accommodating up to 6 guests). It covers deep interior sectors such as Baghaura and the Karnali floodplain. The tour includes the customized safari vehicle, expert driver, licensed senior naturalist guide, national park entry fees, and a freshly prepared bush lunch."""
    ),
    'src/pages/en/tours/bardia-walking-safari.astro': (
        """A <strong>full-day walking safari in Bardia National Park costs €50 per person</strong> with Jungle Nepal Adventure. Escorted by <strong>two certified native Tharu trackers</strong> equipped with traditional fire-hardened bamboo staffs, it runs from 6:30 AM to 6:00 PM and includes park permits, a jungle bush lunch, and an <strong>85%+ sighting probability for wild Bengal tigers</strong> during spring. Walking without two licensed guides is strictly illegal under Nepalese park law."""
    ),
    'src/pages/en/tours/bardia-rafting-safari.astro': (
        """A <strong>full-day rafting safari on the Karnali River in Bardia costs €120 per person</strong>. This silent 35 km river drift offers rare views of freshwater Gangetic river dolphins, critically endangered gharial crocodiles, and riverbank tigers, accompanied by certified river guides with safety gear and riverside lunch included."""
    ),
    'src/pages/en/tours/chitwan-walking-safari.astro': (
        """A <strong>guided walking safari in Chitwan National Park costs €70 per person</strong>. Led by two certified naturalists through community buffer forests, it offers a near-guaranteed <strong>95% sighting probability for greater one-horned rhinos</strong> (>690 recorded individuals), sloth bears, and river crocodilians without the disruption of motor vehicles."""
    ),
    'src/pages/en/tours/chitwan-jeep-safari.astro': (
        """A <strong>full-day private jeep safari in Chitwan National Park costs €190 per vehicle</strong> (accommodating up to 6 passengers). The itinerary penetrates deep into the UNESCO World Heritage core sectors (Kasara and Sukhibhar) to track greater one-horned rhinos, sloth bears, wild elephants, and Bengal tigers alongside a licensed senior naturalist."""
    )
}

pattern_snippet = re.compile(
    r'\s*<!-- GOOGLE FEATURED SNIPPET & DIRECT ANSWER BLOCK \(POSITION 0 & LLM CITATION\) -->\s*<div class="direct-answer-snippet[^"]*".*?</div>\s*</div>',
    re.DOTALL
)

for file_path, intro_text in files_map.items():
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if snippet exists
    if not pattern_snippet.search(content):
        print(f"No direct answer snippet in {file_path}")
        continue

    # Remove snippet
    content = pattern_snippet.sub('', content)

    # Now insert intro_text right after the first <h2 ...> in the apercu section
    # Find <h2 ...>
    h2_match = re.search(r'(<h2[^>]*>.*?</h2>)', content, re.DOTALL)
    if h2_match:
        h2_full = h2_match.group(1)
        new_para = f'\n            <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">\n              {intro_text}\n            </p>'
        content = content.replace(h2_full, h2_full + new_para, 1)
        print(f"Successfully updated {file_path}")
    else:
        print(f"Could not find <h2> in {file_path}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("All activity pages processed.")
