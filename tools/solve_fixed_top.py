import json, os, random
from PIL import Image

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

base_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public'
for i in items:
    p = os.path.join(base_dir, i['file'].lstrip('/'))
    if os.path.exists(p):
        im = Image.open(p)
        i['aspect'] = im.size[1] / float(im.size[0])
    else:
        i['aspect'] = 0.666

def get(k):
    for i in items:
        if k in i['file']:
            return i
    print(f"NOT FOUND: {k}")
    return None

# Fixed head for each column as seen in user screenshot:
col1_fixed = [
    get("tiger_territory_marking"),    # Horiz Tigre marquage (0.666)
    get("perruche_tete_prune_fleur")   # Vert Perruche (1.778)
]

col2_fixed = [
    get("tigre_bengale_embuscade_vertical") # Vert Regard perçant (1.781)
]

col3_fixed = [
    get("marabout_chevelu_pose_marais"),    # Horiz Marabout (0.5625)
    get("gavial_gange_nage_riviere"),       # Horiz Gavial (0.6660)
    get("tigre_bengale_traversee_riviere")  # Horiz Tigre traversée (0.5625)
]

fixed_files = set(i['file'] for i in col1_fixed + col2_fixed + col3_fixed)

# The remaining 15 items in our 21-photo pool:
pool_21_names = [
    "tigre_bengale_pistage",
    "portrait_elephant_asie",
    "bebe_macaque_mere",
    "langur_gris_cri_alarme",
    "elephant_asie_male_jungle",
    "lezard_agame_jardin_camouflage",
    "varan_bengale_arbre",
    "leopard_asie_affut_lisiere",
    "crocodile_marais_rapti",
    "paon_bleu_parade_roue",
    "tiger_water_pond",
    "rhino_unicorne_oiseaux_pique_boeuf",
    "tchitrec_paradis_longues_rectrices",
    "rhino_unicorne_brume",
    "calao_bicorne_canopee"
]

remaining_pool = [get(name) for name in pool_21_names if get(name) and get(name)['file'] not in fixed_files]
print("Remaining pool to distribute:", len(remaining_pool))

best_diff = 999
best_cols = None

for _ in range(500000):
    shuffled = random.sample(remaining_pool, len(remaining_pool))
    c1_tail = shuffled[:5]
    c2_tail = shuffled[5:11]
    c3_tail = shuffled[11:15]
    
    c1 = col1_fixed + c1_tail
    c2 = col2_fixed + c2_tail
    c3 = col3_fixed + c3_tail
    
    s1 = sum(x['aspect'] for x in c1)
    s2 = sum(x['aspect'] for x in c2)
    s3 = sum(x['aspect'] for x in c3)
    
    diff = max(s1, s2, s3) - min(s1, s2, s3)
    if diff < best_diff:
        best_diff = diff
        best_cols = (c1, c2, c3, s1, s2, s3)
        if diff < 0.01:
            break

c1, c2, c3, s1, s2, s3 = best_cols
print(f"\nBest constrained balance diff: {best_diff:.4f}")
print(f"Col 1 (height={s1:.4f}):")
for i in c1:
    print(f"  - [{i['category']}] {i['title']} ({i['aspect']:.4f})")
print(f"Col 2 (height={s2:.4f}):")
for i in c2:
    print(f"  - [{i['category']}] {i['title']} ({i['aspect']:.4f})")
print(f"Col 3 (height={s3:.4f}):")
for i in c3:
    print(f"  - [{i['category']}] {i['title']} ({i['aspect']:.4f})")

ordered_21 = c1 + c2 + c3
seen = set(i['file'] for i in ordered_21)
remaining = [i for i in items if i['file'] not in seen]
new_items = ordered_21 + remaining

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(new_items, f, indent=2, ensure_ascii=False)

print("Saved constrained layout to wildlife_gallery.json!")
