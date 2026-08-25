with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Section delimiters
idx_carte = c.find('id="carte-nepal"')
idx_concept = c.find('id="concept"')
idx_galerie = c.find('id="galerie-faune"')
idx_pisteurs = c.find('id="pisteurs"')

# Section start tags
start_concept = c.rfind('<!--', 0, idx_concept)
start_galerie = c.rfind('<!--', 0, idx_galerie)
start_pisteurs = c.rfind('<!--', 0, idx_pisteurs)

concept_block = c[start_concept:start_galerie].strip()
galerie_block = c[start_galerie:start_pisteurs].strip()

# Construct new string:
# Before concept -> galerie_block -> concept_block -> after galerie
new_c = c[:start_concept] + galerie_block + "\n\n  " + concept_block + "\n\n  " + c[start_pisteurs:]

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(new_c)

print("✓ Swapped successfully!")
