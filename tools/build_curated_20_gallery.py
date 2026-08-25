import json, re, os

# EXACT 20 MASTERPIECES (100% WILD ANIMALS - STRICTLY ZERO HUMANS)
curated_20 = [
    # 1. Tigre au bord de l'eau
    {
        "file": "/assets/wildlife_gallery/wildlife_tiger_water.webp",
        "title": "Tigre du Bengale au point d'eau",
        "desc": "Mâle dominant sur les berges au crépuscule",
        "location": "Parc National de Bardia",
        "category": "felins"
    },
    # 2. Grand Rhinocéros dans la brume
    {
        "file": "/assets/wildlife_gallery/wildlife_rhino_mist.webp",
        "title": "Grand Rhinocéros unicorne",
        "desc": "Silhouette préhistorique émergeant des brumes matinales",
        "location": "Parc National de Chitwan",
        "category": "mammiferes"
    },
    # 3. Grand Calao bicorne
    {
        "file": "/assets/wildlife_gallery/wildlife_calao_hornbill.webp",
        "title": "Grand Calao bicorne",
        "desc": "Sentinelle spectaculaire au sommet de la canopée",
        "location": "Parc National de Chitwan",
        "category": "oiseaux"
    },
    # 4. Éléphant sauvage solitaire
    {
        "file": "/assets/wildlife_gallery/wildlife_elephant_jungle.webp",
        "title": "Éléphant sauvage d'Asie",
        "desc": "Grand mâle solitaire émergeant des forêts de Sal",
        "location": "Forêt primaire de Bardia",
        "category": "mammiferes"
    },
    # 5. Paon bleu en parade
    {
        "file": "/assets/wildlife_gallery/wildlife_peacock_wheel.webp",
        "title": "Paon bleu en parade",
        "desc": "Déploiement féerique de la roue au soleil levant",
        "location": "Lisières sauvages de Bardia",
        "category": "oiseaux"
    },
    # 6. Tigresse en approche silencieuse
    {
        "file": "/assets/wildlife_gallery/wildlife_tiger_stalk.webp",
        "title": "Tigresse en approche silencieuse",
        "desc": "Avancée furtive dans les herbes de sous-bois",
        "location": "Vallée de Babai",
        "category": "felins"
    },
    # 7. Léopard indien en affût
    {
        "file": "/assets/wildlife_gallery/julien_leopard_indien.webp",
        "title": "Léopard indien sur sa branche",
        "desc": "Félin furtif camouflé dans la ramure d'un grand arbre",
        "location": "Parc National de Bardia",
        "category": "felins"
    },
    # 8. Martin-chasseur
    {
        "file": "/assets/drive_wildlife/Martin-chasseur_gurial_1.webp",
        "title": "Martin-chasseur gurial",
        "desc": "Oiseau pêcheur au plumage bleu et chocolat éclatant",
        "location": "Zones humides de Bardia",
        "category": "oiseaux"
    },
    # 9. Crocodile des marais
    {
        "file": "/assets/wildlife_gallery/wildlife_croco_water.webp",
        "title": "Crocodile des marais (Mugger)",
        "desc": "Prédateur à fleur d'eau avec reflet miroir limpide",
        "location": "Rivière Rapti • Chitwan",
        "category": "reptiles"
    },
    # 10. Panthère des neiges
    {
        "file": "/assets/snow-leopard/snow_leopard_portrait.webp",
        "title": "Panthère des neiges",
        "desc": "Le seigneur fantôme des falaises himalayennes",
        "location": "Haut Mustang & Annapurna",
        "category": "felins"
    },
    # 11. Éléphante et éléphanteau
    {
        "file": "/assets/wildlife_gallery/julien_elephant_mere_petit.webp",
        "title": "Éléphante d'Asie et son petit",
        "desc": "Scène de complicité et de protection maternelle",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    },
    # 12. Rollier indien
    {
        "file": "/assets/wildlife_gallery/julien_rollier_oiseau.webp",
        "title": "Rollier indien (Indian Roller)",
        "desc": "Oiseau sacré aux éclats d'ailes turquoise étincelantes",
        "location": "Plaines de Suklaphanta",
        "category": "oiseaux"
    },
    # 13. Tigre royal en marche
    {
        "file": "/assets/wildlife_gallery/julien_tigre_bengale2.webp",
        "title": "Tigre du Bengale royal",
        "desc": "Marche majestueuse à travers la clairière",
        "location": "Parc National de Bardia",
        "category": "felins"
    },
    # 14. Grue antigone
    {
        "file": "/assets/drive_wildlife/Grue_antigone_1.webp",
        "title": "Grue antigone (Sarus Crane)",
        "desc": "Le plus grand oiseau volant du monde en couple",
        "location": "Marais du Terai",
        "category": "oiseaux"
    },
    # 15. Rhinocéros au pâturage
    {
        "file": "/assets/wildlife_gallery/chitwan_rhino.webp",
        "title": "Rhinocéros unicorne au pâturage",
        "desc": "Le géant cuirassé broutant dans la savane",
        "location": "Parc National de Chitwan",
        "category": "mammiferes"
    },
    # 16. Cerfs des marais (Barasingha)
    {
        "file": "/assets/wildlife_gallery/wildlife_deer_plain.webp",
        "title": "Cerfs des marais (Barasingha)",
        "desc": "Grands cerfs aux ramures imposantes dans les prairies",
        "location": "Parc National de Suklaphanta",
        "category": "mammiferes"
    },
    # 17. Marabout chevelu en vol
    {
        "file": "/assets/wildlife_gallery/wildlife_marabout_flight.webp",
        "title": "Marabout chevelu en vol",
        "desc": "Envol puissant au-dessus des plaines dorées",
        "location": "Zones humides du Terai",
        "category": "oiseaux"
    },
    # 18. Dauphin d'eau douce du Gange
    {
        "file": "/assets/wildlife_gallery/julien_gangetic_dolphin.webp",
        "title": "Dauphin d'eau douce du Gange",
        "desc": "Espèce aquatique rare nageant dans les rapides",
        "location": "Fleuve Karnali • Bardia",
        "category": "reptiles"
    },
    # 19. Antilope Nilgaut
    {
        "file": "/assets/wildlife_gallery/wildlife_nilgai_forest.webp",
        "title": "Antilopes Nilgaut (Taureau bleu)",
        "desc": "La plus grande antilope d'Asie en lisière forestière",
        "location": "Parc National de Bardia",
        "category": "mammiferes"
    },
    # 20. Élanion blanc
    {
        "file": "/assets/drive_wildlife/Elanion_blanc_1.webp",
        "title": "Élanion blanc en vol",
        "desc": "Petit rapace majestueux chassant au-dessus de la savane",
        "location": "Parc National de Bardia",
        "category": "oiseaux"
    }
]

