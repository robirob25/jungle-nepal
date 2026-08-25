import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

map_section_html = """  <!-- ========================================================================= -->
  <!-- 4.5 CARTE GÉOGRAPHIQUE INTERACTIVE DU NÉPAL SAUVAGE -->
  <!-- ========================================================================= -->
  <section id="carte-nepal" class="py-20 sm:py-28 bg-[#030b14] text-white relative overflow-hidden border-t border-white/5">
    <!-- Ambient backlights -->
    <div class="absolute top-1/2 left-1/4 -translate-y-1/2 w-96 h-96 bg-emerald-500/10 rounded-full blur-[120px] pointer-events-none"></div>
    <div class="absolute bottom-10 right-1/4 w-96 h-96 bg-amber-500/5 rounded-full blur-[140px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-12 sm:mb-16">
        <span class="inline-flex items-center gap-2 text-xs font-black uppercase tracking-widest text-amber-400 bg-amber-950/60 border border-amber-500/30 px-4 py-1.5 rounded-full mb-4 shadow-inner">
          <span>🗺️</span>
          <span>Géographie Sauvage & Sanctuaires</span>
        </span>
        <h2 class="font-black text-3xl sm:text-5xl text-white tracking-tight leading-tight">
          Où se déroulent nos expéditions ?
        </h2>
        <p class="mt-4 text-base sm:text-lg text-slate-300 font-medium leading-relaxed">
          De la jungle primaire de Bardia aux sanctuaires fluviaux de Chitwan et aux hauts sommets de l'Himalaya. Explorez la carte du Népal authentique.
        </p>
      </div>

      <!-- Main Map Container Card -->
      <div class="rounded-3xl bg-slate-900/90 border border-white/15 p-4 sm:p-8 lg:p-10 shadow-[0_25px_60px_rgba(0,0,0,0.7)] relative overflow-hidden backdrop-blur-xl">
        
        <!-- Interactive Map Visual Canvas -->
        <div class="relative w-full aspect-[1024/510] rounded-2xl overflow-hidden bg-[#f4f1ea] border border-white/20 shadow-inner group select-none">
          
          <!-- Background Exact Illustrated Map Image -->
          <img 
            src="/assets/map_nepal_wildlife.webp" 
            alt="Carte des parcs nationaux et sanctuaires faune du Népal - Bardia, Chitwan, Katmandou" 
            class="w-full h-full object-cover object-center pointer-events-none"
          />

          <!-- Interactive Hotspot 1: Parc National de Bardia -->
          <button 
            type="button"
            onclick="selectMapLocation('bardia')"
            class="map-pin-btn absolute top-[48%] left-[19%] -translate-x-1/2 -translate-y-1/2 w-9 h-9 sm:w-11 sm:h-11 rounded-full bg-emerald-600/90 text-white flex items-center justify-center border-2 border-white shadow-xl hover:scale-125 transition-transform duration-200 cursor-pointer z-30 group/pin"
            aria-label="Explorer le Parc National de Bardia"
          >
            <span class="absolute inset-0 rounded-full bg-emerald-400 animate-ping opacity-75 pointer-events-none"></span>
            <span class="relative font-black text-sm sm:text-base leading-none">+</span>
            
            <!-- Tooltip Hover Preview -->
            <div class="hidden sm:block absolute bottom-full left-1/2 -translate-x-1/2 mb-3 px-3.5 py-1.5 rounded-xl bg-slate-950/95 border border-emerald-500/40 text-xs text-white whitespace-nowrap opacity-0 pointer-events-none group-hover/pin:opacity-100 group-hover/pin:pointer-events-auto transition-opacity shadow-2xl z-40">
              <span class="font-extrabold text-emerald-400">📍 Bardia National Park</span> • Sanctuaire du Tigre
            </div>
          </button>

          <!-- Interactive Hotspot 2: Parc National de Chitwan -->
          <button 
            type="button"
            onclick="selectMapLocation('chitwan')"
            class="map-pin-btn absolute top-[72%] left-[46.5%] -translate-x-1/2 -translate-y-1/2 w-9 h-9 sm:w-11 sm:h-11 rounded-full bg-emerald-600/90 text-white flex items-center justify-center border-2 border-white shadow-xl hover:scale-125 transition-transform duration-200 cursor-pointer z-30 group/pin"
            aria-label="Explorer le Parc National de Chitwan"
          >
            <span class="absolute inset-0 rounded-full bg-emerald-400 animate-ping opacity-75 pointer-events-none"></span>
            <span class="relative font-black text-sm sm:text-base leading-none">+</span>
            
            <div class="hidden sm:block absolute bottom-full left-1/2 -translate-x-1/2 mb-3 px-3.5 py-1.5 rounded-xl bg-slate-950/95 border border-emerald-500/40 text-xs text-white whitespace-nowrap opacity-0 pointer-events-none group-hover/pin:opacity-100 group-hover/pin:pointer-events-auto transition-opacity shadow-2xl z-40">
              <span class="font-extrabold text-emerald-400">📍 Chitwan National Park</span> • Rhinocéros & Tharu
            </div>
          </button>

          <!-- Interactive Hotspot 3: Katmandou -->
          <button 
            type="button"
            onclick="selectMapLocation('katmandou')"
            class="map-pin-btn absolute top-[68%] left-[60.5%] -translate-x-1/2 -translate-y-1/2 w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-rose-600/90 text-white flex items-center justify-center border-2 border-white shadow-xl hover:scale-125 transition-transform duration-200 cursor-pointer z-30 group/pin"
            aria-label="Explorer Katmandou"
          >
            <span class="relative font-black text-xs sm:text-sm">★</span>
            <div class="hidden sm:block absolute bottom-full left-1/2 -translate-x-1/2 mb-3 px-3.5 py-1.5 rounded-xl bg-slate-950/95 border border-rose-500/40 text-xs text-white whitespace-nowrap opacity-0 pointer-events-none group-hover/pin:opacity-100 group-hover/pin:pointer-events-auto transition-opacity shadow-2xl z-40">
              <span class="font-extrabold text-rose-400">⭐ Katmandou</span> • Capitale & Temples
            </div>
          </button>

          <!-- Interactive Hotspot 4: Pokhara & Annapurnas -->
          <button 
            type="button"
            onclick="selectMapLocation('annapurna')"
            class="map-pin-btn absolute top-[55%] left-[46.5%] -translate-x-1/2 -translate-y-1/2 w-8 h-8 sm:w-9 sm:h-9 rounded-full bg-amber-600/90 text-white flex items-center justify-center border-2 border-white shadow-xl hover:scale-125 transition-transform duration-200 cursor-pointer z-30 group/pin"
            aria-label="Explorer Annapurna & Pokhara"
          >
            <span class="relative font-black text-xs">🏔️</span>
            <div class="hidden sm:block absolute bottom-full left-1/2 -translate-x-1/2 mb-3 px-3.5 py-1.5 rounded-xl bg-slate-950/95 border border-amber-500/40 text-xs text-white whitespace-nowrap opacity-0 pointer-events-none group-hover/pin:opacity-100 group-hover/pin:pointer-events-auto transition-opacity shadow-2xl z-40">
              <span class="font-extrabold text-amber-400">🏔️ Annapurnas & Pokhara</span>
            </div>
          </button>

          <!-- Interactive Hotspot 5: Lac Rara -->
          <button 
            type="button"
            onclick="selectMapLocation('rara')"
            class="map-pin-btn absolute top-[21%] left-[24.5%] -translate-x-1/2 -translate-y-1/2 w-8 h-8 sm:w-9 sm:h-9 rounded-full bg-sky-600/90 text-white flex items-center justify-center border-2 border-white shadow-xl hover:scale-125 transition-transform duration-200 cursor-pointer z-30 group/pin"
            aria-label="Explorer le Lac Rara"
          >
            <span class="relative font-black text-xs">💧</span>
            <div class="hidden sm:block absolute bottom-full left-1/2 -translate-x-1/2 mb-3 px-3.5 py-1.5 rounded-xl bg-slate-950/95 border border-sky-500/40 text-xs text-white whitespace-nowrap opacity-0 pointer-events-none group-hover/pin:opacity-100 group-hover/pin:pointer-events-auto transition-opacity shadow-2xl z-40">
              <span class="font-extrabold text-sky-400">💧 Lac Rara</span> • Lac d'altitude
            </div>
          </button>

        </div>

        <!-- Dynamic Destination Card Below Map -->
        <div id="map-detail-card" class="mt-6 sm:mt-8 p-6 sm:p-7 rounded-2xl bg-slate-950/90 border border-emerald-500/30 flex flex-col md:flex-row items-start md:items-center justify-between gap-6 transition-all duration-300">
          <div class="space-y-1.5 flex-1">
            <div class="flex flex-wrap items-center gap-2.5">
              <span id="map-detail-badge" class="px-3 py-1 rounded-full text-xs font-black uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                Parc National de Bardia (Ouest Sauvage)
              </span>
              <span id="map-detail-fauna" class="text-xs font-semibold text-amber-300">
                🐅 Tigre du Bengale • 🐘 Éléphants sauvages • 🐆 Léopards
              </span>
            </div>
            <h3 id="map-detail-title" class="text-xl sm:text-2xl font-black text-white tracking-tight">
              Le sanctuaire ultime pour le safari à pied en forêt primaire
            </h3>
            <p id="map-detail-desc" class="text-xs sm:text-sm text-slate-300 leading-relaxed max-w-3xl">
              Immersion totale dans la plus vaste forêt préservée du Népal et la mystérieuse vallée de la Babai. Moins de 2% des touristes du Népal y accèdent, garantissant une observation animale exclusive et respectueuse.
            </p>
          </div>
          <div class="shrink-0 flex items-center gap-3 w-full md:w-auto">
            <a 
              id="map-detail-link" 
              href="/destinations/bardia" 
              class="w-full md:w-auto px-6 py-3.5 rounded-full bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold text-xs sm:text-sm text-center shadow-lg shadow-emerald-950/50 transition-all hover:scale-105 active:scale-95"
            >
              Explorer le guide Bardia →
            </a>
          </div>
        </div>

        <!-- Destination Selection Buttons / Pills -->
        <div class="mt-6 flex flex-wrap items-center justify-center gap-2 sm:gap-3">
          <button 
            onclick="selectMapLocation('bardia')" 
            class="map-pill-btn px-4 py-2 rounded-full text-xs font-black border transition-all duration-200 bg-emerald-600 text-white border-emerald-400/50 cursor-pointer shadow-md"
            data-loc="bardia"
          >
            🐅 Bardia National Park
          </button>
          <button 
            onclick="selectMapLocation('chitwan')" 
            class="map-pill-btn px-4 py-2 rounded-full text-xs font-black border transition-all duration-200 bg-white/10 text-slate-300 hover:bg-white/20 border-white/10 hover:text-white cursor-pointer"
            data-loc="chitwan"
          >
            🦏 Chitwan National Park
          </button>
          <button 
            onclick="selectMapLocation('katmandou')" 
            class="map-pill-btn px-4 py-2 rounded-full text-xs font-black border transition-all duration-200 bg-white/10 text-slate-300 hover:bg-white/20 border-white/10 hover:text-white cursor-pointer"
            data-loc="katmandou"
          >
            ⭐ Vallée de Katmandou
          </button>
          <button 
            onclick="selectMapLocation('annapurna')" 
            class="map-pill-btn px-4 py-2 rounded-full text-xs font-black border transition-all duration-200 bg-white/10 text-slate-300 hover:bg-white/20 border-white/10 hover:text-white cursor-pointer"
            data-loc="annapurna"
          >
            🏔️ Pokhara & Annapurnas
          </button>
          <button 
            onclick="selectMapLocation('rara')" 
            class="map-pill-btn px-4 py-2 rounded-full text-xs font-black border transition-all duration-200 bg-white/10 text-slate-300 hover:bg-white/20 border-white/10 hover:text-white cursor-pointer"
            data-loc="rara"
          >
            💧 Lac Rara & Hautes Terres
          </button>
        </div>

      </div>

    </div>
  </section>

  <script is:inline>
    // MAP INTERACTIVE LOGIC
    var mapLocationsData = {
      bardia: {
        badge: "Parc National de Bardia (Ouest Sauvage)",
        fauna: "🐅 Tigre du Bengale • 🐘 Éléphants sauvages • 🐆 Léopards",
        title: "Le sanctuaire ultime pour le safari à pied en forêt primaire",
        desc: "Immersion totale dans la plus vaste forêt préservée du Népal et la mystérieuse vallée de la Babai. Moins de 2% des touristes du Népal y accèdent, garantissant une observation animale exclusive et respectueuse.",
        link: "/destinations/bardia",
        linkText: "Explorer le guide Bardia →"
      },
      chitwan: {
        badge: "Parc National de Chitwan (Terai Central)",
        fauna: "🦏 Grand Rhinocéros unicorne • 🐊 Gavials • 🦌 Cerfs Axis",
        title: "Le royaume préservé des rhinocéros unicornes et du peuple Tharu",
        desc: "Classé au patrimoine mondial de l'UNESCO, Chitwan est le haut lieu de conservation mondial du grand rhinocéros d'Asie et des rivières à crocodiles, bordé par les villages traditionnels Tharu.",
        link: "/destinations/chitwan",
        linkText: "Explorer le guide Chitwan →"
      },
      katmandou: {
        badge: "Vallée de Katmandou (Cœur Culturel)",
        fauna: "🏛️ Temples Séculaires • 🕊️ Stupas de Swayambhunath & Boudhanath",
        title: "La porte d'entrée mythique de l'Himalaya et de nos expéditions",
        desc: "Accueil chaleureux, briefing complet avec nos pisteurs et découverte des ruelles médiévales de Patan et Bhaktapur avant le départ vers la jungle profonde.",
        link: "/destinations/katmandou",
        linkText: "Explorer Katmandou →"
      },
      annapurna: {
        badge: "Massif des Annapurnas & Pokhara",
        fauna: "🏔️ Sommets à 8 000 m • 🦅 Aigles de l'Himalaya • 🌸 Rhododendrons",
        title: "La transition spectaculaire entre jungle subtropicale et géants de glace",
        desc: "Panoramas à couper le souffle sur le Machapuchare (6 993 m) et le lac sacré Phewa, point de départ de nos traversées complètes 'Jungle & Montagnes'.",
        link: "/destinations/annapurna",
        linkText: "Explorer les Annapurnas →"
      },
      rara: {
        badge: "Lac Rara & Hautes Terres de l'Ouest",
        fauna: "💧 Lac turquoise à 2 990 m • 🌲 Forêts de conifères • 🫎 Cerfs porte-musc",
        title: "Le plus grand lac du Népal, aux confins du monde sauvage",
        desc: "Une expédition exclusive et confidentielle reliant les eaux cristallines du lac Rara jusqu'aux plaines sauvages du parc de Bardia.",
        link: "/tours/rara-lake-bardia",
        linkText: "Voir l'expédition Lac Rara →"
      }
    };

    window.selectMapLocation = function(locKey) {
      var data = mapLocationsData[locKey];
      if (!data) return;

      var badge = document.getElementById('map-detail-badge');
      var fauna = document.getElementById('map-detail-fauna');
      var title = document.getElementById('map-detail-title');
      var desc = document.getElementById('map-detail-desc');
      var link = document.getElementById('map-detail-link');

      if (badge) badge.textContent = data.badge;
      if (fauna) fauna.textContent = data.fauna;
      if (title) title.textContent = data.title;
      if (desc) desc.textContent = data.desc;
      if (link) {
        link.href = data.link;
        link.textContent = data.linkText;
      }

      // Update pill buttons style
      var pills = document.querySelectorAll('.map-pill-btn');
      pills.forEach(function(pill) {
        if (pill.getAttribute('data-loc') === locKey) {
          pill.classList.remove('bg-white/10', 'text-slate-300', 'border-white/10');
          pill.classList.add('bg-emerald-600', 'text-white', 'border-emerald-400/50', 'shadow-md');
        } else {
          pill.classList.remove('bg-emerald-600', 'text-white', 'border-emerald-400/50', 'shadow-md');
          pill.classList.add('bg-white/10', 'text-slate-300', 'border-white/10');
        }
      });
    };
  </script>
"""

# Insert map_section_html right before Section 5 (Galerie faune)
content = content.replace(
    '<!-- ========================================================================= -->\n  <!-- 5. GALERIE COLLAGE SAUVAGE DU NÉPAL',
    map_section_html + '\n\n  <!-- ========================================================================= -->\n  <!-- 5. GALERIE COLLAGE SAUVAGE DU NÉPAL'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("Inserted interactive map section into index.astro!")
