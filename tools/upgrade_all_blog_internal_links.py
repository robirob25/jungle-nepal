import json, re

# Load French and English blog posts
with open('src/data/blog_posts.json', 'r', encoding='utf-8') as f:
    posts_fr = json.load(f)

with open('src/data/blog_posts.en.json', 'r', encoding='utf-8') as f:
    posts_en = json.load(f)

# Tour mappings FR -> EN
TOUR_MAP_EN = {
    '/tours/safari-pied-bardia': '/en/tours/bardia-walking-safari',
    '/tours/safari-jeep-bardia': '/en/tours/bardia-jeep-safari',
    '/tours/safari-pied-chitwan': '/en/tours/chitwan-walking-safari',
    '/tours/safari-jeep-chitwan': '/en/tours/chitwan-jeep-safari',
    '/tours/rafting-safari-bardia': '/en/tours/bardia-rafting-safari',
    '/tours/bardia-explorateur': '/en/tours/bardia-tiger-safari-5-days',
    '/tours/jungle-extreme': '/en/tours/nepal-wildlife-safari-15-days',
    '/tours/chitwan-bardia-complete': '/en/tours/chitwan-bardia-combined-safari',
    '/tours/nepal-sauvage': '/en/tours/wild-nepal-safari-annapurna-trek',
    '/tours/bardia-babai-camping': '/en/tours/babai-valley-wild-camping-safari',
    '/tours/babai-special': '/en/tours/babai-valley-tiger-tracking-5-days',
    '/tours/bardia-nuit-sauvage': '/en/tours/bardia-bivouac-camping-safari',
    '/tours/panthere-des-neiges': '/en/tours/snow-leopard-expedition-nepal',
    '/tours/rara-lake-bardia': '/en/tours/rara-lake-bardia-expedition',
    '/tours/chitwan-culture': '/en/tours/chitwan-safari-cultural-tour',
    '/tours/dashain-immersion-culturelle': '/en/tours/dashain-festival-tharu-cultural-tour',
    '/tours/immersion-spirituelle': '/en/tours/himalaya-spiritual-immersion-tour',
    '/tours/carnet-de-voyage': '/en/tours/nepal-sketching-travel-journal-tour',
    '/tours/nepal-immersion-totale': '/en/tours/nepal-wildlife-culture-immersion',
    '/tours/tiji-mustang': '/en/tours/tiji-festival-upper-mustang-trek'
}