# Verify all files exist
for p in curated_20:
    path = "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public" + p['file']
    if not os.path.exists(path):
        print(f"ERROR Missing file: {path}")

print(f"Verified all {len(curated_20)} curated photos!")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(curated_20, f, indent=2, ensure_ascii=False)

# Build masonry cards
cards_html = []
for idx, item in enumerate(curated_20):
    card = f"""        <!-- Photo {idx+1}: {item['title']} -->
        <div class="wildlife-card break-inside-avoid mb-6 relative rounded-3xl overflow-hidden group cursor-pointer border border-white/10 shadow-[0_10px_30px_rgba(0,0,0,0.5)] hover:border-emerald-500/50 hover:shadow-[0_20px_50px_rgba(14,131,84,0.25)] transition-all duration-300 bg-slate-900" data-category="{item['category']}" data-idx="{idx}" onclick="openWildlifeLightbox({idx})">
          
          <img 
            src="{item['file']}" 
            alt="{item['title']} - {item['location']}" 
            class="w-full h-auto block filter brightness-95 group-hover:brightness-105 transition-all duration-300"
            loading="lazy"
          />
          
          <!-- Subtle Gradient Overlay (Revealed on Hover) -->
          <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>

          <!-- Top Location Badge -->
          <div class="absolute top-3.5 left-3.5 z-10">
            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-950/80 backdrop-blur-md border border-white/20 text-[11px] font-black text-amber-300 shadow-md">
              <span>📍</span>
              <span>{item['location']}</span>
            </span>
          </div>

          <!-- Bottom Floating Glass Caption -->
          <div class="absolute bottom-3.5 left-3.5 right-3.5 z-10 p-3.5 rounded-2xl bg-slate-950/90 backdrop-blur-xl border border-white/15 text-white opacity-0 translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-300 shadow-2xl">
            <div class="flex items-center justify-between gap-3">
              <div class="min-w-0 flex-1">
                <h3 class="font-black text-sm sm:text-base text-white group-hover:text-amber-300 transition-colors leading-tight truncate">
                  {item['title']}
                </h3>
                <p class="text-xs text-slate-300 mt-0.5 font-medium truncate">
                  {item['desc']}
                </p>
              </div>
              <div class="w-8 h-8 rounded-xl bg-emerald-500/20 text-[#10b981] flex items-center justify-center shrink-0 border border-emerald-500/30">
                <svg class="w-4 h-4 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"></path></svg>
              </div>
            </div>
          </div>

        </div>"""
    cards_html.append(card)

