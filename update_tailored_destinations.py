import json
import os

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/processed_tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

exact_google_url = "https://www.google.com/search?sca_esv=a1a5ed640a4c7c37&cs=0&sxsrf=APpeQntnDL5GNsUQ_hIZE3WXkqPaN3biMw:1787312489201&q=Jungle+Nepal+Adventure+Avis&rflfq=1&num=20&stick=H4sIAAAAAAAAAONgkxK2MDA0NLY0MLYwNjUxMzMwMzMy3sDI-IpR2qs0Lz0nVcEvtSAxR8ExpSw1r6S0KFXBsSyzeBErPlkAWhIrKFYAAAA&rldimm=8011390383546606623&tbm=lcl&hl=fr-FR&sa=X&ved=2ahUKEwjW85Pw0bGWAxVfTaQEHX8wKpkQ9fQKegQIERAG&biw=1470&bih=798&dpr=2#lkt=LocalPoiReviews"

destinations_data = {
    "bardia": {
        "title": "Parc national de Bardia",
        "badge": "🐅 Sanctuaire Suprême du Tigre du Bengale",
        "tag_h2": "Sanctuaire sauvage",
        "title_h2": "Le royaume sauvage du tigre du Bengale",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2025/12/Tigre-Bardia.png",
        "intro": "Avant sa création officielle en 1988, le parc national de Bardia était une réserve de chasse royale dédiée à la monarchie népalaise. Sa transformation en sanctuaire protégé a permis de préserver l'un des écosystèmes les plus sauvages et intacts d'Asie.",
        "description_p1": "Aujourd'hui, le parc national de Bardia est le véritable sanctuaire de la faune sauvage au Népal. S'étendant sur 968 km² de forêts de sals denses, de savanes herbeuses et de méandres fluviaux le long de la rivière Karnali, il abrite la plus dense population de tigres du Bengale en liberté du pays.",
        "description_p2": "Contrairement aux parcs touristiques bondés, Bardia se découvre principalement à pied, accompagné de deux maîtres pisteurs natifs. Vous pisterez le tigre, le grand rhinocéros indien, les hardes d'éléphants sauvages, les cerfs chitals et le discret léopard dans un silence absolu.",
        "fiche_items": [
            ("Meilleure période", "D'octobre à mai (Pic d'observation des tigres aux points d'eau entre mars et mai)"),
            ("Mode d'exploration", "Safaris silencieux à pied (walking safari), affûts, jeep 4x4 ouverte et canoë"),
            ("Encadrement d'élite", "2 maîtres pisteurs natifs certifiés par groupe (dont Pawan, ex-BBC Wildlife)"),
            ("Format de groupe", "Micro-groupes exclusifs de 4 à 8 explorateurs max pour garantir le silence"),
            ("Hébergement", "Éco-lodges de brousse en bordure de parc & campements sauvages en tente à Babai")
        ],
        "culture_tag": "Gardiens de la forêt",
        "culture_title": "La communauté Tharu & l'harmonie avec la forêt",
        "culture_text": "Les Tharus sont les gardiens indigènes de Bardia. Vivant en lisière du sanctuaire depuis des siècles, ils possèdent une connaissance intime des plantes médicinales, des pistes animales et des équilibres sacrés de la jungle. Nos séjours intègrent des nuits chez l'habitant et des repas traditionnels cuisinés au feu de bois.",
        "fauna_label": "Espèces emblématiques observées :",
        "fauna_highlight": ["Tigre royal du Bengale", "Grand Rhinocéros unicorne", "Éléphant sauvage d'Asie", "Cerf des marais", "Dauphin du Gange", "Crocodile Gavial"],
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/12/Safari-a-pied-Bardia.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/tigre-sur-route.png",
            "https://junglenepal.com/wp-content/uploads/2017/01/Campement-dans-la-jungle-Bardia-Nepalc.jpg",
            "https://junglenepal.com/wp-content/uploads/2025/12/Tharu-danse.png"
        ],
        "related_tours": ["nepal-sauvage", "babai-special", "bardia-babai-camping", "bardia-explorateur", "bardia-nuit-sauvage", "jungle-extreme"]
    },
    "chitwan": {
        "title": "Parc national de Chitwan",
        "badge": "🦏 Patrimoine Mondial de l'UNESCO",
        "tag_h2": "Biodiversité du Terai",
        "title_h2": "Le sanctuaire historique des grands rhinocéros",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png",
        "intro": "Classé au patrimoine mondial de l’UNESCO depuis 1984, le parc national de Chitwan abrite l'une des biodiversités les plus spectaculaires et foisonnantes du continent asiatique.",
        "description_p1": "Le parc national de Chitwan est mondialement reconnu comme le meilleur endroit pour observer le grand rhinocéros indien à une corne (Rhinoceros unicornis) dans son habitat naturel. Les plaines inondables et les hautes herbes à éléphants offrent des scènes animalières d'une rare intensité.",
        "description_p2": "Entre safaris en jeep ouverte, marches silencieuses dans la jungle avec nos guides experts et balades douces en canoë traditionnel sur la rivière Rapti au milieu des gavials et des oiseaux migrateurs, Chitwan allie aventure brute et confort d'écolodges chaleureux.",
        "fiche_items": [
            ("Meilleure période", "D'octobre à avril (Climat doux et herbes coupées favorisant l'observation)"),
            ("Mode d'exploration", "Safaris en jeep 4x4, pirogues traditionnelles sur la Rapti et marches d'approche"),
            ("Faune principale", "Grand rhinocéros unicorne, ours lippu, crocodile gavial, éléphants et 500+ oiseaux"),
            ("Format de voyage", "Séjours accessibles à tous, idéaux en famille, couple ou micro-groupes"),
            ("Hébergement", "Éco-lodges de charme avec jardins tropicaux en bordure de rivière")
        ],
        "culture_tag": "Traditions du Terai",
        "culture_title": "Culture Tharu & artisanat local",
        "culture_text": "Les villages bordant Chitwan perpétuent des traditions millénaires : maisons en torchis ornées de fresques sacrées, danses des bâtons au clair de lune et cuisine locale parfumée. Chaque séjour contribue directement à la vitalité de ces communautés.",
        "fauna_label": "Espèces emblématiques observées :",
        "fauna_highlight": ["Grand Rhinocéros unicorne", "Tigre du Bengale", "Ours lippu (Sloth Bear)", "Crocodile Gavial du Gange", "Cerf sambar", "500+ espèces d'oiseaux"],
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/03/68.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/ours-lippu-chitwan.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/elephants-1900332_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2025/12/tharu-1.jpg"
        ],
        "related_tours": ["chitwan-culture", "chitwan-bardia-complete", "nepal-immersion-totale"]
    },
    "suklaphanta": {
        "title": "Parc national de Suklaphanta",
        "badge": "🦌 L'Éden Sauvage Hors des Sentiers Battus",
        "tag_h2": "Expédition Ouest Sauvage",
        "title_h2": "Les grandes savanes vierges de l'Extrême-Ouest",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2025/12/Suklaphata-1024x585-1.jpg",
        "intro": "Situé à l'extrême ouest du Népal, à la frontière de l'Inde, le parc national de Suklaphanta est l'un des territoires les plus sauvages, préservés et secrets de tout l'Himalaya.",
        "description_p1": "Suklaphanta est mondialement réputé pour abriter la plus grande harde de cerfs des marais (Barasingha) au monde, comptant plus de 2 000 individus qui évoluent librement dans d'immenses prairies herbeuses dorées.",
        "description_p2": "Le parc constitue également un corridor biologique vital pour le tigre du Bengale, le léopard, les hardes d'éléphants sauvages et plus de 420 espèces d'oiseaux aquatiques et migrateurs. C'est l'expérience safari ultime pour les explorateurs en quête de solitude totale.",
        "fiche_items": [
            ("Meilleure période", "De novembre à mai (Période sèche idéale pour traverser les grandes plaines)"),
            ("Mode d'exploration", "Safaris 4x4 d'expédition, affûts naturalistes et miradors d'observation"),
            ("Caractère du séjour", "Immersion brute hors sentiers battus, 0% de tourisme de masse"),
            ("Accès logistique", "Vol intérieur vers Dhangadhi puis transfert privatisé en 4x4 d'expédition"),
            ("Hébergement", "Lodges authentiques locaux et bivouacs de brousse")
        ],
        "culture_tag": "Ethnies Rana Tharu",
        "culture_title": "L'Ouest authentique du Népal",
        "culture_text": "Loin de toute agitation touristique, Suklaphanta offre un contact authentique et émouvant avec les ethnies Rana Tharu de l'extrême ouest, réputées pour leurs costumes colorés ornés de bijoux d'argent et leur hospitalité sincère.",
        "fauna_label": "Espèces emblématiques observées :",
        "fauna_highlight": ["Cerf des marais (Barasingha)", "Tigre du Bengale", "Léopard indien", "Éléphant sauvage", "Florican du Bengale", "Chacal doré"],
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/12/Suklaphata-1024x585-1.jpg",
            "https://junglenepal.com/wp-content/uploads/2025/12/Elephant-sauvage-Bardia.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/2-1.png",
            "https://junglenepal.com/wp-content/uploads/2025/12/jungle-walk-Babai-valley.png"
        ],
        "related_tours": ["jungle-extreme", "rara-lake-bardia", "bardia-explorateur"]
    },
    "annapurna": {
        "title": "Les Annapurna & Pokhara",
        "badge": "🏔️ Sommets Sacrés & Balcons Himalayens",
        "tag_h2": "Treks alpins & paysages mythiques",
        "title_h2": "La verticalité majestueuse de l'Himalaya",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2017/01/himalayas-5817277_1920.jpg",
        "intro": "La région de l'Annapurna offre des contrastes géographiques et culturels vertigineux : des vallées subtropicales jusqu'aux parois de glace flirtant avec les 8 000 mètres d'altitude.",
        "description_p1": "Située au nord de la paisible ville de Pokhara, la région de l'Annapurna permet de vivre une randonnée alpine d'exception : balades contemplatives sur les crêtes de Poon Hill, traversées de forêts de rhododendrons géants ou immersion vers les sanctuaires sacrés.",
        "description_p2": "Combiner un trek dans les Annapurna avec un safari animalier dans le Terai (Bardia ou Chitwan) permet de vivre l'intégralité du Népal : la grandeur des géants de neige et la luxuriance mystique de la jungle.",
        "fiche_items": [
            ("Meilleure période", "Octobre à décembre (Ciel cristallin) et mars à mai (Rhododendrons en fleur)"),
            ("Altitude & Dénivelé", "De 800m (Pokhara) à plus de 3 200m / 4 130m selon l'itinéraire"),
            ("Niveau physique", "Accessible à tout bon marcheur (4 à 6h de marche par jour à rythme modéré)"),
            ("Logistique & Confort", "Nuits en lodges de montagne (tea houses) chaleureux et portage des sacs"),
            ("Encadrement", "Guides francophones certifiés haute montagne et équipe locale dévouée")
        ],
        "culture_tag": "Villages de montagne",
        "culture_title": "L'hospitalité des peuples Gurung & Magar",
        "culture_text": "Au fil des sentiers de pierre et des ponts suspendus au-dessus des torrents glaciaires, vous ferez étape dans des villages préservés où les montagnards Gurung vous accueilleront autour d'un thé chaud et d'un copieux Dal Bhat au coin du feu.",
        "fauna_label": "Faune & Flore d'altitude :",
        "fauna_highlight": ["Monal de l'Himalaya (oiseau national)", "Mouton bleu (Bharal)", "Cerf porte-musc", "Tahr de l'Himalaya", "Vautour de l'Himalaya", "Forêts de rhododendrons géants"],
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2026/01/Machapuchare-himalaya-montagne.png",
            "https://junglenepal.com/wp-content/uploads/2026/01/Himalaya-haut-sommet.png",
            "https://junglenepal.com/wp-content/uploads/2026/01/Nepal-Himalaya-hiver.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/1.png"
        ],
        "related_tours": ["tiji-mustang", "nepal-sauvage", "immersion-spirituelle", "carnet-de-voyage"]
    },
    "katmandou": {
        "title": "Katmandou & la Vallée des Rois",
        "badge": "🕉️ Cité Impériale & Cœur Spirituel",
        "tag_h2": "Patrimoine & Histoire",
        "title_h2": "Le cœur battant et sacré du Népal",
        "hero_img": "https://junglenepal.com/wp-content/uploads/2025/03/79.png",
        "intro": "Au premier abord, Katmandou peut sembler bouillonnante et déroutante. Mais laissez-lui quelques heures, et elle finit par vous enchanter par sa ferveur spirituelle et sa poésie intemporelle.",
        "description_p1": "Véritable musée à ciel ouvert classé par l'UNESCO, la vallée de Katmandou abrite les cités royales médiévales de Patan et Bhaktapur, le grand stûpa bouddhiste de Bodnath aux yeux bienveillants et le sanctuaire hindou de Pashupatinath au bord de la rivière sacrée Bagmati.",
        "description_p2": "C'est à Katmandou que commence chaque aventure avec Jungle Nepal Adventure. Nous y assurons un accueil francophone personnalisé dès l'aéroport, le briefing d'expédition avec l'équipe et la découverte des ruelles d'artisans à l'écart des foules.",
        "fiche_items": [
            ("Meilleure période", "Accessible toute l'année (Climat doux et ensoleillé d'octobre à mai)"),
            ("Points d'intérêt majeurs", "Bodnath, Pashupatinath, Swayambhunath, cités royales de Patan & Bhaktapur"),
            ("Mode d'exploration", "Visites guidées à pied dans les ruelles historiques & transferts privatifs"),
            ("Accueil & Logistique", "Prise en charge personnalisée dès l'atterrissage & briefing avec Robin"),
            ("Hébergement", "Éco-hôtels de charme et auberges de patrimoine au calme de la vallée")
        ],
        "culture_tag": "Artisanat d'exception",
        "culture_title": "Art Newar & ferveur millénaire",
        "culture_text": "Les maîtres artisans newars sculptent le bois, le cuivre et le bronze avec le même génie depuis des siècles. Les toits de pagodes dorées, les cours intérieures secrètes et les moulins à prières créent une atmosphère de sérénité inoubliable.",
        "fauna_label": "Patrimoine & Lieux sacrés :",
        "fauna_highlight": ["Grand Stûpa de Bodnath", "Sanctuaire de Pashupatinath", "Cité médiévale de Bhaktapur", "Temple des singes (Swayambhunath)", "Rizières de Nagarkot", "Palais royaux de Patan"],
        "gallery": [
            "https://junglenepal.com/wp-content/uploads/2025/03/79.png",
            "https://junglenepal.com/wp-content/uploads/2017/01/buddha-2641500_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2017/01/temple-5790023_1920.jpg",
            "https://junglenepal.com/wp-content/uploads/2026/01/Groupe-touriste-Nagarkot-Nepal.jpg"
        ],
        "related_tours": ["nepal-sauvage", "nepal-immersion-totale", "immersion-spirituelle", "carnet-de-voyage"]
    }
}

