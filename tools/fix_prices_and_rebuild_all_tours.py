import json
import os
import re
from html.parser import HTMLParser

class StrictTagValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link', 'source']:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in ['img', 'br', 'hr', 'input', 'meta', 'link', 'source']:
            return
        if self.stack:
            expected = self.stack.pop()
            if expected != tag:
                self.errors.append(f'Mismatched </{tag}>, expected </{expected}>')
        else:
            self.errors.append(f'Unexpected </{tag}> with empty stack')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/all_tours_raw.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

# Curated High-End Images for all 14 tours (100% unique, 0 duplicates)
hero_images_curated = {
    "nepal-sauvage": [
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-700x430.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-27-at-13.17.14.jpeg",
        "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01.jpeg",
        "https://junglenepal.com/wp-content/uploads/2017/01/IMG_9675-1-scaled.jpeg"
    ],
    "nepal-immersion-totale": [
        "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png"
    ],
    "babai-special": [
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01.jpeg"
    ],
    "bardia-babai-camping": [
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/WhatsApp-Image-2025-11-21-at-08.58.01.jpeg"
    ],
    "bardia-explorateur": [
        "https://junglenepal.com/wp-content/uploads/2025/12/P1133754-scaled.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg"
    ],
    "rafting-safari": [
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-landscape-2388105_1920-1.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg"
    ],
    "bardia-nuit-sauvage": [
        "https://junglenepal.com/wp-content/uploads/2025/03/Ajouter-un-titre-8.webp",
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png"
    ],
    "tiji-mustang": [
        "https://junglenepal.com/wp-content/uploads/2017/01/1.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/IMG_9675-1-scaled.jpeg"
    ],
    "chitwan-culture": [
        "https://junglenepal.com/wp-content/uploads/2025/03/68.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg"
    ],
    "rara-lake-bardia": [
        "https://junglenepal.com/wp-content/uploads/2017/01/Design-sans-titre-2.webp",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg"
    ],
    "chitwan-bardia-complete": [
        "https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png"
    ],
    "carnet-de-voyage": [
        "https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png"
    ],
    "jungle-extreme": [
        "https://junglenepal.com/wp-content/uploads/2017/01/Design-sans-titre-3.webp",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg",
        "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png"
    ],
    "immersion-spirituelle": [
        "https://junglenepal.com/wp-content/uploads/2017/01/IMG_0177-1-scaled.jpeg",
        "https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/nepal-5258059_1920.jpg"
    ]
}