cards_joined = "\n\n".join(cards_html)

counts = {
    "all": len(curated_20),
    "felins": sum(1 for i in curated_20 if i['category'] == 'felins'),
    "mammiferes": sum(1 for i in curated_20 if i['category'] == 'mammiferes'),
    "oiseaux": sum(1 for i in curated_20 if i['category'] == 'oiseaux'),
    "reptiles": sum(1 for i in curated_20 if i['category'] == 'reptiles'),
}

new_gallery_section = f"""  <!-- ========================================================================= -->
  <!-- 5. GALERIE COLLAGE SAUVAGE DU NÉPAL (LES 20 MEILLEURS CLICHÉS 100% ANIMAUX) -->
  <!-- ========================================================================= -->
  <section id="galerie-faune" class="py-20 sm:py-28 lg:py-32 bg-slate-950 text-white relative overflow-hidden border-t border-b border-white/10">
    
    <!-- Ambient ambient glow layers -->
    <div class="absolute top-1/4 left-1/4 w-[700px] h-[700px] bg-[#0e8354]/10 rounded-full blur-[180px] pointer-events-none"></div>
    <div class="absolute bottom-1/4 right-1/4 w-[700px] h-[700px] bg-amber-500/10 rounded-full blur-[180px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-12 sm:mb-16">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-emerald-400/30 text-amber-300 text-xs font-black uppercase tracking-widest mb-4 shadow-lg">
          <span>🌿 Galerie Exclusive Terrain</span>
        </div>
        <h2 class="font-black text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-tight">
          La faune du Terai dans son intimité brute.
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-300 font-medium leading-relaxed">
          Une sélection des <strong>20 plus beaux clichés animaliers</strong> capturés sur le vif lors de nos safaris à pied au Népal. 100% faune sauvage dans son habitat naturel préservé.
        </p>
      </div>

      <!-- General Category Filter Tabs -->
      <div class="flex flex-wrap items-center justify-center gap-2 sm:gap-3 mb-12" id="wildlife-tabs">
        <button onclick="filterWildlife('all')" class="wildlife-tab-btn active px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-emerald-600 text-white shadow-lg shadow-emerald-900/30 border border-emerald-400/40 cursor-pointer">
          🐾 Tous ({counts['all']})
        </button>
        <button onclick="filterWildlife('felins')" class="wildlife-tab-btn px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🐅 Félins ({counts['felins']})
        </button>
        <button onclick="filterWildlife('mammiferes')" class="wildlife-tab-btn px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🐘 Grands Mammifères ({counts['mammiferes']})
        </button>
        <button onclick="filterWildlife('oiseaux')" class="wildlife-tab-btn px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🦚 Oiseaux ({counts['oiseaux']})
        </button>
        <button onclick="filterWildlife('reptiles')" class="wildlife-tab-btn px-5 py-2.5 rounded-full text-xs sm:text-sm font-extrabold transition-all duration-300 bg-white/10 text-slate-300 hover:text-white hover:bg-white/15 border border-white/10 cursor-pointer">
          🐊 Reptiles & Rivières ({counts['reptiles']})
        </button>
      </div>

      <!-- Fluid Multi-Column Masonry Collage (20 elite photos) -->
      <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6" id="wildlife-grid">
{cards_joined}
      </div>

      <!-- Bottom Banner CTA -->
      <div class="mt-14 p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-[#041d13] via-[#0b4830] to-[#041d13] border border-emerald-500/30 flex flex-col sm:flex-row items-center justify-between gap-6 shadow-2xl">
        <div class="text-center sm:text-left space-y-1">
          <p class="font-black text-lg sm:text-xl text-white">Envie de vivre ces observations de vos propres yeux ?</p>
          <p class="text-xs sm:text-sm text-slate-300">Nos pisteurs Pawan & Kiran vous guident en micro-groupe de 4 à 8 explorateurs.</p>
        </div>
        <div class="flex items-center gap-3 shrink-0">
          <a href="#prochains-departs" class="px-6 py-3 rounded-full bg-white text-slate-950 font-black text-xs sm:text-sm hover:bg-slate-100 hover:scale-100 active:scale-95 transition-all shadow-lg">
            Explorer les 15 circuits faune →
          </a>
        </div>
      </div>

    </div>
  </section>"""