for dest_key, d in destinations_data.items():
    # Build matching cards
    matching_cards_html = ""
    for t in tours:
        short_id = t["short_id"]
        if short_id in d["related_tours"]:
            matching_cards_html += f"""
            <article class="bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between">
              <a href="../tours/{short_id}.html" class="relative h-64 overflow-hidden block group">
                <img src="{t.get('hero_img', d['hero_img'])}" alt="{t['title']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
                <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent"></div>
                <span class="absolute top-4 left-4 bg-slate-950/80 backdrop-blur-md text-amber-300 text-xs font-black px-3 py-1 rounded-full border border-amber-400/30">
                  {t['badge']}
                </span>
                <span class="absolute bottom-4 left-4 text-white font-black text-sm">
                  {t['duration']} • {t['price']}
                </span>
              </a>
              <div class="p-6 flex-1 flex flex-col justify-between">
                <div>
                  <h3 class="font-black text-lg text-slate-900 hover:text-[#0e8354] transition-colors leading-snug">
                    <a href="../tours/{short_id}.html">{t['title']}</a>
                  </h3>
                  <p class="mt-2 text-xs text-slate-600 line-clamp-2 font-normal">
                    {t['overview']}
                  </p>
                </div>
                <div class="mt-5 pt-4 border-t border-slate-100 flex items-center justify-between">
                  <span class="text-xs font-bold text-[#0e8354]">Départs confirmés 2026/2027</span>
                  <a href="../tours/{short_id}.html" class="px-4 py-2 rounded-full bg-[#0e8354] hover:bg-[#0c6d46] text-white font-extrabold text-xs shadow transition-all">
                    Voir le séjour →
                  </a>
                </div>
              </div>
            </article>
            """

    fauna_badges_html = "".join([f'<span class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-full bg-emerald-50 text-[#0e8354] text-xs font-extrabold border border-emerald-200 shadow-sm"><i data-lucide="check" class="w-3.5 h-3.5"></i><span>{f}</span></span>' for f in d["fauna_highlight"]])
    gallery_html = "".join([f'<div class="rounded-2xl overflow-hidden shadow-md h-60 group"><img src="{img}" alt="{d["title"]}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy"/></div>' for img in d["gallery"]])

    fiche_rows_html = ""
    for label, val in d["fiche_items"]:
        fiche_rows_html += f"""
        <div>
          <p class="text-xs font-bold uppercase tracking-wider text-slate-400">{label}</p>
          <p class="font-bold text-slate-900 mt-0.5">{val}</p>
        </div>
        """

    full_page = f"""<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{d['title']} | Destinations Jungle Nepal Adventure</title>
  <meta name="description" content="{d['intro'][:160]}">

  <!-- WeRoad Exact Font -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
          }},
          colors: {{
            jungle: {{
              50: '#f1f7f4',
              500: '#109363',
              600: '#0e8354',
              950: '#041d13',
            }},
            safari: {{
              50: '#faf8f5',
              100: '#f4efe6',
            }}
          }}
        }}
      }}
    }}
  </script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <style> body {{ font-family: 'Plus Jakarta Sans', sans-serif; }} </style>
</head>
<body class="bg-safari-50 text-slate-800 antialiased selection:bg-slate-950 selection:text-white">

  <!-- TOP BANNER -->
  <aside class="bg-gradient-to-r from-[#073021] via-[#0e5c3e] to-[#073021] text-white text-xs py-2.5 px-4 font-bold text-center border-b border-emerald-500/20 shadow-sm" id="top-bar">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      <div class="w-6 hidden sm:block"></div>
      <div class="flex-1 text-center whitespace-nowrap overflow-hidden text-ellipsis">
        <span>🐅 <strong>Saison 2026-2027</strong> : Départs garantis en micro-groupes • <strong>-100€</strong> avec le code <span class="bg-white/15 px-2 py-0.5 rounded text-amber-300 font-black">JUNGLE100</span></span>
      </div>
      <button onclick="document.getElementById('top-bar').style.display='none'" class="text-white/80 hover:text-white">✕</button>
    </div>
  </aside>

  <!-- NAVBAR SUR FOND BLANC AVEC LOGO NOIR TRANSPARENT -->
  <header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-0 z-40">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex items-center justify-between">
      
      <a href="../index.html" class="flex items-center gap-2 group shrink-0">
        <img src="../assets/logo_dark.png" alt="Jungle Nepal Adventure Logo" class="h-14 sm:h-16 w-auto object-contain group-hover:scale-105 transition-transform duration-300" />
      </a>

      <nav class="hidden lg:flex items-center gap-6 xl:gap-8 text-[14px] font-bold text-slate-700">
        <a href="../index.html#prochains-departs" class="hover:text-[#0e8354] transition-colors">Tous les 14 séjours</a>
        <div class="relative group py-2">
          <a href="index.html" class="text-[#0e8354] font-black border-b-2 border-[#0e8354] pb-0.5 flex items-center gap-1">
            <span>Destinations</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5 transition-transform duration-300 group-hover:rotate-180 opacity-80" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" /></svg>
          </a>
          <div class="absolute top-full left-0 pt-2 w-72 opacity-0 translate-y-2 pointer-events-none group-hover:opacity-100 group-hover:translate-y-0 group-hover:pointer-events-auto transition-all duration-300 z-50">
            <div class="bg-white/98 backdrop-blur-2xl border border-slate-200/90 rounded-3xl p-3 shadow-[0_20px_50px_rgba(0,0,0,0.15)] space-y-1 text-slate-900">
              <a href="bardia.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-slate-50 transition-colors">
                <div class="w-9 h-9 rounded-xl bg-emerald-50 text-[#0e8354] flex items-center justify-center font-bold text-sm shrink-0 border border-emerald-100">🐅</div>
                <div><p class="font-extrabold text-xs text-slate-900">Parc national de Bardia</p><p class="text-[10px] text-slate-500">Tigres du Bengale & safaris à pied</p></div>
              </a>
              <a href="chitwan.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-slate-50 transition-colors">
                <div class="w-9 h-9 rounded-xl bg-emerald-50 text-[#0e8354] flex items-center justify-center font-bold text-sm shrink-0 border border-emerald-100">🦏</div>
                <div><p class="font-extrabold text-xs text-slate-900">Parc national de Chitwan</p><p class="text-[10px] text-slate-500">Rhinocéros & pirogues de la Rapti</p></div>
              </a>
              <a href="suklaphanta.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-slate-50 transition-colors">
                <div class="w-9 h-9 rounded-xl bg-emerald-50 text-[#0e8354] flex items-center justify-center font-bold text-sm shrink-0 border border-emerald-100">🦌</div>
                <div><p class="font-extrabold text-xs text-slate-900">Parc national de Suklaphanta</p><p class="text-[10px] text-slate-500">Cerfs des marais & ouest sauvage</p></div>
              </a>
              <a href="annapurna.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-slate-50 transition-colors">
                <div class="w-9 h-9 rounded-xl bg-emerald-50 text-[#0e8354] flex items-center justify-center font-bold text-sm shrink-0 border border-emerald-100">🏔️</div>
                <div><p class="font-extrabold text-xs text-slate-900">Les Annapurna & Pokhara</p><p class="text-[10px] text-slate-500">Sommets mythiques & balcons alpins</p></div>
              </a>
              <a href="katmandou.html" class="flex items-center gap-3 p-2.5 rounded-2xl hover:bg-slate-50 transition-colors">
                <div class="w-9 h-9 rounded-xl bg-emerald-50 text-[#0e8354] flex items-center justify-center font-bold text-sm shrink-0 border border-emerald-100">🕉️</div>
                <div><p class="font-extrabold text-xs text-slate-900">Katmandou</p><p class="text-[10px] text-slate-500">Vallée des rois & temples sacrés</p></div>
              </a>
              <div class="pt-2 border-t border-slate-100 mt-1">
                <a href="index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] text-white font-black text-xs">Voir toutes les destinations →</a>
              </div>
            </div>
          </div>
        </div>
        <a href="../index.html#concept" class="hover:text-[#0e8354] transition-colors">L'esprit safari</a>
        <a href="../a-propos.html" class="hover:text-[#0e8354] transition-colors">À propos</a>
        <a href="{exact_google_url}" target="_blank" rel="noopener noreferrer" class="hover:text-[#0e8354] transition-colors flex items-center gap-1"><span class="text-[#00b67a]">★</span> Avis 5.0</a>
        <a href="../contact.html" class="hover:text-[#0e8354] transition-colors">Contacte-nous</a>
      </nav>

      <div class="flex items-center gap-3">
        <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20souhaite%20des%20informations%20sur%20{d['title']}" target="_blank" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#0e8354] hover:bg-[#0c6d46] text-white font-extrabold text-xs sm:text-[13px] shadow-md shadow-[#0e8354]/30 hover:scale-105 active:scale-95 transition-all">
          <i data-lucide="message-circle" class="w-4 h-4"></i>
          <span>WhatsApp direct</span>
        </a>
      </div>

    </div>
  </header>

  <!-- HERO DESTINATION -->
  <section class="relative min-h-[60vh] sm:min-h-[70vh] flex items-center justify-center py-20 px-4 sm:px-6 lg:px-8 overflow-hidden bg-slate-950">
    <div class="absolute inset-0 z-0">
      <img src="{d['hero_img']}" alt="{d['title']}" class="w-full h-full object-cover object-center filter brightness-75 contrast-105"/>
      <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/50 to-black/40"></div>
    </div>

    <div class="relative z-10 max-w-4xl mx-auto text-center flex flex-col items-center">
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/15 backdrop-blur-md border border-white/25 text-amber-300 text-xs font-black uppercase tracking-wider mb-6">
        <span>{d['badge']}</span>
      </div>

      <h1 class="font-black text-4xl sm:text-6xl md:text-7xl text-white tracking-tight leading-[1.08] drop-shadow-2xl">
        {d['title']}
      </h1>

      <p class="mt-6 text-base sm:text-xl text-slate-200 max-w-2xl font-medium leading-relaxed drop-shadow">
        {d['intro']}
      </p>
    </div>
  </section>

  <!-- CONTENU DÉTAILLÉ DE LA DESTINATION -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24 space-y-20">
    
    <!-- 1. PRÉSENTATION & FAUNE -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
      <div class="lg:col-span-7 space-y-6">
        <div class="inline-flex items-center gap-2 text-xs font-black uppercase tracking-wider text-[#0e8354] bg-emerald-50 px-3.5 py-1 rounded-full border border-emerald-200">
          <span>{d['tag_h2']}</span>
        </div>
        <h2 class="font-black text-3xl sm:text-4xl text-slate-950 tracking-tight leading-tight">
          {d['title_h2']}
        </h2>
        <p class="text-slate-600 text-base leading-relaxed font-normal">
          {d['description_p1']}
        </p>
        <p class="text-slate-600 text-base leading-relaxed font-normal">
          {d['description_p2']}
        </p>

        <!-- Highlights Tags -->
        <div class="pt-4 space-y-3">
          <p class="font-black text-xs uppercase tracking-wider text-slate-400">{d['fauna_label']}</p>
          <div class="flex flex-wrap gap-2">
            {fauna_badges_html}
          </div>
        </div>
      </div>

      <!-- Quick Info Fiche Pratique -->
      <div class="lg:col-span-5 bg-white rounded-3xl p-8 border border-slate-200/90 shadow-xl space-y-6">
        <h3 class="font-black text-xl text-slate-950 pb-3 border-b border-slate-100 flex items-center gap-2">
          <i data-lucide="info" class="w-5 h-5 text-[#0e8354]"></i>
          <span>Fiche pratique</span>
        </h3>
        
        <div class="space-y-4 text-sm">
          {fiche_rows_html}
        </div>

        <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20souhaite%20des%20renseignements%20sur%20{d['title']}" target="_blank" class="block w-full text-center py-3.5 rounded-2xl bg-gradient-to-r from-[#0e8354] to-[#109363] text-white font-extrabold text-xs shadow hover:scale-[1.02] active:scale-95 transition-all">
          Poser une question sur cette destination →
        </a>
      </div>
    </div>

    <!-- 2. CULTURE LOCALE SPÉCIFIQUE -->
    <div class="p-8 sm:p-12 rounded-3xl bg-safari-100 border border-slate-200">
      <div class="max-w-3xl space-y-4">
        <span class="inline-block text-xs font-black uppercase tracking-widest text-[#0e8354] bg-white px-3.5 py-1 rounded-full border border-slate-200">
          {d['culture_tag']}
        </span>
        <h3 class="font-black text-2xl sm:text-3xl text-slate-950 tracking-tight">
          {d['culture_title']}
        </h3>
        <p class="text-slate-700 text-sm sm:text-base leading-relaxed font-medium">
          {d['culture_text']}
        </p>
      </div>
    </div>

    <!-- 3. GALERIE PHOTO IMMERSIVE -->
    <div class="space-y-6">
      <div class="flex items-end justify-between">
        <div>
          <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Photographies du terrain</span>
          <h3 class="font-black text-2xl sm:text-3xl text-slate-950">Aperçu visuel de {d['title']}</h3>
        </div>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        {gallery_html}
      </div>
    </div>

    <!-- 4. CIRCUITS ASSOCIÉS À CETTE DESTINATION -->
    <div class="space-y-8 pt-8 border-t border-slate-200">
      <div>
        <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Saison 2026/2027</span>
        <h3 class="font-black text-2xl sm:text-4xl text-slate-950">Les séjours immersifs à {d['title']}</h3>
        <p class="text-slate-600 text-sm mt-1">Départs garantis en micro-groupes. Cliquez sur un circuit pour consulter le programme jour par jour.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        {matching_cards_html}
      </div>
    </div>

  </main>

  <!-- FOOTER -->
  <footer class="bg-slate-950 text-slate-300 pt-16 pb-12 border-t border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center sm:text-left">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-6 pb-12 border-b border-white/10 text-xs">
        <a href="../index.html"><img src="../assets/logo.png" alt="Logo" class="h-16 w-auto object-contain"/></a>
        <div class="flex flex-wrap gap-6 text-slate-400 font-bold">
          <a href="../index.html#prochains-departs" class="hover:text-white">Tous les 14 séjours</a>
          <a href="index.html" class="hover:text-white">Toutes les destinations</a>
          <a href="../a-propos.html" class="hover:text-white">À propos</a>
          <a href="../contact.html" class="hover:text-white">Contact</a>
        </div>
      </div>
      <p class="pt-8 text-xs text-slate-500 text-center">© 2026 Jungle Nepal Adventure • Tous droits réservés.</p>
    </div>
  </footer>

  <!-- BOUTON RETOUR EN HAUT ÉLÉGANT & GRAPHIQUE -->
  <button id="back-to-top" onclick="window.scrollTo({{ top: 0, behavior: 'smooth' }})" class="fixed bottom-6 right-6 sm:bottom-8 sm:right-8 z-40 hidden sm:flex items-center justify-center w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-slate-950/90 hover:bg-[#0e8354] text-white border border-white/25 shadow-[0_10px_30px_rgba(0,0,0,0.45)] backdrop-blur-xl transition-all duration-300 opacity-0 translate-y-4 pointer-events-none hover:scale-110 active:scale-95 group cursor-pointer" aria-label="Retour en haut">
    <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-white group-hover:-translate-y-1 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5">
      <path stroke-linecap="round" stroke-linejoin="round" d="M5 10l7-7m0 0l7 7m-7-7v18" />
    </svg>
  </button>
  <script>
    lucide.createIcons();
    window.addEventListener('scroll', () => {{
      const btn = document.getElementById('back-to-top');
      if (!btn) return;
      if (window.scrollY > 300) {{
        btn.classList.remove('opacity-0', 'translate-y-4', 'pointer-events-none');
        btn.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }} else {{
        btn.classList.add('opacity-0', 'translate-y-4', 'pointer-events-none');
        btn.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }}
    }});
  </script>
</body>
</html>
"""
    dest_path = f'/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations/{dest_key}.html'
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(full_page)
    print(f'Updated tailored destination: {dest_path}')

print("All destination pages overhauled with 100% tailored practical sheets!")
