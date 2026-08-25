import re

# Read template from tiji-mustang.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/tiji-mustang.astro', 'r', encoding='utf-8') as f:
    template = f.read()

# Build the complete French snow leopard page
fr_page = template

# Title & Meta
fr_page = fr_page.replace(
    'title="Tiji Festival – Upper Mustang | Jungle Nepal Adventure"',
    'title="Expédition : Panthère des Neiges Exclusive (17 jours) | Jungle Nepal Adventure"'
)
fr_page = fr_page.replace(
    'Tiji Festival – Upper Mustang',
    'Expédition : Panthère des Neiges Exclusive'
)
fr_page = fr_page.replace(
    '13 jours',
    '17 jours'
)
fr_page = fr_page.replace(
    '13j',
    '17j'
)

# Price
fr_page = re.sub(r'(\b\d[\d\s]*\s*€)', '4 300 €', fr_page) # Update pricing displays to 4 300 €

# Photos in mosaic
# Photo 1 (Big): Snow Leopard portrait
# Photo 2 (Mid): Snow Leopard on high cliff
# Photo 3 (Top right): Annapurna range
# Photo 4 (Bottom right): Pokhara Phewa Lake
fr_page = re.sub(
    r'<div class="grid grid-cols-1 md:grid-cols-4 gap-3 rounded-3xl overflow-hidden h-\[340px\] sm:h-\[460px\] mb-8 relative shadow-lg">.*?</div>\s*<!-- STICKY SUB-NAV',
    """<div class="grid grid-cols-1 md:grid-cols-4 gap-3 rounded-3xl overflow-hidden h-[340px] sm:h-[460px] mb-8 relative shadow-lg">
      <!-- Photo 1 : Portrait Panthère des Neiges (Grande gauche) -->
      <div class="md:col-span-2 h-full overflow-hidden">
        <img 
          src="/assets/snow-leopard/snow_leopard_portrait.jpg" 
          alt="Panthère des Neiges dans l'Himalaya - Portrait" 
          class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer"
          onclick="openLightbox(0)" 
        />
      </div>

      <!-- Photo 2 : Panthère des Neiges sur les falaises de Manang (Milieu) -->
      <div class="hidden md:block md:col-span-1 h-full overflow-hidden">
        <img 
          src="/assets/snow-leopard/snow_leopard_wild_cliff.jpg" 
          alt="Panthère des Neiges en liberté sur les falaises de haute altitude" 
          class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer"
          onclick="openLightbox(1)" 
        />
      </div>

      <!-- Photos 3 & 4 : Annapurna & Pokhara (Colonne droite) -->
      <div class="hidden md:flex flex-col gap-3 h-full">
        <!-- Photo 3 : Chaîne des Annapurnas -->
        <div class="h-1/2 overflow-hidden rounded-tr-2xl">
          <img 
            src="/assets/snow-leopard/annapurna_peaks.jpg" 
            alt="Chaîne des Annapurnas et haute vallée de Manang" 
            class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer"
            onclick="openLightbox(2)" 
          />
        </div>
        <!-- Photo 4 : Pokhara et le lac Phewa -->
        <div class="h-1/2 overflow-hidden rounded-br-2xl relative">
          <img 
            src="/assets/snow-leopard/pokhara_lake.jpg" 
            alt="Pokhara, Lac Phewa et vue sur les sommets de l'Himalaya" 
            class="w-full h-full object-cover hover:scale-105 transition-transform duration-700 cursor-pointer"
            onclick="openLightbox(3)" 
          />
        </div>
      </div>

      <button onclick="openLightbox(0)" class="absolute bottom-4 right-4 bg-white/95 backdrop-blur-md hover:bg-white text-slate-900 font-bold text-xs sm:text-sm px-4 py-2 rounded-xl shadow-lg border border-slate-200 flex items-center gap-2 transition-all hover:scale-105">
        <svg class="w-4 h-4 text-[#0e8354] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect><circle cx="9" cy="9" r="2"></circle><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path></svg>
        <span>Voir toutes les photos (4)</span>
      </button>
    </div>
    <!-- STICKY SUB-NAV""",
    fr_page,
    flags=re.DOTALL
)

