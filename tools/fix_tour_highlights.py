#!/usr/bin/env python3
import json
import glob
import re

tour_highlights = {
    "tiji-mustang": {
        "fr": [
            "3 journées d'immersion totale au cœur du festival sacré de Tiji dans la cité fortifiée de Lo Manthang.",
            "Découverte des danses rituelles masquées des lamas et des cérémonies ancestrales tibétaines.",
            "Exploration des paysages minéraux du Haut Mustang, des falaises ocre et des grottes troglodytiques millénaires.",
            "Visite des monastères historiques de Kagbeni, Tsarang et de la vallée secrète de Chhoser."
        ],
        "en": [
            "3 full days of immersion in the sacred Tiji Festival inside the walled kingdom of Lo Manthang.",
            "Witness the masked ritual dances of Tibetan lamas and ancient spiritual ceremonies.",
            "Exploration of Upper Mustang's stark mineral canyons, ochre cliffs, and centuries-old sky caves.",
            "Visits to legendary monasteries in Kagbeni, Tsarang, and the secluded Chhoser cave valley."
        ]
    },
    "immersion-spirituelle": {
        "fr": [
            "Retraite spirituelle et ressourcement guidés par Justine Luçon entre ashram et montagnes sacrées.",
            "Pratiques quotidiennes de yoga, méditation guidée, respirations conscientes et journée de silence.",
            "Cérémonie de crémation et dévotion à Pashupatinath, et circumambulation au grand Stupa de Boudhanath.",
            "Séjour contemplatif face aux géants des Annapurnas et rituels de paix au bord du lac de Pokhara."
        ],
        "en": [
            "Spiritual retreat and inner wellness guided by Justine Luçon amidst sacred Himalayan ashrams and foothills.",
            "Daily yoga sessions, guided mindfulness meditations, breathwork, and a dedicated day of silence.",
            "Devotional rituals at sacred Pashupatinath and circumambulation around Boudhanath Great Stupa.",
            "Contemplative stay facing the Annapurna range and peaceful lakeside rituals in Pokhara."
        ]
    },
    "carnet-de-voyage": {
        "fr": [
            "Ateliers quotidiens d'aquarelle, de croquis sur le vif et d'écriture nomade avec artistes accompagnateurs.",
            "Croquis des palais royaux médiévaux et ruelles pavées de Bhaktapur et Bandipur.",
            "Immersion artistique dans le village de montagne de Ghachok face aux sommets des Annapurnas.",
            "Rencontres authentiques avec les artisans locaux et composition d'un carnet de voyage unique et personnalisé."
        ],
        "en": [
            "Daily watercolor sketching, urban drawing, and creative journaling guided by field artists.",
            "Sketching sessions in the medieval royal palaces and cobblestone lanes of Bhaktapur and Bandipur.",
            "Artistic village stay in Ghachok overlooking the majestic Annapurna mountain panorama.",
            "Intimate cultural exchanges with local craftspeople and creation of a personalized Nepal travel journal."
        ]
    },
    "dashain-immersion-culturelle": {
        "fr": [
            "Partage exclusif des célébrations sacrées de Dashain (Vijaya Dashami) en immersion familiale chez les Tharu.",
            "Cérémonies des bénédictions (Tika & Jamara) et danses traditionnelles au cœur des villages.",
            "4 jours de safaris à pied et en jeep dans le parc national de Bardia avec nos maîtres pisteurs.",
            "Panorama grandiose sur les Annapurnas depuis les balcons de Ghachok et découverte des cités royales."
        ],
        "en": [
            "Exclusive participation in sacred Dashain festivities (Vijaya Dashami) hosted by native Tharu families.",
            "Traditional Tika & Jamara blessings and cultural folk dances in authentic village communities.",
            "4 full days of walking tracking and jeep safaris in Bardia National Park with master trackers.",
            "Sweeping Annapurna mountain panoramas from Ghachok and exploration of Kathmandu's royal heritage."
        ]
    },
    "rafting-safari": {
        "fr": [
            "Descente sportive en rafting sur les eaux cristallines de la rivière Bheri à travers des gorges sauvages.",
            "Randonnée et exploration de l'unique réserve de faune de Dhorpatan à la recherche du Grand Bharal (Mouton bleu).",
            "Immersion authentique dans les villages traditionnels Magar préservés du tourisme de masse.",
            "Safaris animaliers et campements le long des rivières sauvages de l'ouest népalais."
        ],
        "en": [
            "Whitewater rafting expedition along the pristine rapids and wilderness gorges of the Bheri River.",
            "Trekking in Nepal's only hunting and wildlife reserve at Dhorpatan to spot Blue Sheep (Bharal).",
            "Authentic cultural stays in remote Magar tribal villages completely untouched by mass tourism.",
            "Wildlife foot tracking and wilderness riverside camps across western Nepal."
        ]
    },
    "rara-lake-bardia": {
        "fr": [
            "Grande expédition en 4x4 tout-terrain à travers les pistes escarpées du Moyen-Ouest népalais.",
            "Découverte du spectaculaire lac Rara, le plus grand et plus pur joyau lacustre d'altitude du Népal (3 000 m).",
            "Randonnées sauvages à travers les forêts de pins bleus et de genévriers du parc national de Rara.",
            "Safaris complets à pied et en jeep dans la jungle de Bardia sur les traces des tigres et éléphants."
        ],
        "en": [
            "Overland 4x4 expedition across the rugged wilderness trails of western Nepal.",
            "Discovery of legendary Rara Lake, Nepal's largest and most pristine high-altitude lake (3,000m).",
            "Wild alpine hikes through fragrant blue pine and juniper forests within Rara National Park.",
            "Complete walking safaris and 4x4 tracking in Bardia National Park for wild tigers and elephants."
        ]
    },
    "bardia-explorateur": {
        "fr": [
            "3 journées intensives d'observation de la faune sauvage dans le parc le plus préservé du Népal.",
            "Combinaison complète : safaris à pied silencieux, journée en jeep 4x4 et safari flottant sur la rivière.",
            "Pistage du tigre du Bengale, du rhinocéros unicorne et des troupeaux d'éléphants sauvages.",
            "Hébergement en écolodge de charme et immersion chaleureuse dans la culture traditionnelle Tharu."
        ],
        "en": [
            "3 intensive days of wildlife exploration in Nepal's most pristine national park.",
            "Complete safari mix: silent foot tracking, full-day 4x4 jeep drive, and floating river safari.",
            "Tracking Bengal tigers, Greater One-Horned rhinos, and wild Asian elephant herds.",
            "Authentic boutique ecolodge stay with warm cultural evenings among native Tharu hosts."
        ]
    },
    "chitwan-culture": {
        "fr": [
            "Safari en jeep au cœur de la forêt subtropicale à la recherche des rhinocéros unicornes et cervidés.",
            "Descente silencieuse en pirogue traditionnelle sur la rivière Rapti pour observer gavials et oiseaux aquatiques.",
            "Immersion culturelle chez les villageois Tharu avec danses traditionnelles des bâtons (Tharu Stick Dance).",
            "Safari à pied matinal accompagné d'un guide naturaliste certifié."
        ],
        "en": [
            "Subtropical jungle 4x4 safari targeting Greater One-Horned Rhinos, wild boars, and deer.",
            "Silent wooden canoe drift on the Rapti River observing fish-eating Gharials and exotic birds.",
            "Cultural immersion in Tharu villages with traditional evening Stick Dance performances.",
            "Early morning guided jungle walking safari with certified local naturalists."
        ]
    },
    "bardia-nuit-sauvage": {
        "fr": [
            "Nuit exclusive en bivouac sauvage sous les étoiles au cœur du parc national de Bardia.",
            "Écoute nocturne des bruits de la jungle, rugissements de tigres et cris d'alarme autour du feu de camp.",
            "Safaris en jeep tout-terrain et marches d'approche à l'aube et au crépuscule.",
            "Encadrement d'élite par deux maîtres pisteurs natifs assurant discrétion et sécurité totale."
        ],
        "en": [
            "Exclusive wilderness bush camp night under starry skies deep inside Bardia National Park.",
            "Nighttime jungle acoustic tracking listening to tiger calls, alarm barks, and river murmurs around the campfire.",
            "4x4 jeep safari and dawn/dusk stalking on foot with native trackers.",
            "Expert safety supervision by two seasoned Tharu trackers."
        ]
    },
    "bardia-babai-camping": {
        "fr": [
            "Expédition exclusive dans la secrète et inaccessible vallée de Babai, sanctuaire vierge de Bardia.",
            "4 jours de camping sauvage en bivouac le long des méandres sauvages de la rivière Babai.",
            "Pistage à pied des tigres du Bengale, léopards, ours lippus et troupeaux d'éléphants sauvages.",
            "Remontée des corridors fluviaux en bateau et observation privilégiée des crocodiles gavials."
        ],
        "en": [
            "Exclusive expedition into the secluded, pristine Babai Valley in the depths of Bardia.",
            "4 days of wild bush camping along the untamed meandering channels of the Babai River.",
            "Foot tracking Bengal tigers, leopards, sloth bears, and wild elephant herds.",
            "River navigation along wildlife corridors with exceptional sightings of rare Gharials."
        ]
    },
    "babai-special": {
        "fr": [
            "Immersion profonde dans la vallée isolée de Babai, loin des circuits touristiques classiques.",
            "Safaris combinés : navigation silencieuse sur la rivière, marches en forêt et exploration en 4x4.",
            "Affûts stratégiques sur les berges et points d'eau fréquentés par les grands félins.",
            "Soirée de partage et découverte des traditions locales avec la communauté Tharu de Bardia."
        ],
        "en": [
            "Deep wilderness immersion into the secluded Babai Valley, far off conventional tourist tracks.",
            "Multi-modal safaris: silent river drifting, foot tracking in dense sal forests, and 4x4 drives.",
            "Strategic waterhole and riverbank hides for prime predator viewing.",
            "Evening cultural exchanges and traditional hospitality with native Tharu communities."
        ]
    },
    "nepal-immersion-totale": {
        "fr": [
            "Les plus beaux trésors du Népal en un seul voyage : cités royales de Katmandou, Patan et Bhaktapur.",
            "Lever de soleil spectaculaire sur la chaîne himalayenne depuis Nagarkot et balade à Pokhara.",
            "Descente en rafting sur la rivière Trishuli et découverte de la jungle de Chitwan en jeep et pirogue.",
            "Pèlerinage sacré à Lumbini, lieu de naissance historique de Siddhartha Gautama Bouddha."
        ],
        "en": [
            "Nepal's finest treasures in one seamless journey: royal squares of Kathmandu, Patan, and Bhaktapur.",
            "Spectacular Himalayan sunrise from Nagarkot and leisure stay beside Pokhara's Lake Phewa.",
            "Thrilling whitewater rafting on the Trishuli River and Chitwan jungle safaris by jeep and canoe.",
            "Sacred visit to Lumbini, the UNESCO-listed birthplace of Gautama Buddha."
        ]
    },
    "nepal-sauvage": {
        "fr": [
            "La grande traversée du Népal reliant les sommets sacrés de l'Himalaya aux jungles tropicales du Teraï.",
            "3 jours d'immersion totale et safaris à pied dans le parc national de Bardia avec nos pisteurs.",
            "Séjour reposant et contemplatif dans le village traditionnel de Ghachok au pied des Annapurnas.",
            "Découvertes culturelles et spirituelles majeures à Lumbini, Katmandou et Bhaktapur."
        ],
        "en": [
            "Cross-country journey connecting the sacred Himalayan peaks to the tropical wilderness of the Terai.",
            "3 full days of foot tracking and deep wilderness exploration in Bardia National Park.",
            "Peaceful cultural stay in the authentic mountain village of Ghachok beneath the Annapurna massif.",
            "Major spiritual and historic discoveries in Lumbini, Kathmandu, and medieval Bhaktapur."
        ]
    },
    "chitwan-bardia-complete": {
        "fr": [
            "Le grand combiné des deux parcs emblématiques du Népal : la luxuriance de Chitwan et la sauvagerie de Bardia.",
            "Safaris diversifiés : jeeps 4x4, marches silencieuses en jungle, canoë sur la Rapti et affûts fluviaux.",
            "Bivouac sauvage immersif dans la vallée secrète de Babai au cœur du territoire des tigres.",
            "Observation des rhinocéros unicornes, tigres du Bengale, éléphants et dauphins du Gange."
        ],
        "en": [
            "The ultimate dual-sanctuary expedition: subtropical Chitwan paired with untamed Bardia.",
            "Diverse safari activities: 4x4 jeep drives, silent jungle tracking, canoeing, and river hides.",
            "Overnight wild bush camping in the remote Babai Valley deep within tiger territory.",
            "Encounters with Greater One-Horned rhinos, Bengal tigers, wild elephants, and Gangetic dolphins."
        ]
    },
    "jungle-extreme": {
        "fr": [
            "Le circuit de référence pour les passionnés de grands prédateurs et photographes animaliers.",
            "5 journées complètes de pistage intensif à pied dans le parc national de Bardia avec Pawan et Kiran.",
            "Affûts matinaux et vespéraux prolongés au ras du sol sur les points d'eau et berges de la Geruwa.",
            "Exploration complémentaire des vastes prairies et forêts du parc national de Suklaphanta."
        ],
        "en": [
            "The premier expedition for dedicated wildlife photographers and apex predator enthusiasts.",
            "5 full days of intensive foot tracking in Bardia National Park with master trackers Pawan & Kiran.",
            "Dawn-to-dusk ground-level hides along waterholes and Geruwa River sandbanks.",
            "Additional wildlife exploration across the open savannas and marshes of Suklaphanta National Park."
        ]
    },
    "panthere-des-neiges": {
        "fr": [
            "9 journées complètes de prospection et d'affût en haute altitude dans la vallée isolée de Manang (3 600 m - 4 700 m).",
            "Pistage d'élite avec nos repéreurs himalayens natifs et matériel optique professionnel (longues-vues Swarovski).",
            "Acclimatation progressive et sécurisée le long du mythique sentier des Annapurnas.",
            "Découverte des monastères tibétains séculaires de Braka Gompa et de la culture bouddhiste des hautes vallées."
        ],
        "en": [
            "9 dedicated days of high-altitude spotting and hides in the remote Manang Valley (3,600m - 4,700m).",
            "Elite tracking with native Himalayan spotters using professional high-end spotting scopes.",
            "Safe, gradual acclimatization program along the legendary Annapurna trail.",
            "Visits to ancient 600-year-old Tibetan monasteries like Braka Gompa and Himalayan cultural immersion."
        ]
    }
}

