#!/usr/bin/env python3
"""
Curate Wildlife Gallery: Eliminates all photo duplicates, near-clones, and repetitive shots
across both French and English homepages. Injects 13 brand new authentic wildlife species
from Robin's high-res expeditions in Bardia and Chitwan.
"""

import os
import re
import json
from PIL import Image

BASE_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'

REPLACEMENTS_FR = {
    22: {
        'file': '/assets/drive_wildlife/2026-05-08_-_0000273923_-_Sur_les_traces_du_Tigre.webp',
        'title': 'Sur les traces du Tigre',
        'desc': 'Empreinte fraîche géante de Tigre du Bengale découverte lors du pistage à pied',
        'location': 'Pistage en jungle • Bardia',
        'category': 'felins',
        'alt': "Empreinte fraîche géante de Tigre du Bengale lors d'un pistage à pied - Parc national de Bardia"
    },
    26: {
        'file': '/assets/drive_wildlife/Pygargue___t_te_grise_1.webp',
        'title': 'Pygargue à tête grise',
        'desc': 'Grand rapace pêcheur veillant sur les courants tumultueux de la Karnali',
        'location': 'Rivière Karnali • Bardia',
        'category': 'oiseaux',
        'alt': 'Pygargue à tête grise en vigie au-dessus des eaux - Parc national de Bardia'
    },
    33: {
        'file': '/assets/drive_wildlife/Guepier_orient_1.webp',
        'title': "Guêpier d'Orient",
        'desc': 'Oiseau émeraude aux teintes dorées capturant des insectes en plein vol',
        'location': 'Plaines de Bardia',
        'category': 'oiseaux',
        'alt': "Guêpier d'Orient aux couleurs chatoyantes - Plaines sauvages de Bardia"
    },
    40: {
        'file': '/assets/drive_wildlife/Martin-chasseur_gurial_1.webp',
        'title': 'Martin-chasseur gurial',
        'desc': "Le géant des martins-pêcheurs d'Asie au bec rouge corail spectaculaire",
        'location': 'Zones humides de Chitwan',
        'category': 'oiseaux',
        'alt': 'Martin-chasseur gurial (Stork-billed Kingfisher) - Parc national de Chitwan'
    },
    43: {
        'file': '/assets/drive_wildlife/2026-05-05_-_0000272847_-_Rhinoc_ros_indien_sur_la_piste.webp',
        'title': 'Rhinocéros indien sur la piste',
        'desc': "Colosse préhistorique croisé au détour d'un sentier forestier au petit matin",
        'location': 'Pistes de Chitwan',
        'category': 'mammiferes',
        'alt': 'Grand Rhinocéros unicorne sur une piste forestière - Parc national de Chitwan'
    },
    52: {
        'file': '/assets/drive_wildlife/Drongo___raquettes_1.webp',
        'title': 'Drongo à raquettes',
        'desc': 'Passereau acrobate noir corbeau paré de deux spectaculaires raquettes caudales',
        'location': 'Forêts de Sal • Bardia',
        'category': 'oiseaux',
        'alt': 'Drongo à raquettes dans les arbres de Sal - Parc national de Bardia'
    },
    57: {
        'file': '/assets/drive_wildlife/Francolin_1.webp',
        'title': 'Francolin noir (Black Francolin)',
        'desc': 'Oiseau terrestre au plumage cryptique arpentant les clairières herbeuses',
        'location': 'Savanes de Suklaphanta',
        'category': 'oiseaux',
        'alt': 'Francolin noir dans les herbes dorées - Parc national de Suklaphanta'
    },
    59: {
        'file': '/assets/drive_wildlife/Tisserin_baya_5.webp',
        'title': 'Tisserin baya (Baya Weaver)',
        'desc': 'Maître bâtisseur réputé pour ses nids suspendus tressés en fibres végétales',
        'location': 'Plaines du Terai',
        'category': 'oiseaux',
        'alt': 'Tisserin baya et ses nids suspendus - Plaines du Terai'
    },
    66: {
        'file': '/assets/drive_wildlife/Vanneau_indien_1.webp',
        'title': 'Vanneau indien (Red-wattled Lapwing)',
        'desc': 'Échassier vif sentinelle des berges au caroncule rouge et cri retentissant',
        'location': 'Berges de Bardia',
        'category': 'oiseaux',
        'alt': 'Vanneau indien sur les galets de rivière - Parc national de Bardia'
    },
    69: {
        'file': '/assets/drive_wildlife/Percnopt_re_1.webp',
        'title': "Percnoptère d'Égypte (Egyptian Vulture)",
        'desc': "Vautour rare à face jaune d'or planant au-dessus des savanes ouvertes",
        'location': 'Plaines de Suklaphanta & Bardia',
        'category': 'oiseaux',
        'alt': "Percnoptère d'Égypte en vol au-dessus du Terai"
    },
    70: {
        'file': '/assets/drive_wildlife/Shama___croupion_blanc_1.webp',
        'title': 'Shama à croupion blanc',
        'desc': 'Chanteur exceptionnel aux mélodies cristallines dissimulé dans les sous-bois',
        'location': 'Forêt primaire de Bardia',
        'category': 'oiseaux',
        'alt': 'Shama à croupion blanc en sous-bois - Parc national de Bardia'
    },
    72: {
        'file': '/assets/drive_wildlife/Cigone_episcopale_1.webp',
        'title': 'Cigogne épiscopale (Woolly-necked Stork)',
        'desc': 'Échassier majestueux au cou de duvet blanc immaculé arpentant les zones humides',
        'location': 'Plaines inondables de Bardia',
        'category': 'oiseaux',
        'alt': 'Cigogne épiscopale dans les marais - Parc national de Bardia'
    },
    73: {
        'file': '/assets/drive_wildlife/Coucal_ruffin_1.webp',
        'title': 'Coucal ruffon (Lesser Coucal)',
        'desc': 'Oiseau furtif aux ailes cuivrées glissant avec agilité dans les herbes à éléphant',
        'location': 'Savanes de Chitwan',
        'category': 'oiseaux',
        'alt': 'Coucal ruffon dans la végétation dense - Parc national de Chitwan'
    }
}