# Section Aperçu
apercu_html = """        <!-- SECTION 1: APERÇU -->
        <section id="apercu" class="space-y-6">
          <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-normal">
            Partez sur les traces du félin le plus insaisissable et mythique de la planète : la <strong>Panthère des Neiges</strong> (<em>Panthera uncia</em>, le Fantôme des Montagnes). Au cœur de la haute vallée sauvage de Manang (3 600 m – 4 500 m) et des contreforts sacrés des Annapurnas, cette expédition exclusive de 17 jours allie acclimatation progressive, <strong>9 jours complets de pistage intensif</strong> avec nos maîtres pisteurs himalayens spécialisés, et immersion culturelle bouddhiste au monastère séculaire de Braka Gompa.
          </p>

          <!-- Key Highlights Bento Metrics -->
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-2">
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80">
              <span class="text-xs font-bold text-slate-500 block">Durée Totale</span>
              <span class="text-base sm:text-lg font-black text-slate-900">17 Jours</span>
            </div>
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80">
              <span class="text-xs font-bold text-slate-500 block">Pistage Terrain</span>
              <span class="text-base sm:text-lg font-black text-[#0e8354]">9 Jours pleins</span>
            </div>
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80">
              <span class="text-xs font-bold text-slate-500 block">Taille Groupe</span>
              <span class="text-base sm:text-lg font-black text-slate-900">4 à 8 explorateurs</span>
            </div>
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80">
              <span class="text-xs font-bold text-slate-500 block">Altitude Max</span>
              <span class="text-base sm:text-lg font-black text-amber-600">4 200 m</span>
            </div>
          </div>
        </section>"""

fr_page = re.sub(
    r'<section id="apercu".*?</section>',
    apercu_html,
    fr_page,
    flags=re.DOTALL
)

# Section Pour Moi / Profil Voyageur
pour_moi_html = """        <!-- SECTION 2: PROFIL VOYAGEUR & POINTS FORTS -->
        <section id="pour-moi" class="space-y-6">
          <div class="p-6 sm:p-8 rounded-3xl bg-slate-950 text-white space-y-6 border border-emerald-500/20 shadow-xl">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-2xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center text-emerald-400 text-lg font-bold">
                🐾
              </div>
              <div>
                <h2 class="text-xl sm:text-2xl font-black text-white tracking-tight">Ce voyage est fait pour vous si...</h2>
                <p class="text-xs sm:text-sm text-slate-400 font-medium">Une expédition naturaliste rare et engagée</p>
              </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs sm:text-sm">
              <div class="flex items-start gap-2.5">
                <span class="text-emerald-400 font-black">✓</span>
                <span class="text-slate-300">Vous rêvez d'observer le prédateur le plus secret des hautes altitudes dans son sanctuaire naturel.</span>
              </div>
              <div class="flex items-start gap-2.5">
                <span class="text-emerald-400 font-black">✓</span>
                <span class="text-slate-300">Vous appréciez les affûts matinaux patients et l'observation au télescope HD avec des spécialistes.</span>
              </div>
              <div class="flex items-start gap-2.5">
                <span class="text-emerald-400 font-black">✓</span>
                <span class="text-slate-300">Vous recherchez un équilibre parfait entre marche d'altitude, culture Newar et spiritualité tibétaine.</span>
              </div>
              <div class="flex items-start gap-2.5">
                <span class="text-emerald-400 font-black">✓</span>
                <span class="text-slate-300">Vous souhaitez voyager en micro-groupe exclusif (max 8 personnes) avec encadrement d'élite.</span>
              </div>
            </div>
          </div>
        </section>"""

fr_page = re.sub(
    r'<section id="pour-moi".*?</section>',
    pour_moi_html,
    fr_page,
    flags=re.DOTALL
)

