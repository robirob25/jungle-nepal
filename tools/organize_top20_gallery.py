import json

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Find matching items
def find_item(keyword, category=None):
    for i in items:
        if category and i['category'] != category:
            continue
        if keyword.lower() in i['title'].lower() or keyword.lower() in i['file'].lower() or keyword.lower() in i['desc'].lower():
            return i
    return None

# The top 20 requested:
# 5 tigres
t1 = find_item('marquage', 'felins') or find_item('territoir', 'felins') or find_item('tiger_territory', 'felins')
t2 = find_item('point d\'eau', 'felins') or find_item('water_pond', 'felins')
t3 = find_item('pistage', 'felins') or find_item('en marche', 'felins') or find_item('approche', 'felins')
t4 = find_item('regard', 'felins') or find_item('embuscade', 'felins')
t5 = find_item('traversee', 'felins') or find_item('savane', 'felins') or find_item('baignade', 'felins')

# 1 leopard
l1 = find_item('leopard', 'felins')

# 2 rhino
r1 = find_item('brume', 'mammiferes') or find_item('rhino_unicorne_brume', 'mammiferes')
r2 = find_item('martins', 'mammiferes') or find_item('pique_boeuf', 'mammiferes')

# 2 elephants
e1 = find_item('elephant_asie_male', 'mammiferes') or find_item('sauvage d\'asie', 'mammiferes')
e2 = find_item('portrait_elephant', 'mammiferes') or find_item('face_jungle', 'mammiferes')

# 1 grand calao
c1 = find_item('calao', 'oiseaux')

# 2 autres oiseaux
o1 = find_item('paon', 'oiseaux')
o2 = find_item('tchitrec', 'oiseaux') or find_item('marabout', 'oiseaux')

# 2 reptiles
rep1 = find_item('varan_bengale_arbre', 'reptiles') or find_item('varan', 'reptiles')
rep2 = find_item('agame', 'reptiles') or find_item('serpent', 'reptiles')

# 2 crocodiles (Crocodile des marais + Gavial du Gange)
croc1 = find_item('crocodile', 'reptiles') or find_item('mugger', 'reptiles')
croc2 = find_item('gavial', 'reptiles')

# 2 singes
s1 = find_item('bebe_macaque', 'mammiferes') or find_item('singe', 'mammiferes')
s2 = find_item('langur', 'mammiferes') or find_item('semnopith', 'mammiferes')

# 1 autre au choix: Ours lippu (Sloth Bear)
choice1 = find_item('ours_lippu', 'mammiferes') or find_item('sloth', 'mammiferes')

top20 = [t1, t2, t3, t4, t5, l1, r1, r2, e1, e2, c1, o1, o2, rep1, rep2, croc1, croc2, s1, s2, choice1]

# Filter out None and remove duplicates within top20
clean_top20 = []
seen_files = set()
for x in top20:
    if x and x['file'] not in seen_files:
        clean_top20.append(x)
        seen_files.add(x['file'])

print(f"Clean top 20 count: {len(clean_top20)}")
for idx, x in enumerate(clean_top20):
    print(f" {idx+1}. [{x['category'].upper()}] {x['title']} ({x['file']})")

# The rest of photos
remaining = [i for i in items if i['file'] not in seen_files]
print(f"Remaining photos count: {len(remaining)}")

ordered_items = clean_top20 + remaining

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
    json.dump(ordered_items, f, indent=2, ensure_ascii=False)

print("Saved organized list with top 20 matching exact user prompt!")
