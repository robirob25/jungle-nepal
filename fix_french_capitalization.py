import re, glob, os

# 1. Update Homepage (index.astro)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    fr = f.read()

# Fix Title Case on Filter Pills
fr = fr.replace('<span>Safaris & Grands Félins (11)</span>', '<span>Safaris et grands félins (11)</span>')
fr = fr.replace('<span>Bivouacs & Nuits Sauvages (5)</span>', '<span>Bivouacs et nuits sauvages (5)</span>')
fr = fr.replace('<span>Rhinocéros & Chitwan (3)</span>', '<span>Rhinocéros et Chitwan (3)</span>')
fr = fr.replace('<span>Rafting & Expéditions Rivières (3)</span>', '<span>Rafting et expéditions rivières (3)</span>')
fr = fr.replace('<span>Himalaya, Mustang & Spiritualité (6)</span>', '<span>Himalaya, Mustang et spiritualité (6)</span>')
fr = fr.replace('<span>Grands Tours 360° (10)</span>', '<span>Grands tours 360° (10)</span>')

# Fix Dynamic Title Map in JavaScript
fr = re.sub(
    r'const titleMap = \{.*?\};',
    """const titleMap = {
          'all': 'Les 15 séjours immersifs au Népal',
          'safari': '🐅 Safaris et grands félins',
          'bivouac': '⛺ Bivouacs et nuits sauvages en jungle',
          'chitwan': '🦏 Rhinocéros et parc national de Chitwan',
          'rafting': '🚣 Rafting et expéditions rivières',
          'mustang-himalaya': '🏔️ Himalaya, Mustang et spiritualité',
          'culture': '🏔️ Himalaya, Mustang et spiritualité',
          'grand-tour': '🇳🇵 Grands tours et immersion 360°'
        };""",
    fr,
    flags=re.DOTALL
)

# Fix ALL CAPS badges in Hero / Sections
fr = fr.replace('DÉPARTS GARANTIS • PETITS GROUPES DE 4 À 8 EXPLORATEURS', 'Départs garantis • Petits groupes de 4 à 8 explorateurs')
fr = fr.replace('Nos Maîtres pisteurs & Organisateurs', 'Nos maîtres pisteurs et organisateurs')
fr = fr.replace('L\'EXPERIENCE SAFARI EN IMMERSION', 'L\'expérience safari en immersion')
fr = fr.replace('VOUS AVEZ DES QUESTIONS ?', 'Vous avez des questions ?')
fr = fr.replace('FAITES LE PREMIER PAS', 'Faites le premier pas')

# Fix Trip Card titles & badges
fr = fr.replace('🏔️ Himalaya & Faune Mythique', '🏔️ Himalaya et faune mythique')
fr = fr.replace('🐾 9j Pistage Pur', '🐾 9j pistage pur')
fr = fr.replace('Expédition : Panthère des Neiges Exclusive', 'Expédition : panthère des neiges exclusive')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(fr)

print("Fixed French sentence casing on index.astro!")

# 2. Fix across all French Tour Pages
tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

for tp in tour_files:
    with open(tp, 'r', encoding='utf-8') as f:
        c = f.read()

    # Titles and badges
    c = c.replace('Expédition : Panthère des Neiges Exclusive', 'Expédition : panthère des neiges exclusive')
    c = c.replace('Saison Panthère', 'Saison panthère')
    c = c.replace('SÉLECTIONNEZ VOTRE DÉPART :', 'Sélectionnez votre départ :')
    c = c.replace('LES TEMPS FORTS DU VOYAGE', 'Les temps forts du voyage')
    c = c.replace('CE QUI EST INCLUS DANS VOTRE SÉJOUR', 'Ce qui est inclus dans votre séjour')
    c = c.replace('INCLUS DANS LE TARIF', 'Inclus dans le tarif')
    c = c.replace('NON INCLUS', 'Non inclus')
    c = c.replace('VOS QUESTIONS FRÉQUENTES', 'Vos questions fréquentes')
    c = c.replace('AVIS VOYAGEURS VÉRIFIÉS', 'Avis voyageurs vérifiés')
    c = c.replace('VOUS POURRIEZ AUSSI AIMER CES EXPÉDITIONS', 'Vous pourriez aussi aimer ces expéditions')
    c = c.replace('POURSUIVRE L\'EXPLORATION', 'Poursuivre l\'exploration')
    c = c.replace('🏔️ Himalaya, Mustang & Spiritualité', '🏔️ Himalaya, Mustang et spiritualité')
    c = c.replace('🐅 Safaris & Grands Félins', '🐅 Safaris et grands félins')
    c = c.replace('⛺ Bivouacs & Nuits Sauvages', '⛺ Bivouacs et nuits sauvages')
    c = c.replace('🦏 Rhinocéros & Chitwan', '🦏 Rhinocéros et Chitwan')
    c = c.replace('🚣 Rafting & Expéditions Rivières', '🚣 Rafting et expéditions rivières')
    c = c.replace('🇳🇵 Grands Tours 360°', '🇳🇵 Grands tours 360°')

    with open(tp, 'w', encoding='utf-8') as f:
        f.write(c)

print(f"Fixed French casing across {len(tour_files)} French tour pages!")

# 3. Fix About page
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'r', encoding='utf-8') as f:
    ap = f.read()

ap = ap.replace('NOTRE HISTOIRE & NOTRE MISSION', 'Notre histoire et notre mission')
ap = ap.replace('NOTRE ÉQUIPE SUR LE TERRAIN', 'Notre équipe sur le terrain')
ap = ap.replace('LES 4 PILIERS DE NOTRE ENGAGEMENT', 'Les 4 piliers de notre engagement')
ap = ap.replace('NOS SÉJOURS EMBLÉMATIQUES', 'Nos séjours emblématiques')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    ap.write(ap)

print("Fixed French casing on a-propos.astro!")
