#!/usr/bin/env python3
"""
Unify Tour and Activity Counts across the entire website:
- 18 circuits immersifs (Multi-day tours)
- 5 activités à la journée (Day activities)
Harmonizes headers, footers, i18n dictionaries, tour pages, destinations, about and contact pages.
"""

import os
import re

BASE_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'

def replace_in_file(rel_path, pattern, replacement):
    path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(path):
        print(f"Skipping missing: {rel_path}")
        return 0
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content, count = re.subn(pattern, replacement, content)
    if count > 0:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[{rel_path}] Replaced {count} occurrence(s)")
    return count

def main():
    print("=== 1. Harmonizing Footer & Navigation ===")
    replace_in_file(
        'src/components/Footer.astro',
        r'\{isEn \? "Immersive Tours \(20\)" : "Circuits immersifs \(20\)"\}',
        '{isEn ? "Immersive Tours (18)" : "Circuits immersifs (18)"}'
    )
    replace_in_file(
        'src/components/Footer.astro',
        r'\{isEn \? "View 20 tours" : "Voir les 20 circuits"\}',
        '{isEn ? "View all 18 tours" : "Voir les 18 circuits"}'
    )
    replace_in_file(
        'src/components/Footer.astro',
        r'\{isEn \? "View all activities" : "Voir les 5 activités"\}',
        '{isEn ? "View all 5 activities" : "Voir les 5 activités"}'
    )

    print("\n=== 2. Harmonizing UI i18n Translations ===")
    replace_in_file(
        'src/i18n/ui.ts',
        r"'nav\.tours': 'Tous les 20 séjours'",
        "'nav.tours': 'Tous les 18 circuits'"
    )
    replace_in_file(
        'src/i18n/ui.ts',
        r"'catalog\.title_1': 'Les 20 séjours '",
        "'catalog.title_1': 'Les 18 circuits '"
    )
    replace_in_file(
        'src/i18n/ui.ts',
        r"'nav\.tours': 'All 20 Expeditions'",
        "'nav.tours': 'All 18 Expeditions'"
    )
    replace_in_file(
        'src/i18n/ui.ts',
        r"'catalog\.title_1': '20 Immersive '",
        "'catalog.title_1': '18 Immersive '"
    )

    print("\n=== 3. Harmonizing Layout Meta Description ===")
    replace_in_file(
        'src/layouts/Layout.astro',
        r'20 séjours d\'exception',
        "18 circuits d'exception & 5 activités"
    )
    replace_in_file(
        'src/layouts/Layout.astro',
        r'20 bespoke expeditions',
        "18 bespoke expeditions & 5 day activities"
    )

    print("\n=== 4. Harmonizing 404 Page ===")
    replace_in_file(
        'src/pages/404.astro',
        r'Découvrir les 20 séjours',
        'Découvrir les 18 circuits'
    )
    replace_in_file(
        'src/pages/404.astro',
        r'Discover our 20 tours',
        'Discover our 18 tours'
    )

    print("\n=== 5. Harmonizing About Pages (FR & EN) ===")
    replace_in_file(
        'src/pages/a-propos.astro',
        r'15 circuits',
        '18 circuits'
    )
    replace_in_file(
        'src/pages/a-propos.astro',
        r"Explorer l'ensemble de nos 21 séjours & départs garantis",
        "Explorer l'ensemble de nos 18 circuits & départs garantis"
    )
    replace_in_file(
        'src/pages/en/about.astro',
        r'15 circuits',
        '18 tours'
    )
    replace_in_file(
        'src/pages/en/about.astro',
        r'Explore Tours & expeditions & Guaranteed Departures',
        'Explore all 18 tours & guaranteed departures'
    )

    print("\n=== 6. Harmonizing Homepages Filter Badges ===")
    replace_in_file(
        'src/pages/index.astro',
        r'Safaris & Grands Félins \(17 séjours\)',
        'Safaris & Grands Félins (18 circuits)'
    )
    replace_in_file(
        'src/pages/en/index.astro',
        r'Safaris & Big Cats \(17 tours\)',
        'Safaris & Big Cats (18 tours)'
    )

    print("\n=== 7. Harmonizing Tour Pages CTA Badges ===")
    tours_dir = os.path.join(BASE_DIR, 'src/pages/tours')
    for f in os.listdir(tours_dir):
        if f.endswith('.astro'):
            rel = os.path.join('src/pages/tours', f)
            replace_in_file(rel, r'Découvrir nos 20 circuits au Népal', 'Découvrir nos 18 circuits au Népal')

    print("\n=== 8. Harmonizing Destination Pages ===")
    dest_dir = os.path.join(BASE_DIR, 'src/pages/destinations')
    for f in os.listdir(dest_dir):
        if f.endswith('.astro'):
            rel = os.path.join('src/pages/destinations', f)
            replace_in_file(rel, r'Découvrir nos 20 circuits →', 'Découvrir nos 18 circuits →')

    print("\n=== 9. Harmonizing Blog Index ===")
    replace_in_file(
        'src/pages/blog/index.astro',
        r'Découvrir nos 20 circuits →',
        'Découvrir nos 18 circuits →'
    )

    print("\n=== 10. Harmonizing English Tour Pages (Walking Safaris) ===")
    replace_in_file(
        'src/pages/en/tours/bardia-walking-safari.astro',
        r'All 17 tours',
        'All 18 tours'
    )
    replace_in_file(
        'src/pages/en/tours/bardia-walking-safari.astro',
        r'Our 17 Tours',
        'Our 18 Tours'
    )
    replace_in_file(
        'src/pages/en/tours/bardia-walking-safari.astro',
        r'Explore all 17 tours & departures →',
        'Explore all 18 tours & departures →'
    )
    replace_in_file(
        'src/pages/en/tours/chitwan-walking-safari.astro',
        r'All 17 tours',
        'All 18 tours'
    )

    print("\n=== Done! All tour references harmonized to 18 circuits and 5 activities. ===")

if __name__ == '__main__':
    main()
