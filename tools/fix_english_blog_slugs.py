import json
import re
import os

BASE_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'
FR_POSTS_PATH = os.path.join(BASE_DIR, 'src/data/blog_posts.json')
EN_POSTS_PATH = os.path.join(BASE_DIR, 'src/data/blog_posts.en.json')

SLUG_MAP = {
    'agence-safari-nepal-francophone': 'expert-local-safari-agency-nepal',
    'animaux-bardia-faune-parc-national': 'bardia-national-park-wildlife-animals-guide',
    'animaux-chitwan-faune-parc-national': 'chitwan-national-park-wildlife-animals-guide',
    'animaux-rares-safari-nepal-guide': 'rare-wildlife-nepal-secret-jungle-species-guide',
    'art-du-pistage-jungle-nepal-traces-cris-alarme': 'jungle-tracking-art-nepal-pugmarks-alarm-calls',
    'bardia-ou-chitwan-quel-parc-choisir': 'bardia-or-chitwan-which-park-to-choose-safari-nepal',
    'camping-safari-a-bardia-nuits-en-jungle-au-nepal': 'camping-safari-in-bardia-jungle-bivouac-nepal',
    'cerf-des-marais-suklaphanta-savanes-sauvages-ouest-nepalais': 'swamp-deer-suklaphanta-wild-savannas-western-nepal',
    'combien-de-jours-pour-un-safari-au-nepal': 'how-many-days-for-nepal-safari',
    'combiner-trek-et-safari-au-nepal-guide-complet': 'combining-trek-and-safari-in-nepal-complete-guide',
    'comment-aller-a-bardia-transport-avion-bus-guide': 'how-to-get-to-bardia-flights-buses-transfers',
    'comment-aller-a-chitwan-katmandou-pokhara-bus-avion': 'how-to-get-to-chitwan-bus-flights-private-car',
    'comment-organiser-un-safari-a-bardia-apres-un-trek': 'how-to-organize-bardia-safari-after-trek',
    'comment-organiser-un-safari-a-chitwan-apres-un-trek': 'how-to-organize-chitwan-safari-after-trek',
    'comment-organiser-un-safari-au-nepal': 'how-to-plan-a-safari-in-nepal-complete-guide',
    'comportement-du-rhinoceros-unicornis': 'greater-one-horned-rhino-behavior-guide-nepal',
    'comportement-du-tigre-du-bengale': 'bengal-tiger-behavior-king-of-nepal-jungle',
    'condition-physique-safari-a-pied-nepal': 'physical-fitness-walking-safari-nepal-guide',
    'culture-tharu-nepal-immersion-jungle': 'tharu-culture-nepal-jungle-traditions-village-life',
    'culture-tharu-traditions-cuisine-festival-dashain-bardia': 'tharu-cultural-immersion-bardia-traditions-cuisine-dashain',
    'ecologie-pistage-panthere-des-neiges-bharal-nepal': 'snow-leopard-blue-sheep-ecology-tracking-nepal',
    'elephant-sauvage-nepal-guide-safari': 'wild-asian-elephants-nepal-tracking-guide',
    'gavial-du-gange-crocodiles-nepal-guide': 'gharials-and-marsh-crocodiles-nepal-guide',
    'guide-complet-parc-national-de-bardia-nepal': 'bardia-national-park-complete-safari-guide',
    'guide-complet-parc-national-de-suklaphanta': 'suklaphanta-national-park-complete-safari-guide',
    'guide-ornithologique-nepal-oiseaux-bardia-suklaphanta': 'birdwatching-nepal-guide-bardia-suklaphanta',
    'guide-parc-national-de-chitwan-nepal': 'chitwan-national-park-complete-safari-guide',
    'le-safari-ethique-au-nepal-privilegier-la-marche': 'ethical-safari-nepal-why-walking-and-jeep-matter',
    'leopard-indien-panthere-nepal-guide-safari': 'indian-leopard-in-nepal-safari-guide',
    'nilgaut-cerfs-ongules-sauvages-nepal-guide': 'nilgai-blue-bulls-wild-deer-nepal-guide',
    'observer-les-oiseaux-au-nepal-guide-birdwatching': 'birdwatching-in-nepal-bardia-chitwan-guide',
    'oiseaux-bardia-calao-bicorne-rollier-indien-tchitrec-paradis': 'birds-of-bardia-hornbill-indian-roller-paradise-flycatcher',
    'ou-voir-panthere-des-neiges-nepal-dolpo-mustang': 'where-to-see-snow-leopard-nepal-dolpo-mustang',
    'panthere-des-neiges-au-nepal': 'snow-leopard-expedition-nepal-chances-reality',
    'pistage-a-pied-nepal-journee-type-pisteurs-tharu': 'walking-safari-nepal-tiger-tracking-tharu-guides',
    'pister-le-tigre-du-bengale-a-bardia': 'tracking-bengal-tigers-in-bardia-safari-story',
    'prix-dun-safari-au-nepal': 'cost-of-safari-in-nepal-prices-budget-guide',
    'prix-preparation-expedition-panthere-des-neiges-nepal': 'snow-leopard-expedition-nepal-cost-gear-preparation',
    'quand-partir-au-nepal-pour-un-safari-guide': 'best-time-for-safari-in-nepal-weather-seasons',
    'quels-animaux-voir-lors-dun-safari-au-nepal': 'what-animals-can-you-see-on-nepal-safari',
    'rapaces-chouettes-oiseaux-proie-nepal-guide': 'raptors-owls-birds-of-prey-nepal-guide',
    'reptiles-varans-agames-serpents-nepal-guide': 'reptiles-of-nepal-monitor-lizards-agamas-snakes-guide',
    'sac-safari-nepal': 'what-to-pack-for-nepal-safari-packing-list',
    'safari-a-pied-au-nepal-guide-complet': 'walking-safaris-in-nepal-complete-guide',
    'safari-a-pied-nepal-danger-regles-securite-guide': 'walking-safari-nepal-danger-safety-rules',
    'safari-bardia-prix-forfaits-et-ce-que-ca-inclut': 'bardia-safari-prices-packages-inclusions',
    'safari-combine-inde-nepal-corbett-dudhwa-suklaphanta-bardia': 'india-nepal-wildlife-safari-corbett-dudhwa-bardia',
    'safari-dos-elephant-nepal-pourquoi-refuser-cette-pratique': 'elephant-back-safari-nepal-ethical-reasons-to-avoid',
    'safari-nepal-en-famille-guide-securite': 'family-safari-in-nepal-safety-practical-guide',
    'safari-nepal-en-famille-securite-lodges-enfants': 'nepal-family-safari-safety-lodges-children',
    'safari-nepal-ou-afrique-que-choisir': 'nepal-vs-africa-safari-which-to-choose',
    'safari-nepal-ou-inde-comparatif-ranthambore-corbett-bardia': 'nepal-vs-india-safari-comparison-ranthambore-corbett-bardia',
    'safari-photo-au-nepal-spots-materiel-conseils': 'nepal-wildlife-photo-safari-gear-spots-tips',
    'safari-photo-tigre-nepal-bardia-guide-affut': 'bengal-tiger-photography-safari-bardia-nepal',
    'safari-pirogue-rafting-nepal-guide': 'canoe-safari-wildlife-rafting-nepal-guide',
    'sante-paludisme-vaccins-safari-nepal-conseils-medicaux': 'safari-health-malaria-vaccines-nepal-medical-guide',
    'singes-nepal-langurs-macaques-guide': 'monkeys-of-nepal-langurs-macaques-guide',
    'tigre-bardia-observation-chances-spots': 'tigers-in-bardia-sighting-chances-best-spots',
    'trek-jungle-nepal-safari-pied': 'jungle-trekking-nepal-walking-safari-guide',
    'voir-des-tigres-au-nepal': 'bengal-tigers-in-nepal-wildlife-safari-guide'
}

