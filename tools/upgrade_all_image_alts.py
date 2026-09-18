import json, re, glob, os

# Full SEO ALT generation engine
def generate_seo_alt(src, current_alt="", context_title="", lang="fr"):
    src_lower = src.lower()
    fname = os.path.splitext(os.path.basename(src))[0].lower()
    fname_clean = fname.replace('-', ' ').replace('_', ' ')
    
    species_fr = ""
    species_en = ""
    biome_fr = ""
    biome_en = ""
    location_fr = "parc national de Bardia, Teraï, Népal"
    location_en = "Bardia National Park, Terai, Nepal"
    
    if "chitwan" in src_lower or "chitwan" in context_title.lower():
        location_fr = "parc national de Chitwan, Teraï, Népal"
        location_en = "Chitwan National Park, Terai, Nepal"
    elif "suklaphanta" in src_lower or "suklaphanta" in context_title.lower():
        location_fr = "réserve faunique de Suklaphanta, Teraï occidental, Népal"
        location_en = "Suklaphanta Wildlife Reserve, Western Terai, Nepal"
    elif "panthere-des-neiges" in src_lower or "snow-leopard" in src_lower or "panthere-des-neiges" in context_title.lower():
        location_fr = "hautes vallées himalayennes du Mustang et Dolpo, Népal"
        location_en = "high Himalayan valleys of Mustang and Dolpo, Nepal"
    elif "rara" in src_lower or "rara" in context_title.lower():
        location_fr = "parc national du lac Rara, haut Himalaya népalais"
        location_en = "Rara Lake National Park, High Himalayas, Nepal"
    elif "katmandou" in src_lower or "boudhanath" in src_lower:
        location_fr = "vallée de Katmandou, Népal"
        location_en = "Kathmandu Valley, Nepal"
    elif "annapurna" in src_lower:
        location_fr = "massif des Annapurnas, Himalaya du Népal"
        location_en = "Annapurna Range, Nepalese Himalayas"

    if "tigre" in fname_clean or "tiger" in fname_clean:
        if any(w in fname_clean for w in ["eau", "water", "traversee", "riviere"]):
            species_fr = "Tigre du Bengale (Panthera tigris) traversant une rivière"
            species_en = "Bengal tiger (Panthera tigris) crossing a river channel"
            biome_fr = "dans les cours d'eau de la forêt de sals"
            biome_en = "through the riverbeds of the sal forest"
        elif any(w in fname_clean for w in ["herbe", "grass", "hautes"]):
            species_fr = "Tigre du Bengale (Panthera tigris) en affût discret"
            species_en = "Bengal tiger (Panthera tigris) stalking through tall elephant grass"
            biome_fr = "dans les hautes herbes à éléphant (phantas)"
            biome_en = "in the dense alluvial grasslands (phantas)"
        elif any(w in fname_clean for w in ["repos", "plage", "berges", "sable"]):
            species_fr = "Tigre du Bengale mâle adulte au repos"
            species_en = "Adult male Bengal tiger resting on a sandy riverbank"
            biome_fr = "sur une berge ensoleillée de la rivière Karnali"
            biome_en = "on a sunny gravel bar along the Karnali River"
        else:
            species_fr = "Tigre du Bengale sauvage (Panthera tigris)"
            species_en = "Wild Bengal tiger (Panthera tigris)"
            biome_fr = "dans son habitat naturel de jungle tropicale"
            biome_en = "in its natural tropical jungle habitat"

    elif "rhino" in fname_clean or "rhinoceros" in fname_clean:
        if "brume" in fname_clean or "mist" in fname_clean:
            species_fr = "Grand rhinocéros unicorne (Rhinoceros unicornis) émergeant de la brume matinale"
            species_en = "Greater one-horned rhinoceros (Rhinoceros unicornis) emerging through morning mist"
            biome_fr = "dans les prairies humides alluviales"
            biome_en = "in the damp alluvial floodplains"
        elif any(w in fname_clean for w in ["eau", "marais", "boue"]):
            species_fr = "Rhinocéros unicorne prenant un bain de boue rafraîchissant"
            species_en = "One-horned rhino wallowing in a muddy watering hole"
            biome_fr = "dans un marécage ombragé"
            biome_en = "inside a shaded tropical wetland"
        else:
            species_fr = "Grand rhinocéros d'Asie (Rhinoceros unicornis)"
            species_en = "Asian greater one-horned rhinoceros"
            biome_fr = "au cœur des savanes d'herbes géantes"
            biome_en = "amidst towering elephant grasslands"

    elif "calao" in fname_clean or "hornbill" in fname_clean:
        if "bicorne" in fname_clean or "great" in fname_clean:
            species_fr = "Grand calao bicorne (Buceros bicornis) perché au sommet de la canopée"
            species_en = "Great Hornbill (Buceros bicornis) perched atop the primary canopy"
            biome_fr = "sur une branche maîtresse de figuier sauvage"
            biome_en = "upon a massive wild fig branch"
        elif any(w in fname_clean for w in ["pie", "oriental", "pied"]):
            species_fr = "Calao pie oriental (Anthracoceros albirostris) en vol"
            species_en = "Oriental Pied Hornbill (Anthracoceros albirostris) in flight"
            biome_fr = "au-dessus des lisières forestières"
            biome_en = "across forest edge corridors"
        else:
            species_fr = "Calao sauvage du Teraï"
            species_en = "Wild hornbill of the Terai"
            biome_fr = "dans la canopée de la forêt primaire"
            biome_en = "within the primary forest canopy"

    elif "rollier" in fname_clean or "roller" in fname_clean:
        if any(w in fname_clean for w in ["vol", "envol", "turquoise"]):
            species_fr = "Rollier indien (Coracias benghalensis) déployant ses ailes bleu turquoise en plein vol"
            species_en = "Indian Roller (Coracias benghalensis) displaying vibrant turquoise wings in flight"
            biome_fr = "au-dessus des savanes alluviales"
            biome_en = "over the open alluvial grasslands"
        else:
            species_fr = "Rollier indien (Coracias benghalensis) à l'affût"
            species_en = "Indian Roller (Coracias benghalensis) perched on a lookout branch"
            biome_fr = "sur une branche d'acacia surplombant la clairière"
            biome_en = "on an acacia perch overlooking the savannah"

    elif "tchitrec" in fname_clean or "flycatcher" in fname_clean:
        species_fr = "Tchitrec de paradis mâle (Terpsiphone paradisi) aux longues rectrices flottantes"
        species_en = "Asian Paradise Flycatcher male (Terpsiphone paradisi) with long flowing tail streamers"
        biome_fr = "dans les sous-bois ombragés de la forêt galerie"
        biome_en = "in the dense, shaded understory of the riverine forest"

    elif "leopard" in fname_clean or "panthere" in fname_clean:
        if "neige" in fname_clean or "snow" in fname_clean:
            species_fr = "Panthère des neiges (Panthera uncia), le fantôme de l'Himalaya"
            species_en = "Snow leopard (Panthera uncia), ghost of the high Himalayas"
            biome_fr = "sur une falaise rocheuse escarpée balayée par les vents"
            biome_en = "upon a steep, wind-swept rocky crag"
        else:
            species_fr = "Léopard indien (Panthera pardus fusca) camouflé dans les branchages"
            species_en = "Indian leopard (Panthera pardus fusca) camouflaged among tree branches"
            biome_fr = "dans la frondaison d'un arbre de sal"
            biome_en = "within the dense foliage of a sal tree"

    elif "elephant" in fname_clean:
        if any(w in fname_clean for w in ["petit", "mere", "calf"]):
            species_fr = "Éléphante d'Asie sauvage (Elephas maximus) et son petit éléphanteau"
            species_en = "Wild Asian elephant cow (Elephas maximus) accompanying her young calf"
            biome_fr = "longeant un corridor forestier tropical"
            biome_en = "navigating a tropical riverine corridor"
        else:
            species_fr = "Grand éléphant sauvage d'Asie (Elephas maximus)"
            species_en = "Majestic wild Asian bull elephant (Elephas maximus)"
            biome_fr = "traversant les savanes inondables"
            biome_en = "crossing the vast alluvial floodplains"

    elif "gavial" in fname_clean or "crocodile" in fname_clean:
        if "gavial" in fname_clean:
            species_fr = "Gavial du Gange (Gavialis gangeticus) au museau effilé thermorégulant au soleil"
            species_en = "Gharial crocodile (Gavialis gangeticus) with slender snout basking in the sun"
            biome_fr = "sur un banc de sable préservé de la rivière Karnali"
            biome_en = "on a pristine sandbar along the Karnali River"
        else:
            species_fr = "Crocodile des marais (Crocodylus palustris)"
            species_en = "Mugger crocodile (Crocodylus palustris)"
            biome_fr = "immobile sur les berges d'un bras mort"
            biome_en = "basking along the banks of a river oxbow"

    elif "vautour" in fname_clean or "vulture" in fname_clean:
        species_fr = "Groupe de vautours chaugouns (Gyps bengalensis) en observation"
        species_en = "Critically endangered White-rumped Vultures (Gyps bengalensis) perched on a dead snag"
        biome_fr = "sur les cimes d'un arbre mort de la savane"
        biome_en = "atop a dead tree in the open savannah"

    elif any(w in fname_clean for w in ["chouette", "owl", "chevech"]):
        species_fr = "Chevêchette de jungle ou chouette tachetée (Athene brama)"
        species_en = "Jungle Owlet or Spotted Owlet (Athene brama) peering from a tree hollow"
        biome_fr = "dans la cavité d'un tronc d'arbre centenaire"
        biome_en = "inside an old-growth tree hollow"

    elif "perruche" in fname_clean or "parakeet" in fname_clean:
        species_fr = "Perruche à tête prune (Psittacula cyanocephala) butinant un arbre en fleur"
        species_en = "Plum-headed Parakeet (Psittacula cyanocephala) foraging in a flowering jungle tree"
        biome_fr = "au sommet des bosquets subtropicaux"
        biome_en = "in the subtropical forest canopy"

    elif "martin" in fname_clean or "kingfisher" in fname_clean:
        species_fr = "Martin-chasseur ou martin-pêcheur aux couleurs vives"
        species_en = "Colorful kingfisher perched on a riverside branch"
        biome_fr = "au-dessus des eaux calmes de la rivière"
        biome_en = "above tranquil river waters"

    elif "nilgaut" in fname_clean or "nilgai" in fname_clean:
        species_fr = "Antilope Nilgaut ou Taureau Bleu (Boselaphus tragocamelus)"
        species_en = "Nilgai or Blue Bull antelope (Boselaphus tragocamelus)"
        biome_fr = "dans les plaines ouvertes et clairières sèches"
        biome_en = "across open grasslands and scrub borders"

    elif "chacal" in fname_clean or "jackal" in fname_clean:
        species_fr = "Chacal doré (Canis aureus) en patrouille furtive"
        species_en = "Golden Jackal (Canis aureus) prowling silently"
        biome_fr = "à travers les herbes dorées de la savane"
        biome_en = "through tall golden savannah grass"

    elif "varan" in fname_clean or "monitor" in fname_clean:
        species_fr = "Varan du Bengale (Varanus bengalensis), dragon des terres basses"
        species_en = "Bengal monitor lizard (Varanus bengalensis)"
        biome_fr = "longeant les berges sablonneuses de la jungle"
        biome_en = "scouting along sandy riverbanks"

    elif any(w in fname_clean for w in ["langur", "macaque", "singe", "monkey"]):
        species_fr = "Langur sacré d'Hanuman (Semnopithecus hector) servant de sentinelle anti-prédateur"
        species_en = "Hanuman Grey Langur (Semnopithecus hector) keeping watch as jungle sentinel"
        biome_fr = "perché sur une termitière dans la forêt de sals"
        biome_en = "perched atop a termite mound in the sal forest"

    elif any(w in fname_clean for w in ["camp", "bivouac", "tente", "tent"]):
        species_fr = "Campement de bivouac sauvage et safari nature Jungle Nepal Adventure"
        species_en = "Wild jungle wilderness campsite with Jungle Nepal Adventure"
        biome_fr = "au bord de la rivière Babai"
        biome_en = "along the remote Babai River"

    elif any(w in fname_clean for w in ["guide", "photographe", "pistage", "adrien", "robin", "safari_a_pied", "suivez", "traces"]):
        species_fr = "Guide naturaliste et pisteurs locaux en safari à pied d'observation de la faune"
        species_en = "Local naturalist guides and wildlife trackers on foot safari"
        biome_fr = "en immersion totale dans la forêt primaire"
        biome_en = "deep inside the primary tropical forest"

    elif any(w in fname_clean for w in ["pirogue", "rafting", "bateau"]):
        species_fr = "Safari fluvial silencieux en pirogue traditionnelle en bois"
        species_en = "Silent river safari in a traditional wooden dugout canoe"
        biome_fr = "glissant sur les eaux calmes de la rivière"
        biome_en = "gliding along calm river channels"

    elif any(w in fname_clean for w in ["tharu", "village", "spectacle"]):
        species_fr = "Immersion culturelle et traditions du peuple indigène Tharu"
        species_en = "Cultural immersion and ancestral traditions of the indigenous Tharu people"
        biome_fr = "dans un village vernaculaire en lisière de jungle"
        biome_en = "in a traditional earthen village bordering the jungle"

    elif any(w in fname_clean for w in ["temple", "boudhanath", "stupa"]):
        species_fr = "Grand Stupa bouddhiste sacré de Boudhanath orné de drapeaux de prières"
        species_en = "Sacred Buddhist Boudhanath Stupa draped with prayer flags"
        biome_fr = "au cœur du patrimoine spirituel népalais"
        biome_en = "in the historic spiritual heart of Kathmandu"

    if species_fr:
        if lang == "fr":
            return f"{species_fr} {biome_fr} au {location_fr}"
        else:
            return f"{species_en} {biome_en} in {location_en}"
    else:
        if lang == "fr":
            return f"Observation de la faune sauvage et safari ({fname_clean}) au {location_fr}"
        else:
            return f"Wildlife observation and jungle safari ({fname_clean}) in {location_en}"