REPLACEMENTS_EN = {
    22: {
        'file': '/assets/drive_wildlife/2026-05-08_-_0000273923_-_Sur_les_traces_du_Tigre.webp',
        'title': 'Tracking the Bengal Tiger',
        'desc': 'Fresh giant tiger pugmark discovered during foot tracking in the primary jungle',
        'location': 'Jungle Tracking • Bardia',
        'category': 'felins',
        'alt': 'Fresh Bengal Tiger pugmark during jungle tracking - Bardia National Park'
    },
    26: {
        'file': '/assets/drive_wildlife/Pygargue___t_te_grise_1.webp',
        'title': 'Grey-headed Fish Eagle',
        'desc': 'Majestic fishing raptor keeping watch over the rushing Karnali currents',
        'location': 'Karnali River • Bardia',
        'category': 'oiseaux',
        'alt': 'Grey-headed Fish Eagle perched above Karnali River - Bardia National Park'
    },
    33: {
        'file': '/assets/drive_wildlife/Guepier_orient_1.webp',
        'title': 'Asian Green Bee-eater',
        'desc': 'Glittering emerald plumage catching flying insects in mid-air',
        'location': 'Bardia Plains',
        'category': 'oiseaux',
        'alt': 'Asian Green Bee-eater on branch - Bardia Plains'
    },
    40: {
        'file': '/assets/drive_wildlife/Martin-chasseur_gurial_1.webp',
        'title': 'Stork-billed Kingfisher',
        'desc': "Asia's largest kingfisher sporting a massive coral-red dagger bill",
        'location': 'Chitwan Wetlands',
        'category': 'oiseaux',
        'alt': 'Stork-billed Kingfisher perched above waters - Chitwan National Park'
    },
    43: {
        'file': '/assets/drive_wildlife/2026-05-05_-_0000272847_-_Rhinoc_ros_indien_sur_la_piste.webp',
        'title': 'Indian Rhino on Forest Track',
        'desc': 'Prehistoric armored giant met along a quiet jungle trail in the morning mist',
        'location': 'Chitwan Forest Trails',
        'category': 'mammiferes',
        'alt': 'Greater One-horned Rhinoceros on jungle path - Chitwan National Park'
    },
    52: {
        'file': '/assets/drive_wildlife/Drongo___raquettes_1.webp',
        'title': 'Racket-tailed Drongo',
        'desc': 'Acrobatic glossy black songbird boasting twin extended paddle tail streamers',
        'location': 'Sal Forests • Bardia',
        'category': 'oiseaux',
        'alt': 'Greater Racket-tailed Drongo in canopy - Bardia National Park'
    },
    57: {
        'file': '/assets/drive_wildlife/Francolin_1.webp',
        'title': 'Black Francolin',
        'desc': 'Cryptic terrestrial gamebird striding through golden grassland clearings',
        'location': 'Suklaphanta Grasslands',
        'category': 'oiseaux',
        'alt': 'Black Francolin in native savanna - Suklaphanta National Park'
    },
    59: {
        'file': '/assets/drive_wildlife/Tisserin_baya_5.webp',
        'title': 'Baya Weaver',
        'desc': 'Master avian architect famed for intricately woven pendulous hanging nests',
        'location': 'Terai Plains',
        'category': 'oiseaux',
        'alt': 'Baya Weaver at woven nest - Terai Plains'
    },
    66: {
        'file': '/assets/drive_wildlife/Vanneau_indien_1.webp',
        'title': 'Red-wattled Lapwing',
        'desc': 'Alert shoreline sentinel with vivid scarlet wattles and resounding alarm calls',
        'location': 'Bardia Riverbanks',
        'category': 'oiseaux',
        'alt': 'Red-wattled Lapwing along river gravel - Bardia National Park'
    },
    69: {
        'file': '/assets/drive_wildlife/Percnopt_re_1.webp',
        'title': 'Egyptian Vulture',
        'desc': 'Endangered pale vulture with vivid golden-yellow facial skin soaring over open savanna',
        'location': 'Suklaphanta & Bardia Plains',
        'category': 'oiseaux',
        'alt': 'Egyptian Vulture soaring over Terai plains'
    },
    70: {
        'file': '/assets/drive_wildlife/Shama___croupion_blanc_1.webp',
        'title': 'White-rumped Shama',
        'desc': 'Renowned virtuoso songbird with stepped tail perched in shadowed forest thickets',
        'location': 'Primary Bardia Forest',
        'category': 'oiseaux',
        'alt': 'White-rumped Shama in dense undergrowth - Bardia National Park'
    },
    72: {
        'file': '/assets/drive_wildlife/Cigone_episcopale_1.webp',
        'title': 'Woolly-necked Stork',
        'desc': 'Stately wetland wader with downy snow-white neck pacing the marshes',
        'location': 'Bardia Floodplains',
        'category': 'oiseaux',
        'alt': 'Woolly-necked Stork in natural marsh - Bardia National Park'
    },
    73: {
        'file': '/assets/drive_wildlife/Coucal_ruffin_1.webp',
        'title': 'Lesser Coucal',
        'desc': 'Secretive copper-winged bird weaving smoothly through dense elephant grass',
        'location': 'Chitwan Grasslands',
        'category': 'oiseaux',
        'alt': 'Lesser Coucal in tall grass - Chitwan National Park'
    }
}