EN_TITLE_TRANSLATIONS = {
    'prix-dun-safari-au-nepal': {
        'title': 'Cost of a Safari in Nepal: Prices, Budget & Expert Tips (2026)',
        'description': 'How much does a safari in Nepal cost? Discover the complete budget to visit national parks: permit fees, guide rates, lodges, jeep rentals, and flight costs.'
    },
    'bardia-ou-chitwan-quel-parc-choisir': {
        'title': 'Bardia or Chitwan: Which National Park to Choose for a Nepal Safari?',
        'description': 'Bardia or Chitwan? Compare Nepal\'s two leading national parks to choose the best safari: Bengal tigers, wild walking safaris, rhinos, travel times, and atmosphere.'
    },
    'quand-partir-au-nepal-pour-un-safari-guide': {
        'title': 'When to Go to Nepal for a Safari: Best Seasons & Wildlife Calendar',
        'description': 'What is the best time for a safari in Nepal? Discover optimal seasons to see tigers, rhinos, and wild elephants across Bardia and Chitwan.'
    },
    'pister-le-tigre-du-bengale-a-bardia': {
        'title': 'Tracking Bengal Tigers in Bardia: 4 Days on Foot in Nepal\'s Wild Jungle',
        'description': 'In Bardia in western Nepal, track the Royal Bengal tiger on foot: tracking stories, sighting probabilities, and real wildlife photography.'
    },
    'safari-bardia-prix-forfaits-et-ce-que-ca-inclut': {
        'title': 'Bardia Safari Prices & Packages: What Is Included (2026 Guide)',
        'description': 'Planning a safari in Bardia? Comprehensive guide to park permits, certified Tharu guide fees, eco-lodges, jeep rentals, and all-inclusive packages.'
    },
    'combien-de-jours-pour-un-safari-au-nepal': {
        'title': 'How Many Days for a Nepal Safari? Ideal Duration & Itineraries',
        'description': 'Wondering how many days to plan for a wildlife safari in Nepal? Ideal durations for Bardia and Chitwan, post-trek extensions, and travel advice.'
    },
    'guide-complet-parc-national-de-suklaphanta': {
        'title': 'Suklaphanta National Park: Complete Safari Guide to Nepal\'s Wild West',
        'description': 'Discover Suklaphanta, Nepal\'s best-kept wilderness secret: vast open grasslands, world\'s largest swamp deer herds, elusive tigers, and travel tips.'
    },
    'combiner-trek-et-safari-au-nepal-guide-complet': {
        'title': 'Combining Trekking and Safari in Nepal: Complete Guide from Himalayas to Jungle',
        'description': 'How to combine a mountain trek and wildlife safari in Nepal: route planning, smart transport connections, packing gear, and best ethical itineraries.'
    },
    'camping-safari-a-bardia-nuits-en-jungle-au-nepal': {
        'title': 'Camping Safari in Bardia: Jungle Bivouacs and Wild Nights in Nepal (2026)',
        'description': 'Experience a wild camping safari in Bardia: sleeping under the stars, night jungle sounds, Tharu campfire meals, safety protocols, and tiger tracking.'
    },
    'le-safari-ethique-au-nepal-privilegier-la-marche': {
        'title': 'Ethical Wildlife Safari in Nepal: Why Choose Walking & Jeep Tracking',
        'description': 'Why does Jungle Nepal advocate for foot and jeep safaris while strictly rejecting elephant rides? Our ethical commitments for responsible wildlife tourism.'
    },
    'agence-safari-nepal-francophone': {
        'title': 'Local Safari Agency in Nepal: The Jungle Nepal Adventure Difference',
        'description': 'Looking for an expert local agency for your wildlife safari in Nepal? Discover our native Tharu guides, personalized itineraries, and ethical small-group ethos.'
    },
    'sac-safari-nepal': {
        'title': 'What to Pack for a Safari in Nepal: The Ultimate Jungle Packing List',
        'description': 'What clothes, gear, and camera equipment should you pack for a Nepal jungle safari? Neutral colors, leech socks, binoculars, and field checklist.'
    },
    'safari-nepal-en-famille-guide-securite': {
        'title': 'Family Safari in Nepal: Practical Safety Guide & Kid-Friendly Lodges (2026)',
        'description': 'Planning a Nepal safari with children? Age recommendations, health and malaria precautions, family-friendly eco-lodges, and gentle wildlife activities.'
    },
    'comportement-du-tigre-du-bengale': {
        'title': 'Bengal Tiger Behavior: Understanding the King of the Nepal Jungle',
        'description': 'Learn about the secret life and behavior of the Bengal tiger in Nepal: territory marking, hunting strategies, pugmark interpretation, and coexistence.'
    },
    'comportement-du-rhinoceros-unicornis': {
        'title': 'Greater One-Horned Rhino Behavior: Understanding Nepal\'s Armored Giant',
        'description': 'Dive into the fascinating behavior of the Indian rhino in Chitwan and Bardia: wallowing habits, charging signs, sensory abilities, and conservation success.'
    },
    'panthere-des-neiges-au-nepal': {
        'title': 'Snow Leopard in Nepal: High Altitude Expedition, Sighting Odds & Reality (2026)',
        'description': 'Tracking the ghost of the mountains in Nepal: where to spot snow leopards, realistic sighting probabilities, physical requirements, and ethical guidelines.'
    },
    'trek-jungle-nepal-safari-pied': {
        'title': 'Jungle Trekking in Nepal: The Complete Walking Safari Guide',
        'description': 'Forget classic mountain paths: explore Nepal\'s subtropical jungles on foot with expert Tharu trackers. Safety rules, best seasons, and raw wilderness encounters.'
    },
    'safari-nepal-ou-afrique-que-choisir': {
        'title': 'Nepal Safari vs African Safari: Why Nepal Offers an Unmatched Walking Experience',
        'description': 'Can a safari in Nepal rival the Serengeti or Kruger? Discover why tracking tigers on foot in Nepal provides a much rawer, intimate, and authentic experience.'
    }
}

