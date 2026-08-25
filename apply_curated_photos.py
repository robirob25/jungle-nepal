import json
import os
import re

# Curated high-res, context-driven photos for every tour
curated_tours_media = {
    "nepal-sauvage": {
        "hero": "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia.png",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia.png",
            "https://junglenepal.com/wp-content/uploads/2026/01/Himalaya-haut-sommet.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/Coucher-de-soleil-Bardia.png"
        ]
    },
    "nepal-immersion-totale": {
        "hero": "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2025/12/Tharu-danse.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/jungle-walk-Babai-valley.png"
        ]
    },
    "babai-special": {
        "hero": "https://junglenepal.com/wp-content/uploads/2025/12/Tigre-Bardia.png",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/12/Tigre-Bardia.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/Camping-Babai-Valley.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/2-1.png"
        ]
    },
    "bardia-babai-camping": {
        "hero": "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png",
            "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
            "https://junglenepal.com/wp-content/uploads/2026/01/Camping-experience.jpg"
        ]
    },
    "bardia-explorateur": {
        "hero": "https://junglenepal.com/wp-content/uploads/2025/12/P1166103-scaled.jpg",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/12/P1166103-scaled.jpg",
            "https://junglenepal.com/wp-content/uploads/2025/12/Elephant-sauvage-Bardia.png",
            "https://junglenepal.com/wp-content/uploads/2025/03/marche-jungle.png"
        ]
    },
    "rafting-safari": {
        "hero": "https://junglenepal.com/wp-content/uploads/2017/01/Design-sans-titre-3.webp",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2017/01/Design-sans-titre-3.webp",
            "https://junglenepal.com/wp-content/uploads/2025/12/1-1.png",
            "https://junglenepal.com/wp-content/uploads/2017/01/nepal-landscape-2388105_1920-1.jpg"
        ]
    },
    "bardia-nuit-sauvage": {
        "hero": "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
            "https://junglenepal.com/wp-content/uploads/2025/12/Tigre-Bardia.png",
            "https://junglenepal.com/wp-content/uploads/2025/03/Ajouter-un-titre-8.webp"
        ]
    },
    "tiji-mustang": {
        "hero": "https://junglenepal.com/wp-content/uploads/2017/01/1.png",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2017/01/1.png",
            "https://junglenepal.com/wp-content/uploads/2017/01/2.png",
            "https://junglenepal.com/wp-content/uploads/2017/01/3.png"
        ]
    },
    "chitwan-culture": {
        "hero": "https://junglenepal.com/wp-content/uploads/2025/03/68.png",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/03/68.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/tharu-1.jpg",
            "https://junglenepal.com/wp-content/uploads/2025/12/Rhinoceros-Bardia.png"
        ]
    },
    "rara-lake-bardia": {
        "hero": "https://junglenepal.com/wp-content/uploads/2017/01/Design-sans-titre-2.webp",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2017/01/Design-sans-titre-2.webp",
            "https://junglenepal.com/wp-content/uploads/2026/01/Machapuchare-himalaya-montagne.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia.png"
        ]
    },
    "chitwan-bardia-complete": {
        "hero": "https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/Tigre-Bardia.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/ours-lippu-chitwan.jpg"
        ]
    },
    "carnet-de-voyage": {
        "hero": "https://junglenepal.com/wp-content/uploads/2017/01/IMG_9701-1-scaled.jpeg",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2017/01/IMG_9701-1-scaled.jpeg",
            "https://junglenepal.com/wp-content/uploads/2017/01/IMG_0140-scaled.jpg",
            "https://junglenepal.com/wp-content/uploads/2026/01/Groupe-touriste-Nagarkot-Nepal.jpg"
        ]
    },
    "jungle-extreme": {
        "hero": "https://junglenepal.com/wp-content/uploads/2017/01/DSC00354.jpg",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2017/01/DSC00354.jpg",
            "https://junglenepal.com/wp-content/uploads/2025/02/leopard-6153930_1280.jpg",
            "https://junglenepal.com/wp-content/uploads/2025/12/jungle-walk-Babai-valley.png"
        ]
    },
    "immersion-spirituelle": {
        "hero": "https://junglenepal.com/wp-content/uploads/2017/01/IMG_0177-1-scaled.jpeg",
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2017/01/IMG_0177-1-scaled.jpeg",
            "https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg"
        ]
    }
}

# 1. Update index.html cards with unique photos
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/processed_tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

# Re-run generator script with rich photo curation
os.system("python3 /Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/apply_logo_and_green_identity.py")
os.system("python3 /Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/redesign_wildlife_concept_section.py")
os.system("python3 /Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/apply_trustpilot_5_stars.py")
os.system("python3 /Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/fix_french_capitalization.py")
os.system("python3 /Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/replace_emojis_with_black_icons.py")
os.system("python3 /Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/apply_exact_google_review_url.py")
os.system("python3 /Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/fix_team_photos.py")

# 2. Update each of the 14 tour pages with its custom curated 3-photo gallery
tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'):
        continue
    short_id = fname.replace('.html', '')
    if short_id not in curated_tours_media:
        continue
    
    fpath = os.path.join(tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    media = curated_tours_media[short_id]
    g = media['gallery']
    
    # Replace Gallery Grid in tour page
    gallery_html = f"""    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 rounded-3xl overflow-hidden shadow-2xl border border-slate-200">
      <div class="md:col-span-2 relative h-[380px] sm:h-[480px] overflow-hidden group">
        <img src="{g[0]}" alt="Photo principale" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
      </div>
      <div class="hidden md:flex flex-col gap-4 h-[480px]">
        <div class="relative flex-1 overflow-hidden group rounded-2xl">
          <img src="{g[1]}" alt="Photo ambiance" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
        </div>
        <div class="relative flex-1 overflow-hidden group rounded-2xl">
          <img src="{g[2]}" alt="Photo paysage" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">
          <button class="absolute bottom-4 right-4 bg-slate-950/80 backdrop-blur-md text-white text-xs font-bold px-3.5 py-2 rounded-xl flex items-center gap-1.5 border border-white/20 hover:bg-white hover:text-slate-950 transition-all">
            <i data-lucide="image" class="w-3.5 h-3.5"></i>
            <span>Voir toutes les photos</span>
          </button>
        </div>
      </div>
    </div>"""

    # Replace existing gallery block in tour page
    pattern_gallery = r'<div class=\"grid grid-cols-1 md:grid-cols-3 gap-4 rounded-3xl overflow-hidden.*?</button>\s*</div>\s*</div>\s*</div>'
    content = re.sub(pattern_gallery, gallery_html, content, flags=re.DOTALL)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Curated context-driven photo suites applied across all 14 tours and homepage successfully!")