# 1. Update Blog Posts (FR & EN)
for lang, path in [('fr', 'src/data/blog_posts.json'), ('en', 'src/data/blog_posts.en.json')]:
    with open(path, 'r', encoding='utf-8') as f:
        posts = json.load(f)
    
    updated_posts = 0
    for p in posts:
        content = p.get('content', '')
        # Replace all <img ...> tags with updated alt
        def replace_img(match):
            tag = match.group(0)
            src_match = re.search(r'src=[\"\']([^\"\']+)[\"\']', tag)
            if not src_match:
                return tag
            src = src_match.group(1)
            new_alt = generate_seo_alt(src, context_title=p.get('title', ''), lang=lang)
            # Remove old alt if present
            clean_tag = re.sub(r'\s+alt=[\"\'][^\"\']*[\"\']', '', tag)
            # Insert new alt right after <img
            res = clean_tag.replace('<img', f'<img alt="{new_alt}"', 1)
            return res
            
        new_content = re.sub(r'<img[^>]+>', replace_img, content)
        if new_content != content:
            p['content'] = new_content
            updated_posts += 1
            
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    print(f"Updated images in {updated_posts} {lang.upper()} blog posts!")

# 2. Update Wildlife Gallery JSON
if os.path.exists('src/data/wildlife_gallery.json'):
    with open('src/data/wildlife_gallery.json', 'r', encoding='utf-8') as f:
        gallery = json.load(f)
    for item in gallery:
        src = item.get('src', '') or item.get('image', '')
        if src:
            item['alt'] = generate_seo_alt(src, lang='fr')
            item['alt_en'] = generate_seo_alt(src, lang='en')
    with open('src/data/wildlife_gallery.json', 'w', encoding='utf-8') as f:
        json.dump(gallery, f, ensure_ascii=False, indent=2)
    print("Updated src/data/wildlife_gallery.json!")

print("All ALT tags upgraded with species, biotope, and exact location!")
