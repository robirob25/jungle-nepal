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

def get_item_by_fname(fname):
    for i in items:
        if fname in i['file']:
            return i
    return None

# The 21 photos to perfectly balance into 3 columns of 7 photos:
# Adding the vertical Tchitrec de paradis or Chevêchette to fill the left column gap!
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

# We want 3 columns of 7 items each where sum of aspects is almost identical
# Column 1 (Left):
# Let's carefully compose Column 1, Column 2, Column 3:
col1_files = [
    "tiger_territory_marking.webp", # Horiz Tiger
    "perruche_tete_prune_fleur.webp", # Vert Bird
    "crocodile_marais_rapti.webp", # Horiz Croc
    "bebe_macaque_mere.webp", # Horiz Macaque
    "varan_bengale_arbre.webp", # Vert Varan
    "tchitrec_paradis_longues_rectrices.webp", # Vert Tchitrec (Fills the gap!)
    "rhino_unicorne_brume.webp" # Horiz Rhino
]

col2_files = [
    "tigre_bengale_embuscade_vertical.webp", # Vert Tiger
    "calao_bicorne_canopee.webp", # Horiz Hornbill
    "leopard_asie_affut_lisiere.webp", # Vert Leopard
    "gavial_gange_nage_riviere.webp", # Horiz Gharial
    "langur_gris_cri_alarme.webp", # Vert Langur
    "elephant_asie_male_jungle.webp", # Horiz Elephant
    "lezard_agame_jardin_camouflage.webp" # Horiz Agame
]

col3_files = [
    "marabout_chevelu_pose_marais.webp", # Horiz Marabout
    "portrait_elephant_asie.webp", # Vert Elephant
    "paon_bleu_parade_roue.webp", # Horiz Peacock
    "tiger_water_pond.webp", # Horiz Tiger
    "rhino_unicorne_oiseaux_pique_boeuf.webp", # Horiz Rhino & Martins
    "tigre_bengale_traversee_riviere.webp", # Horiz River Tiger
    "tigre_bengale_pistage.webp" # Horiz King Tiger
]

c1_items = [get_item_by_fname(f) for f in col1_files]
c2_items = [get_item_by_fname(f) for f in col2_files]
c3_items = [get_item_by_fname(f) for f in col3_files]

h1 = sum(i['aspect'] for i in c1_items)
h2 = sum(i['aspect'] for i in c2_items)
h3 = sum(i['aspect'] for i in c3_items)

print(f"Col 1 aspect sum (7 items): {h1:.3f}")
print(f"Col 2 aspect sum (7 items): {h2:.3f}")
print(f"Col 3 aspect sum (7 items): {h3:.3f}")

# Order for sequential CSS columns: col1 items, then col2 items, then col3 items
ordered_21 = c1_items + c2_items + c3_items
seen_21 = set(i['file'] for i in ordered_21)

remaining = [i for i in items if i['file'] not in seen_21]

new_total_list = ordered_21 + remaining

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(new_total_list, f, indent=2, ensure_ascii=False)

print(f"Total curated gallery: {len(new_total_list)}")
