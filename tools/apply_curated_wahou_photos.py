import json, re, glob

# Master curated database combining the best of original site + Google Drive photos
curated_tours = {
    "bardia-explorateur": {
        "main": "/assets/original_site/tigre_bardia.png",
        "gallery": [
            "/assets/original_site/tigre_bardia.png",
            "/assets/drive_photos/julien_safari_a_pied.jpg",
            "/assets/drive_photos/adrien_bardia_forest.jpg",
            "/assets/original_site/safari_pied.png"
        ]
    },
    "chitwan-culture": {
        "main": "/assets/original_site/chitwan_rhino.png",
        "gallery": [
            "/assets/original_site/chitwan_rhino.png",
            "/assets/original_site/elephants_river.jpg",
            "/assets/drive_photos/julien_elephant_mere_petit.jpg",
            "/assets/drive_photos/adrien_bhaktapur1.jpg"
        ]
    },
    "rafting-safari": {
        "main": "/assets/original_site/rafting_wild.jpg",
        "gallery": [
            "/assets/original_site/rafting_wild.jpg",
            "/assets/drive_photos/julien_gangetic_dolphin.jpg",
            "/assets/drive_photos/adrien_bardia_river.jpg",
            "/assets/drive_photos/adrien_bardia_sunset.jpg"
        ]
    },
    "bardia-nuit-sauvage": {
        "main": "/assets/original_site/bivouac_camp.png",
        "gallery": [
            "/assets/original_site/bivouac_camp.png",
            "/assets/drive_photos/adrien_bardia_camp.jpg",
            "/assets/drive_photos/julien_photographes_jungle.jpg",
            "/assets/original_site/tigre_route.png"
        ]
    },
    "rara-lake-bardia": {
        "main": "/assets/drive_photos/fred_wild2.jpg",
        "gallery": [
            "/assets/drive_photos/fred_wild2.jpg",
            "/assets/original_site/tigre_water.jpg",
            "/assets/drive_photos/antoine_wild3.jpg",
            "/assets/drive_photos/fred_wild5.jpg"
        ]
    },
    "bardia-babai-camping": {
        "main": "/assets/original_site/babai_walk.png",
        "gallery": [
            "/assets/original_site/babai_walk.png",
            "/assets/drive_photos/julien_elephant_mere_petit.jpg",
            "/assets/drive_photos/adrien_tigre4.jpg",
            "/assets/original_site/bivouac_camp.png"
        ]
    },
    "nepal-immersion-totale": {
        "main": "/assets/drive_photos/adrien_bhaktapur2.jpg",
        "gallery": [
            "/assets/drive_photos/adrien_bhaktapur2.jpg",
            "/assets/original_site/tigre_bardia.png",
            "/assets/original_site/chitwan_rhino.png",
            "/assets/original_site/machapuchare.png"
        ]
    },
    "babai-special": {
        "main": "/assets/original_site/elephant_bardia.png",
        "gallery": [
            "/assets/original_site/elephant_bardia.png",
            "/assets/drive_photos/adrien_tigre2.jpg",
            "/assets/drive_photos/julien_elephant_jungle.jpg",
            "/assets/drive_photos/adrien_bardia_sunset.jpg"
        ]
    },
    "chitwan-bardia-complete": {
        "main": "/assets/drive_photos/julien_tigre_bengale2.jpg",
        "gallery": [
            "/assets/drive_photos/julien_tigre_bengale2.jpg",
            "/assets/original_site/chitwan_rhino.png",
            "/assets/original_site/elephants_river.jpg",
            "/assets/drive_photos/julien_safari_a_pied.jpg"
        ]
    },
    "tiji-mustang": {
        "main": "/assets/drive_photos/fred_wild5.jpg",
        "gallery": [
            "/assets/drive_photos/fred_wild5.jpg",
            "/assets/original_site/temple_sacred.jpg",
            "/assets/drive_photos/adrien_bhaktapur1.jpg",
            "/assets/drive_photos/antoine_wild3.jpg"
        ]
    },
    "carnet-de-voyage": {
        "main": "/assets/drive_photos/antoine_wild5.jpg",
        "gallery": [
            "/assets/drive_photos/antoine_wild5.jpg",
            "/assets/drive_photos/julien_rollier_oiseau.jpg",
            "/assets/drive_photos/adrien_bhaktapur2.jpg",
            "/assets/drive_photos/adrien_bardia_sunset.jpg"
        ]
    },
    "jungle-extreme": {
        "main": "/assets/drive_photos/julien_leopard_indien.jpg",
        "gallery": [
            "/assets/drive_photos/julien_leopard_indien.jpg",
            "/assets/drive_photos/adrien_tigre1.jpg",
            "/assets/drive_photos/julien_photographes_jungle.jpg",
            "/assets/drive_photos/julien_elephant_mere_petit.jpg"
        ]
    },
    "nepal-sauvage": {
        "main": "/assets/original_site/machapuchare.png",
        "gallery": [
            "/assets/original_site/machapuchare.png",
            "/assets/original_site/tigre_bardia.png",
            "/assets/drive_photos/julien_cerf_axis.jpg",
            "/assets/drive_photos/adrien_katmandou1.jpg"
        ]
    },
    "immersion-spirituelle": {
        "main": "/assets/original_site/temple_sacred.jpg",
        "gallery": [
            "/assets/original_site/temple_sacred.jpg",
            "/assets/drive_photos/adrien_bhaktapur1.jpg",
            "/assets/drive_photos/adrien_katmandou1.jpg",
            "/assets/original_site/nepal_landscape.jpg"
        ]
    },
    "panthere-des-neiges": {
        "main": "/assets/snow-leopard/snow_leopard_portrait.jpg",
        "gallery": [
            "/assets/snow-leopard/snow_leopard_portrait.jpg",
            "/assets/snow-leopard/snow_leopard_wild_cliff.jpg",
            "/assets/snow-leopard/annapurna_peaks.jpg",
            "/assets/snow-leopard/pokhara_lake.jpg"
        ]
    }
}