def get_image_info(rel_path):
    p = os.path.join(BASE_DIR, 'public', rel_path.lstrip('/'))
    if not os.path.exists(p):
        raise FileNotFoundError(f"Image not found: {p}")
    im = Image.open(p)
    w, h = im.size
    aspect = h / w
    return w, h, aspect

def build_card_html(idx, meta):
    w, h, aspect = get_image_info(meta['file'])
    return f'''        <div class="wildlife-card break-inside-avoid mb-6 relative rounded-3xl overflow-hidden group cursor-pointer border border-white/10 shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:border-emerald-800/50 hover:shadow-[0_20px_50px_rgba(14,131,84,0.25)] transition-all duration-300 bg-slate-900" data-category="{meta['category']}" data-idx="{idx}" onclick="openWildlifeLightbox({idx})">
          <img 
            src="{meta['file']}" 
            alt="{meta['alt']}" 
            width="{w}"
            height="{h}"
            style="aspect-ratio: {w}/{h};"
            class="w-full h-auto block filter brightness-95 group-hover:brightness-105 transition-all duration-300" loading="lazy"
            decoding="async"
          />
          <div class="absolute top-3.5 left-3.5 z-10 pointer-events-none">
            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md border border-white/20 text-[11px] font-black text-amber-100 shadow-md">
              <span>{meta['location']}</span>
            </span>
          </div>
          <div class="absolute bottom-3.5 left-3.5 right-3.5 z-10 p-3.5 rounded-2xl bg-slate-950/90 backdrop-blur-xl border border-white/15 text-white opacity-0 translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-300 shadow-2xl pointer-events-none">
            <div class="flex items-center justify-between gap-3">
              <div class="min-w-0 flex-1">
                <h3 class="font-black text-sm sm:text-base text-white group-hover:text-amber-100 transition-colors leading-tight truncate">
                  {meta['title']}
                </h3>
                <p class="text-xs text-slate-300 mt-0.5 font-medium truncate">
                  {meta['desc']}
                </p>
              </div>
              <div class="w-8 h-8 rounded-xl bg-white/10 text-slate-200 flex items-center justify-center shrink-0 border border-white/10">
                <svg class="w-4 h-4 text-slate-200" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"></path></svg>
              </div>
            </div>
          </div>
        </div>'''

