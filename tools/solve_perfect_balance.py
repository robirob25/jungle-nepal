import json, os, itertools
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

def get_item_by_fname(fname):
    for i in items:
        if fname in i['file']:
            return i
    return None

# We want 21 photos (7 per column or balanced heights)
# Let's select the 20 existing plus 1 vertical bird (e.g., tchitrec_paradis_longues_rectrices.webp)
pool_files = [
    # Tigers (5)
    "tiger_territory_marking.webp",
    "tigre_bengale_embuscade_vertical.webp",
    "tigre_bengale_traversee_riviere.webp",
    "tiger_water_pond.webp",
    "tigre_bengale_pistage.webp",
    # Leopard (1)
    "leopard_asie_affut_lisiere.webp",
    # Rhinos (2)
    "rhino_unicorne_brume.webp",
    "rhino_unicorne_oiseaux_pique_boeuf.webp",
    # Elephants (2)
    "portrait_elephant_asie.webp",
    "elephant_asie_male_jungle.webp",
    # Birds (5: Calao, Perruche, Marabout, Paon, Tchitrec)
    "calao_bicorne_canopee.webp",
    "perruche_tete_prune_fleur.webp",
    "marabout_chevelu_pose_marais.webp",
    "paon_bleu_parade_roue.webp",
    "tchitrec_paradis_longues_rectrices.webp",
    # Reptiles (2)
    "varan_bengale_arbre.webp",
    "lezard_agame_jardin_camouflage.webp",
    # Crocodiles (2)
    "crocodile_marais_rapti.webp",
    "gavial_gange_nage_riviere.webp",
    # Monkeys (2)
    "bebe_macaque_mere.webp",
    "langur_gris_cri_alarme.webp"
]

selected_pool = [get_item_by_fname(f) for f in pool_files]
print("Pool size:", len(selected_pool))

# Let's divide into 3 columns of 7 items each
# Total aspect sum:
tot = sum(i['aspect'] for i in selected_pool)
print(f"Total aspect sum of 21 photos: {tot:.3f}, Target per column of 7: {tot/3:.3f}")

# Let's find 3 columns (c1, c2, c3) of 7 items each where sum(aspect) is as close as possible
# with good species mix in each column:
# Each column should have:
# - at least 1-2 felines
# - at least 1-2 birds
# - at least 1 large mammal
# - at least 1 reptile/croc

best_diff = 999
best_partition = None

# Let's test a structured composition:
# Col 1 (7 items):
# Tiger (0.666), Perruche Vert (1.778), Crocodile (0.562), Baby Macaque (0.714), Varan Vert (1.501), Tchitrec Vert (1.778), Rhino (0.666) -> total ~ 7.665? Wait, let's balance!
# Let's count vertical photos:
# Verticals in pool: Perruche (1.778), Varan (1.501), Tiger Embuscade (1.781), Leopard Affut (1.778), Langur (1.250), Portrait Elephant (1.333), Tchitrec (1.778)
# Total 7 verticals!
# Horizontals in pool: 14 horizontals (~0.562 to 0.714)
# With 7 verticals and 14 horizontals across 3 columns:
# Ideal distribution:
# Col 1: 2 verticals + 5 horizontals = 7 items (2*1.6 + 5*0.6 = 3.2 + 3.0 = 6.2)
# Col 2: 2 verticals + 5 horizontals = 7 items (2*1.6 + 5*0.6 = 3.2 + 3.0 = 6.2)
# Col 3: 3 verticals + 4 horizontals = 7 items (3*1.5 + 4*0.6 = 4.5 + 2.4 = 6.9)
# Or if Col 3 uses slightly lower aspect verticals (Langur 1.25 + Portrait Elephant 1.33 + Tchitrec 1.77 = 4.35 + 4*0.56 = 6.6)
# Let's find the exact combination where sums are nearly equal!

v_items = [i for i in selected_pool if i['aspect'] > 1.0]
h_items = [i for i in selected_pool if i['aspect'] <= 1.0]
print(f"Verticals: {len(v_items)}, Horizontals: {len(h_items)}")

for v in v_items:
    print(f" Vert: {v['title']} (aspect={v['aspect']:.3f})")

# Let's write an optimizer to find the closest 3-way partition
from itertools import combinations

for c1_v in combinations(v_items, 2):
    rem_v = [v for v in v_items if v not in c1_v]
    for c2_v in combinations(rem_v, 2):
        c3_v = [v for v in rem_v if v not in c2_v]
        
        for c1_h in combinations(h_items, 5):
            rem_h = [h for h in h_items if h not in c1_h]
            for c2_h in combinations(rem_h, 5):
                c3_h = [h for h in rem_h if h not in c2_h]
                
                sum1 = sum(i['aspect'] for i in c1_v) + sum(i['aspect'] for i in c1_h)
                sum2 = sum(i['aspect'] for i in c2_v) + sum(i['aspect'] for i in c2_h)
                sum3 = sum(i['aspect'] for i in c3_v) + sum(i['aspect'] for i in c3_h)
                
                diff = max(sum1, sum2, sum3) - min(sum1, sum2, sum3)
                if diff < best_diff:
                    best_diff = diff
                    best_partition = (list(c1_v) + list(c1_h), list(c2_v) + list(c2_h), list(c3_v) + list(c3_h), sum1, sum2, sum3)

print(f"\nBest partition max height difference: {best_diff:.4f}")
col1, col2, col3, s1, s2, s3 = best_partition
print(f"Col 1 height sum: {s1:.3f}")
for i in col1:
    print(f"  - [{i['category']}] {i['title']} ({i['aspect']:.3f})")
print(f"Col 2 height sum: {s2:.3f}")
for i in col2:
    print(f"  - [{i['category']}] {i['title']} ({i['aspect']:.3f})")
print(f"Col 3 height sum: {s3:.3f}")
for i in col3:
    print(f"  - [{i['category']}] {i['title']} ({i['aspect']:.3f})")

