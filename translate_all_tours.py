import json

# Comprehensive English translations for all 15 tours
en_tour_translations = {
    "bardia-explorateur": {
        "title_en": "Bardia Explorer – 5 Days in the Wild Jungle",
        "duration_en": "5 Days",
        "group_size_en": "Small group 4 to 8 explorers",
        "badge_en": "🐅 Safari & Tiger Tracking",
        "overview_en": "This 5-day adventure is designed for nature and wildlife lovers seeking the pristine beauty of Bardia National Park. Track wild Bengal tigers, Asian one-horned rhinos, and wild elephants on foot alongside our expert local Tharu master trackers.",
        "highlights_en": [
            "Full-day walking safari tracking Bengal tigers with expert guides",
            "Jeep safari deep into the remote core zones of Bardia",
            "Traditional canoe river safari on the Karnali & Geruwa rivers",
            "Authentic Tharu cultural village immersion and organic local gastronomy",
            "Charming ecolodge accommodation at the edge of the jungle"
        ]
    },
    "chitwan-culture": {
        "title_en": "Chitwan – Wildlife Safari & Indigenous Culture",
        "duration_en": "4 Days",
        "group_size_en": "Small group 4 to 8 explorers",
        "badge_en": "🦏 Rhinos & Chitwan Wildlife",
        "overview_en": "A rich, immersive short stay combining the thrill of wildlife safaris with the warmth of local indigenous culture. Chitwan is Asia's prime sanctuary for observing the Greater One-Horned Rhinoceros, vibrant birdlife, and the traditional way of life of the Tharu people.",
        "highlights_en": [
            "Thrilling 4x4 open jeep safari in Chitwan National Park",
            "Peaceful dugout canoe drift on the Rapti river observing gharials and rhinos",
            "Traditional Tharu cultural dance performance and village exploration",
            "Comfortable stay in an authentic riverside eco-resort"
        ]
    },
    "rafting-safari": {
        "title_en": "Wild Rivers & Hidden Heritage – Rafting & Safari Expedition",
        "duration_en": "18 Days",
        "group_size_en": "Small group 4 to 8 explorers",
        "badge_en": "🚣 Wild Rivers & Rafting",
        "overview_en": "Embark on an extraordinary journey through Nepal blending ancient cultural heritage, untouched nature, and adrenaline-pumping wild river rafting. From Kathmandu's royal palaces to the roaring gorges of the Bheri and pristine safaris in Bardia.",
        "highlights_en": [
            "Multi-day self-sufficient wild river rafting and sandbank riverside bivouacs",
            "Walking and jeep safaris in the remote heart of Bardia National Park",
            "Exploration of UNESCO World Heritage medieval cities in Kathmandu Valley",
            "Total immersion in Nepal's untamed western wilderness"
        ]
    },
    "bardia-nuit-sauvage": {
        "title_en": "Bardia Wild Night – Jungle Immersion & Bush Camping",
        "duration_en": "2 Days",
        "group_size_en": "Micro-group 2 to 6 explorers",
        "badge_en": "⛺ Jungle Bivouacs & Wild Nights",
        "overview_en": "An intense, authentic micro-adventure in the deep forest of Bardia. Spend a magical night under the stars listening to the sounds of the nocturnal jungle, preceded and followed by intensive tracking on foot with our veteran wildlife rangers.",
        "highlights_en": [
            "Exclusive wilderness bush camp inside safe forest clearing",
            "Sunset and sunrise tiger and elephant tracking on foot",
            "Campfire dinner under the Himalayan starry canopy",
            "High-adrenaline sensory encounter with raw nature"
        ]
    },
    "rara-lake-bardia": {
        "title_en": "Rara Lake & Bardia Expedition – The Ultimate Off-the-Beaten-Track Adventure",
        "duration_en": "17 Days",
        "group_size_en": "Small group 4 to 8 explorers",
        "badge_en": "🏔️ Himalayas, Mustang & Spirituality",
        "overview_en": "An epic overland crossing uniting the sapphire alpine waters of Rara Lake at 3,000 meters with the dense subtropical tiger jungles of Bardia. Experience remote Himalayan villages, alpine forests, and wild river valleys untouched by modern tourism.",
        "highlights_en": [
            "Trekking around the crystal-clear sapphire waters of Lake Rara (3,000m)",
            "Deep wildlife tracking in Bardia National Park's pristine tiger corridors",
            "Pristine off-grid Himalayan mountain villages and sacred temples",
            "Private 4x4 overland expedition through Western Nepal's hidden gems"
        ]
    },
    "bardia-babai-camping": {
        "title_en": "Bardia Babai Valley – Wild Camping in Untamed Nature",
        "duration_en": "8 Days",
        "group_size_en": "Small group 4 to 8 explorers",
        "badge_en": "⛺ Jungle Bivouacs & Wild Nights",
        "overview_en": "The Babai Valley is Bardia's most secret, protected sanctuary. Reserved for true adventurers, this multi-day expedition takes you deep into isolated gorges where wild herds of elephants, tigers, and elusive leopards roam free.",
        "highlights_en": [
            "Several nights of mobile wild camping along the Babai River",
            "Strictly restricted conservation territory with zero tourist traffic",
            "Unrivaled wildlife spotting: tigers, rhinos, sloth bears, and wild elephants",
            "Escorted by senior government rangers and local master trackers"
        ]
    },
    "nepal-immersion-totale": {
        "title_en": "Nepal Total Immersion – Culture, Wildlife & Adventure",
        "duration_en": "14 Days",
        "group_size_en": "Small group 4 to 8 explorers",
        "badge_en": "🇳🇵 Grand 360° Expeditions",
        "overview_en": "The complete 360° quintessential Nepal journey. Experience the spiritual majesty of Kathmandu Valley, the tranquility of Pokhara beneath the Annapurnas, thrilling river rafting, and intense wildlife safaris in both Chitwan and Bardia.",
        "highlights_en": [
            "Comprehensive grand loop: Kathmandu, Pokhara, Trishuli river, Chitwan & Bardia",
            "River rafting adventure with scenic riverside lunch",
            "Walking and jeep safaris with maximum tiger and rhino encounter odds",
            "Cultural encounters with Newar, Gurung, and Tharu communities"
        ]
    },
    "babai-special": {
        "title_en": "Deep Into the Wild: Babai Special Experience",
        "duration_en": "5 Days",
        "group_size_en": "Small group 4 to 8 explorers",
        "badge_en": "⛺ Jungle Bivouacs & Wild Nights",
        "overview_en": "An exclusive 5-day immersion into the mysterious Babai Valley. Combining rugged 4x4 exploration, guided foot patrols along riverbanks, and authentic night camps in the prime territory of Bengal tigers.",
        "highlights_en": [
            "Exclusive access to the pristine Babai river valley",
            "High density of big cats and wild ungulates",
            "Wild glamping with field cook and comfortable tent setups",
            "Unmatched tranquility and silence far from civilization"
        ]
    },
    "chitwan-bardia-complete": {
        "title_en": "Chitwan + Bardia – The Complete Nepal Jungle Safari",
        "duration_en": "12 Days",
        "group_size_en": "Small group 4 to 8 explorers",
        "badge_en": "🐅 Safari & Big Cats",
        "overview_en": "Why choose between Nepal's two greatest national parks? This ultimate wildlife safari takes you from the lush riverine grasslands of Chitwan (rhino paradise) to the deep sal forests of Bardia (tiger kingdom).",
        "highlights_en": [
            "Direct comparison of Nepal's two crown-jewel national parks",
            "Greater One-Horned Rhinoceros tracking in Chitwan & Bengal Tiger tracking in Bardia",
            "Multiple safari modes: open 4x4 jeep, traditional dugout canoes, and walking safaris",
            "Comfortable boutique lodges and personalized wildlife mentoring"
        ]
    },
    "tiji-mustang": {
        "title_en": "Tiji Festival – Upper Mustang Forbidden Kingdom",
        "duration_en": "13 Days",
        "group_size_en": "Small group 4 to 8 explorers",
        "badge_en": "🏔️ Himalayas, Mustang & Spirituality",
        "overview_en": "Journey behind the great Himalayan barrier into the ancient Kingdom of Lo (Upper Mustang). Witness the mesmerizing, sacred three-day Tiji Festival in Lo Manthang with masked lama dances, cliffside cave monasteries, and Tibetan Buddhist rituals.",
        "highlights_en": [
            "Exclusive attendance at the vibrant three-day Tiji Festival in Lo Manthang",
            "Spectacular trans-Himalayan scenery: eroded ochre canyons, caves, and snow peaks",
            "Centuries-old Tibetan Buddhist monasteries and royal palaces",
            "Scenic domestic flights between Pokhara and Jomsom through Kali Gandaki gorge"
        ]
    },
    "carnet-de-voyage": {
        "title_en": "Nepal Sketching & Travel Journaling Expedition",
        "duration_en": "15 Days",
        "group_size_en": "Small group 4 to 8 explorers",
        "badge_en": "🏔️ Himalayas, Mustang & Spirituality",
        "overview_en": "An artistic and sensory voyage designed for sketchers, watercolorists, photographers, and mindful travelers. Capture the colors of ancient medieval squares, golden Himalayan dawns, and untamed wildlife with guided creative workshops.",
        "highlights_en": [
            "Daily creative sketching and photography pauses in extraordinary settings",
            "Private visits to historic temples, mountain balconies, and wild jungles",
            "Harmonious rhythm balancing cultural immersion, nature walks, and creative free time",
            "Warm exchanges with local painters, artisans, and monks"
        ]
    },
    "jungle-extreme": {
        "title_en": "Extreme Jungle – Special Wildlife & Big Cat Expedition",
        "duration_en": "15 Days",
        "group_size_en": "Small group 4 to 8 explorers",
        "badge_en": "🐅 Safari & Big Cats",
        "overview_en": "Our most demanding and rewarding safari expedition, entirely dedicated to passionate wildlife photographers and naturalists. 15 intensive days in Bardia, Babai, and Suklaphanta targeting tigers, leopards, rhinos, and rare marsh deer.",
        "highlights_en": [
            "Maximum field hours: dawn-to-dusk tracking with elite wildlife spotters",
            "Exploration of 3 major wildlife sanctuaries: Bardia, Babai Valley, and Suklaphanta",
            "Strategic hideouts, machans (watchtowers), and riverside waiting posts",
            "Unrivaled photographic opportunities under optimal natural lighting"
        ]
    },
    "nepal-sauvage": {
        "title_en": "Wild Nepal – From Dense Jungle to Sacred Annapurna Peaks",
        "duration_en": "15 Days",
        "group_size_en": "Small group 4 to 8 explorers",
        "badge_en": "🏔️ Himalayas, Mustang & Spirituality",
        "overview_en": "A breathtaking contrast between the steaming subtropical jungles of the Terai and the snowcapped summits of the Himalayas. Track rhinos and tigers in Bardia before ascending into the tranquil alpine villages and pine forests of the Annapurnas.",
        "highlights_en": [
            "Complete ecological gradient from 150m jungle plains to 3,200m Himalayan panoramas",
            "Walking safaris in Bardia National Park with senior trackers",
            "Scenic trekking in the Annapurna foothills with sunrise over Machapuchare",
            "Serene stays in mountain lodges and authentic village homestays"
        ]
    },
    "immersion-spirituelle": {
        "title_en": "Spiritual Immersion in the Himalayas & Sacred Valleys",
        "duration_en": "12 Days",
        "group_size_en": "Small group 4 to 8 explorers",
        "badge_en": "🏔️ Himalayas, Mustang & Spirituality",
        "overview_en": "A transformative, meditative journey connecting with the deep sacred roots of Nepal. Discover Tibetan Buddhist monasteries, sacred Hindu cremation ghats at Pashupatinath, meditation caves, and peaceful high-altitude Himalayan retreats.",
        "highlights_en": [
            "Privileged meetings and teachings with Tibetan Buddhist lamas and Hindu yogis",
            "Dawn meditation sessions facing the snowcapped peaks of the Himalayas",
            "Pilgrimages to sacred sites: Boudhanath, Swayambhunath, Namo Buddha, and Lumbini",
            "Peaceful, serene rhythm fostering self-reflection and authentic connections"
        ]
    },
    "panthere-des-neiges": {
        "title_en": "Exclusive Snow Leopard Expedition (17 Days)",
        "duration_en": "17 Days",
        "group_size_en": "Small group 4 to 8 explorers",
        "badge_en": "🏔️ Himalayas, Mustang & Spirituality",
        "overview_en": "Embark on an extraordinary 17-day expedition tracking the most elusive and legendary big cat on Earth: the Snow Leopard ('Ghost of the Mountains'). High in the remote wilderness of Manang (3,600m – 4,500m) and the Annapurnas, experience 9 full field days of intensive tracking alongside expert Himalayan trackers, progressive altitude acclimatization, and ancient Buddhist heritage at the 600-year-old Braka Gompa monastery.",
        "highlights_en": [
            "9 full days in the field dedicated to tracking and observing the Snow Leopard",
            "Elite tracking with native Himalayan trackers and professional spotting scopes",
            "Safe stepwise altitude acclimatization (Chame 2,700m, Manang 3,600m, Gangapurna lake)",
            "Rich cultural discovery in Bhaktapur, Bandipur and the 600-year-old Braka Gompa monastery",
            "Panoramic flight over the Annapurna range and relaxing natural hot springs"
        ]
    }
}

# Update src/data/tours.json
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

for t in tours:
    slug = t.get('slug')
    if slug in en_tour_translations:
        trans = en_tour_translations[slug]
        t['title_en'] = trans['title_en']
        t['duration_en'] = trans['duration_en']
        t['group_size_en'] = trans['group_size_en']
        t['badge_en'] = trans['badge_en']
        t['overview_en'] = trans['overview_en']
        t['highlights_en'] = trans['highlights_en']

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'w', encoding='utf-8') as f:
    json.dump(tours, f, indent=2, ensure_ascii=False)

print("Updated src/data/tours.json with complete 100% English translations for all 15 tours!")