def process_file(rel_path, replacements, is_en=False):
    filepath = os.path.join(BASE_DIR, rel_path)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract wildlifeData
    m = re.search(r'window\.wildlifeData\s*=\s*(\[.*?\]);', content, re.DOTALL)
    if not m:
        raise ValueError(f"wildlifeData not found in {rel_path}")

    data = json.loads(m.group(1))
    print(f"[{rel_path}] Found {len(data)} items in wildlifeData")

    # Replace in wildlifeData
    for idx, meta in replacements.items():
        w, h, aspect = get_image_info(meta['file'])
        data[idx] = {
            'file': meta['file'],
            'title': meta['title'],
            'desc': meta['desc'],
            'location': meta['location'],
            'category': meta['category'],
            'aspect': aspect
        }

    # Replace each card in HTML
    for idx, meta in replacements.items():
        pattern = re.compile(
            rf'<div class="wildlife-card[^"]*"[^>]*data-idx="{idx}"[^>]*>.*?</div>\s*</div>\s*</div>\s*</div>',
            re.DOTALL
        )
        card_match = pattern.search(content)
        if not card_match:
            # Try alternate pattern if closing tags differ
            pattern = re.compile(
                rf'<div class="wildlife-card[^"]*"[^>]*data-idx="{idx}".*?</div>\s*</div>\s*</div>\s*</div>',
                re.DOTALL
            )
            card_match = pattern.search(content)

        if not card_match:
            print(f"⚠️ Warning: could not find card with data-idx='{idx}' in {rel_path}")
        else:
            new_card_html = build_card_html(idx, meta)
            content = content[:card_match.start()] + new_card_html + content[card_match.end():]
            print(f"  ✓ Replaced card #{idx+1} ({meta['title']})")

    # Update wildlifeData in script dynamically with re.sub
    new_json = json.dumps(data, ensure_ascii=False)
    content, count_sub = re.subn(
        r'window\.wildlifeData\s*=\s*\[.*?\];',
        f'window.wildlifeData = {new_json};',
        content,
        count=1,
        flags=re.DOTALL
    )
    assert count_sub == 1, f"Failed to update window.wildlifeData in {rel_path}"

    # Update tab counts
    # Big Cats (9), Large Mammals (20), Rare Birds (37), Reptiles & Rivers (9)
    if not is_en:
        content = re.sub(r'Grands félins \(\d+\)', 'Grands félins (9)', content)
        content = re.sub(r'Grands mammifères \(\d+\)', 'Grands mammifères (20)', content)
        content = re.sub(r'Oiseaux rares \(\d+\)', 'Oiseaux rares (37)', content)
        content = re.sub(r'Reptiles et rivières \(\d+\)', 'Reptiles et rivières (9)', content)
    else:
        content = re.sub(r'Big Cats \(\d+\)', 'Big Cats (9)', content)
        content = re.sub(r'Large Mammals \(\d+\)', 'Large Mammals (20)', content)
        content = re.sub(r'Rare Birds \(\d+\)', 'Rare Birds (37)', content)
        content = re.sub(r'Reptiles & Rivers \(\d+\)', 'Reptiles & Rivers (9)', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Successfully updated {rel_path}!")

if __name__ == '__main__':
    print("=== Curating French Homepage Gallery ===")
    process_file('src/pages/index.astro', REPLACEMENTS_FR, is_en=False)
    print("\n=== Curating English Homepage Gallery ===")
    process_file('src/pages/en/index.astro', REPLACEMENTS_EN, is_en=True)