# Section Programme Jour par Jour (17 Jours)
programme_html = """        <!-- SECTION 3: ITINÉRAIRE JOUR PAR JOUR (17J) -->
        <section id="programme" class="space-y-6">
          <div class="flex items-center justify-between">
            <h2 class="font-black text-2xl text-slate-950 tracking-tight">Itinéraire Jour par Jour (17 jours)</h2>
            <span class="text-xs font-bold text-[#0e8354] bg-emerald-50 border border-emerald-200 px-3 py-1 rounded-full">Expédition Exclusive</span>
          </div>

          <div class="space-y-4 relative before:absolute before:inset-0 before:left-4 before:w-0.5 before:bg-slate-200">
            
            <!-- J1 -->
            <div class="relative pl-10 space-y-2 p-5 rounded-2xl bg-white border border-slate-200 shadow-sm hover:border-emerald-500/40 transition-colors">
              <div class="absolute left-2.5 top-6 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <div class="flex items-center justify-between">
                <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 1</span>
                <span class="text-[11px] font-bold text-slate-400">Arrivée & Immersion</span>
              </div>
              <h3 class="font-black text-base sm:text-lg text-slate-900">Arrivée à Katmandou – Transfert direct vers la cité historique de Bhaktapur</h3>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                Accueil à l'aéroport international et transfert direct vers la cité historique de Bhaktapur. Installation à l'hôtel et présentation de l'expédition. Ce choix permet une première immersion culturelle immédiate, à l'écart de l'agitation du centre de la capitale.
              </p>
            </div>

            <!-- J2 -->
            <div class="relative pl-10 space-y-2 p-5 rounded-2xl bg-white border border-slate-200 shadow-sm hover:border-emerald-500/40 transition-colors">
              <div class="absolute left-2.5 top-6 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <div class="flex items-center justify-between">
                <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 2</span>
                <span class="text-[11px] font-bold text-slate-400">Vol panoramique</span>
              </div>
              <h3 class="font-black text-base sm:text-lg text-slate-900">Vol Katmandou – Pokhara : Panorama sur les Annapurnas & Temps libre</h3>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                Vol domestique de 30 minutes vers Pokhara, offrant un panorama unique sur la chaîne des Annapurnas. Temps libre l’après-midi pour explorer les abords du lac Phewa, les temples, organiser les derniers préparatifs et profiter de la vue sur les montagnes. Nuit à l'hôtel.
              </p>
            </div>

            <!-- J3 -->
            <div class="relative pl-10 space-y-2 p-5 rounded-2xl bg-white border border-slate-200 shadow-sm hover:border-emerald-500/40 transition-colors">
              <div class="absolute left-2.5 top-6 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <div class="flex items-center justify-between">
                <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 3</span>
                <span class="text-[11px] font-bold text-slate-400">Remontée de vallée (2 700 m)</span>
              </div>
              <h3 class="font-black text-base sm:text-lg text-slate-900">Pokhara – Chame (2 700 m) : Route 4x4, premier palier & Sources chaudes</h3>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                Départ en véhicule privatif pour Chame (environ 6h de piste). Ce trajet marque le début de la remontée de la vallée. Premier palier d'acclimatation à l'altitude. En fin de journée, accès aux sources d'eau chaude naturelles en bord de rivière. Nuit à l'hôtel.
              </p>
            </div>

            <!-- J4 -->
            <div class="relative pl-10 space-y-2 p-5 rounded-2xl bg-white border border-slate-200 shadow-sm hover:border-emerald-500/40 transition-colors">
              <div class="absolute left-2.5 top-6 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <div class="flex items-center justify-between">
                <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 4</span>
                <span class="text-[11px] font-bold text-slate-400">Haute altitude (3 600 m)</span>
              </div>
              <h3 class="font-black text-base sm:text-lg text-slate-900">Chame – Manang (3 600 m) & Marche d'acclimatation au Lac de Gangapurna</h3>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                Trajet de 2 heures pour rejoindre Manang. Pour valider ce deuxième palier de contrôle d'acclimatation, une marche est programmée vers le lac glaciaire turquoise de Gangapurna. Nuit à l'hôtel.
              </p>
            </div>

            <!-- J5-13 -->
            <div class="relative pl-10 space-y-3 p-6 sm:p-7 rounded-3xl bg-gradient-to-br from-emerald-950/90 to-slate-950 text-white border border-emerald-500/30 shadow-2xl">
              <div class="absolute left-2.5 top-8 w-3.5 h-3.5 rounded-full bg-amber-400 border-2 border-slate-950 shadow"></div>
              <div class="flex items-center justify-between">
                <span class="text-xs font-black uppercase tracking-widest text-amber-300">Jours 5 à 13 (9 Jours)</span>
                <span class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 text-[11px] font-extrabold border border-emerald-500/30">Cœur de l'Expédition</span>
              </div>
              <h3 class="font-black text-xl sm:text-2xl text-white tracking-tight">
                Expédition Léopard des Neiges – 9 Jours de suivi et de pistage intensif
              </h3>
              <p class="text-xs sm:text-sm text-slate-300 leading-relaxed font-normal">
                Neuf jours complets sur le terrain dédiés au suivi et à l'observation du Léopard des neiges aux côtés de nos maîtres pisteurs himalayens expérimentés munis de longues-vues HD Swarovski. L'itinéraire intègre une flexibilité permettant d'effectuer une journée de césure et de transition culturelle au monastère de Braka Gompa, un site historique majeur vieux de 600 ans.
              </p>
              <div class="pt-2 flex flex-wrap gap-2 text-[11px] font-bold text-amber-200">
                <span class="px-2.5 py-1 rounded-lg bg-white/10 border border-white/15">🐾 Affûts crépusculaires</span>
                <span class="px-2.5 py-1 rounded-lg bg-white/10 border border-white/15">🔭 Longues-vues HD</span>
                <span class="px-2.5 py-1 rounded-lg bg-white/10 border border-white/15">🕉️ Braka Gompa (600 ans)</span>
              </div>
            </div>

            <!-- J14 -->
            <div class="relative pl-10 space-y-2 p-5 rounded-2xl bg-white border border-slate-200 shadow-sm hover:border-emerald-500/40 transition-colors">
              <div class="absolute left-2.5 top-6 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <div class="flex items-center justify-between">
                <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 14</span>
                <span class="text-[11px] font-bold text-slate-400">Village Newar</span>
              </div>
              <h3 class="font-black text-base sm:text-lg text-slate-900">Manang – Bandipur : Descente et découverte du village traditionnel</h3>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                Amorce de la descente des hautes altitudes. Trajet de 6 à 7 heures de route pour rejoindre Bandipur, un village traditionnel Newar reconnu pour son architecture préservée et son panorama sur les sommets environnants. Nuit sur place.
              </p>
            </div>

            <!-- J15 -->
            <div class="relative pl-10 space-y-2 p-5 rounded-2xl bg-white border border-slate-200 shadow-sm hover:border-emerald-500/40 transition-colors">
              <div class="absolute left-2.5 top-6 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <div class="flex items-center justify-between">
                <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 15</span>
                <span class="text-[11px] font-bold text-slate-400">Retour Capitale</span>
              </div>
              <h3 class="font-black text-base sm:text-lg text-slate-900">Bandipur – Katmandou & Fin de journée libre à Thamel</h3>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                Route de retour vers Katmandou (environ 4h de trajet). Installation à l'hôtel et fin de journée libre pour se reposer et explorer le quartier de Thamel.
              </p>
            </div>

            <!-- J16 -->
            <div class="relative pl-10 space-y-2 p-5 rounded-2xl bg-white border border-slate-200 shadow-sm hover:border-emerald-500/40 transition-colors">
              <div class="absolute left-2.5 top-6 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <div class="flex items-center justify-between">
                <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 16</span>
                <span class="text-[11px] font-bold text-slate-400">Patrimoine UNESCO</span>
              </div>
              <h3 class="font-black text-base sm:text-lg text-slate-900">Visite culturelle de Katmandou et quartier de Thamel</h3>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                Journée consacrée à la découverte des grands sites culturels de la vallée de Katmandou (Swayambhunath, Pashupatinath, ruelles artisanales).
              </p>
            </div>

            <!-- J17 -->
            <div class="relative pl-10 space-y-2 p-5 rounded-2xl bg-white border border-slate-200 shadow-sm hover:border-emerald-500/40 transition-colors">
              <div class="absolute left-2.5 top-6 w-3 h-3 rounded-full bg-[#0e8354] border-2 border-white shadow"></div>
              <div class="flex items-center justify-between">
                <span class="text-xs font-black uppercase tracking-wider text-[#0e8354]">Jour 17</span>
                <span class="text-[11px] font-bold text-slate-400">Départ</span>
              </div>
              <h3 class="font-black text-base sm:text-lg text-slate-900">Transfert à l'aéroport & Vol retour</h3>
              <p class="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                Transfert à l'aéroport international pour votre départ avec des images inoubliables du Fantôme des Montagnes.
              </p>
            </div>

          </div>
        </section>"""

