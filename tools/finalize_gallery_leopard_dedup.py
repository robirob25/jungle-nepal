import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Photo 52 -> ours_lippu_sloth_bear.webp
# Photo 53 -> cerf_sambar_dans_eau.webp

c = c.replace(
    '/assets/curated_gallery/ours_lippu_termitiere.webp',
    '/assets/curated_gallery/ours_lippu_sloth_bear.webp'
)

c = c.replace(
    '/assets/curated_gallery/chat_jungle_felin_sauvage.webp',
    '/assets/curated_gallery/cerf_sambar_dans_eau.webp'
)

c = c.replace('Chat de jungle (Jungle Cat)', 'Cerf Sambar dans la rivière')
c = c.replace('Chat des marais (Jungle Cat)', 'Cerf Sambar (Grand cervidé d\'Asie)')
c = c.replace('Petit félin sauvage agile traquant dans les hautes herbes', 'Le plus grand cervidé d\'Asie traversant les cours d\'eau de Bardia')

# Update category to mammiferes
c = c.replace(
    'data-category="felins" data-idx="52"',
    'data-category="mammiferes" data-idx="52"'
)

c = c.replace(
    '{"file": "/assets/curated_gallery/chat_jungle_felin_sauvage.webp", "title": "Chat des marais (Jungle Cat)", "desc": "Petit félin sauvage agile traquant dans les hautes herbes", "location": "Parc national de Bardia", "category": "felins", "aspect": 1.7777777777777777}',
    '{"file": "/assets/curated_gallery/cerf_sambar_dans_eau.webp", "title": "Cerf Sambar (Grand cervidé d\'Asie)", "desc": "Le plus grand cervidé d\'Asie traversant les cours d\'eau de Bardia", "location": "Parc national de Bardia", "category": "mammiferes", "aspect": 1.7777777777777777}'
)

c = c.replace(
    '{"file": "/assets/curated_gallery/ours_lippu_termitiere.webp"',
    '{"file": "/assets/curated_gallery/ours_lippu_sloth_bear.webp"'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Successfully replaced duplicate leopards with authentic Sloth Bear and Sambar Deer!")