# 1. Update tours.json
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

for t in tours:
    slug = t['slug']
    if slug in curated_tours:
        t['image'] = curated_tours[slug]['main']
        t['gallery'] = curated_tours[slug]['gallery']

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'w', encoding='utf-8') as f:
    json.dump(tours, f, indent=2, ensure_ascii=False)

# 2. Update index.astro trip cards
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx_code = f.read()

for slug, data in curated_tours.items():
    main_img = data['main']
    pattern = rf'(<!-- TRIP CARD:.*?/tours/{slug}\.html.*?<img\s+src=[\'"])[^\'"]+([\'"])'
    idx_code = re.sub(pattern, rf'\g<1>{main_img}\g<2>', idx_code, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx_code)

# 3. Update all 15 tour detail pages
for slug, data in curated_tours.items():
    tp = f'/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/{slug}.astro'
    if not glob.os.path.exists(tp):
        continue

    with open(tp, 'r', encoding='utf-8') as f:
        c = f.read()

    gal = data['gallery']
    gallery_replacement = f"""    <!-- PHOTO MOSAIC GALLERY WEROAD (CURATED WAHOU PHOTOS) -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-2.5 sm:gap-3 rounded-2xl sm:rounded-3xl overflow-hidden h-[280px] sm:h-[380px] md:h-[460px] mb-8 relative shadow-lg">
      <div class="md:col-span-2 h-full overflow-hidden">
        <img src="{gal[0]}" alt="Expédition Népal Sauvage" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(0)"/>
      </div>
      <div class="hidden md:block md:col-span-1 h-full overflow-hidden">
        <img src="{gal[1]}" alt="Expédition Népal Sauvage" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(1)"/>
      </div>
      <div class="hidden md:flex flex-col gap-3 h-full">
        <div class="h-1/2 overflow-hidden rounded-tr-2xl">
          <img src="{gal[2]}" alt="Expédition Népal Sauvage" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(2)"/>
        </div>
        <div class="h-1/2 overflow-hidden rounded-br-2xl relative">
          <img src="{gal[3]}" alt="Expédition Népal Sauvage" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(3)"/>
        </div>
      </div>

      <button onclick="openLightbox(0)" class="absolute bottom-4 right-4 bg-white/95 backdrop-blur-md hover:bg-white text-slate-900 font-bold text-xs sm:text-sm px-4 py-2 rounded-xl shadow-lg border border-slate-200 flex items-center gap-2 transition-all hover:scale-105 cursor-pointer">
        <svg class="w-4 h-4 text-[#0e8354] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect><circle cx="9" cy="9" r="2"></circle><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path></svg>
        <span>Voir toutes les photos</span>
      </button>
    </div>"""

    c = re.sub(
        r'<!-- PHOTO MOSAIC GALLERY WEROAD.*?<!-- STICKY SUB-NAV WEROAD -->',
        gallery_replacement + '\n\n    <!-- STICKY SUB-NAV WEROAD -->',
        c,
        flags=re.DOTALL
    )

    # Update galleryImages array in JS
    js_gal_str = ',\n      '.join([f'"{img}"' for img in gal])
    c = re.sub(
        r'const galleryImages = \[.*?\];',
        f'const galleryImages = [\n      {js_gal_str}\n    ];',
        c,
        flags=re.DOTALL
    )

    with open(tp, 'w', encoding='utf-8') as f:
        f.write(c)

print("Applied curated Wahou photo balance across all 15 tours!")