fr_page = re.sub(
    r'<section id="programme".*?</section>',
    programme_html,
    fr_page,
    flags=re.DOTALL
)

# Inclusions
inclusions_html = """        <!-- SECTION 4: INCLUSIONS & EXCLUSIONS -->
        <section id="inclusions" class="space-y-6">
          <h2 class="font-black text-2xl text-slate-950 tracking-tight">Ce qui est inclus dans votre séjour</h2>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="p-6 sm:p-7 rounded-3xl bg-emerald-50/80 border border-emerald-200 space-y-4">
              <h3 class="font-extrabold text-base text-emerald-950 flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-[#0e8354] text-white flex items-center justify-center text-xs">✓</span>
                <span>Inclus dans le tarif (4 300 €)</span>
              </h3>
              <ul class="space-y-2.5 text-xs sm:text-sm text-slate-700">
                <li class="flex items-start gap-2.5"><span>•</span><span>Vol intérieur régulier Katmandou – Pokhara</span></li>
                <li class="flex items-start gap-2.5"><span>•</span><span>Tous les transferts et transports privatifs en 4x4 tout-terrain</span></li>
                <li class="flex items-start gap-2.5"><span>•</span><span>9 jours complets de pistage avec maîtres pisteurs himalayens</span></li>
                <li class="flex items-start gap-2.5"><span>•</span><span>Permis d'entrée de trek et d'expédition en zone protégée (ACAP)</span></li>
                <li class="flex items-start gap-2.5"><span>•</span><span>Hébergements en lodges traditionnels de montagne et hôtels de charme</span></li>
                <li class="flex items-start gap-2.5"><span>•</span><span>Pension complète durant l'ensemble de l'expédition en montagne</span></li>
                <li class="flex items-start gap-2.5"><span>•</span><span>Équipement d'optique longue-vue haute définition partagé</span></li>
                <li class="flex items-start gap-2.5"><span>•</span><span>Assistance francophone 24/7 avec Robin</span></li>
              </ul>
            </div>

            <div class="p-6 sm:p-7 rounded-3xl bg-slate-50 border border-slate-200 space-y-4">
              <h3 class="font-extrabold text-base text-slate-900 flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-slate-300 text-slate-700 flex items-center justify-center text-xs">✕</span>
                <span>Non inclus</span>
              </h3>
              <ul class="space-y-2.5 text-xs sm:text-sm text-slate-600">
                <li class="flex items-start gap-2.5"><span>•</span><span>Vols internationaux aller-retour jusqu'à Katmandou</span></li>
                <li class="flex items-start gap-2.5"><span>•</span><span>Visa pour le Népal (obtenu facilement à l'arrivée)</span></li>
                <li class="flex items-start gap-2.5"><span>•</span><span>Assurance secours & rapatriement en haute altitude (obligatoire)</span></li>
                <li class="flex items-start gap-2.5"><span>•</span><span>Boissons personnelles, snacks et pourboires pour l'équipe</span></li>
              </ul>
            </div>
          </div>
        </section>"""

