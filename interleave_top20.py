import json

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

def get_item(filename):
    for i in items:
        if filename in i['file']:
            return i
    print(f"NOT FOUND: {filename}")
    return None

# Selected 20 photos (strictly: 5 tigres, 1 leopard, 2 rhino, 2 elephants, 1 calao, 3 oiseaux, 2 reptiles, 2 crocodiles, 2 singes)
# Replacing sloth bear with perruche_tete_prune_fleur.webp
curated_20_files = [
    # 1. Tiger (Horiz)
    "tiger_territory_marking.webp",
    # 2. Bird (Vert - Colorful pink/green)
    "perruche_tete_prune_fleur.webp",
    # 3. Croc (Horiz - Water/Mirror)
    "crocodile_marais_rapti.webp",
    # 4. Monkey (Horiz - Baby Macaque)
    "bebe_macaque_mere.webp",
    # 5. Reptile (Vert - Tree Monitor)
    "varan_bengale_arbre.webp",
    # 6. Tiger (Vert - Intense eyes behind tree)
    "tigre_bengale_embuscade_vertical.webp",
    # 7. Rhino (Horiz - Mist savanna)
    "rhino_unicorne_brume.webp",
    # 8. Hornbill (Horiz - Great Hornbill)
    "calao_bicorne_canopee.webp",
    # 9. Leopard (Horiz - Spotted cat)
    "leopard_asie_affut_lisiere.webp",
    # 10. Monkey (Vert - Alarm call langur)
    "langur_gris_cri_alarme.webp",
    # 11. Elephant (Horiz - Deep jungle)
    "elephant_asie_male_jungle.webp",
    # 12. Bird (Vert - Paradise flycatcher white streamer)
    "tchitrec_paradis_longues_rectrices.webp",
    # 13. Croc (Horiz - Gharial swimming)
    "gavial_gange_nage_riviere.webp",
    # 14. Tiger (Horiz - River crossing)
    "tigre_bengale_traversee_riviere.webp",
    # 15. Reptile (Horiz - Agame lizard)
    "lezard_agame_jardin_camouflage.webp",
    # 16. Elephant (Vert - Powerful portrait)
    "portrait_elephant_asie.webp",
    # 17. Bird (Horiz - Peacock full fan display)
    "paon_bleu_parade_roue.webp",
    # 18. Tiger (Horiz - Waterhole)
    "tiger_water_pond.webp",
    # 19. Rhino (Horiz - Rhino & mynas)
    "rhino_unicorne_oiseaux_pique_boeuf.webp",
    # 20. Tiger (Horiz - King approaching)
    "tigre_bengale_pistage.webp"
]

curated_20 = []
seen = set()
for fname in curated_20_files:
    item = get_item(fname)
    if item:
        curated_20.append(item)
        seen.add(item['file'])

print(f"Top 20 count: {len(curated_20)}")

# Check category counts:
cat_counts = {}
for i in curated_20:
    c = i['category']
    cat_counts[c] = cat_counts.get(c, 0) + 1

print("Category breakdown in top 20:", cat_counts)

# Remaining photos (including Sloth Bear and all others)
remaining = [i for i in items if i['file'] not in seen]
print(f"Remaining photos count: {len(remaining)}")

all_ordered = curated_20 + remaining

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(all_ordered, f, indent=2, ensure_ascii=False)

print("Saved new interleaved list!")
