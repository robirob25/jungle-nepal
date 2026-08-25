import re

tour_tags = {
    "bardia-explorateur": "safari",
    "chitwan-culture": "chitwan",
    "rafting-safari": "rafting bivouac safari grand-tour",
    "bardia-nuit-sauvage": "safari bivouac",
    "rara-lake-bardia": "mustang-himalaya safari grand-tour",
    "bardia-babai-camping": "safari bivouac",
    "nepal-immersion-totale": "chitwan safari rafting grand-tour",
    "babai-special": "safari bivouac",
    "chitwan-bardia-complete": "chitwan safari bivouac rafting grand-tour",
    "tiji-mustang": "mustang-himalaya grand-tour",
    "carnet-de-voyage": "mustang-himalaya grand-tour",
    "jungle-extreme": "safari grand-tour",
    "nepal-sauvage": "safari mustang-himalaya grand-tour",
    "immersion-spirituelle": "mustang-himalaya grand-tour"
}

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by <article class="trip-card
    parts = content.split('<article class="trip-card')
    fixed_parts = [parts[0]]

    for part in parts[1:]:
        # Identify which tour this part belongs to
        tour_slug = None
        for slug in tour_tags.keys():
            if f'{slug}.html' in part or f'/tours/{slug}' in part:
                tour_slug = slug
                break
        
        if tour_slug:
            tags = tour_tags[tour_slug]
            # Replace existing data-category="..." in the opening of this article
            # The opening tag is before the first '>'
            header, rest = part.split('>', 1)
            header = re.sub(r'data-category="[^"]*"', f'data-category="{tags}"', header)
            fixed_parts.append(header + '>' + rest)
        else:
            fixed_parts.append(part)

    new_content = '<article class="trip-card'.join(fixed_parts)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Fixed all 14 trip cards in {filepath}!")

fix_file('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro')
fix_file('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro')
