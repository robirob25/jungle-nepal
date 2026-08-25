import os
import json
import re

exact_google_url = "https://www.google.com/search?sca_esv=a1a5ed640a4c7c37&cs=0&sxsrf=APpeQntnDL5GNsUQ_hIZE3WXkqPaN3biMw:1787312489201&q=Jungle+Nepal+Adventure+Avis&rflfq=1&num=20&stick=H4sIAAAAAAAAAONgkxK2MDA0NLY0MLYwNjUxMzMwMzMy3sDI-IpR2qs0Lz0nVcEvtSAxR8ExpSw1r6S0KFXBsSyzeBErPlkAWhIrKFYAAAA&rldimm=8011390383546606623&tbm=lcl&hl=fr-FR&sa=X&ved=2ahUKEwjW85Pw0bGWAxVfTaQEHX8wKpkQ9fQKegQIERAG&biw=1470&bih=798&dpr=2#lkt=LocalPoiReviews"

# Translation dictionaries for all common terms and specific components
FR_TO_EN = [
    ("L'autre côté du Népal", "The Other Side of Nepal"),
    ("Là où les routes s'arrêtent.", "Where roads end."),
    ("Là où les territoires sauvages recommencent.", "Where wild territories begin."),
    ("Guidé par ceux qui y vivent.", "Guided by those who live there."),
    ("Offrez-vous votre voyage nature au Népal.", "Experience the ultimate wildlife safari in Nepal."),
    ("Tous les 14 circuits", "All 14 Adventures"),
    ("Tous les 14 séjours", "All 14 Trips"),
    ("Toute l'année (Saison 2026–2027)", "All year (Season 2026–2027)"),
    ("Rechercher un séjour", "Find an Adventure"),
    ("Idées de séjours :", "Featured Expeditions:"),
    ("Départs garantis • Petits groupes de 4 à 8 explorateurs", "Guaranteed Departures • Small Groups of 4 to 8 Explorers"),
    ("Les 14 séjours immersifs au Népal", "14 Immersive Expeditions in Nepal"),
    ("Sélectionnez votre aventure pour explorer le détail jour par jour, la fiche d'inclusions et réserver votre place.", "Select your adventure to explore day-by-day itineraries, inclusions and reserve your spot."),
    ("Affichage de", "Showing"),
    ("séjours", "trips"),
    ("Tous les séjours", "All Trips"),
    ("Safaris et pistage Bardia", "Bardia Safari & Tracking"),
    ("Bivouacs et nuits sauvages", "Wild Bivouac & Camping"),
    ("Chitwan et rhinocéros", "Chitwan & Rhinos"),
    ("Treks et lac Rara", "Treks & Rara Lake"),
    ("Culture et immersions", "Culture & Spiritual"),
    ("Voir le séjour →", "View Trip Details →"),
    ("Voir le séjour", "View Trip"),
    ("Départs confirmés 2026/2027", "Confirmed Departures 2026/2027"),
    ("Vivre la jungle à hauteur d'homme.", "Experience the Jungle at Eye Level."),
    ("Découvrez les images réelles de nos safaris à pied avec Pawan, Robin et les maîtres pisteurs de Bardia.", "Discover raw, authentic footage from our walking safaris with Pawan, Robin and Bardia master trackers."),
    ("Immersion sur le terrain", "On-Field Immersion"),
    ("Explorer les 14 séjours 2026/2027 →", "Explore All 14 Trips 2026/2027 →"),
    ("Échanger avec Robin sur WhatsApp", "Chat with Robin on WhatsApp"),
    ("Nos Maîtres Pisteurs & Guides", "Our Master Trackers & Guides"),
    ("L'alliance humaine franco-népalaise au service de la faune", "A Unique Franco-Nepalese Alliance Dedicated to Wildlife"),
    ("Ce que disent nos voyageurs.", "What Our Travelers Say."),
    ("Note globale", "Overall rating"),
    ("basée sur les retours d'expérience vérifiés • 100% d'avis 5 étoiles ⭐", "based on verified traveler reviews • 100% 5-star rating ⭐"),
    ("Consulter tous les 19 avis vérifiés sur Google (5.0 / 5)", "Read all 19 verified reviews on Google (5.0 / 5)"),
    ("Foire aux questions", "Frequently Asked Questions"),
    ("Tout ce qu'il faut savoir avant de partir en safari au Népal", "Everything you need to know before going on safari in Nepal"),
    ("© 2026 Jungle Nepal Adventure • Tous droits réservés.", "© 2026 Jungle Nepal Adventure • All rights reserved."),
    ("WhatsApp direct", "Direct WhatsApp"),
    ("Itinéraire détaillé", "Detailed Itinerary"),
    ("Inclus & Extras", "Inclusions & Extras"),
    ("À propos", "About Us"),
    ("Contacte-nous", "Contact Us"),
    ("Contact", "Contact"),
    ("Avis 5.0", "Reviews 5.0"),
    ("Avis", "Reviews"),
    ("Départs & Prix", "Dates & Prices"),
    ("Partager ce séjour", "Share this trip"),
    ("Copier le lien direct", "Copy direct link"),
    ("Envoyer sur WhatsApp", "Send on WhatsApp"),
    ("Partager par Email", "Share via Email"),
    ("Voir toutes les destinations →", "View All Destinations →"),
    ("Parc national de Bardia", "Bardia National Park"),
    ("Tigres du Bengale & safaris à pied", "Bengal Tigers & Walking Safaris"),
    ("Parc national de Chitwan", "Chitwan National Park"),
    ("Rhinocéros & pirogues de la Rapti", "One-Horned Rhinos & River Canoes"),
    ("Parc national de Suklaphanta", "Suklaphanta National Park"),
    ("Cerfs des marais & ouest sauvage", "Swamp Deer & Untamed Wild West"),
    ("Les Annapurna & Pokhara", "Annapurna Range & Pokhara"),
    ("Sommets mythiques & balcons alpins", "Sacred Peaks & Alpine Balconies"),
    ("Katmandou", "Kathmandu Valley"),
    ("Vallée des rois & temples sacrés", "Valley of Gods & Sacred Temples"),
    ("Fiche pratique", "Practical Guide"),
    ("Meilleure période", "Best Season"),
    ("Mode d'exploration", "Exploration Mode"),
    ("Format de groupe", "Group Size"),
    ("Encadrement", "Guidance & Trackers"),
    ("Hébergement", "Accommodation"),
    ("Poser une question sur cette destination →", "Ask a question about this destination →"),
    ("Aperçu visuel de", "Visual Showcase of"),
    ("Les séjours immersifs à", "Immersive Expeditions in"),
    ("Départs garantis en micro-groupes. Cliquez sur un circuit pour consulter le programme jour par jour.", "Guaranteed small group departures. Click on any trip to see day-by-day itineraries."),
    ("Saison 2026/2027", "Season 2026/2027"),
    ("Espèces emblématiques observées :", "Iconic Wildlife Encountered:"),
    ("Faune & Flore d'altitude :", "High-Altitude Wildlife & Flora:"),
    ("Patrimoine & Lieux sacrés :", "Sacred Heritage & Landmarks:"),
    ("Tigre royal du Bengale", "Royal Bengal Tiger"),
    ("Grand Rhinocéros unicorne", "Greater One-Horned Rhino"),
    ("Éléphant sauvage d'Asie", "Wild Asian Elephant"),
    ("Cerf des marais", "Swamp Deer (Barasingha)"),
    ("Dauphin du Gange", "Ganges River Dolphin"),
    ("Crocodile Gavial", "Gharial Crocodile"),
    ("Ours lippu (Sloth Bear)", "Sloth Bear"),
    ("Léopard indien", "Indian Leopard"),
    ("Monal de l'Himalaya (oiseau national)", "Himalayan Monal (National Bird)"),
    ("Mouton bleu (Bharal)", "Blue Sheep (Bharal)"),
    ("Cerf porte-musc", "Musk Deer"),
    ("Tahr de l'Himalaya", "Himalayan Tahr"),
    ("Grand Stûpa de Bodnath", "Boudhanath Stupa"),
    ("Sanctuaire de Pashupatinath", "Pashupatinath Temple"),
    ("Cité médiévale de Bhaktapur", "Medieval City of Bhaktapur"),
    ("Temple des singes (Swayambhunath)", "Monkey Temple (Swayambhunath)"),
    ("Palais royaux de Patan", "Patan Royal Palace"),
    ("Rizières de Nagarkot", "Nagarkot Terraces"),
    ("Nos Destinations", "Our Destinations"),
    ("Sanctuaires Sauvages du Népal", "Nepal's Wild Sanctuaries"),
    ("Des sanctuaires inviolés du Terai aux sommets himalayens, découvrez les 5 grands territoires explorés avec nos maîtres pisteurs.", "From pristine Terai jungles to majestic Himalayan heights, explore the 5 sacred regions guided by our master trackers."),
    ("Explorer la région", "Explore this region"),
    ("Découvrir la destination →", "Discover Destination →"),
    ("Territoire", "Territory"),
    ("Mode d'approche", "Approach"),
    ("Grande Faune", "Big Wildlife"),
    ("Micro-Groupes", "Small Groups"),
    ("100% à pied", "100% On Foot"),
    ("Tigres & Rhinos", "Tigers & Rhinos"),
    ("4 à 8 pers. max", "4 to 8 pers. max"),
    ("Bardia & Babai", "Bardia & Babai Valley"),
    ("Langue", "Language"),
    ("Changer de langue", "Change Language"),
    ("Français", "French"),
    ("Anglais", "English")
]

