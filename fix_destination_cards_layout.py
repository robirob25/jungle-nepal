with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Move titles OUT of the images and place them BELOW the images in the content container.
# 2. Remove "Explorer la région" text and make "Découvrir la destination →" span the full card width or align neatly.

import re

# Template for clean destination cards
def make_clean_card(slug, img_url, alt, badge_text, title, desc):
    return f"""    <article class="group bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-sm hover:shadow-2xl hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between">
      <a href="/destinations/{slug}.html" class="relative aspect-[4/3] overflow-hidden block">
        <img src="{img_url}" alt="{alt}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" loading="lazy" />
        <div class="absolute inset-0 bg-gradient-to-t from-slate-950/60 via-transparent to-transparent"></div>
        <span class="absolute top-4 left-4 bg-slate-950/80 backdrop-blur-md text-amber-100 text-xs font-black px-3.5 py-1.5 rounded-full border border-white/10 shadow">
          {badge_text}
        </span>
      </a>

      <div class="p-6 sm:p-7 flex-1 flex flex-col justify-between space-y-4">
        <div>
          <h2 class="font-black text-2xl text-slate-950 group-hover:text-[#0e8354] transition-colors tracking-tight leading-snug">
            <a href="/destinations/{slug}.html">{title}</a>
          </h2>
          <p class="text-sm text-slate-600 line-clamp-3 leading-relaxed font-normal mt-3">
            {desc}
          </p>
        </div>

        <div class="pt-4 border-t border-slate-100">
          <a href="/destinations/{slug}.html" class="w-full py-3 px-4 rounded-2xl bg-[#0e5c3e] hover:bg-[#09422b] text-white font-extrabold text-xs sm:text-sm flex items-center justify-center gap-2 shadow-md shadow-emerald-950/20 active:scale-98 transition-all text-center">
            <span>Découvrir la destination</span>
            <span>→</span>
          </a>
        </div>
      </div>
    </article>"""

# Replace all 5 destination cards in main section
cards_data = [
    (
        "bardia",
        "https://junglenepal.com/wp-content/uploads/2025/12/Tigre-Bardia.png",
        "Parc national de Bardia",
        "Sanctuaire du tigre du Bengale",
        "Parc national de Bardia",
        "Avant sa création officielle en 1988, le parc national de Bardia était une réserve de chasse royale dédiée à la monarchie népalaise. Sa transformation en sanctuaire protégé a permis de préserver l'un des écosystèmes les plus sauvages et intacts d'Asie."
    ),
    (
        "chitwan",
        "https://junglenepal.com/wp-content/uploads/2025/12/rhinoceros-Nepal.png",
        "Parc national de Chitwan",
        "Patrimoine mondial de l'UNESCO",
        "Parc national de Chitwan",
        "Classé au patrimoine mondial de l'UNESCO depuis 1984, le parc national de Chitwan abrite l'une des biodiversités les plus spectaculaires et foisonnantes du continent asiatique."
    ),
    (
        "suklaphanta",
        "https://junglenepal.com/wp-content/uploads/2025/12/Suklaphata-1024x585-1.jpg",
        "Parc national de Suklaphanta",
        "L'Éden sauvage secret",
        "Parc national de Suklaphanta",
        "Situé à l'extrême ouest du Népal, à la frontière de l'Inde, le parc national de Suklaphanta est l'un des territoires les plus sauvages, préservés et secrets de tout l'Himalaya."
    ),
    (
        "annapurna",
        "https://junglenepal.com/wp-content/uploads/2017/01/himalayas-5817277_1920.jpg",
        "Les Annapurna & Pokhara",
        "Sommets sacrés & treks",
        "Les Annapurna & Pokhara",
        "La région de l'Annapurna offre des contrastes géographiques et culturels vertigineux : des forêts tropicales luxuriantes jusqu'aux parois de glace flirtant avec les 8 000 mètres."
    ),
    (
        "katmandou",
        "/assets/drive_photos/adrien_bhaktapur1.webp",
        "Katmandou & la Vallée des Rois",
        "Cité millénaire & temples",
        "Katmandou & la vallée des rois",
        "Au premier abord, Katmandou peut sembler déroutante et bouillonnante. Mais laissez-lui quelques heures, et elle finit par vous enchanter par sa ferveur spirituelle et sa poésie intemporelle."
    )
]

new_grid_html = '\n\n    '.join([make_clean_card(*card) for card in cards_data])

# Extract grid container in index.astro
grid_start = c.find('<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">')
grid_end = c.find('</div>\n  </main>', grid_start)

c = c[:grid_start + len('<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">\n      ')] + new_grid_html + '\n    ' + c[grid_end:]

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Relocated titles below images and cleaned CTA buttons in destinations/index.astro!")