with open(EN_POSTS_PATH, 'r', encoding='utf-8') as f:
    posts_en = json.load(f)

# Update each English post
for post in posts_en:
    old_slug = post['slug']
    if old_slug in SLUG_MAP:
        new_slug = SLUG_MAP[old_slug]
        post['slug'] = new_slug
        
        # Check title/desc translations
        if old_slug in EN_TITLE_TRANSLATIONS:
            post['title'] = EN_TITLE_TRANSLATIONS[old_slug]['title']
            post['description'] = EN_TITLE_TRANSLATIONS[old_slug]['description']

# Update internal links within all English posts' content
for post in posts_en:
    content = post.get('content', '')
    for old_slug, new_slug in SLUG_MAP.items():
        # Replace /en/blog/old-slug and /blog/old-slug
        content = re.sub(rf'href=["\']/en/blog/{old_slug}(/|["\'])', rf'href="/en/blog/{new_slug}\1', content)
        content = re.sub(rf'href=["\']/blog/{old_slug}(/|["\'])', rf'href="/en/blog/{new_slug}\1', content)
    post['content'] = content

with open(EN_POSTS_PATH, 'w', encoding='utf-8') as f:
    json.dump(posts_en, f, ensure_ascii=False, indent=2)

print(f"Updated {len(posts_en)} English posts with new English slugs and internal links!")