# 1. Update src/data/tours.json
with open("src/data/tours.json", "r", encoding="utf-8") as f:
    tours_fr = json.load(f)

for t in tours_fr:
    slug = t.get("slug")
    if slug in tour_highlights:
        t["highlights"] = tour_highlights[slug]["fr"]

with open("src/data/tours.json", "w", encoding="utf-8") as f:
    json.dump(tours_fr, f, ensure_ascii=False, indent=2)

print("Updated src/data/tours.json")

# 2. Update src/data/tours.en.json
with open("src/data/tours.en.json", "r", encoding="utf-8") as f:
    tours_en = json.load(f)

for t in tours_en:
    slug = t.get("slug")
    if slug in tour_highlights:
        t["highlights"] = tour_highlights[slug]["en"]

with open("src/data/tours.en.json", "w", encoding="utf-8") as f:
    json.dump(tours_en, f, ensure_ascii=False, indent=2)

print("Updated src/data/tours.en.json")

# 3. Update all src/pages/tours/*.astro files
for slug, data in tour_highlights.items():
    fr_file = f"src/pages/tours/{slug}.astro"
    if glob.glob(fr_file):
        with open(fr_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Build list items
        new_items = "".join([
            f'<li class="flex items-start gap-3"><span class="w-2 h-2 rounded-full bg-[#0e8354] mt-2 shrink-0"></span><span>{item}</span></li>'
            for item in data["fr"]
        ])
        
        # Replace between <ul class="space-y-3 ..."> and </ul> inside the highlights box
        pattern = r'(<h3[^>]*>.*?Les temps forts du voyage.*?</h3>\s*<ul[^>]*>).*?(</ul>)'
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, rf'\g<1>{new_items}\g<2>', content, flags=re.DOTALL)
            with open(fr_file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Patched FR Astro: {fr_file}")
        else:
            print(f"Warning: pattern not found in {fr_file}")

# 4. Update all src/pages/en/tours/*.astro files
for slug, data in tour_highlights.items():
    en_file = f"src/pages/en/tours/{slug}.astro"
    if glob.glob(en_file):
        with open(en_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_items = "".join([
            f'<li class="flex items-start gap-3"><span class="w-2 h-2 rounded-full bg-[#0e8354] mt-2 shrink-0"></span><span>{item}</span></li>'
            for item in data["en"]
        ])
        
        pattern = r'(<h3[^>]*>.*?Trip Highlights.*?</h3>\s*<ul[^>]*>).*?(</ul>)'
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, rf'\g<1>{new_items}\g<2>', content, flags=re.DOTALL)
            with open(en_file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Patched EN Astro: {en_file}")
        else:
            print(f"Warning: pattern not found in {en_file}")

print("All tour highlights fixed and synchronized!")