fr_page = re.sub(
    r'<section id="inclusions".*?</section>',
    inclusions_html,
    fr_page,
    flags=re.DOTALL
)

# Right Column Booking Sidebar
sidebar_html = """      <!-- RIGHT COLUMN: STICKY BOOKING BOX -->
      <div class="lg:col-span-4">
        <div id="booking-card" class="sticky top-28 bg-slate-950 text-white rounded-3xl p-6 sm:p-7 border border-emerald-500/30 shadow-[0_20px_50px_rgba(0,0,0,0.5)] space-y-6">
          
          <div class="flex items-baseline justify-between border-b border-white/10 pb-4">
            <div>
              <span class="text-xs font-bold text-slate-400">Tarif par personne</span>
              <p class="text-3xl sm:text-4xl font-black text-amber-300 tracking-tight">4 300 €</p>
            </div>
            <span class="text-xs font-bold px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
              17 jours tout compris
            </span>
          </div>

          <div class="space-y-3 text-xs text-slate-300">
            <div class="flex items-center justify-between">
              <span>👥 Taille du groupe :</span>
              <strong class="text-white">4 à 8 explorateurs max</strong>
            </div>
            <div class="flex items-center justify-between">
              <span>📅 Meilleure période :</span>
              <strong class="text-amber-300">Nov – Mars (hiver himalayen)</strong>
            </div>
            <div class="flex items-center justify-between">
              <span>🏔️ Sanctuaire :</span>
              <strong class="text-white">Vallée de Manang (Annapurnas)</strong>
            </div>
            <div class="flex items-center justify-between">
              <span>🐾 Pistage terrain :</span>
              <strong class="text-emerald-400">9 jours complets</strong>
            </div>
          </div>

          <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20suis%20intéressé%20par%20l'expédition%20Panthère%20des%20Neiges%20(4300€)" target="_blank" rel="noopener noreferrer" class="w-full flex items-center justify-center gap-2 py-3.5 px-6 rounded-full bg-gradient-to-r from-[#0e8354] via-[#109363] to-[#0e8354] hover:brightness-110 text-white font-black text-sm shadow-lg shadow-[#0e8354]/40 hover:scale-105 active:scale-95 transition-all text-center">
            <svg class="w-5 h-5 text-white shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
            <span>Réserver via WhatsApp (Robin)</span>
          </a>

          <p class="text-[11px] text-center text-slate-400 font-medium">
            Réponse garantie en moins de 2 heures. Échange direct avec Robin pour la liste d'équipement grand froid et la logistique.
          </p>

        </div>
      </div>"""

