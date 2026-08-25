import json, re, glob, os

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/data/tours.json', 'r', encoding='utf-8') as f:
    tours = json.load(f)

tour_map = {t['slug']: t for t in tours}

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

updated_files = 0
total_cards_updated = [0]

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    
    def fix_card(match):
        card_content = match.group(0)
        
        # Find tour slug
        slug_match = re.search(r'href=[\'"]/tours/([^.]+)\.html[\'"]', card_content)
        if not slug_match:
            return card_content
        
        slug = slug_match.group(1)
        if slug not in tour_map:
            return card_content
        
        correct_img = tour_map[slug]['image']
        
        # Replace the img src inside this card
        card_fixed = re.sub(
            r'(<img\s+[^>]*?src=[\'"])[^\'"]+([\'"][^>]*>)',
            rf'\g<1>{correct_img}\g<2>',
            card_content,
            count=1
        )
        if card_fixed != card_content:
            total_cards_updated[0] += 1
        return card_fixed

    # Match each <article class="trip-card ..."> ... </article>
    c = re.sub(r'<article class=[\'"]trip-card[^>]*>.*?</article>', fix_card, c, flags=re.DOTALL)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated_files += 1

print(f"Synchronized {total_cards_updated[0]} trip cards across {updated_files} astro files with the exact official featured images!")