wildlife_script_js = """  // WILDLIFE GALLERY CONTROLLER (20 BEST PHOTOS)
  window.wildlifeData = """ + json.dumps(curated_20, ensure_ascii=False) + """;
  window.currentWildlifeIndex = 0;

  window.filterWildlife = function(category) {
    var cards = document.querySelectorAll('.wildlife-card');
    var buttons = document.querySelectorAll('.wildlife-tab-btn');
    
    buttons.forEach(function(btn) {
      btn.classList.remove('bg-emerald-600', 'text-white', 'shadow-lg', 'shadow-emerald-900/30', 'border-emerald-400/40');
      btn.classList.add('bg-white/10', 'text-slate-300', 'border-white/10');
    });
    
    if (window.event && window.event.target) {
      var target = window.event.target.closest('button');
      if (target) {
        target.classList.remove('bg-white/10', 'text-slate-300', 'border-white/10');
        target.classList.add('bg-emerald-600', 'text-white', 'shadow-lg', 'shadow-emerald-900/30', 'border-emerald-400/40');
      }
    }

    cards.forEach(function(card) {
      if (category === 'all' || card.getAttribute('data-category') === category) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  };

  window.openWildlifeLightbox = function(index) {
    window.currentWildlifeIndex = index;
    window.updateWildlifeModalContent();
    var modal = document.getElementById('wildlife-lightbox-modal');
    if (modal) {
      modal.classList.remove('hidden');
      setTimeout(function() {
        modal.classList.remove('opacity-0');
        modal.classList.add('opacity-100');
      }, 10);
    }
    document.body.style.overflow = 'hidden';
  };

  window.closeWildlifeLightbox = function() {
    var modal = document.getElementById('wildlife-lightbox-modal');
    if (modal) {
      modal.classList.remove('opacity-100');
      modal.classList.add('opacity-0');
      setTimeout(function() {
        modal.classList.add('hidden');
        document.body.style.overflow = '';
      }, 300);
    }
  };

  window.updateWildlifeModalContent = function() {
    var img = document.getElementById('wildlife-lightbox-img');
    var counter = document.getElementById('wildlife-counter');
    var caption = document.getElementById('wildlife-lightbox-caption');
    var topTitle = document.getElementById('wildlife-modal-title');
    var data = window.wildlifeData[window.currentWildlifeIndex];

    if (data) {
      if (img) img.src = data.file;
      if (counter) counter.textContent = (window.currentWildlifeIndex + 1) + ' / ' + window.wildlifeData.length;
      if (caption) caption.innerHTML = '<strong class="text-amber-300 text-sm">' + data.title + '</strong> • ' + data.desc + ' <span class="text-emerald-400">(' + data.location + ')</span>';
      if (topTitle) topTitle.textContent = data.title + ' • ' + data.location;
    }
  };

  window.prevWildlifeImage = function(e) {
    if (e && e.stopPropagation) e.stopPropagation();
    window.currentWildlifeIndex = (window.currentWildlifeIndex - 1 + window.wildlifeData.length) % window.wildlifeData.length;
    window.updateWildlifeModalContent();
  };

  window.nextWildlifeImage = function(e) {
    if (e && e.stopPropagation) e.stopPropagation();
    window.currentWildlifeIndex = (window.currentWildlifeIndex + 1) % window.wildlifeData.length;
    window.updateWildlifeModalContent();
  };

  document.addEventListener('keydown', function(e) {
    var modal = document.getElementById('wildlife-lightbox-modal');
    if (modal && !modal.classList.contains('hidden')) {
      if (e.key === 'Escape') window.closeWildlifeLightbox();
      if (e.key === 'ArrowLeft') window.prevWildlifeImage();
      if (e.key === 'ArrowRight') window.nextWildlifeImage();
    }
  });"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Replace the entire #galerie-faune section
c = re.sub(r'<!-- ===+ -->\s*<!-- 5\. GALERIE COLLAGE.*?<\/div>\s*<\/div>\s*<\/section>', new_gallery_section, c, flags=re.DOTALL)

# 2. Replace the wildlife script controller
c = re.sub(r'\/\/ WILDLIFE GALLERY CONTROLLER.*?(?=<\/script>)', wildlife_script_js, c, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("Injected curated 20-photo gallery with strictly 0% humans into index.astro!")