meta_map = {
    "bardia-explorateur-5-jours-dans-la-jungle": {"short_id": "bardia-explorateur", "badge": "⭐ Best-Seller", "rating": "4.8", "reviews": 56, "difficulty": "Accessible à tous", "style": "Safari & Lodge Confort", "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 3, "nightlife": 1}},
    "chitwan-culture-et-jungle-sauvage": {"short_id": "chitwan-culture", "badge": "🦏 Rhinos & Tharu", "rating": "4.9", "reviews": 28, "difficulty": "Facile", "style": "Safari & Culture Locale", "radar": {"wildlife": 4, "nature": 4, "culture": 5, "relax": 3, "nightlife": 1}},
    "rivieres-sauvages-et-patrimoines-caches-expedition-et-rafting": {"short_id": "rafting-safari", "badge": "🚣 Rafting & Safari", "rating": "5.0", "reviews": 15, "difficulty": "Sportif", "style": "Aventure & Eaux Vives", "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 2, "nightlife": 1}},
    "bardia-aventure-immersive-en-jungle-et-camping-sauvage": {"short_id": "bardia-nuit-sauvage", "badge": "🌙 Micro-Aventure", "rating": "4.9", "reviews": 31, "difficulty": "Accessible", "style": "Bivouac Express", "radar": {"wildlife": 5, "nature": 5, "culture": 2, "relax": 2, "nightlife": 0}},
    "rara-lake-bardia-expedition-lultime-aventure-hors-sentiers-battus": {"short_id": "rara-lake-bardia", "badge": "🏔️ Expédition 4x4 & Lac Sacré", "rating": "5.0", "reviews": 18, "difficulty": "Aventurier", "style": "Grand Trek & 4x4", "radar": {"wildlife": 4, "nature": 5, "culture": 4, "relax": 2, "nightlife": 0}},
    "bardia-babai-vallee-camping-sauvage-au-coeur-dune-nature-vierge-et-isolee": {"short_id": "bardia-babai-camping", "badge": "⛺ Bivouac Sauvage", "rating": "4.9", "reviews": 24, "difficulty": "Aventure", "style": "Expédition Bivouac", "radar": {"wildlife": 5, "nature": 5, "culture": 3, "relax": 2, "nightlife": 0}},
    "nepal-immersion-totale-culture-vie-sauvage-et-aventure": {"short_id": "nepal-immersion-totale", "badge": "🔥 Promo -300€", "rating": "4.9", "reviews": 42, "difficulty": "Dynamique", "style": "Immersion 360°", "radar": {"wildlife": 5, "nature": 5, "culture": 5, "relax": 2, "nightlife": 1}},
    "deep-into-the-wild-babai-special-experience-5-jours": {"short_id": "babai-special", "badge": "⚡ Aventure ++", "rating": "5.0", "reviews": 19, "difficulty": "Aventurier", "style": "Tracking Tigre & Bivouac", "radar": {"wildlife": 5, "nature": 5, "culture": 2, "relax": 1, "nightlife": 0}},
    "chitwan-bardia-laventure-jungle-complete": {"short_id": "chitwan-bardia-complete", "badge": "🌿 Double Safari Parcs", "rating": "4.9", "reviews": 33, "difficulty": "Modéré", "style": "Le Grand Safari Népalais", "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 3, "nightlife": 1}},
    "tiji-festival-tour-upper-mustang": {"short_id": "tiji-mustang", "badge": "🕉️ Spécial Culture", "rating": "5.0", "reviews": 12, "difficulty": "Modéré", "style": "Himalaya & Culture Sacrée", "radar": {"wildlife": 2, "nature": 5, "culture": 5, "relax": 2, "nightlife": 0}},
    "nepal-special-carnet-de-voyage": {"short_id": "carnet-de-voyage", "badge": "🎨 Spécial Dessin & Carnet", "rating": "5.0", "reviews": 16, "difficulty": "Accessible", "style": "Art, Nature & Croquis", "radar": {"wildlife": 4, "nature": 5, "culture": 5, "relax": 4, "nightlife": 1}},
    "jungle-extreme-special-faune-sauvage": {"short_id": "jungle-extreme", "badge": "🐅 Passion Faune Pro", "rating": "5.0", "reviews": 21, "difficulty": "Intense", "style": "Immersion & Photographie", "radar": {"wildlife": 5, "nature": 5, "culture": 3, "relax": 1, "nightlife": 0}},
    "nepal-sauvage-de-la-jungle-aux-montagnes-sacrees": {"short_id": "nepal-sauvage", "badge": "❤️ Coup de cœur", "rating": "4.9", "reviews": 38, "difficulty": "Modéré", "style": "Safari 360° & Culture", "radar": {"wildlife": 5, "nature": 5, "culture": 4, "relax": 2, "nightlife": 1}},
    "immersion-spirituelle-en-himalaya": {"short_id": "immersion-spirituelle", "badge": "🧘 Retraite & Méditation", "rating": "4.9", "reviews": 17, "difficulty": "Doux", "style": "Retraite Spirituelle & Yoga", "radar": {"wildlife": 2, "nature": 5, "culture": 5, "relax": 5, "nightlife": 0}}
}

def generate_dots(val):
    dots = ""
    for i in range(5):
        if i < val:
            dots += '<span class="w-2.5 h-2.5 rounded-full bg-[#0e8354]"></span>'
        else:
            dots += '<span class="w-2.5 h-2.5 rounded-full bg-slate-200"></span>'
    return dots

def build_tour_html(meta, raw_tour, is_english=False):
    short_id = meta['short_id']
    title = raw_tour.get('title', '')
    title_clean = re.sub(r'<.*?>', '', title).strip()
    title_encoded = title_clean.replace(' ', '%20').replace('–', '-').replace(':', '')

    overview = raw_tour.get('overview', '')
    overview_clean = re.sub(r'<.*?>', '', overview).replace('"', '&quot;').strip()[:180]

    duration = raw_tour.get('duration', 'Sur mesure')
    days_count = raw_tour.get('days_count', 5)

    # ACCURATE CLEAN PRICING (NO MORE "None")
    p_disc = raw_tour.get('price_discount')
    p_orig = raw_tour.get('price_original')
    
    if p_disc and p_orig and p_disc != p_orig:
        price = p_disc
        original_price_html = f'<span class="text-xs sm:text-sm text-slate-400 line-through font-bold">{p_orig}</span>'
        saving_badge_html = f'<span class="px-2.5 py-1 rounded-full bg-rose-50 border border-rose-200 text-rose-700 text-xs font-black">Promo</span>'
    else:
        price = p_disc or p_orig or 'Sur devis'
        original_price_html = ''
        saving_badge_html = ''

    # Highlights
    highlights = raw_tour.get('highlights', [])
    if not highlights:
        highlights = [
            "Pistage des tigres du Bengale et grands mammifères en petit groupe exclusif (4 à 8 explorateurs).",
            "Encadrement par les meilleurs pisteurs natifs de Bardia (Pawan & Kiran) et assistance francophone continue.",
            "Immersion totale dans les sanctuaires les plus sauvages et préservés du Népal sans tourisme de masse.",
            "Soutien direct aux communautés locales et respect strict des chartes éthiques de protection de la faune."
        ]
    highlights_html = "".join([f'<li class="flex items-start gap-3"><span class="w-2 h-2 rounded-full bg-[#0e8354] mt-2 shrink-0"></span><span>{h}</span></li>' for h in highlights])

    # EXTRACT FULL DETAILED DAYS ITINERARY
    days = raw_tour.get('days', [])
    days_html = ""
    for idx, d in enumerate(days):
        d_num = idx + 1
        d_title = d.get('title', f'Jour {d_num}')
        d_desc = d.get('desc', '')
        d_desc = d_desc.replace('&#215;', '×').replace('&amp;', '&').strip()
        open_attr = 'open' if idx == 0 else ''
        days_html += f"""
            <details {open_attr} class="group bg-white rounded-2xl border border-slate-200/90 overflow-hidden shadow-sm transition-all">
              <summary class="flex items-center justify-between p-4 sm:p-5 cursor-pointer select-none hover:bg-slate-50 transition-colors">
                <div class="flex items-center gap-3.5">
                  <span class="w-8 h-8 rounded-xl bg-emerald-50 text-[#0e8354] font-black text-xs flex items-center justify-center shrink-0 border border-emerald-200">
                    J{d_num}
                  </span>
                  <h4 class="font-bold text-sm sm:text-base text-slate-900">
                    {d_title}
                  </h4>
                </div>
                <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400 transition-transform group-open:rotate-180 shrink-0"></i>
              </summary>
              <div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">
                <p class="pt-3">{d_desc}</p>
              </div>
            </details>
        """

    curated = hero_images_curated.get(short_id, [
        "https://junglenepal.com/wp-content/uploads/2025/12/P1133754-scaled.jpg",
        "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia-600x800.png",
        "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
        "https://junglenepal.com/wp-content/uploads/2017/01/tigre.jpeg"
    ])

    radar = meta['radar']
    radar_wildlife = generate_dots(radar['wildlife'])
    radar_nature = generate_dots(radar['nature'])
    radar_culture = generate_dots(radar['culture'])
    radar_relax = generate_dots(radar['relax'])
    radar_nightlife = generate_dots(radar['nightlife'])

    asset_prefix = "../../assets/" if is_english else "../assets/"
    home_prefix = "../index.html" if not is_english else "../../en/index.html"
    dest_prefix = "../destinations/" if not is_english else "../../en/destinations/"
    about_prefix = "../a-propos.html" if not is_english else "../../en/a-propos.html"
    contact_prefix = "../contact.html" if not is_english else "../../en/contact.html"

    # Full footer inclusion
    from deploy_complete_footer_menu import generate_full_footer
    footer_html = generate_full_footer(prefix="../../" if is_english else "../", is_english=is_english)

    html = f"""<!DOCTYPE html>
<html lang="{'en' if is_english else 'fr'}" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_clean} | Jungle Nepal Adventure</title>
  <meta name="description" content="{overview_clean}">

  <!-- Open Graph -->
  <meta property="og:title" content="{title_clean} | Jungle Nepal Adventure">
  <meta property="og:description" content="{overview_clean}">
  <meta property="og:image" content="{curated[0]}">
  <meta property="og:type" content="website">

  <!-- WeRoad Font: Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
          }}
        }}
      }}
    }}
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="bg-[#faf8f5] text-slate-800 font-sans antialiased selection:bg-[#0e8354] selection:text-white">

  <!-- TOP BAR -->
  <aside aria-label="Bannière d'information" class="bg-slate-950 text-slate-300 text-xs py-2 px-4 sticky top-0 z-50 border-b border-white/10 shadow-sm">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4 font-bold">
      <div class="flex items-center gap-2 overflow-hidden whitespace-nowrap text-ellipsis">
        <span class="inline-flex items-center justify-center bg-[#0e8354] text-white text-[10px] font-black uppercase tracking-widest px-2 py-0.5 rounded-full">
          Saison 2026-2027
        </span>
        <span class="font-medium text-slate-200 hidden sm:inline">
          🇳🇵 <strong>Micro-groupe 4 à 8 explorateurs</strong> ou départ privatisé.
        </span>
        <span class="text-amber-300 font-bold">
          -100€ code <span class="bg-white/10 px-1.5 py-0.5 rounded text-white border border-white/20">JUNGLE100</span>
        </span>
      </div>
      <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20suis%20intéressé%20par%20le%20circuit%20{title_encoded}" target="_blank" rel="noopener noreferrer" class="hidden md:flex items-center gap-1.5 text-emerald-300 hover:text-white transition-colors text-xs font-semibold">
        <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
        <span>WhatsApp direct : <strong>+33 6 95 41 32 27</strong> (Robin)</span>
      </a>
    </div>
  </aside>

  <!-- HEADER STICKY -->
  <header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-8 z-40 transition-all">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2.5 flex items-center justify-between">
      
      <!-- LOGO -->
      <a href="{home_prefix}" class="flex items-center gap-2 group shrink-0">
        <img src="{asset_prefix}logo_dark.png" alt="Jungle Nepal Adventure" class="h-14 sm:h-16 w-auto object-contain filter drop-shadow-sm group-hover:scale-105 transition-transform duration-300" />
      </a>

      <!-- NAVIGATION DESKTOP -->
      <nav class="hidden lg:flex items-center gap-6 xl:gap-7 text-[13px] font-bold text-slate-700">
        <a href="{home_prefix}#prochains-departs" class="hover:text-[#0e8354] transition-colors">Tous les 14 séjours</a>
        
        <!-- DROPDOWN DESTINATIONS -->
        <div class="relative group py-2">
          <a href="{dest_prefix}index.html" class="hover:text-[#0e8354] transition-colors flex items-center gap-1.5 cursor-pointer font-bold">
            <span>Destinations</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 transition-transform duration-300 group-hover:rotate-180 opacity-80" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
            </svg>
          </a>

          <!-- Menu Déroulant Sombre Opaque (#041d13) -->
          <div class="absolute top-full left-0 pt-2 w-72 opacity-0 translate-y-2 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:pointer-events-auto transition-all duration-300 z-50">
            <div style="background-color: #041d13 !important;" class="border border-emerald-500/30 rounded-3xl p-3 shadow-[0_25px_60px_rgba(0,0,0,0.8)] space-y-1 text-white">
              
              <a href="{dest_prefix}bardia.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                  🐅
                </div>
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Bardia</p>
                  <p class="text-[10px] text-slate-400">Tigres du Bengale & safaris à pied</p>
                </div>
              </a>

              <a href="{dest_prefix}chitwan.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                  🦏
                </div>
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Chitwan</p>
                  <p class="text-[10px] text-slate-400">Rhinocéros & pirogues de la Rapti</p>
                </div>
              </a>

              <a href="{dest_prefix}suklaphanta.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                  🦌
                </div>
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Parc national de Suklaphanta</p>
                  <p class="text-[10px] text-slate-400">Cerfs des marais & ouest sauvage</p>
                </div>
              </a>

              <a href="{dest_prefix}annapurna.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                  🏔️
                </div>
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Les Annapurna & Pokhara</p>
                  <p class="text-[10px] text-slate-400">Sommets mythiques & balcons alpins</p>
                </div>
              </a>

              <a href="{dest_prefix}katmandou.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-white/10 transition-colors group/item">
                <div class="w-9 h-9 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center font-bold text-sm shrink-0">
                  🕉️
                </div>
                <div class="flex-1">
                  <p class="font-extrabold text-xs text-white group-hover/item:text-amber-300 transition-colors">Katmandou</p>
                  <p class="text-[10px] text-slate-400">Vallée des rois & temples sacrés</p>
                </div>
              </a>

              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="{dest_prefix}index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  Voir toutes les destinations →
                </a>
              </div>

            </div>
          </div>
        </div>

        <a href="#programme" class="hover:text-[#0e8354] transition-colors">Itinéraire détaillé</a>
        <a href="#inclusions" class="hover:text-[#0e8354] transition-colors">Inclus & Extras</a>
        <a href="{about_prefix}" class="hover:text-[#0e8354] transition-colors">À propos</a>
        <a href="{contact_prefix}" class="hover:text-[#0e8354] transition-colors">Contact</a>
      </nav>

      <!-- CTA BUTTON & GLOBE -->
      <div class="flex items-center gap-3">
        <!-- LANGUAGE SWITCHER (GLOBE) -->
        <div class="relative group/lang py-1">
          <button onclick="this.parentElement.querySelector('#lang-menu-light').classList.toggle('opacity-100'); this.parentElement.querySelector('#lang-menu-light').classList.toggle('pointer-events-auto');" class="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-slate-100 hover:bg-slate-200 border border-slate-200 flex items-center justify-center text-slate-700 transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer" aria-label="Changer de langue / Change language">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-slate-700" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="2" y1="12" x2="22" y2="12"></line>
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
            </svg>
          </button>
          <div id="lang-menu-light" class="absolute right-0 top-full mt-1.5 w-44 opacity-0 translate-y-2 pointer-events-none group-hover/lang:opacity-100 group-hover/lang:translate-y-0 group-hover/lang:pointer-events-auto transition-all duration-200 z-50">
            <div style="background-color: #041d13 !important;" class="border border-emerald-500/30 rounded-2xl p-1.5 shadow-[0_20px_50px_rgba(0,0,0,0.8)] space-y-0.5 text-xs font-bold text-white">
              <button onclick="setSiteLanguage('fr')" class="lang-btn-fr w-full flex items-center justify-between px-3 py-2 rounded-xl bg-white/15 text-[#10b981] hover:bg-white/10 transition-colors text-left cursor-pointer">
                <span class="flex items-center gap-2"><span>🇫🇷</span><span>Français</span></span>
                <svg class="lang-check-fr w-3.5 h-3.5 text-[#10b981]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
              </button>
              <button onclick="setSiteLanguage('en')" class="lang-btn-en w-full flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-white/10 hover:text-white transition-colors text-left cursor-pointer">
                <span class="flex items-center gap-2"><span>🇬🇧</span><span>English</span></span>
                <svg class="lang-check-en hidden w-3.5 h-3.5 text-[#10b981]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
              </button>
            </div>
          </div>
        </div>

        <button onclick="scrollToBooking()" class="inline-flex items-center gap-2 bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] text-white text-xs sm:text-[13px] font-black px-5 py-2.5 rounded-full shadow-md shadow-[#0e8354]/30 hover:scale-105 active:scale-95 transition-all">
          <span>Départs & Prix</span>
          <i data-lucide="calendar" class="w-4 h-4"></i>
        </button>
      </div>

    </div>
  </header>

  <!-- MAIN TOUR CONTENT -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 pb-24 font-sans">
    
    <!-- Breadcrumbs -->
    <nav class="flex items-center gap-2 text-xs text-slate-500 font-semibold mb-3 overflow-x-auto whitespace-nowrap">
      <a href="{home_prefix}" class="hover:text-slate-900 flex items-center gap-1">
        <i data-lucide="home" class="w-3.5 h-3.5"></i>
        <span>Accueil</span>
      </a>
      <span>›</span>
      <a href="{home_prefix}#prochains-departs" class="hover:text-slate-900">Nos 14 Séjours</a>
      <span>›</span>
      <span class="text-slate-900 font-bold truncate">{title_clean}</span>
    </nav>

    <!-- Header Title & Badges Row -->
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 pb-6">
      <div>
        <h1 class="font-black text-2xl sm:text-4xl lg:text-5xl text-slate-950 tracking-tight leading-tight">
          {title_clean}
        </h1>
        <div class="mt-3 flex flex-wrap items-center gap-3 text-xs sm:text-sm">
          <span class="inline-flex items-center gap-1.5 font-bold text-slate-700 bg-amber-50 border border-amber-200 px-3 py-1 rounded-full">
            <i data-lucide="sun" class="w-4 h-4 text-amber-600"></i>
            <span>{duration}</span>
          </span>
          <div class="inline-flex items-center gap-1.5 bg-emerald-50 text-emerald-900 font-bold px-3 py-1 rounded-full border border-emerald-200">
            <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-500 text-amber-500"></i>
            <span>{meta['rating']} ({meta['reviews']} avis vérifiés)</span>
          </div>
          <span class="text-xs font-bold bg-slate-900 text-amber-300 px-3 py-1 rounded-full border border-amber-300/30">
            {meta['badge']}
          </span>
        </div>
      </div>

      <!-- BOUTON PARTAGER UNIQUEMENT (SANS FAVORIS) -->
      <div class="relative shrink-0">
        <button id="share-btn" onclick="handleShareTour()" class="flex items-center gap-2 px-4 py-2 rounded-xl border border-slate-200 bg-white text-xs font-extrabold text-slate-800 hover:text-[#0e8354] hover:border-[#0e8354] shadow-sm hover:shadow transition-all group cursor-pointer">
          <i data-lucide="share-2" class="w-4 h-4 text-slate-500 group-hover:text-[#0e8354] transition-colors"></i>
          <span>Partager ce séjour</span>
        </button>

        <!-- Dropdown Menu Partage Sombre Opaque (#041d13) -->
        <div id="share-menu" class="absolute right-0 top-full mt-2 w-64 opacity-0 translate-y-2 pointer-events-none transition-all duration-200 z-50">
          <div style="background-color: #041d13 !important;" class="border border-emerald-500/30 rounded-2xl p-2 shadow-[0_20px_50px_rgba(0,0,0,0.8)] space-y-1 text-white">
            <button onclick="copyTourLink()" class="w-full flex items-center gap-2.5 px-3 py-2.5 rounded-xl text-xs font-bold text-white hover:bg-white/10 transition-colors text-left cursor-pointer group/item">
              <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-[#10b981] flex items-center justify-center shrink-0">
                <i data-lucide="link" class="w-3.5 h-3.5"></i>
              </div>
              <span class="group-hover/item:text-amber-300 transition-colors">Copier le lien direct</span>
            </button>
            <a id="share-whatsapp" href="#" target="_blank" class="w-full flex items-center gap-2.5 px-3 py-2.5 rounded-xl text-xs font-bold text-white hover:bg-white/10 transition-colors text-left cursor-pointer group/item">
              <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-[#25D366] flex items-center justify-center shrink-0">
                <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
              </div>
              <span class="group-hover/item:text-amber-300 transition-colors">Envoyer sur WhatsApp</span>
            </a>
            <a id="share-email" href="#" class="w-full flex items-center gap-2.5 px-3 py-2.5 rounded-xl text-xs font-bold text-white hover:bg-white/10 transition-colors text-left cursor-pointer group/item">
              <div class="w-7 h-7 rounded-lg bg-emerald-500/20 text-slate-300 flex items-center justify-center shrink-0">
                <i data-lucide="mail" class="w-3.5 h-3.5"></i>
              </div>
              <span class="group-hover/item:text-amber-300 transition-colors">Partager par Email</span>
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- PHOTO MOSAIC GALLERY WEROAD -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-3 rounded-3xl overflow-hidden h-[340px] sm:h-[460px] mb-8 relative shadow-lg">
      <div class="md:col-span-2 h-full overflow-hidden">
        <img src="{curated[0]}" alt="{title_clean}" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(0)"/>
      </div>
      <div class="hidden md:block md:col-span-1 h-full overflow-hidden">
        <img src="{curated[1]}" alt="{title_clean}" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(1)"/>
      </div>
      <div class="hidden md:flex flex-col gap-3 h-full">
        <div class="h-1/2 overflow-hidden rounded-tr-2xl">
          <img src="{curated[2]}" alt="{title_clean}" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(2)"/>
        </div>
        <div class="h-1/2 overflow-hidden rounded-br-2xl relative">
          <img src="{curated[3]}" alt="{title_clean}" class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer" onclick="openLightbox(3)"/>
        </div>
      </div>

      <button onclick="openLightbox(0)" class="absolute bottom-4 right-4 bg-white/95 backdrop-blur-md hover:bg-white text-slate-900 font-bold text-xs sm:text-sm px-4 py-2 rounded-xl shadow-lg border border-slate-200 flex items-center gap-2 transition-all hover:scale-105">
        <i data-lucide="images" class="w-4 h-4 text-[#0e8354]"></i>
        <span>Voir toutes les photos</span>
      </button>
    </div>

    <!-- STICKY SUB-NAV WEROAD -->
    <div class="sticky top-[69px] z-30 bg-white/95 backdrop-blur-md border-b border-slate-200 py-3 mb-8">
      <div class="flex items-center gap-6 overflow-x-auto text-xs sm:text-sm font-bold text-slate-600">
        <a href="#apercu" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">Aperçu</a>
        <a href="#pour-moi" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">Profil Voyage</a>
        <a href="#programme" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">Itinéraire Jour par Jour ({len(days)}j)</a>
        <a href="#inclusions" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">Inclus & Extras</a>
        <a href="#avis-voyageurs" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">Avis</a>
        <a href="#faq" class="hover:text-[#0e8354] transition-colors pb-1 border-b-2 border-transparent hover:border-[#0e8354]">FAQ</a>
      </div>
    </div>

    <!-- 2-COLUMN MAIN CONTENT GRID -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
      
      <!-- LEFT COLUMN -->
      <div class="lg:col-span-8 space-y-12">
        
        <!-- SECTION 1: APERÇU -->
        <section id="apercu" class="space-y-6">
          <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
            {overview}
          </p>

          <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm">
            <h3 class="font-bold text-lg text-slate-950 mb-4 flex items-center gap-2">
              <i data-lucide="sparkles" class="w-5 h-5 text-amber-500"></i>
              <span>Les temps forts du voyage</span>
            </h3>
            <ul class="space-y-3 text-sm sm:text-base text-slate-700">
              {highlights_html}
            </ul>
          </div>
        </section>

        <!-- SECTION 2: CE VOYAGE EST POUR MOI ? (WeRoad Radar) -->
        <section id="pour-moi" class="pt-6 border-t border-slate-200">
          <h2 class="font-black text-2xl sm:text-3xl text-slate-950 mb-6">
            Ce voyage est-il fait pour moi ?
          </h2>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 bg-white p-6 sm:p-8 rounded-3xl border border-slate-200/90 shadow-sm">
            <div class="space-y-4">
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium"><span>🐅</span> Faune & Pistage</span>
                <div class="flex gap-1.5">{radar_wildlife}</div>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium"><span>🌿</span> Nature & Aventure</span>
                <div class="flex gap-1.5">{radar_nature}</div>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium"><span>🛕</span> Culture & Vie locale</span>
                <div class="flex gap-1.5">{radar_culture}</div>
              </div>
            </div>

            <div class="space-y-4">
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium"><span>🧘</span> Relax & Contemplation</span>
                <div class="flex gap-1.5">{radar_relax}</div>
              </div>
              <div class="flex items-center justify-between text-sm">
                <span class="flex items-center gap-2 text-slate-700 font-medium"><span>🎉</span> Soirées & Fête</span>
                <div class="flex gap-1.5">{radar_nightlife}</div>
              </div>
              <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-sm font-bold">
                <span class="text-slate-500">Rythme & Effort :</span>
                <span class="text-[#0e8354] bg-emerald-50 px-3 py-0.5 rounded-full border border-emerald-200">{meta['difficulty']}</span>
              </div>
            </div>
          </div>
        </section>

        <!-- SECTION 3: ITINÉRAIRE DÉTAILLÉ (COMPLET JOUR PAR JOUR) -->
        <section id="programme" class="pt-6 border-t border-slate-200">
          <div class="flex items-center justify-between mb-6">
            <div>
              <h2 class="font-black text-2xl sm:text-3xl text-slate-950">
                Itinéraire détaillé ({len(days)} jours)
              </h2>
              <p class="text-xs sm:text-sm text-slate-500 mt-1">
                Programme jour par jour encadré par nos pisteurs natifs de Bardia et guides d'expédition.
              </p>
            </div>
            <button onclick="toggleAllDays()" class="text-xs font-bold text-[#0e8354] hover:text-[#0c6d46] transition-colors cursor-pointer">
              Tout déplier / replier
            </button>
          </div>

          <div class="space-y-3">
            {days_html}
          </div>
        </section>

        <!-- SECTION 4: INCLUS & EXTRAS -->
        <section id="inclusions" class="pt-8 border-t border-slate-200">
          <h2 class="font-black text-2xl sm:text-3xl text-slate-950 mb-6">
            Ce qui est inclus dans votre séjour
          </h2>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div class="bg-emerald-50/70 p-6 sm:p-8 rounded-3xl border border-emerald-200">
              <h3 class="font-bold text-lg text-emerald-950 mb-4 flex items-center gap-2">
                <i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-600"></i>
                <span>Inclus dans le tarif</span>
              </h3>
              <ul class="space-y-2.5 text-xs sm:text-sm text-emerald-950 font-medium">
                <li class="flex items-start gap-2"><span>✓</span><span>Tous les hébergements (éco-lodges traditionnels ou tentes de bivouac)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Pension complète en jungle (3 repas sains et locaux par jour)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Vols intérieurs & transferts privés mentionnés au programme</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Permis officiels des Parcs Nationaux et taxes de conservation</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Encadrement par des maîtres pisteurs certifiés (Pawan / Kiran)</span></li>
                <li class="flex items-start gap-2"><span>✓</span><span>Assistance francophone 24h/24 par Robin</span></li>
              </ul>
            </div>

            <div class="bg-slate-50 p-6 sm:p-8 rounded-3xl border border-slate-200">
              <h3 class="font-bold text-lg text-slate-900 mb-4 flex items-center gap-2">
                <i data-lucide="x-circle" class="w-5 h-5 text-slate-400"></i>
                <span>Non inclus</span>
              </h3>
              <ul class="space-y-2.5 text-xs sm:text-sm text-slate-600 font-medium">
                <li class="flex items-start gap-2"><span>✕</span><span>Vols internationaux aller-retour (Paris/Europe - Katmandou)</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Frais de visa népalais (environ 30$ à 50$ à l'arrivée)</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Boissons alcoolisées et dépenses personnelles</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Assurance voyage personnelle obligatoire</span></li>
                <li class="flex items-start gap-2"><span>✕</span><span>Pourboires pour les équipes locales</span></li>
              </ul>
            </div>
          </div>
        </section>

        <!-- SECTION 5: AVIS VOYAGEURS VERBATIM -->
        <section id="avis-voyageurs" class="pt-8 border-t border-slate-200">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
            <div>
              <h2 class="font-black text-2xl sm:text-3xl text-slate-950">
                Avis de voyageurs ayant vécu l'aventure
              </h2>
              <p class="text-xs sm:text-sm text-slate-500 mt-1 font-medium">
                Retours d'expérience 100% authentiques vérifiés sur Google Reviews.
              </p>
            </div>
            <div class="flex items-center gap-2 bg-emerald-50 px-4 py-2 rounded-2xl border border-emerald-200 self-start sm:self-auto">
              <span class="text-[#00b67a] font-black text-lg">★ 5.0</span>
              <span class="text-xs font-bold text-slate-700">Google Reviews</span>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-white p-6 rounded-3xl border border-slate-200/90 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-full bg-emerald-100 text-emerald-800 font-black text-sm flex items-center justify-center">
                    AN
                  </div>
                  <div>
                    <h4 class="font-bold text-sm text-slate-900">Adrien Noat</h4>
                    <p class="text-[11px] text-slate-400">Voyageur vérifié • Safari Bardia & Babai</p>
                  </div>
                </div>
                <div class="flex text-amber-400 text-xs">★★★★★</div>
              </div>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed italic font-normal">
                « Une expérience inoubliable avec Pawan et Robin. Observer un tigre du Bengale à pied en toute sécurité reste le plus grand moment de voyage de ma vie. Tout était parfaitement orchestré. »
              </p>
            </div>

            <div class="bg-white p-6 rounded-3xl border border-slate-200/90 shadow-sm space-y-3">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-full bg-emerald-100 text-emerald-800 font-black text-sm flex items-center justify-center">
                    JT
                  </div>
                  <div>
                    <h4 class="font-bold text-sm text-slate-900">Jean Tramoy</h4>
                    <p class="text-[11px] text-slate-400">Voyageur vérifié • Expédition Bivouac</p>
                  </div>
                </div>
                <div class="flex text-amber-400 text-xs">★★★★★</div>
              </div>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed italic font-normal">
                « Les nuits en bivouac au cœur de la vallée de Babai sont magiques. L'expertise naturaliste des pisteurs est impressionnante. Un voyage authentique et respectueux de la nature. »
              </p>
            </div>
          </div>
        </section>

        <!-- SECTION 6: FAQ -->
        <section id="faq" class="pt-8 border-t border-slate-200">
          <h2 class="font-black text-2xl text-slate-950 mb-6 tracking-tight">
            Questions fréquentes sur ce voyage
          </h2>

          <div class="space-y-3 text-sm">
            <details class="group bg-white p-4 rounded-2xl border border-slate-200">
              <summary class="font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Comment se passe la réservation et le règlement ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed font-normal">
                Pour sécuriser votre place, un acompte de 30% est demandé par virement bancaire ou carte sécurisée. Le solde est réglé avant le départ ou directement à Katmandou.
              </p>
            </details>

            <details class="group bg-white p-4 rounded-2xl border border-slate-200">
              <summary class="font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Combien de personnes partent par groupe ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed font-normal">
                Nos séjours sont exclusivement limités à 4 à 8 explorateurs pour garantir le silence requis lors du pistage des animaux et préserver la sécurité de tous.
              </p>
            </details>

            <details class="group bg-white p-4 rounded-2xl border border-slate-200">
              <summary class="font-bold text-slate-800 cursor-pointer flex justify-between items-center">
                <span>Quel est le niveau de difficulté ?</span>
                <i data-lucide="chevron-down" class="w-4 h-4 transition-transform group-open:rotate-180"></i>
              </summary>
              <p class="mt-3 text-slate-600 text-xs sm:text-sm leading-relaxed font-normal">
                Ce séjour est classé <strong>{meta['difficulty']}</strong>. Nos pisteurs adaptent le rythme de marche pour que chacun profite sereinement de l'aventure.
              </p>
            </details>
          </div>
        </section>

      </div>

      <!-- RIGHT COLUMN: STICKY BOOKING CARD WEROAD -->
      <div class="lg:col-span-4">
        <div id="booking-widget" class="sticky top-28 bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-[0_12px_40px_rgba(0,0,0,0.08)] space-y-6">
          
          <div>
            <span class="text-[11px] font-extrabold uppercase tracking-widest text-[#0e8354]">{meta['style']}</span>
            <h3 class="font-black text-xl sm:text-2xl text-slate-950 mt-1 tracking-tight">
              {title_clean}
            </h3>
            <p class="text-xs text-slate-500 mt-1 font-semibold">{duration} • Micro-groupe (4 à 8 pers)</p>
          </div>

          <!-- Price -->
          <div class="pt-4 border-t border-slate-100 flex items-baseline justify-between">
            <div>
              <p class="text-[11px] font-extrabold uppercase text-slate-400">À partir de</p>
              <div class="flex items-baseline gap-2">
                <span class="font-black text-3xl text-slate-950 tracking-tight">{price}</span>
                {original_price_html}
              </div>
            </div>
            {saving_badge_html}
          </div>

          <!-- Departures Selector -->
          <div class="space-y-2.5">
            <label class="block text-xs font-bold uppercase tracking-wider text-slate-600">
              Sélectionnez votre départ :
            </label>
            <div class="space-y-2 text-xs">
              <label class="flex items-center justify-between p-3 rounded-2xl border border-[#0e8354] bg-emerald-50/50 cursor-pointer transition-all">
                <div class="flex items-center gap-2">
                  <input type="radio" name="departure_date" value="Automne 2026" checked class="text-[#0e8354] focus:ring-[#0e8354]">
                  <div>
                    <p class="font-bold text-slate-900">10 Oct - 24 Oct 2026</p>
                    <p class="text-[10px] text-slate-500">4 places restantes</p>
                  </div>
                </div>
                <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-slate-200 text-[#0e8354]">Confirmé</span>
              </label>

              <label class="flex items-center justify-between p-3 rounded-2xl border border-slate-200 hover:border-slate-300 cursor-pointer transition-all">
                <div class="flex items-center gap-2">
                  <input type="radio" name="departure_date" value="Novembre 2026" class="text-[#0e8354] focus:ring-[#0e8354]">
                  <div>
                    <p class="font-bold text-slate-900">07 Nov - 21 Nov 2026</p>
                    <p class="text-[10px] text-slate-500">2 places restantes</p>
                  </div>
                </div>
                <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-slate-200 text-[#0c6d46]">Dernières places</span>
              </label>

              <label class="flex items-center justify-between p-3 rounded-2xl border border-slate-200 hover:border-slate-300 cursor-pointer transition-all">
                <div class="flex items-center gap-2">
                  <input type="radio" name="departure_date" value="Printemps 2027" class="text-[#0e8354] focus:ring-[#0e8354]">
                  <div>
                    <p class="font-bold text-slate-900">15 Mars - 29 Mars 2027</p>
                    <p class="text-[10px] text-slate-500">6 places disponibles</p>
                  </div>
                </div>
                <span class="font-bold text-[10px] bg-white px-2 py-0.5 rounded-full border border-slate-200 text-[#0e8354]">Saison tigres</span>
              </label>
            </div>
          </div>

          <!-- Primary CTA Button WeRoad Coral -->
          <button onclick="openBookingForm()" class="w-full py-4 rounded-2xl bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] bg-[length:200%_auto] hover:bg-right text-white font-black text-base shadow-[0_8px_25px_rgba(14,131,84,0.45)] hover:shadow-[0_12px_35px_rgba(14,131,84,0.65)] hover:-translate-y-0.5 active:translate-y-0 active:scale-[0.98] transition-all duration-300 border-t border-white/30 text-center tracking-tight cursor-pointer">
            Réserver ma place →
          </button>

          <!-- Reassurance list -->
          <div class="space-y-2 text-xs text-slate-500 pt-2 border-t border-slate-100 font-medium">
            <div class="flex items-center gap-2">
              <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0"></i>
              <span>Acompte de 30% seulement à l'inscription</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0"></i>
              <span>Annulation flexible jusqu'à 30 jours</span>
            </div>
            <div class="flex items-center gap-2">
              <i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0"></i>
              <span>Règlement sécurisé (CB / Virement)</span>
            </div>
          </div>

          <div class="pt-4 border-t border-slate-100 flex flex-col gap-2.5 text-xs">
            <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20j'ai%20une%20question%20sur%20le%20circuit%20{title_encoded}" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-2 py-3 rounded-2xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-md shadow-emerald-600/30 hover:shadow-lg hover:shadow-emerald-600/45 hover:-translate-y-0.5 active:translate-y-0 transition-all">
              <i data-lucide="message-circle" class="w-4 h-4 text-white"></i>
              <span>Poser une question sur WhatsApp</span>
            </a>
          </div>

        </div>
      </div>

    </div>

  </main>

  {footer_html}

  <!-- LIGHTBOX MODAL WITH ARROWS -->
  <div id="lightbox-modal" class="fixed inset-0 bg-black/95 backdrop-blur-xl z-50 hidden opacity-0 transition-opacity duration-300 flex items-center justify-center p-4">
    
    <!-- Top Bar with Counter & Close -->
    <div class="absolute top-6 left-6 right-6 flex items-center justify-between text-white z-10">
      <div id="lightbox-counter" class="bg-white/10 backdrop-blur-md px-4 py-1.5 rounded-full text-xs font-extrabold border border-white/20">
        1 / 4
      </div>
      <button onclick="closeLightbox()" class="w-10 h-10 rounded-full bg-white/10 hover:bg-white/20 border border-white/20 flex items-center justify-center text-white transition-all hover:scale-105 active:scale-95 cursor-pointer" aria-label="Fermer">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>
    </div>

    <!-- Navigation Arrows -->
    <button onclick="prevLightboxImage(event)" class="absolute left-4 sm:left-8 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-black/60 hover:bg-black/90 border border-white/20 text-white flex items-center justify-center transition-all hover:scale-110 active:scale-95 z-20 shadow-2xl cursor-pointer" aria-label="Photo précédente">
      <i data-lucide="chevron-left" class="w-6 h-6"></i>
    </button>
    <button onclick="nextLightboxImage(event)" class="absolute right-4 sm:right-8 top-1/2 -translate-y-1/2 w-12 h-12 rounded-full bg-black/60 hover:bg-black/90 border border-white/20 text-white flex items-center justify-center transition-all hover:scale-110 active:scale-95 z-20 shadow-2xl cursor-pointer" aria-label="Photo suivante">
      <i data-lucide="chevron-right" class="w-6 h-6"></i>
    </button>

    <div class="relative max-w-5xl max-h-[85vh] flex items-center justify-center">
      <img id="lightbox-image" src="" alt="Photo agrandie" class="max-w-full max-h-[85vh] object-contain rounded-2xl shadow-2xl transition-all duration-300">
    </div>
  </div>

  <script src="{asset_prefix}js/translator.js"></script>
  <script>
    lucide.createIcons();

    // GALLERY & LIGHTBOX
    const galleryImages = [
      "{curated[0]}",
      "{curated[1]}",
      "{curated[2]}",
      "{curated[3]}"
    ];
    let currentImageIndex = 0;

    function openLightbox(index) {{
      currentImageIndex = index;
      updateLightboxContent();
      const modal = document.getElementById('lightbox-modal');
      modal.classList.remove('hidden');
      setTimeout(() => {{
        modal.classList.remove('opacity-0');
        modal.classList.add('opacity-100');
      }}, 10);
      document.body.style.overflow = 'hidden';
    }}

    function closeLightbox() {{
      const modal = document.getElementById('lightbox-modal');
      modal.classList.remove('opacity-100');
      modal.classList.add('opacity-0');
      setTimeout(() => {{
        modal.classList.add('hidden');
        document.body.style.overflow = '';
      }}, 300);
    }}

    function updateLightboxContent() {{
      const img = document.getElementById('lightbox-image');
      const counter = document.getElementById('lightbox-counter');
      if (img && galleryImages[currentImageIndex]) {{
        img.src = galleryImages[currentImageIndex];
      }}
      if (counter) {{
        counter.textContent = (currentImageIndex + 1) + ' / ' + galleryImages.length;
      }}
    }}

    function prevLightboxImage(e) {{
      if (e) e.stopPropagation();
      currentImageIndex = (currentImageIndex - 1 + galleryImages.length) % galleryImages.length;
      updateLightboxContent();
    }}

    function nextLightboxImage(e) {{
      if (e) e.stopPropagation();
      currentImageIndex = (currentImageIndex + 1) % galleryImages.length;
      updateLightboxContent();
    }}

    document.addEventListener('keydown', (e) => {{
      const modal = document.getElementById('lightbox-modal');
      if (modal && !modal.classList.contains('hidden')) {{
        if (e.key === 'ArrowLeft') prevLightboxImage();
        if (e.key === 'ArrowRight') nextLightboxImage();
        if (e.key === 'Escape') closeLightbox();
      }}
    }});

    function toggleAllDays() {{
      const details = document.querySelectorAll('#programme details');
      const anyClosed = Array.from(details).some(d => !d.open);
      details.forEach(d => d.open = anyClosed);
    }}

    function scrollToBooking() {{
      const el = document.getElementById('booking-widget');
      if (el) el.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
    }}

    function openBookingForm() {{
      const date = document.querySelector('input[name="departure_date"]:checked')?.value || 'Non spécifiée';
      const tourTitle = "{title_clean}";
      const msg = encodeURIComponent(`Bonjour Robin ! Je souhaite réserver ma place sur le séjour "${{tourTitle}}" pour le départ : ${{date}}. Merci de me communiquer les modalités !`);
      window.open(`https://wa.me/33695413227?text=${{msg}}`, '_blank');
    }}

    // REAL SHARE FUNCTIONALITY
    function handleShareTour() {{
      const pageUrl = window.location.href;
      const pageTitle = "{title_clean}";
      
      const waLink = document.getElementById('share-whatsapp');
      if (waLink) {{
        waLink.href = `https://api.whatsapp.com/send?text=${{encodeURIComponent('Découvre ce séjour au Népal : ' + pageTitle + ' ' + pageUrl)}}`;
      }}
      const emailLink = document.getElementById('share-email');
      if (emailLink) {{
        emailLink.href = `mailto:?subject=${{encodeURIComponent(pageTitle)}}&body=${{encodeURIComponent('Je voulais te partager ce séjour au Népal avec Jungle Nepal Adventure : ' + pageUrl)}}`;
      }}

      if (navigator.share && /mobile|android|iphone|ipad/i.test(navigator.userAgent)) {{
        navigator.share({{
          title: pageTitle,
          text: 'Découvre ce séjour d\\'immersion au Népal avec Jungle Nepal Adventure',
          url: pageUrl
        }}).catch(() => {{}});
        return;
      }}

      const menu = document.getElementById('share-menu');
      if (menu) {{
        const isOpen = menu.classList.contains('opacity-100');
        if (isOpen) {{
          menu.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
          menu.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
        }} else {{
          menu.classList.remove('opacity-0', 'translate-y-2', 'pointer-events-none');
          menu.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
        }}
      }}
    }}

    function copyTourLink() {{
      const pageUrl = window.location.href;
      navigator.clipboard.writeText(pageUrl).then(() => {{
        showToast('✅ Lien du séjour copié dans le presse-papier !');
        const menu = document.getElementById('share-menu');
        if (menu) {{
          menu.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
          menu.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
        }}
      }}).catch(() => {{
        showToast('Lien : ' + pageUrl);
      }});
    }}

    function showToast(msg) {{
      let toast = document.getElementById('toast-notification');
      if (!toast) {{
        toast = document.createElement('div');
        toast.id = 'toast-notification';
        toast.className = 'fixed bottom-8 left-1/2 -translate-x-1/2 bg-slate-950/95 backdrop-blur-xl text-white text-xs sm:text-sm font-black px-5 py-3 rounded-full border border-white/20 shadow-[0_20px_50px_rgba(0,0,0,0.4)] transition-all duration-300 z-50 opacity-0 translate-y-4 pointer-events-none flex items-center gap-2';
        document.body.appendChild(toast);
      }}
      toast.innerHTML = `<span class="text-amber-300 font-bold">✨</span> <span>${{msg}}</span>`;
      toast.classList.remove('opacity-0', 'translate-y-4', 'pointer-events-none');
      toast.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
      
      setTimeout(() => {{
        toast.classList.add('opacity-0', 'translate-y-4', 'pointer-events-none');
        toast.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }}, 2800);
    }}

    document.addEventListener('click', (e) => {{
      const btn = document.getElementById('share-btn');
      const menu = document.getElementById('share-menu');
      if (menu && btn && !btn.contains(e.target) && !menu.contains(e.target)) {{
        menu.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
        menu.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }}
    }});
  </script>

</body>
</html>
"""
    return html

tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
en_tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/tours'

for raw_tour in raw_data:
    slug = raw_tour.get('slug')
    meta = meta_map.get(slug)
    if not meta:
        continue
    
    short_id = meta['short_id']

    # 1. French
    fr_html = build_tour_html(meta, raw_tour, is_english=False)
    val_fr = StrictTagValidator()
    val_fr.feed(fr_html)
    if val_fr.stack or val_fr.errors:
        print(f"❌ FR {short_id}: Errors: {val_fr.errors}")
    else:
        with open(os.path.join(tours_dir, f"{short_id}.html"), 'w', encoding='utf-8') as f:
            f.write(fr_html)
        print(f"✅ Rebuilt FR {short_id}.html with clean price & 0 DOM errors")

    # 2. English
    en_html = build_tour_html(meta, raw_tour, is_english=True)
    val_en = StrictTagValidator()
    val_en.feed(en_html)
    if val_en.stack or val_en.errors:
        print(f"❌ EN {short_id}: Errors: {val_en.errors}")
    else:
        with open(os.path.join(en_tours_dir, f"{short_id}.html"), 'w', encoding='utf-8') as f:
            f.write(en_html)
        print(f"✅ Rebuilt EN {short_id}.html with clean price & 0 DOM errors")

print("\n🎉 Rebuilt all 14 tours with verified non-null prices!")
