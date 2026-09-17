#!/usr/bin/env python3
import os
import re

PAGES_DIR = "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages"
EN_DIR = os.path.join(PAGES_DIR, "en")

FR_TO_EN_REPLACEMENTS = [
    # Language attributes & metadata
    ('lang="fr"', 'lang="en"'),
    ("lang='fr'", "lang='en'"),
    ('lang: "fr"', 'lang: "en"'),
    ("lang: 'fr'", "lang: 'en'"),
    ('fr-FR', 'en-US'),
    ('https://junglenepal.com/a-propos.html', 'https://junglenepal.com/en/about.html'),
    ('https://junglenepal.com/contact.html', 'https://junglenepal.com/en/contact.html'),
    ('https://junglenepal.com/destinations.html', 'https://junglenepal.com/en/destinations.html'),

    # Links
    ('href="/"', 'href="/en/"'),
    ("href='/'", "href='/en/'"),
    ('href="/#', 'href="/en/#'),
    ('href="/a-propos.html"', 'href="/en/about.html"'),
    ('href="/contact.html"', 'href="/en/contact.html"'),
    ('href="/mentions-legales"', 'href="/en/legal-mentions.html"'),
    ('href="/mentions-legales.html"', 'href="/en/legal-mentions.html"'),
    ('data/blog_posts.json', 'data/blog_posts.en.json'),
    ('href="/destinations.html"', 'href="/en/destinations.html"'),
    ('href="/destinations/', 'href="/en/destinations/'),
    ('href="/tours/', 'href="/en/tours/'),
    ('href="/blog.html"', 'href="/en/blog.html"'),
    ('href="/blog/', 'href="/en/blog/'),

    # Hero & Homepage Titles & Subtitles
    ("L'autre côté du Népal", "The Other Side of Nepal"),
    ("Là où les routes s’arrêtent.", "Where roads end."),
    ("Là où les routes s'arrêtent.", "Where roads end."),
    ("Là où les territoires sauvages recommencanent.", "Where untamed wilderness begins."),
    ("Là où les territoires sauvages recommencent.", "Where untamed wilderness begins."),
    ("Guidé par ceux qui y vivent.", "Guided by those who live there."),
    ("Offrez-vous votre voyage nature au Népal.", "Embark on your ultimate wildlife adventure in Nepal."),

    # Search Box & Filters
    ("<span>OÙ ?</span>", "<span>WHERE?</span>"),
    ("<span>QUAND ?</span>", "<span>WHEN?</span>"),
    ("Tous les sédays (15)", "All 15 Expeditions"),
    ("Tous les sédays", "All Expeditions"),
    ("Tous les séjours (15)", "All 15 Expeditions"),
    ("Tous les séjours", "All Expeditions"),
    ("Tous les 15 séjours", "All 15 Expeditions"),
    ("Tous les 15 Séjours", "All 15 Expeditions"),
    ("Les 15 séjours", "15 Expeditions"),
    ("15 séjours d'exception", "15 Exclusive Expeditions"),
    ("Safaris & Grands Félins (Bardia & Himalaya)", "Safaris & Big Cats (Bardia & Himalayas)"),
    ("Bivouacs & Nuits Sauvages en Jungle", "Jungle Bivouacs & Wild Nights"),
    ("Rhinocéros & Parc de Chitwan", "Rhinos & Chitwan National Park"),
    ("Rafting & Expéditions Rivières", "Rafting & River Expeditions"),
    ("Himalaya, mustang & spiritualité", "Himalayas, Mustang & Spirituality"),
    ("Grands Tours Immersion 360°", "360° Total Immersion Tours"),
    ("Toute l'année", "All Year Round"),
    ("Printemps", "Spring"),
    ("Automne", "Autumn"),
    ("Hiver", "Winter"),
    (">Rechercher<", ">Search Expeditions<"),
    ('aria-label="Rechercher"', 'aria-label="Search"'),

    # Filter Carousel Pills
    ("Safaris & Tigres", "Safaris & Tigers"),
    ("Bivouacs Jungle", "Jungle Bivouacs"),
    ("Rhinocéros & Chitwan", "Rhinos & Chitwan"),
    ("Rafting & Aventure", "Rafting & Adventure"),
    ("Mustang & Himalaya", "Mustang & Himalayas"),
    ("Tours Immersion", "Immersion Tours"),

    # Catalog & Section Badges / Headings
    ("Départs garantis • Petits groupes de 4 à 10 explorateurs", "Guaranteed Departures • Small Groups of 4 to 10 Explorers"),
    ("immersifs", "Immersive"),
    ("au Népal", "in Nepal"),
    ("Sélectionnez votre aventure pour explorer le détail jour par jour, la fiche d'inclusions et réserver votre place.", "Select your adventure to view day-by-day itineraries, complete inclusions, and reserve your spot."),
    ("Créer un séjour sur-mesure", "Create a Custom Trip"),
    ("Découvrir le circuit", "View Expedition Details"),
    ("Découvrir la destination", "Discover Destination"),
    ("Voir le séjour", "View Expedition"),
    ("Voir tous les séjours", "View All Expeditions"),
    ("Toutes les destinations", "All Destinations"),
    ("Voir toutes les destinations", "View All Destinations"),
    ("Demander un devis sur-mesure", "Request a Custom Quote"),
    ("Réserver ce voyage", "Book This Trip"),
    ("Poser une question à Robin sur WhatsApp", "Ask Robin on WhatsApp"),
    ("Contacter Robin sur WhatsApp", "Contact Robin on WhatsApp"),
    ("Micro-groupes 4 à 10 pers.", "Small Groups (4-10 max)"),
    ("Micro-groupes de 4 à 10 explorateurs", "Small Groups of 4 to 10 Explorers"),
    ("100% Pisteurs natifs", "100% Native Trackers"),
    ("Départs garantis", "Guaranteed Departures"),
    ("À partir de", "From"),
    ("Jours", "Days"),
    ("jours", "days"),

    # Destinations Names & Subtitles
    ("Parc national de Bardia", "Bardia National Park"),
    ("Parc national de Chitwan", "Chitwan National Park"),
    ("Parc national de Suklaphanta", "Suklaphanta National Park"),
    ("Les Annapurna & Pokhara", "Annapurna & Pokhara"),
    ("Katmandou", "Kathmandu"),
    ("Tigres du Bengale & safaris à pied", "Bengal Tigers & Walking Safaris"),
    ("Rhinocéros & pirogues de la Rapti", "One-Horned Rhinos & River Canoes"),
    ("Cerfs des marais & ouest sauvage", "Swamp Deer & Untamed Wild West"),
    ("Sommets mythiques & balcons alpins", "Sacred Peaks & Alpine Balconies"),
    ("Vallée des rois & temples sacrés", "Valley of Kings & Sacred Temples"),

    # Concept / Spirit & Guides
    ("L'esprit safari au Népal", "The Safari Spirit in Nepal"),
    ("L'esprit safari", "The Safari Spirit"),
    ("Pourquoi nos expéditions sont uniques", "Why Our Expeditions Are Unique"),
    ("Nos guides pisteurs", "Our Native Trackers & Guides"),
    ("Nos guides", "Our Guides"),
    ("Nés dans le Teraï, formés par la jungle.", "Born in the Terai, raised by the jungle."),

    # Common Section Headers
    ("Itinéraire Jour par Jour", "Day-by-Day Itinerary"),
    ("Fiche pratique & technique", "Technical & Practical Overview"),
    ("Ce qui est inclus / non inclus", "Inclusions & Exclusions"),
    ("Ce qui est inclus", "What's Included"),
    ("Ce qui n'est pas inclus", "What's Not Included"),
    ("Foire aux questions", "Frequently Asked Questions"),
    ("Questions fréquentes", "Frequently Asked Questions"),
    ("Avis des voyageurs", "Traveler Reviews"),
    ("Galerie faune", "Wildlife Gallery"),
    ("Informations pratiques", "Practical Details"),
    ("Budget & Tarifs", "Pricing & Budget"),
    ("Conseils de préparation", "Preparation Tips"),

    # Days
    ("Jour 1", "Day 1"),
    ("Jour 2", "Day 2"),
    ("Jour 3", "Day 3"),
    ("Jour 4", "Day 4"),
    ("Jour 5", "Day 5"),
    ("Jour 6", "Day 6"),
    ("Jour 7", "Day 7"),
    ("Jour 8", "Day 8"),
    ("Jour 9", "Day 9"),
    ("Jour 10", "Day 10"),
    ("Jour 11", "Day 11"),
    ("Jour 12", "Day 12"),
    ("Jour 13", "Day 13"),
    ("Jour 14", "Day 14"),
    ("Jour 15", "Day 15"),
    ("Jour 16", "Day 16"),
    ("Jour 17", "Day 17"),
    ("Jour 18", "Day 18"),
]