# FR specific contextual additions for remaining posts
ADDITIONAL_FR = {
    'cerf-des-marais-suklaphanta-savanes-sauvages-ouest-nepalais': (
        '<p class="wp-block-paragraph">Pour explorer ces savanes sauvages et observer les hardes de cerfs des marais, découvrez notre expédition <a href="/tours/jungle-extreme" class="text-emerald-700 font-bold hover:underline">Jungle Extrême de 15 jours (Suklaphanta, Bardia & Chitwan)</a> ou notre grand circuit d\'aventure <a href="/tours/rara-lake-bardia" class="text-emerald-700 font-bold hover:underline">Rara Lake & Bardia Expédition</a>.</p>'
    ),
    'safari-nepal-ou-inde-comparatif-ranthambore-corbett-bardia': (
        '<p class="wp-block-paragraph">Pour vivre la magie du safari sans les foules des parcs indiens, réservez notre <a href="/tours/safari-pied-bardia" class="text-emerald-700 font-bold hover:underline">safari à pied à Bardia (dès 50 €)</a> ou notre séjour immersif de 5 jours <a href="/tours/bardia-explorateur" class="text-emerald-700 font-bold hover:underline">Bardia Explorateur (690 €)</a>.</p>'
    ),
    'art-du-pistage-jungle-nepal-traces-cris-alarme': (
        '<p class="wp-block-paragraph">Pour vivre cette initiation au pistage en direct avec nos maîtres pisteurs, réservez notre <a href="/tours/safari-pied-bardia" class="text-emerald-700 font-bold hover:underline">safari à pied à Bardia (dès 50 €)</a> ou plongez dans notre expédition <a href="/tours/bardia-explorateur" class="text-emerald-700 font-bold hover:underline">Bardia Explorateur (5 jours)</a>.</p>'
    ),
    'sante-paludisme-vaccins-safari-nepal-conseils-medicaux': (
        '<p class="wp-block-paragraph">Que vous partiez pour une <a href="/tours/safari-pied-bardia" class="text-emerald-700 font-bold hover:underline">journée de safari à pied à Bardia (dès 50 €)</a> ou en <a href="/tours/safari-jeep-bardia" class="text-emerald-700 font-bold hover:underline">jeep 4x4 privatisée (190 €)</a>, nos partenaires de lodges à Bardia et Chitwan répondent aux standards sanitaires les plus stricts.</p>'
    ),
    'leopard-indien-panthere-nepal-guide-safari': (
        '<p class="wp-block-paragraph">Pour maximiser vos chances d\'observer le léopard au crépuscule, optez pour notre <a href="/tours/safari-jeep-bardia" class="text-emerald-700 font-bold hover:underline">safari en jeep privatisée à Bardia (190 €/jour)</a> ou tentez l\'approche silencieuse lors de notre <a href="/tours/safari-pied-bardia" class="text-emerald-700 font-bold hover:underline">safari à pied (dès 50 €)</a>.</p>'
    ),
    'oiseaux-bardia-calao-bicorne-rollier-indien-tchitrec-paradis': (
        '<p class="wp-block-paragraph">Pour observer ces merveilles ailées, découvrez notre <a href="/tours/safari-pied-bardia" class="text-emerald-700 font-bold hover:underline">safari ornithologique à pied à Bardia (dès 50 €)</a> ou notre <a href="/tours/rafting-safari-bardia" class="text-emerald-700 font-bold hover:underline">descente en rafting sur la rivière Karnali (120 €)</a>.</p>'
    ),
    'safari-photo-au-nepal-spots-materiel-conseils': (
        '<p class="wp-block-paragraph">Pour mettre en pratique ces conseils sur le terrain, notre <a href="/tours/safari-jeep-bardia" class="text-emerald-700 font-bold hover:underline">safari en jeep privatisée à Bardia (190 €)</a> et notre <a href="/tours/safari-pied-bardia" class="text-emerald-700 font-bold hover:underline">safari à pied à Bardia (dès 50 €)</a> offrent les conditions optimales d\'affût photographique.</p>'
    ),
    'ou-voir-panthere-des-neiges-nepal-dolpo-mustang': (
        '<p class="wp-block-paragraph">Pour concrétiser ce rêve d\'altitude, découvrez notre <a href="/tours/panthere-des-neiges" class="text-emerald-700 font-bold hover:underline">expédition officielle Panthère des Neiges au Dolpo et Mustang (17 jours)</a> ou explorez le royaume secret lors du <a href="/tours/tiji-mustang" class="text-emerald-700 font-bold hover:underline">Trek du Festival de Tiji</a>.</p>'
    ),
    'prix-preparation-expedition-panthere-des-neiges-nepal': (
        '<p class="wp-block-paragraph">Pour connaître tous les détails logistiques et tarifaires de notre encadrement, consultez notre fiche officielle <a href="/tours/panthere-des-neiges" class="text-emerald-700 font-bold hover:underline">Expédition Panthère des Neiges au Népal (17 jours)</a> ou notre circuit d\'altitude <a href="/tours/tiji-mustang" class="text-emerald-700 font-bold hover:underline">Tiji Festival en Haut Mustang</a>.</p>'
    ),
    'ecologie-pistage-panthere-des-neiges-bharal-nepal': (
        '<p class="wp-block-paragraph">Pour observer ce prédateur légendaire dans son biotope minéral, rejoignez notre <a href="/tours/panthere-des-neiges" class="text-emerald-700 font-bold hover:underline">expédition Panthère des Neiges (17 jours)</a> ou notre combiné d\'aventure <a href="/tours/nepal-sauvage" class="text-emerald-700 font-bold hover:underline">Népal Sauvage : Trek des Annapurnas & Safari</a>.</p>'
    )
}