def make_globe_dropdown(is_english=False, rel_depth=0):
    fr_active = not is_english
    en_active = is_english
    
    # Calculate links
    prefix_to_root = "../" * rel_depth
    
    if is_english:
        # On english page, link to FR equivalent
        fr_href = prefix_to_root + ("index.html" if rel_depth == 0 else "")
        en_href = "#"
    else:
        # On french page, link to EN equivalent
        fr_href = "#"
        en_href = prefix_to_root + "en/" + ("index.html" if rel_depth == 0 else "")

    return f"""<!-- LANGUAGE SWITCHER (GLOBE) -->
      <div class="relative group/lang py-1">
        <button class="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white/10 hover:bg-white/20 border border-white/20 backdrop-blur-md flex items-center justify-center text-white transition-all duration-200 hover:scale-105 active:scale-95 cursor-pointer" aria-label="Change language">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
          </svg>
        </button>
        <div class="absolute right-0 top-full mt-1.5 w-44 opacity-0 translate-y-2 pointer-events-none group-hover/lang:opacity-100 group-hover/lang:translate-y-0 group-hover/lang:pointer-events-auto transition-all duration-200 z-50">
          <div style="background-color: #041d13 !important;" class="border border-white/20 rounded-2xl p-1.5 shadow-2xl space-y-0.5 text-xs font-bold text-white">
            <a href="{fr_href}" class="flex items-center justify-between px-3 py-2 rounded-xl {'bg-white/15 text-[#10b981]' if fr_active else 'text-slate-300 hover:bg-white/10 hover:text-white'} transition-colors">
              <span class="flex items-center gap-2"><span>🇫🇷</span><span>Français</span></span>
              {('<svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 text-[#10b981]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>' if fr_active else '')}
            </a>
            <a href="{en_href}" class="flex items-center justify-between px-3 py-2 rounded-xl {'bg-white/15 text-[#10b981]' if en_active else 'text-slate-300 hover:bg-white/10 hover:text-white'} transition-colors">
              <span class="flex items-center gap-2"><span>🇬🇧</span><span>English</span></span>
              {('<svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 text-[#10b981]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg>' if en_active else '')}
            </a>
          </div>
        </div>
      </div>"""