def adjust_imports(content, rel_depth):
    prefix = "../" * (rel_depth + 1)
    
    content = re.sub(r"from\s+['\"](\.\./)+layouts/", f"from '{prefix}layouts/", content)
    content = re.sub(r"from\s+['\"](\.\./)+components/", f"from '{prefix}components/", content)
    content = re.sub(r"from\s+['\"](\.\./)+data/", f"from '{prefix}data/", content)
    content = re.sub(r"from\s+['\"](\.\./)+i18n/", f"from '{prefix}i18n/", content)
    return content

def translate_file(src_path, dst_path, rel_depth):
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Adjust relative import paths for Astro components
    content = adjust_imports(content, rel_depth)

    # 2. Apply FR -> EN string replacements
    for fr, en in FR_TO_EN_REPLACEMENTS:
        content = content.replace(fr, en)

    # Ensure target directory exists
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Generated: {dst_path}")

def main():
    os.makedirs(EN_DIR, exist_ok=True)
    
    # Process all files under src/pages except en/ directory itself
    for root, dirs, files in os.walk(PAGES_DIR):
        if "en" in root.split(os.sep):
            continue
            
        for file in files:
            if not file.endswith(".astro"):
                continue
            
            target_file = file
            if file == "a-propos.astro":
                target_file = "about.astro"
            elif file == "mentions-legales.astro":
                target_file = "legal-mentions.astro"

            src_full = os.path.join(root, file)
            rel_dir = os.path.relpath(root, PAGES_DIR)
            rel_path = os.path.join(rel_dir, target_file) if rel_dir != "." else target_file
            dst_full = os.path.join(EN_DIR, rel_path)
            
            rel_depth = len(rel_path.split(os.sep))
            translate_file(src_full, dst_full, rel_depth)

if __name__ == "__main__":
    main()
