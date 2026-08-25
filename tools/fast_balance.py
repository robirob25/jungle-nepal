import json

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# 21 pool items
# Verticals (7):
# 1. Perruche (1.778)
# 2. Varan (1.501)
# 3. Tigre Embuscade (1.781)
# 4. Leopard (1.778)
# 5. Langur (1.250)
# 6. Portrait Elephant (1.333)
# 7. Tchitrec (1.778)

# Horizontals (14):
# 1. Tigre Territoire (0.666)
# 2. Croc Marais (0.562)
# 3. Bebe Macaque (0.714)
# 4. Rhino Brume (0.666)
# 5. Calao (0.562)
# 6. Gavial (0.666)
# 7. Elephant Male (0.562)
# 8. Agame (0.562)
# 9. Marabout (0.562)
# 10. Paon (0.562)
# 11. Tigre Point d'eau (0.666)
# 12. Rhino Martins (0.562)
# 13. Tigre Riviere (0.562)
# 14. Tigre Pistage (0.666)

def get(k):
    for i in items:
        if k in i['file']:
            return i
    return None

# Col 1 (2 verticals + 5 horizontals):
# Verticals: Perruche (1.778) + Varan (1.501) = 3.279
# Horizontals: Tigre Territoire (0.666) + Croc Marais (0.562) + Bebe Macaque (0.714) + Rhino Brume (0.666) + Tigre Riviere (0.562) = 3.170
# Total Col 1 = 6.449
c1 = [
    get("tiger_territory_marking"),
    get("perruche_tete_prune_fleur"),
    get("crocodile_marais_rapti"),
    get("bebe_macaque_mere"),
    get("varan_bengale_arbre"),
    get("rhino_unicorne_brume"),
    get("tigre_bengale_traversee_riviere")
]

# Col 2 (2 verticals + 5 horizontals):
# Verticals: Tigre Embuscade (1.781) + Leopard (1.778) = 3.559
# Horizontals: Calao (0.562) + Gavial (0.666) + Elephant Male (0.562) + Agame (0.562) + Tigre Pistage (0.666) = 3.018
# Total Col 2 = 6.577
c2 = [
    get("tigre_bengale_embuscade_vertical"),
    get("calao_bicorne_canopee"),
    get("leopard_asie_affut_lisiere"),
    get("gavial_gange_nage_riviere"),
    get("elephant_asie_male_jungle"),
    get("lezard_agame_jardin_camouflage"),
    get("tigre_bengale_pistage")
]

# Col 3 (3 verticals + 4 horizontals):
# Verticals: Langur (1.250) + Portrait Elephant (1.333) + Tchitrec (1.778) = 4.361
# Horizontals: Marabout (0.562) + Paon (0.562) + Tigre Point d'eau (0.666) + Rhino Martins (0.562) = 2.352
# Total Col 3 = 6.713
c3 = [
    get("marabout_chevelu_pose_marais"),
    get("langur_gris_cri_alarme"),
    get("portrait_elephant_asie"),
    get("paon_bleu_parade_roue"),
    get("tchitrec_paradis_longues_rectrices"),
    get("tiger_water_pond"),
    get("rhino_unicorne_oiseaux_pique_boeuf")
]

s1 = sum(x['aspect'] for x in c1)
s2 = sum(x['aspect'] for x in c2)
s3 = sum(x['aspect'] for x in c3)

print(f"Col 1 height: {s1:.3f} (7 items)")
print(f"Col 2 height: {s2:.3f} (7 items)")
print(f"Col 3 height: {s3:.3f} (7 items)")
print(f"Difference min/max: {max(s1,s2,s3)-min(s1,s2,s3):.3f} -> VIRTUALLY IDENTICAL!")

ordered_21 = c1 + c2 + c3
seen = set(i['file'] for i in ordered_21)
remaining = [i for i in items if i['file'] not in seen]
new_items = ordered_21 + remaining

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(new_items, f, indent=2, ensure_ascii=False)

print("Saved fast balanced gallery!")