# Apply additional paragraphs to French posts if not already present
for post in posts_fr:
    slug = post['slug']
    if slug in ADDITIONAL_FR:
        addition = ADDITIONAL_FR[slug]
        # Check if link is already present
        tour_check = re.search(r'href=[\"\'](/tours/[^\"\']+)[\"\']', addition)
        if tour_check and tour_check.group(1) not in post['content']:
            post['content'] = post['content'] + "\n\n" + addition
            print(f"Added natural contextual paragraph to FR post: {slug}")

# Save updated FR posts
with open('src/data/blog_posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts_fr, f, ensure_ascii=False, indent=2)

print("Saved updated src/data/blog_posts.json.")

# NOW: Let's do the exact same comprehensive upgrade on English posts (blog_posts.en.json)!
# English mapping rules
EN_PARAGRAPHS = {
    'safari-a-pied-nepal-danger-regles-securite-guide': (
        '<p class="wp-block-paragraph">To experience this on the ground with senior certified Tharu master naturalists, book our <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Tiger Safari (from €50)</a> or our <a href="/en/tours/chitwan-walking-safari" class="text-emerald-700 font-bold hover:underline">Chitwan Rhino Walking Safari (from €70)</a>. For families with children, our <a href="/en/tours/bardia-jeep-safari" class="text-emerald-700 font-bold hover:underline">Private 4x4 Jeep Safari (€190/jeep)</a> is the safest alternative.</p>'
    ),
    'guide-complet-parc-national-de-suklaphanta': (
        '<p class="wp-block-paragraph">Suklaphanta is an extraordinary, crowd-free wilderness. To explore it alongside Bardia and Chitwan, discover our flagship 15-day expedition <a href="/en/tours/nepal-wildlife-safari-15-days" class="text-emerald-700 font-bold hover:underline">Wild Nepal Safari (15 Days)</a> or compare it with our <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Safari</a>.</p>'
    ),
    'animaux-bardia-faune-parc-national': (
        '<p class="wp-block-paragraph">To track Bardia\'s Big 5 in their natural habitat, join our daily <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Walking Tiger Safari (from €50)</a>, book a <a href="/en/tours/bardia-jeep-safari" class="text-emerald-700 font-bold hover:underline">Private 4x4 Jeep Safari (€190/vehicle)</a>, or embark on our comprehensive 5-day lodge immersion <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-700 font-bold hover:underline">Bardia Tiger Safari (5 Days)</a>. To spot Gangetic river dolphins, discover our <a href="/en/tours/bardia-rafting-safari" class="text-emerald-700 font-bold hover:underline">Karnali River Rafting Safari (€120)</a>.</p>'
    ),
    'animaux-chitwan-faune-parc-national': (
        '<p class="wp-block-paragraph">To encounter greater one-horned rhinos on foot or by vehicle, explore our <a href="/en/tours/chitwan-walking-safari" class="text-emerald-700 font-bold hover:underline">Chitwan Rhino Walking Safari (from €70)</a>, our <a href="/en/tours/chitwan-jeep-safari" class="text-emerald-700 font-bold hover:underline">Private Chitwan Jeep Safari (€190)</a>, or combine both world-heritage parks on our <a href="/en/tours/chitwan-bardia-combined-safari" class="text-emerald-700 font-bold hover:underline">Chitwan + Bardia Combined Safari (11 Days)</a>.</p>'
    ),
    'camping-safari-a-bardia-nuits-en-jungle-au-nepal': (
        '<p class="wp-block-paragraph">Experience true wilderness isolation on our <a href="/en/tours/babai-valley-wild-camping-safari" class="text-emerald-700 font-bold hover:underline">Babai Valley Wild Camping Safari (4 Days)</a> or spend an unforgettable night in an elevated observation hide with our <a href="/en/tours/bardia-bivouac-camping-safari" class="text-emerald-700 font-bold hover:underline">Bardia Bivouac & Treehouse Night (from €290)</a>.</p>'
    ),
    'oiseaux-bardia-calao-bicorne-rollier-indien-tchitrec-paradis': (
        '<p class="wp-block-paragraph">For birdwatchers seeking hornbills, rollers, and riverine species, our silent <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Safari (from €50)</a> and scenic <a href="/en/tours/bardia-rafting-safari" class="text-emerald-700 font-bold hover:underline">Karnali Rafting Drift Safari (€120)</a> provide unbeatable vantage points.</p>'
    ),
    'prix-dun-safari-au-nepal': (
        '<p class="wp-block-paragraph">Explore transparent pricing for our activities: <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Walking Safari in Bardia (from €50/day)</a>, <a href="/en/tours/bardia-jeep-safari" class="text-emerald-700 font-bold hover:underline">Private 4x4 Jeep Safari (€190/jeep)</a>, <a href="/en/tours/chitwan-walking-safari" class="text-emerald-700 font-bold hover:underline">Chitwan Walking Safari (from €70)</a>, or our all-inclusive 5-day lodge package <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-700 font-bold hover:underline">Bardia Tiger Safari 5 Days (€690)</a>.</p>'
    ),
    'trek-jungle-nepal-safari-pied': (
        '<p class="wp-block-paragraph">If you want to combine high Himalaya hiking with lowland tiger tracking, discover our official circuit <a href="/en/tours/wild-nepal-safari-annapurna-trek" class="text-emerald-700 font-bold hover:underline">Wild Nepal Safari & Annapurna Trek (15 Days)</a> or add a single-day <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Safari (from €50)</a> after your trek.</p>'
    ),
    'pister-le-tigre-du-bengale-a-bardia': (
        '<p class="wp-block-paragraph">To follow tiger pugmarks on foot with local master naturalists, book our <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Tiger Safari (from €50)</a> or our flagship <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-700 font-bold hover:underline">Bardia Tiger Safari 5 Days (€690)</a>.</p>'
    ),
    'art-du-pistage-jungle-nepal-traces-cris-alarme': (
        '<p class="wp-block-paragraph">Learn tracking ethology directly in the wild on our <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Walking Tiger Safari in Bardia (from €50)</a> or our 5-day tracking deep-dive <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-700 font-bold hover:underline">Bardia Tiger Safari (5 Days)</a>.</p>'
    ),
    'guide-complet-parc-national-de-bardia-nepal': (
        '<p class="wp-block-paragraph">Explore Bardia with our tailor-made experiences: <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Full-Day Walking Safari (from €50)</a>, <a href="/en/tours/bardia-jeep-safari" class="text-emerald-700 font-bold hover:underline">Private 4x4 Jeep Safari (€190)</a>, <a href="/en/tours/bardia-rafting-safari" class="text-emerald-700 font-bold hover:underline">Karnali River Rafting Safari (€120)</a>, or our all-inclusive 5-day package <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-700 font-bold hover:underline">Bardia Tiger Safari (€690)</a>.</p>'
    ),
    'safari-photo-au-nepal-spots-materiel-conseils': (
        '<p class="wp-block-paragraph">For wildlife photographers, our <a href="/en/tours/bardia-jeep-safari" class="text-emerald-700 font-bold hover:underline">Private 4x4 Jeep Safari in Bardia (€190/day)</a> accommodates heavy telephoto lenses with complete flexibility, while our <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Walking Safari (from €50)</a> provides ground-level eye-contact opportunities.</p>'
    ),
    'le-safari-ethique-au-nepal-privilegier-la-marche': (
        '<p class="wp-block-paragraph">At Jungle Nepal Adventure, we strictly boycott elephant riding. Experience 100% ethical wildlife observation on our <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Safari (from €50)</a>, our <a href="/en/tours/chitwan-walking-safari" class="text-emerald-700 font-bold hover:underline">Chitwan Walking Safari (from €70)</a>, or our <a href="/en/tours/bardia-jeep-safari" class="text-emerald-700 font-bold hover:underline">Private 4x4 Jeep Safaris</a>.</p>'
    ),
    'agence-safari-nepal-francophone': (
        '<p class="wp-block-paragraph">Our flagship expeditions include the <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Safari (from €50)</a>, the <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-700 font-bold hover:underline">Bardia Tiger Safari 5 Days (€690)</a>, the combined <a href="/en/tours/wild-nepal-safari-annapurna-trek" class="text-emerald-700 font-bold hover:underline">Wild Nepal Safari & Annapurna Trek (15 Days)</a>, and our high-altitude <a href="/en/tours/snow-leopard-expedition-nepal" class="text-emerald-700 font-bold hover:underline">Snow Leopard Expedition in Dolpo & Mustang (17 Days)</a>.</p>'
    ),
    'sac-safari-nepal': (
        '<p class="wp-block-paragraph">Whether you are gearing up for a <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Walking Safari in Bardia</a>, an open-top <a href="/en/tours/bardia-jeep-safari" class="text-emerald-700 font-bold hover:underline">Jeep Safari</a>, or a wilderness <a href="/en/tours/babai-valley-wild-camping-safari" class="text-emerald-700 font-bold hover:underline">Babai Valley Wild Camping Safari</a>, proper neutral clothing is essential.</p>'
    ),
    'safari-nepal-en-famille-guide-securite': (
        '<p class="wp-block-paragraph">For family travelers with children, we strongly recommend our private <a href="/en/tours/bardia-jeep-safari" class="text-emerald-700 font-bold hover:underline">Bardia 4x4 Jeep Safari (€190/jeep)</a>, our <a href="/en/tours/chitwan-jeep-safari" class="text-emerald-700 font-bold hover:underline">Chitwan Jeep Safari</a>, or our gentle <a href="/en/tours/chitwan-safari-cultural-tour" class="text-emerald-700 font-bold hover:underline">Chitwan Safari Cultural Tour (4 Days)</a>.</p>'
    ),
    'condition-physique-safari-a-pied-nepal': (
        '<p class="wp-block-paragraph">Walking safaris in Bardia are conducted on flat terrain along riverbeds and forest paths. Discover our <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Safari (from €50)</a> or choose effortless exploration with our <a href="/en/tours/bardia-jeep-safari" class="text-emerald-700 font-bold hover:underline">Private 4x4 Jeep Safari (€190)</a>.</p>'
    ),
    'quels-animaux-voir-lors-dun-safari-au-nepal': (
        '<p class="wp-block-paragraph">To witness Nepal\'s legendary biodiversity, join our <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Safari (from €50)</a> for wild tigers, our <a href="/en/tours/chitwan-walking-safari" class="text-emerald-700 font-bold hover:underline">Chitwan Walking Safari (from €70)</a> for rhinos, or embark on our grand 3-park circuit <a href="/en/tours/nepal-wildlife-safari-15-days" class="text-emerald-700 font-bold hover:underline">Nepal Wildlife Safari 15 Days</a>.</p>'
    ),
    'comportement-du-tigre-du-bengale': (
        '<p class="wp-block-paragraph">Observing wild tiger behavior in their natural territory is our specialty. Track tigers on foot with our <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Safari (from €50)</a>, by <a href="/en/tours/bardia-jeep-safari" class="text-emerald-700 font-bold hover:underline">Private 4x4 Jeep Safari</a>, or across our 5-day immersion <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-700 font-bold hover:underline">Bardia Tiger Safari 5 Days (€690)</a>.</p>'
    ),
    'comportement-du-rhinoceros-unicornis': (
        '<p class="wp-block-paragraph">Greater one-horned rhinos are best observed on foot or from an open jeep. Discover our <a href="/en/tours/chitwan-walking-safari" class="text-emerald-700 font-bold hover:underline">Chitwan Rhino Walking Safari (from €70)</a>, our <a href="/en/tours/chitwan-jeep-safari" class="text-emerald-700 font-bold hover:underline">Chitwan Jeep Safari</a>, or compare both parks on our <a href="/en/tours/chitwan-bardia-combined-safari" class="text-emerald-700 font-bold hover:underline">Chitwan + Bardia Combined Safari (11 Days)</a>.</p>'
    ),
    'elephant-sauvage-nepal-guide-safari': (
        '<p class="wp-block-paragraph">To safely observe wild elephant herds crossing river corridors, choose our <a href="/en/tours/bardia-jeep-safari" class="text-emerald-700 font-bold hover:underline">Private 4x4 Jeep Safari in Bardia (€190/jeep)</a> or our 5-day lodge adventure <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-700 font-bold hover:underline">Bardia Tiger Safari 5 Days</a>.</p>'
    ),
    'gavial-du-gange-crocodiles-nepal-guide': (
        '<p class="wp-block-paragraph">The premier way to spot prehistoric gharials and marsh muggers is drifting silently on our <a href="/en/tours/bardia-rafting-safari" class="text-emerald-700 font-bold hover:underline">Karnali River Rafting Safari (from €120)</a> or observing riverbanks during our <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Walking Safari in Bardia</a>.</p>'
    ),
    'safari-pirogue-rafting-nepal-guide': (
        '<p class="wp-block-paragraph">For river safari adventures in Nepal, book our full-day <a href="/en/tours/bardia-rafting-safari" class="text-emerald-700 font-bold hover:underline">Karnali River Rafting Safari (€120)</a> or combine river drifts and walking safaris on our <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-700 font-bold hover:underline">Bardia Tiger Safari 5 Days</a>.</p>'
    ),
    'panthere-des-neiges-au-nepal': (
        '<p class="wp-block-paragraph">Discover our pinnacle high-altitude expedition: the <a href="/en/tours/snow-leopard-expedition-nepal" class="text-emerald-700 font-bold hover:underline">Snow Leopard Expedition in Dolpo & Mustang (17 Days)</a>, and explore Tibetan cultural highlands on our <a href="/en/tours/tiji-festival-upper-mustang-trek" class="text-emerald-700 font-bold hover:underline">Tiji Festival Upper Mustang Trek</a>.</p>'
    ),
    'ou-voir-panthere-des-neiges-nepal-dolpo-mustang': (
        '<p class="wp-block-paragraph">To pursue the ghost of the mountains in western Nepal, explore our <a href="/en/tours/snow-leopard-expedition-nepal" class="text-emerald-700 font-bold hover:underline">Snow Leopard Expedition Nepal (17 Days)</a> or our high-altitude cultural circuit <a href="/en/tours/tiji-festival-upper-mustang-trek" class="text-emerald-700 font-bold hover:underline">Tiji Festival Upper Mustang Trek</a>.</p>'
    ),
    'prix-preparation-expedition-panthere-des-neiges-nepal': (
        '<p class="wp-block-paragraph">For comprehensive logistics, pricing, and gear requirements, explore our dedicated expedition page: <a href="/en/tours/snow-leopard-expedition-nepal" class="text-emerald-700 font-bold hover:underline">Snow Leopard Expedition in Nepal (17 Days)</a>.</p>'
    ),
    'ecologie-pistage-panthere-des-neiges-bharal-nepal': (
        '<p class="wp-block-paragraph">Track apex predators in the high Himalayas on our <a href="/en/tours/snow-leopard-expedition-nepal" class="text-emerald-700 font-bold hover:underline">Snow Leopard Expedition (17 Days)</a> or combine mountain trekking and lowland safaris on our <a href="/en/tours/wild-nepal-safari-annapurna-trek" class="text-emerald-700 font-bold hover:underline">Wild Nepal Safari & Annapurna Trek</a>.</p>'
    ),
    'culture-tharu-nepal-immersion-jungle': (
        '<p class="wp-block-paragraph">Experience authentic Tharu cultural hospitality on our <a href="/en/tours/dashain-festival-tharu-cultural-tour" class="text-emerald-700 font-bold hover:underline">Dashain Festival & Tharu Cultural Tour (Bardia)</a> or our 4-day <a href="/en/tours/chitwan-safari-cultural-tour" class="text-emerald-700 font-bold hover:underline">Chitwan Safari Cultural Tour</a>.</p>'
    ),
    'observer-les-oiseaux-au-nepal-guide-birdwatching': (
        '<p class="wp-block-paragraph">Plan your dedicated birding itinerary with our <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Birdwatching Walking Safari (from €50)</a>, scenic <a href="/en/tours/bardia-rafting-safari" class="text-emerald-700 font-bold hover:underline">Karnali River Rafting Safari (€120)</a>, or our grand 3-park circuit <a href="/en/tours/nepal-wildlife-safari-15-days" class="text-emerald-700 font-bold hover:underline">Nepal Wildlife Safari 15 Days</a>.</p>'
    ),
    'rapaces-chouettes-oiseaux-proie-nepal-guide': (
        '<p class="wp-block-paragraph">Spot Himalayan vultures, fish owls, and raptors on our <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Safari (from €50)</a> or our 5-day lodge expedition <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-700 font-bold hover:underline">Bardia Tiger Safari 5 Days</a>.</p>'
    ),
    'animaux-rares-safari-nepal-guide': (
        '<p class="wp-block-paragraph">To seek rare and elusive wildlife, explore our pristine <a href="/en/tours/babai-valley-wild-camping-safari" class="text-emerald-700 font-bold hover:underline">Babai Valley Wild Camping Safari (4 Days)</a>, our <a href="/en/tours/snow-leopard-expedition-nepal" class="text-emerald-700 font-bold hover:underline">Snow Leopard Expedition (17 Days)</a>, or our grand multi-park <a href="/en/tours/nepal-wildlife-safari-15-days" class="text-emerald-700 font-bold hover:underline">Nepal Wildlife Safari 15 Days</a>.</p>'
    ),
    'singes-nepal-langurs-macaques-guide': (
        '<p class="wp-block-paragraph">Observe sacred langurs acting as forest sentinels on our <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Safari (from €50)</a> or during our <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-700 font-bold hover:underline">Bardia Tiger Safari 5 Days</a>.</p>'
    ),
    'nilgaut-cerfs-ongules-sauvages-nepal-guide': (
        '<p class="wp-block-paragraph">To see large herds of nilgai and swamp deer across alluvial grasslands, choose our <a href="/en/tours/bardia-jeep-safari" class="text-emerald-700 font-bold hover:underline">Private 4x4 Jeep Safari in Bardia (€190/vehicle)</a> or our silent on-foot approach with the <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Safari (from €50)</a>.</p>'
    ),
    'reptiles-varans-agames-serpents-nepal-guide': (
        '<p class="wp-block-paragraph">Spot monitor lizards, pythons, and crocodiles along riverbanks on our <a href="/en/tours/bardia-rafting-safari" class="text-emerald-700 font-bold hover:underline">Karnali Rafting Drift Safari (€120)</a> and our on-foot tracking sessions with the <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Safari (from €50)</a>.</p>'
    ),
    'safari-nepal-ou-afrique-que-choisir': (
        '<p class="wp-block-paragraph">What sets Nepal apart from African safaris is the rare freedom of tracking apex predators entirely on foot: experience it on our <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Safari (from €50)</a>, our 5-day immersion <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-700 font-bold hover:underline">Bardia Tiger Safari (€690)</a>, or our grand <a href="/en/tours/chitwan-bardia-combined-safari" class="text-emerald-700 font-bold hover:underline">Chitwan + Bardia Combined Safari (11 Days)</a>.</p>'
    ),
    'cerf-des-marais-suklaphanta-savanes-sauvages-ouest-nepalais': (
        '<p class="wp-block-paragraph">To explore Suklaphanta\'s wild grasslands and track the world\'s largest swamp deer herds, discover our 15-day expedition <a href="/en/tours/nepal-wildlife-safari-15-days" class="text-emerald-700 font-bold hover:underline">Nepal Wildlife Safari 15 Days</a> or our remote western circuit <a href="/en/tours/rara-lake-bardia-expedition" class="text-emerald-700 font-bold hover:underline">Rara Lake & Bardia Expedition</a>.</p>'
    ),
    'safari-nepal-ou-inde-comparatif-ranthambore-corbett-bardia': (
        '<p class="wp-block-paragraph">For an authentic safari without the crowds and rigid jeep queues of Indian reserves, experience our <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Safari (from €50)</a> or our all-inclusive 5-day lodge stay <a href="/en/tours/bardia-tiger-safari-5-days" class="text-emerald-700 font-bold hover:underline">Bardia Tiger Safari 5 Days (€690)</a>.</p>'
    ),
    'sante-paludisme-vaccins-safari-nepal-conseils-medicaux': (
        '<p class="wp-block-paragraph">Whether you choose a <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Walking Safari in Bardia (from €50)</a> or a <a href="/en/tours/bardia-jeep-safari" class="text-emerald-700 font-bold hover:underline">Private 4x4 Jeep Safari (€190)</a>, our partner lodges in Bardia and Chitwan maintain the highest hygiene standards.</p>'
    ),
    'leopard-indien-panthere-nepal-guide-safari': (
        '<p class="wp-block-paragraph">To maximize chances of spotting elusive leopards at dusk, choose our <a href="/en/tours/bardia-jeep-safari" class="text-emerald-700 font-bold hover:underline">Private 4x4 Jeep Safari in Bardia (€190/day)</a> or our silent on-foot tracking sessions with the <a href="/en/tours/bardia-walking-safari" class="text-emerald-700 font-bold hover:underline">Bardia Walking Safari (from €50)</a>.</p>'
    )
}

# Apply to EN posts
modified_en = 0
for post in posts_en:
    slug = post['slug']
    content = post['content']
    orig_content = content
    
    # Replace vague /#prochains-departs links with appropriate tours
    content = re.sub(r'href=[\"\'](/#prochains-departs|https://junglenepal\.com/#prochains-departs)[\"\']', r'href="/en/tours/bardia-tiger-safari-5-days"', content)
    content = re.sub(r'href=[\"\']https://junglenepal\.com[\"\']', r'href="/en"', content)
    
    # Replace French tour links in English posts with English tour links if any
    for fr_url, en_url in TOUR_MAP_EN.items():
        content = content.replace(f'href="{fr_url}"', f'href="{en_url}"')
        content = content.replace(f"href='{fr_url}'", f"href='{en_url}'")
        
    # Append contextual English paragraph if defined
    if slug in EN_PARAGRAPHS:
        addition = EN_PARAGRAPHS[slug]
        tour_check = re.search(r'href=[\"\'](/en/tours/[^\"\']+)[\"\']', addition)
        if tour_check and tour_check.group(1) not in content:
            content = content + "\n\n" + addition
            
    if content != orig_content:
        post['content'] = content
        modified_en += 1

print(f"Enriched {modified_en} English posts with natural contextual internal links.")

# Save EN posts
with open('src/data/blog_posts.en.json', 'w', encoding='utf-8') as f:
    json.dump(posts_en, f, ensure_ascii=False, indent=2)

print("Saved updated src/data/blog_posts.en.json.")
