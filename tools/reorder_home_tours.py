import re

ORDER_INDICES = [1, 2, 4, 3, 5, 6, 7, 0, 8, 9, 10, 11, 12, 13, 14, 15]

def reorder_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the trips-grid container
    start_marker = '<div id="trips-grid"'
    start_pos = content.find(start_marker)
    if start_pos == -1:
        print(f"trips-grid not found in {filepath}")
        return

    # Find where the trips-grid ends (before activites section)
    end_marker = '<!-- ========================================================================= -->\n  <!-- 6.2. DEDICATED SECTION'
    end_pos = content.find(end_marker)
    if end_pos == -1:
        end_marker = 'id="activites"'
        end_pos = content.find(end_marker)

    chunk = content[start_pos:end_pos]
    grid_open_end = chunk.find('>') + 1
    grid_header = chunk[:grid_open_end]
    last_div_idx = chunk.rfind('</div>')
    grid_footer = chunk[last_div_idx:]
    cards_html = chunk[grid_open_end:last_div_idx].strip()

    # Extract all 16 article cards
    card_list = re.findall(r'(<article class="trip-card.*?)(?=\s*<article class="trip-card|\Z)', cards_html, re.DOTALL)
    print(f"{filepath}: Found {len(card_list)} cards to reorder.")
    if len(card_list) != 16:
        print(f"Error: expected 16 cards, got {len(card_list)}")
        return

    # Reorder according to ORDER_INDICES
    reordered_cards = [card_list[i].strip() for i in ORDER_INDICES]

    new_cards_html = "\n        \n        ".join(reordered_cards)
    new_chunk = f"{grid_header}\n        \n        {new_cards_html}\n      {grid_footer}"

    new_content = content[:start_pos] + new_chunk + content[end_pos:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✓ Successfully reordered tours in {filepath}")

if __name__ == '__main__':
    reorder_file('src/pages/index.astro')
    reorder_file('src/pages/en/index.astro')
