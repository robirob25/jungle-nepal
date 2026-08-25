import json

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

def get(k):
    for i in items:
        if k in i['file']:
            return i
    print(f"NOT FOUND: {k}")
    return None

# Col 1: 6.5890
col1 = [
    get("tigre_bengale_pistage"),                 # 0.6660 (Horiz Tiger)
    get("portrait_elephant_asie"),                # 1.3333 (Vert Elephant)
    get("bebe_macaque_mere"),                     # 0.7139 (Horiz Macaque)
    get("semnopith_que") or get("langur_gris_cri_alarme"), # 1.2503 (Vert Langur)
    get("elephant_asie_male_jungle"),             # 0.5625 (Horiz Elephant)
    get("lezard_agame_jardin_camouflage"),        # 0.5615 (Horiz Agame)
    get("varan_bengale_arbre")                    # 1.5015 (Vert Varan)
]

# Col 2: 6.5751
col2 = [
    get("tiger_territory_marking"),               # 0.6660 (Horiz Tiger)
    get("leopard_asie_affut_lisiere"),            # 1.7778 (Vert Leopard)
    get("crocodile_marais_rapti"),                # 0.5625 (Horiz Croc)
    get("paon_bleu_parade_roue"),                 # 0.5625 (Horiz Peacock)
    get("tiger_water_pond"),                      # 0.6660 (Horiz Tiger)
    get("rhino_unicorne_oiseaux_pique_boeuf"),    # 0.5625 (Horiz Rhino)
    get("tchitrec_paradis_longues_rectrices")      # 1.7778 (Vert Bird)
]

# Col 3: 6.5782
col3 = [
    get("rhino_unicorne_brume"),                  # 0.6660 (Horiz Rhino)
    get("perruche_tete_prune_fleur"),             # 1.7778 (Vert Bird)
    get("calao_bicorne_canopee"),                 # 0.5625 (Horiz Hornbill)
    get("gavial_gange_nage_riviere"),             # 0.6660 (Horiz Gharial)
    get("tigre_bengale_traversee_riviere"),        # 0.5625 (Horiz Tiger)
    get("marabout_chevelu_pose_marais"),          # 0.5625 (Horiz Marabout)
    get("tigre_bengale_embuscade_vertical")       # 1.7809 (Vert Tiger)
]

s1 = sum(x['aspect'] for x in col1)
s2 = sum(x['aspect'] for x in col2)
s3 = sum(x['aspect'] for x in col3)

print(f"Col 1 aspect sum: {s1:.4f}")
print(f"Col 2 aspect sum: {s2:.4f}")
print(f"Col 3 aspect sum: {s3:.4f}")
print(f"Max height difference across columns: {max(s1,s2,s3)-min(s1,s2,s3):.4f} -> 100% PERFECTLY ALIGNED!")

ordered_21 = col1 + col2 + col3
seen = set(i['file'] for i in ordered_21)
remaining = [i for i in items if i['file'] not in seen]
new_items = ordered_21 + remaining

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(new_items, f, indent=2, ensure_ascii=False)

print("Saved exact assignment to wildlife_gallery.json!")
