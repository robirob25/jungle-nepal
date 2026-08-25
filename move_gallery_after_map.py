with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Current order:
# 1. #prochains-departs
# 2. #carte-nepal
# 3. #concept (Video cinema)
# 4. #galerie-faune
# 5. #pisteurs
# 6. #avis

# Goal order:
# 1. #prochains-departs
# 2. #carte-nepal
# 3. #galerie-faune
# 4. #concept (Video cinema)
# 5. #pisteurs
# 6. #avis

galerie_start_marker = "  <!-- ========================================================================= -->\n  <!-- 5. GALERIE COLLAGE SAUVAGE DU NÉPAL (SÉLECTION PRÉCISE ET CURATÉE) -->\n  <!-- ========================================================================= -->\n  <section id=\"galerie-faune\""
galerie_end_marker = "  </section>\n\n  <!-- ========================================================================= -->\n  <!-- 8. PISTEURS & ÉQUIPE DE TERRAIN -->"

g_start = content.find(galerie_start_marker)
g_end = content.find(galerie_end_marker)

if g_start == -1 or g_end == -1:
    print("Could not find galerie markers")
    exit(1)

galerie_block = content[g_start:g_end + len("  </section>")]

# Remove galerie from after concept
content_without_g = content[:g_start] + content[g_end + len("  </section>\n\n"):]

# Find position to insert: right before #concept
concept_marker = "  <!-- ========================================================================= -->\n  <!-- 7. CINEMA SHOWCASE : L'EXPÉRIENCE EN IMMERSION TOTALE (VIDÉO CENTRALE) -->\n  <!-- ========================================================================= -->\n  <section id=\"concept\""
concept_idx = content_without_g.find(concept_marker)

if concept_idx == -1:
    print("Could not find concept marker")
    exit(1)

new_content = content_without_g[:concept_idx] + galerie_block + "\n\n  " + content_without_g[concept_idx:]

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✓ Successfully moved #galerie-faune right after #carte-nepal!")
