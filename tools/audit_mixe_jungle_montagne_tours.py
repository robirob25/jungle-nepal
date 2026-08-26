import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# The true combinés / Mixe jungle et montagne tours are those having BOTH jungle (safari/chitwan/bardia) AND mountain (himalaya/annapurna/mustang/rara):
# 1. népal sauvage (15j) - Bardia + Pokhara/Annapurna
# 2. rara lake & bardia (13j) - High altitude Rara lake + Bardia jungle
# 3. immersion totale (14j) - Chitwan + Pokhara + Bandipur
# 4. carnet de voyage (15j) - Chitwan + Pokhara/Annapurnas + Katmandou
# 5. rivieres sauvages rafting (18j) - Annapurna + Karnali + Bardia

# Tours that are PURE mountain or PURE jungle must NOT have 'mixe-jungle-montagne':
# - Panthere des neiges (Pure high altitude Himalaya/Manang 4000m+) -> MUST NOT BE in Mixe jungle et montagne
# - Tiji Festival Mustang (Pure high altitude Tibetan plateau/Mustang) -> NOT mixe
# - Immersion spirituelle (Pure mountain ashram/monasteries) -> NOT mixe
# - Jungle extrême (Pure 15 days Bardia/Suklaphanta jungle) -> NOT mixe
# - Chitwan + Bardia (Pure jungle parks) -> NOT mixe

# Let's cleanly update data-category attributes:

# 1. Snow leopard:
c = c.replace(
    'data-category="mustang-himalaya culture safari grand-tour" data-title="expédition panthère des neiges exclusive"',
    'data-category="mustang-himalaya culture safari" data-title="expédition panthère des neiges exclusive"'
)

# 2. Tiji festival:
c = c.replace(
    'data-category="mustang-himalaya culture grand-tour" data-title="tiji festival – upper mustang"',
    'data-category="mustang-himalaya culture" data-title="tiji festival – upper mustang"'
)

# 3. Immersion spirituelle:
c = c.replace(
    'data-category="mustang-himalaya culture grand-tour" data-title="immersion spirituelle en himalaya"',
    'data-category="mustang-himalaya culture" data-title="immersion spirituelle en himalaya"'
)

# 4. Jungle extrême:
c = c.replace(
    'data-category="safari grand-tour" data-title="jungle extrême – spécial faune sauvage"',
    'data-category="safari" data-title="jungle extrême – spécial faune sauvage"'
)

# 5. Chitwan + Bardia:
c = c.replace(
    'data-category="chitwan safari bivouac rafting aventure grand-tour" data-title="chitwan + bardia – l’aventure jungle complète"',
    'data-category="chitwan safari bivouac rafting aventure" data-title="chitwan + bardia – l’aventure jungle complète"'
)

# Now count the actual mixe tours (népal sauvage, rara + bardia, immersion totale, carnet de voyage, rafting + safari):
# Update the counter in the pill to match real count (5 circuits combinés jungle & montagne)
c = c.replace(
    '<span>Mixe jungle et montagne (10)</span>',
    '<span>Mixe jungle et montagne (5)</span>'
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Cleaned Mixe jungle et montagne category tags: Snow Leopard and pure tours removed!")