def translate_html_content(html, rel_depth=0):
    out = html
    # Replace html lang
    out = out.replace('<html lang="fr"', '<html lang="en"')
    
    # Translate terms
    for fr, en in FR_TO_EN:
        out = out.replace(fr, en)
        
    return out

# 1. Update French index.html with interactive Globe
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    fr_index = f.read()

globe_fr = make_globe_dropdown(is_english=False, rel_depth=0)
# Replace static globe button in hero/header
fr_index = re.sub(r'<button class=\"w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-white/10.*?aria-label=\"Changer de langue\">.*?</button>', globe_fr, fr_index, flags=re.DOTALL)
if 'group/lang' not in fr_index:
    # Insert next to whatsapp button
    fr_index = fr_index.replace('<span>WhatsApp direct</span>\n        </a>', f'<span>WhatsApp direct</span>\n        </a>\n        {globe_fr}')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(fr_index)

# 2. Build English index.html (en/index.html)
en_index = translate_html_content(fr_index, rel_depth=1)
# Update links to point locally in en/
en_index = en_index.replace('href="destinations/index.html"', 'href="destinations/index.html"')
en_index = en_index.replace('href="tours/', 'href="tours/')
en_index = en_index.replace('href="a-propos.html"', 'href="a-propos.html"')
en_index = en_index.replace('href="contact.html"', 'href="contact.html"')
en_index = en_index.replace('src="assets/', 'src="../assets/')

