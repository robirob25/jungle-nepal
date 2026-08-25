with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate section #carte-nepal
carte_start_marker = "  <!-- ========================================================================= -->\n  <!-- 7. CARTE DES DESTINATIONS & EXPÉDITIONS (RESPONSIVE & CLEAN MOBILE) -->\n  <!-- ========================================================================= -->\n  <section id=\"carte-nepal\""
carte_end_marker = "  </section>\n\n  <!-- ========================================================================= -->\n  <!-- 8. PISTEURS & ÉQUIPE DE TERRAIN -->"

carte_start_idx = content.find(carte_start_marker)
carte_end_idx = content.find(carte_end_marker)

if carte_start_idx == -1 or carte_end_idx == -1:
    print("Could not find carte markers")
    exit(1)

# Extract full carte section
carte_block = content[carte_start_idx:carte_end_idx + len("  </section>")]

# Remove carte section from current position
content_without_carte = content[:carte_start_idx] + content[carte_end_idx + len("  </section>\n\n"):]

# Locate end of section #prochains-departs
departs_end_marker = "    </div>\n  </section>\n\n        <!-- ========================================================================= -->\n  <!-- 7. CINEMA SHOWCASE : L'EXPÉRIENCE EN IMMERSION TOTALE (VIDÉO CENTRALE) -->"
departs_end_idx = content_without_carte.find(departs_end_marker)

if departs_end_idx == -1:
    # Try alternative matching
    departs_end_marker = "    </div>\n  </section>"
    # Find the one before #concept
    concept_idx = content_without_carte.find('<section id="concept"')
    departs_end_idx = content_without_carte.rfind('  </section>', 0, concept_idx)

# Target insertion point is right after </section> of #prochains-departs
insert_point = content_without_carte.find('  <!-- ========================================================================= -->\n  <!-- 7. CINEMA SHOWCASE : L\'EXPÉRIENCE EN IMMERSION TOTALE (VIDÉO CENTRALE) -->')

if insert_point == -1:
    insert_point = content_without_carte.find('<section id="concept"')

new_content = content_without_carte[:insert_point] + carte_block + "\n\n  " + content_without_carte[insert_point:]

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✓ Successfully moved #carte-nepal right after #prochains-departs!")
