import re

# 1. Update French index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    fr = f.read()

# Add id to h2
fr = re.sub(
    r'<h2 class="font-black text-3xl sm:text-4xl md:text-5xl text-slate-900 tracking-tight">\s*Les 15 séjours immersifs au Népal\s*</h2>',
    '<h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl text-slate-900 tracking-tight transition-all duration-300">\n            Les 15 séjours immersifs au Népal\n          </h2>',
    fr
)

# In filterTrips function, update title
title_code_fr = """
      const sectionTitle = document.getElementById('tours-section-title');
      if (sectionTitle) {
        const titleMap = {
          'all': 'Les 15 séjours immersifs au Népal',
          'safari': '🐅 Safaris & Grands Félins',
          'bivouac': '⛺ Bivouacs & Nuits Sauvages en Jungle',
          'chitwan': '🦏 Rhinocéros & Parc National de Chitwan',
          'rafting': '🚣 Rafting & Expéditions Rivières',
          'mustang-himalaya': '🏔️ Himalaya, Mustang & Spiritualité',
          'culture': '🏔️ Himalaya, Mustang & Spiritualité',
          'grand-tour': '🇳🇵 Grands Tours Immersion 360°'
        };
        sectionTitle.textContent = titleMap[catLower] || 'Les 15 séjours immersifs au Népal';
      }
"""

fr = re.sub(
    r'(const badge = document\.getElementById\(\'trip-count-badge\'\);.*?\}\s*\n)',
    r'\1' + title_code_fr,
    fr,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(fr)

# 2. Update English index.astro
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro', 'r', encoding='utf-8') as f:
    en = f.read()

# Add id to h2
en = re.sub(
    r'<h2 class="font-black text-3xl sm:text-4xl md:text-5xl text-slate-900 tracking-tight">\s*All 15 Immersive Expeditions in Nepal\s*</h2>',
    '<h2 id="tours-section-title" class="font-black text-3xl sm:text-4xl md:text-5xl text-slate-900 tracking-tight transition-all duration-300">\n            All 15 Immersive Expeditions in Nepal\n          </h2>',
    en
)

title_code_en = """
      const sectionTitle = document.getElementById('tours-section-title');
      if (sectionTitle) {
        const titleMap = {
          'all': 'All 15 Immersive Expeditions in Nepal',
          'safari': '🐅 Big Cats & Wildlife Safaris',
          'bivouac': '⛺ Jungle Bivouacs & Wild Nights',
          'chitwan': '🦏 Rhinos & Chitwan National Park',
          'rafting': '🚣 Wild Rivers & Rafting Expeditions',
          'mustang-himalaya': '🏔️ Himalayas, Mustang & Spirituality',
          'culture': '🏔️ Himalayas, Mustang & Spirituality',
          'grand-tour': '🇳🇵 Grand 360° Immersive Expeditions'
        };
        sectionTitle.textContent = titleMap[catLower] || 'All 15 Immersive Expeditions in Nepal';
      }
"""

en = re.sub(
    r'(const badge = document\.getElementById\(\'trip-count-badge\'\);.*?\}\s*\n)',
    r'\1' + title_code_en,
    en,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro', 'w', encoding='utf-8') as f:
    f.write(en)

print("Updated dynamic title switching for both FR and EN homepages!")
