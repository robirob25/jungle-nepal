import json, re

# 1. Update tours.json
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

for t in tours:
    if t['slug'] == 'rafting-safari':
        t['image'] = '/assets/drive_photos/adrien_bardia_river.jpg'
        t['gallery'] = [
            '/assets/drive_photos/adrien_bardia_river.jpg',
            '/assets/original_site/tigre_water_orig.jpg',
            '/assets/original_site/rafting_wild.jpg',
            '/assets/drive_photos/adrien_bardia_sunset.jpg'
        ]
    elif t['slug'] == 'bardia-nuit-sauvage':
        t['image'] = '/assets/original_site/camping_sauvage_bardia.png'
        t['gallery'] = [
            '/assets/original_site/camping_sauvage_bardia.png',
            '/assets/drive_photos/julien_tigre_bengale1.jpg',
            '/assets/original_site/camping_experience.jpg',
            '/assets/drive_photos/adrien_bardia_camp.jpg'
        ]

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'w', encoding='utf-8') as f:
    json.dump(tours, f, indent=2, ensure_ascii=False)

# 2. Update index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    idx_code = f.read()

# Update rafting-safari card image
idx_code = re.sub(
    r'(<!-- TRIP CARD:.*?/tours/rafting-safari\.html.*?<img\s+src=[\'"])[^\'"]+([\'"])',
    r'\g<1>/assets/drive_photos/adrien_bardia_river.jpg\g<2>',
    idx_code,
    flags=re.DOTALL
)

# Update bardia-nuit-sauvage card image
idx_code = re.sub(
    r'(<!-- TRIP CARD:.*?/tours/bardia-nuit-sauvage\.html.*?<img\s+src=[\'"])[^\'"]+([\'"])',
    r'\g<1>/assets/original_site/camping_sauvage_bardia.png\g<2>',
    idx_code,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(idx_code)

# 3. Update rafting-safari.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/rafting-safari.astro', 'r', encoding='utf-8') as f:
    raft_code = f.read()

raft_gallery = """    <!-- PHOTO MOSAIC GALLERY WEROAD (RIVIERE & TIGRE DANS L'EAU) -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-2.5 sm:gap-3 rounded-2xl sm:rounded-3xl overflow-hidden h-[280px] sm:h-[380px] md:h-[460px] mb-8 relative shadow-lg">
      <div class="md:col-span-2 h-full overflow-hidden">
        <img src="/assets/drive_photos/adrien_bardia_river.jpg" alt="Rivière sauvage Karnali" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(0)"/>
      </div>
      <div class="hidden md:block md:col-span-1 h-full overflow-hidden">
        <img src="/assets/original_site/tigre_water_orig.jpg" alt="Tigre du Bengale dans l'eau" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(1)"/>
      </div>
      <div class="hidden md:flex flex-col gap-3 h-full">
        <div class="h-1/2 overflow-hidden rounded-tr-2xl">
          <img src="/assets/original_site/rafting_wild.jpg" alt="Rafting en eau vive" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(2)"/>
        </div>
        <div class="h-1/2 overflow-hidden rounded-br-2xl relative">
          <img src="/assets/drive_photos/adrien_bardia_sunset.jpg" alt="Coucher de soleil sur la rivière" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(3)"/>
        </div>
      </div>

      <button onclick="openLightbox(0)" class="absolute bottom-4 right-4 bg-white/95 backdrop-blur-md hover:bg-white text-slate-900 font-bold text-xs sm:text-sm px-4 py-2 rounded-xl shadow-lg border border-slate-200 flex items-center gap-2 transition-all hover:scale-105 cursor-pointer">
        <svg class="w-4 h-4 text-[#0e8354] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect><circle cx="9" cy="9" r="2"></circle><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path></svg>
        <span>Voir toutes les photos</span>
      </button>
    </div>"""

raft_code = re.sub(
    r'<!-- PHOTO MOSAIC GALLERY WEROAD.*?<!-- STICKY SUB-NAV WEROAD -->',
    raft_gallery + '\n\n    <!-- STICKY SUB-NAV WEROAD -->',
    raft_code,
    flags=re.DOTALL
)

raft_code = re.sub(
    r'const galleryImages = \[.*?\];',
    """const galleryImages = [
      "/assets/drive_photos/adrien_bardia_river.jpg",
      "/assets/original_site/tigre_water_orig.jpg",
      "/assets/original_site/rafting_wild.jpg",
      "/assets/drive_photos/adrien_bardia_sunset.jpg"
    ];""",
    raft_code,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/rafting-safari.astro', 'w', encoding='utf-8') as f:
    f.write(raft_code)

# 4. Update bardia-nuit-sauvage.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/bardia-nuit-sauvage.astro', 'r', encoding='utf-8') as f:
    camp_code = f.read()

camp_gallery = """    <!-- PHOTO MOSAIC GALLERY WEROAD (CAMPING SAUVAGE & TIGRE) -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-2.5 sm:gap-3 rounded-2xl sm:rounded-3xl overflow-hidden h-[280px] sm:h-[380px] md:h-[460px] mb-8 relative shadow-lg">
      <div class="md:col-span-2 h-full overflow-hidden">
        <img src="/assets/original_site/camping_sauvage_bardia.png" alt="Camping sauvage en jungle de Bardia" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(0)"/>
      </div>
      <div class="hidden md:block md:col-span-1 h-full overflow-hidden">
        <img src="/assets/drive_photos/julien_tigre_bengale1.jpg" alt="Tigre du Bengale sauvage" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(1)"/>
      </div>
      <div class="hidden md:flex flex-col gap-3 h-full">
        <div class="h-1/2 overflow-hidden rounded-tr-2xl">
          <img src="/assets/original_site/camping_experience.jpg" alt="Feu de camp et veillée en jungle" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(2)"/>
        </div>
        <div class="h-1/2 overflow-hidden rounded-br-2xl relative">
          <img src="/assets/drive_photos/adrien_bardia_camp.jpg" alt="Bivouac sous les arbres" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(3)"/>
        </div>
      </div>

      <button onclick="openLightbox(0)" class="absolute bottom-4 right-4 bg-white/95 backdrop-blur-md hover:bg-white text-slate-900 font-bold text-xs sm:text-sm px-4 py-2 rounded-xl shadow-lg border border-slate-200 flex items-center gap-2 transition-all hover:scale-105 cursor-pointer">
        <svg class="w-4 h-4 text-[#0e8354] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect><circle cx="9" cy="9" r="2"></circle><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path></svg>
        <span>Voir toutes les photos</span>
      </button>
    </div>"""

camp_code = re.sub(
    r'<!-- PHOTO MOSAIC GALLERY WEROAD.*?<!-- STICKY SUB-NAV WEROAD -->',
    camp_gallery + '\n\n    <!-- STICKY SUB-NAV WEROAD -->',
    camp_code,
    flags=re.DOTALL
)

camp_code = re.sub(
    r'const galleryImages = \[.*?\];',
    """const galleryImages = [
      "/assets/original_site/camping_sauvage_bardia.png",
      "/assets/drive_photos/julien_tigre_bengale1.jpg",
      "/assets/original_site/camping_experience.jpg",
      "/assets/drive_photos/adrien_bardia_camp.jpg"
    ];""",
    camp_code,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/bardia-nuit-sauvage.astro', 'w', encoding='utf-8') as f:
    f.write(camp_code)

print("Updated Riviera & Camping photos on homepage cards and detail galleries!")
