import json, re, glob

# Every tour with jungle gets a distinct, high-impact tiger photo
tours_jungle_tigers = {
    "bardia-explorateur": {
        "main": "/assets/drive_photos/adrien_tigre1.jpg",
        "gallery": [
            "/assets/drive_photos/adrien_tigre1.jpg",
            "/assets/drive_photos/julien_safari_a_pied.jpg",
            "/assets/drive_photos/adrien_bardia_forest.jpg",
            "/assets/drive_photos/julien_cerf_axis.jpg"
        ]
    },
    "bardia-nuit-sauvage": {
        "main": "/assets/drive_photos/julien_tigre_bengale1.jpg",
        "gallery": [
            "/assets/drive_photos/julien_tigre_bengale1.jpg",
            "/assets/original_site/camping_sauvage_bardia.png",
            "/assets/original_site/camping_experience.jpg",
            "/assets/drive_photos/adrien_bardia_camp.jpg"
        ]
    },
    "bardia-babai-camping": {
        "main": "/assets/drive_photos/adrien_tigre4.jpg",
        "gallery": [
            "/assets/drive_photos/adrien_tigre4.jpg",
            "/assets/original_site/babai_walk.png",
            "/assets/drive_photos/julien_elephant_mere_petit.jpg",
            "/assets/drive_photos/adrien_bardia_camp.jpg"
        ]
    },
    "babai-special": {
        "main": "/assets/drive_photos/adrien_tigre2.jpg",
        "gallery": [
            "/assets/drive_photos/adrien_tigre2.jpg",
            "/assets/original_site/elephant_bardia.png",
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
    "chitwan-culture": {
        "main": "/assets/original_site/chitwan_rhino.png",
        "gallery": [
            "/assets/original_site/chitwan_rhino.png",
            "/assets/drive_photos/adrien_tigre3.jpg",
            "/assets/drive_photos/julien_elephant_mere_petit.jpg",
            "/assets/drive_photos/adrien_bhaktapur1.jpg"
        ]
    },
    "jungle-extreme": {
        "main": "/assets/drive_photos/julien_leopard_indien.jpg",
        "gallery": [
            "/assets/drive_photos/julien_leopard_indien.jpg",
            "/assets/drive_photos/adrien_tigre1.jpg",
            "/assets/drive_photos/julien_tigre_bengale3.jpg",
            "/assets/drive_photos/julien_photographes_jungle.jpg"
        ]
    },
    "rafting-safari": {
        "main": "/assets/original_site/tigre_water_orig.jpg",
        "gallery": [
            "/assets/original_site/tigre_water_orig.jpg",
            "/assets/original_site/rafting_wild.jpg",
            "/assets/drive_photos/julien_gangetic_dolphin.jpg",
            "/assets/drive_photos/adrien_bardia_river.jpg"
        ]
    },
    "rara-lake-bardia": {
        "main": "/assets/original_site/tigre_bardia.png",
        "gallery": [
            "/assets/original_site/tigre_bardia.png",
            "/assets/original_site/lac_rara_orig.jpg",
            "/assets/drive_photos/fred_wild2.jpg",
            "/assets/drive_photos/antoine_wild3.jpg"
        ]
    },
    "nepal-immersion-totale": {
        "main": "/assets/original_site/tigre_route.png",
        "gallery": [
            "/assets/original_site/tigre_route.png",
            "/assets/drive_photos/adrien_bhaktapur2.jpg",
            "/assets/original_site/chitwan_rhino.png",
            "/assets/drive_photos/julien_safari_a_pied.jpg"
        ]
    },
    "nepal-sauvage": {
        "main": "/assets/drive_photos/adrien_tigre3.jpg",
        "gallery": [
            "/assets/drive_photos/adrien_tigre3.jpg",
            "/assets/original_site/himalayas_sunrise_peaks.jpg",
            "/assets/original_site/fishtail_sacred_himalaya.jpg",
            "/assets/drive_photos/julien_cerf_axis.jpg"
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
    },
    "tiji-mustang": {
        "main": "/assets/original_site/tiji_festival_orig.jpg",
        "gallery": [
            "/assets/original_site/tiji_festival_orig.jpg",
            "/assets/original_site/mustang_panorama_orig.png",
            "/assets/original_site/mustang_village_orig.png",
            "/assets/drive_photos/fred_wild5.jpg"
        ]
    },
    "carnet-de-voyage": {
        "main": "/assets/drive_photos/antoine_wild5.jpg",
        "gallery": [
            "/assets/drive_photos/antoine_wild5.jpg",
            "/assets/drive_photos/julien_tigre_bengale3.jpg",
            "/assets/drive_photos/julien_rollier_oiseau.jpg",
            "/assets/drive_photos/adrien_bhaktapur2.jpg"
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
    }
}

# 1. Update tours.json
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

for t in tours:
    slug = t['slug']
    if slug in tours_jungle_tigers:
        t['image'] = tours_jungle_tigers[slug]['main']
        t['gallery'] = tours_jungle_tigers[slug]['gallery']

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'w', encoding='utf-8') as f:
    json.dump(tours, f, indent=2, ensure_ascii=False)

# 2. Update index.astro trip cards
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx_code = f.read()

for slug, data in tours_jungle_tigers.items():
    main_img = data['main']
    pattern = rf'(<!-- TRIP CARD:.*?/tours/{slug}\.html.*?<img\s+src=[\'"])[^\'"]+([\'"])'
    idx_code = re.sub(pattern, rf'\g<1>{main_img}\g<2>', idx_code, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx_code)

# 3. Update all 15 tour detail pages
for slug, data in tours_jungle_tigers.items():
    tp = f'/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/{slug}.astro'
    if not glob.os.path.exists(tp):
        continue

    with open(tp, 'r', encoding='utf-8') as f:
        c = f.read()

    gal = data['gallery']
    gallery_replacement = f"""    <!-- PHOTO MOSAIC GALLERY WEROAD (TIGER & JUNGLE VARIETY) -->
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

    js_gal_str = ',\n      '.join([f'"{img}"' for img in gal])
    c = re.sub(
        r'const galleryImages = \[.*?\];',
        f'const galleryImages = [\n      {js_gal_str}\n    ];',
        c,
        flags=re.DOTALL
    )

    with open(tp, 'w', encoding='utf-8') as f:
        f.write(c)

print("Applied distinct tiger and jungle photos across all circuits!")
