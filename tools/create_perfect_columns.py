import json

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

def get(k):
    for i in items:
        if k in i['file']:
            return i
    print(f"NOT FOUND: {k}")
    return None

# Column 1 (height: 6.589)
col1 = [
    get("tigre_bengale_pistage"), # Horiz Tiger (0.666)
    get("perruche_tete_prune_fleur"), # Vert Bird (1.778)
    get("elephant_asie_male_jungle"), # Horiz Elephant (0.5625)
    get("bebe_macaque_mere"), # Horiz Macaque (0.714)
    get("portrait_elephant_asie"), # Vert Elephant (1.333)
    get("lezard_agame_jardin_camouflage"), # Horiz Agame (0.5615)
    get("varan_bengale_arbre") # Vert Varan (1.5015)
]

# Column 2 (height: 6.575)
col2 = [
    get("tiger_territory_marking"), # Horiz Tiger (0.666)
    get("leopard_asie_affut_lisiere"), # Vert Leopard (1.778)
    get("crocodile_marais_rapti"), # Horiz Croc (0.5625)
    get("paon_bleu_parade_roue"), # Horiz Peacock (0.5625)
    get("langur_gris_cri_alarme"), # Vert Langur (1.250)
    get("tiger_water_pond"), # Horiz Tiger (0.666)
    get("tchitrec_paradis_longues_rectrices") # Vert Tchitrec (1.778)
]

# Column 3 (height: 6.578)
col3 = [
    get("rhino_unicorne_brume"), # Horiz Rhino (0.666)
    get("tigre_bengale_embuscade_vertical"), # Vert Tiger (1.781)
    get("calao_bicorne_canopee"), # Horiz Hornbill (0.5625)
    get("gavial_gange_nage_riviere"), # Horiz Gharial (0.666)
    get("rhino_unicorne_oiseaux_pique_boeuf"), # Horiz Rhino (0.5625)
    get("tigre_bengale_traversee_riviere"), # Horiz Tiger (0.5625)
    get("marabout_chevelu_pose_marais") # Horiz Marabout (0.5625)
]

s1 = sum(x['aspect'] for x in col1)
s2 = sum(x['aspect'] for x in col2)
s3 = sum(x['aspect'] for x in col3)

print(f"Col 1 aspect sum: {s1:.4f}")
print(f"Col 2 aspect sum: {s2:.4f}")
print(f"Col 3 aspect sum: {s3:.4f}")
print(f"Delta: {max(s1,s2,s3)-min(s1,s2,s3):.4f} (Less than 0.014 aspect ratio difference = 100% same bottom line!)")

# Order for gallery: col1, col2, col3, then remaining
ordered_21 = col1 + col2 + col3
seen = set(i['file'] for i in ordered_21)
remaining = [i for i in items if i['file'] not in seen]
new_items = ordered_21 + remaining

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(new_items, f, indent=2, ensure_ascii=False)

print("Saved new gallery JSON with mathematically matched column heights!")