fr_page = re.sub(
    r'<div class="lg:col-span-4">\s*<div id="booking-card".*?</div>\s*</div>\s*</div>',
    sidebar_html + '\n    </div>',
    fr_page,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/panthere-des-neiges.astro', 'w', encoding='utf-8') as f:
    f.write(fr_page)

# Generate English version
en_page = fr_page.replace('lang="fr"', 'lang="en"')
en_page = en_page.replace('title="Expédition : Panthère des Neiges Exclusive (17 jours) | Jungle Nepal Adventure"', 'title="Exclusive Snow Leopard Expedition (17 Days) | Jungle Nepal Adventure"')
en_page = en_page.replace('Expédition : Panthère des Neiges Exclusive', 'Exclusive Snow Leopard Expedition')
en_page = en_page.replace('Accueil', 'Home')
en_page = en_page.replace('Nos 15 Séjours', 'Our 15 Expeditions')
en_page = en_page.replace('17 jours tout compris', '17 days all-inclusive')
en_page = en_page.replace('Tarif par personne', 'Price per person')
en_page = en_page.replace('Taille du groupe :', 'Group Size:')
en_page = en_page.replace('4 à 8 explorateurs max', '4 to 8 explorers max')
en_page = en_page.replace('Meilleure période :', 'Best Season:')
en_page = en_page.replace('Nov – Mars (hiver himalayen)', 'Nov – March (Himalayan winter)')
en_page = en_page.replace('Sanctuaire :', 'Sanctuary:')
en_page = en_page.replace('Vallée de Manang (Annapurnas)', 'Manang Valley (Annapurnas)')
en_page = en_page.replace('Pistage terrain :', 'Field Tracking:')
en_page = en_page.replace('9 jours complets', '9 full days')
en_page = en_page.replace('Réserver via WhatsApp (Robin)', 'Book via WhatsApp (Robin)')
en_page = en_page.replace('/tours/panthere-des-neiges.html', '/en/tours/panthere-des-neiges.html')
en_page = en_page.replace('Voir toutes les photos (4)', 'View all photos (4)')
en_page = en_page.replace("import Layout from '../../layouts/Layout.astro';", "import Layout from '../../../layouts/Layout.astro';")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/tours/panthere-des-neiges.astro', 'w', encoding='utf-8') as f:
    f.write(en_page)

print("Generated full-fidelity French and English Snow Leopard pages!")