# Update globe in English index
globe_en = make_globe_dropdown(is_english=True, rel_depth=1)
en_index = re.sub(r'<!-- LANGUAGE SWITCHER \(GLOBE\) -->.*?</div>\s*</div>\s*</div>', globe_en, en_index, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/index.html', 'w', encoding='utf-8') as f:
    f.write(en_index)

print("Generated en/index.html successfully!")

# 3. Build English a-propos.html and contact.html
for fname in ['a-propos.html', 'contact.html']:
    src_path = os.path.join('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal', fname)
    if not os.path.exists(src_path):
        continue
    with open(src_path, 'r', encoding='utf-8') as f:
        fr_page = f.read()
    
    # Add globe on FR page
    globe_fr_sub = make_globe_dropdown(is_english=False, rel_depth=0)
    fr_page = re.sub(r'<!-- LANGUAGE SWITCHER \(GLOBE\) -->.*?</div>\s*</div>\s*</div>', globe_fr_sub, fr_page, flags=re.DOTALL)
    if 'group/lang' not in fr_page:
        fr_page = fr_page.replace('<span>WhatsApp direct</span>\n        </a>', f'<span>WhatsApp direct</span>\n        </a>\n        {globe_fr_sub}')
    with open(src_path, 'w', encoding='utf-8') as f:
        f.write(fr_page)
        
    # Translate and write EN page
    en_page = translate_html_content(fr_page, rel_depth=1)
    en_page = en_page.replace('src="assets/', 'src="../assets/')
    en_page = en_page.replace('href="index.html"', 'href="index.html"')
    globe_en_sub = make_globe_dropdown(is_english=True, rel_depth=1)
    en_page = re.sub(r'<!-- LANGUAGE SWITCHER \(GLOBE\) -->.*?</div>\s*</div>\s*</div>', globe_en_sub, en_page, flags=re.DOTALL)
    
    with open(os.path.join('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en', fname), 'w', encoding='utf-8') as f:
        f.write(en_page)
        
print("Generated en/a-propos.html and en/contact.html successfully!")

# 4. Build English destinations/*.html
dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations'
for fname in os.listdir(dest_dir):
    if not fname.endswith('.html'):
        continue
    src_path = os.path.join(dest_dir, fname)
    with open(src_path, 'r', encoding='utf-8') as f:
        fr_dest = f.read()
    
    # Update FR dest with globe
    globe_fr_dest = make_globe_dropdown(is_english=False, rel_depth=1)
    fr_dest = re.sub(r'<!-- LANGUAGE SWITCHER \(GLOBE\) -->.*?</div>\s*</div>\s*</div>', globe_fr_dest, fr_dest, flags=re.DOTALL)
    if 'group/lang' not in fr_dest:
        fr_dest = fr_dest.replace('<span>WhatsApp direct</span>\n        </a>', f'<span>WhatsApp direct</span>\n        </a>\n        {globe_fr_dest}')
    with open(src_path, 'w', encoding='utf-8') as f:
        f.write(fr_dest)

    # Translate EN dest
    en_dest = translate_html_content(fr_dest, rel_depth=2)
    en_dest = en_dest.replace('src="../assets/', 'src="../../assets/')
    globe_en_dest = make_globe_dropdown(is_english=True, rel_depth=2)
    en_dest = re.sub(r'<!-- LANGUAGE SWITCHER \(GLOBE\) -->.*?</div>\s*</div>\s*</div>', globe_en_dest, en_dest, flags=re.DOTALL)
    
    with open(os.path.join('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/destinations', fname), 'w', encoding='utf-8') as f:
        f.write(en_dest)

print("Generated en/destinations/*.html successfully!")

# 5. Build English tours/*.html
tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'):
        continue
    src_path = os.path.join(tours_dir, fname)
    with open(src_path, 'r', encoding='utf-8') as f:
        fr_tour = f.read()

    # Add globe on FR tour
    globe_fr_tour = make_globe_dropdown(is_english=False, rel_depth=1)
    fr_tour = re.sub(r'<!-- LANGUAGE SWITCHER \(GLOBE\) -->.*?</div>\s*</div>\s*</div>', globe_fr_tour, fr_tour, flags=re.DOTALL)
    if 'group/lang' not in fr_tour:
        fr_tour = fr_tour.replace('<button onclick="scrollToBooking()"', f'{globe_fr_tour}\n      <button onclick="scrollToBooking()"')
    with open(src_path, 'w', encoding='utf-8') as f:
        f.write(fr_tour)

    # Translate EN tour
    en_tour = translate_html_content(fr_tour, rel_depth=2)
    en_tour = en_tour.replace('src="../assets/', 'src="../../assets/')
    globe_en_tour = make_globe_dropdown(is_english=True, rel_depth=2)
    en_tour = re.sub(r'<!-- LANGUAGE SWITCHER \(GLOBE\) -->.*?</div>\s*</div>\s*</div>', globe_en_tour, en_tour, flags=re.DOTALL)

    with open(os.path.join('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/en/tours', fname), 'w', encoding='utf-8') as f:
        f.write(en_tour)

print("Generated en/tours/*.html successfully!")
