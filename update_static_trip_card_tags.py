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

def update_cards(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    for slug, tags in tour_tags.items():
        # Match article containing href="...slug.html..."
        # Replace its data-category="..." with data-category="{tags}"
        pattern = rf'(<article\s+class=[\'\"][^\'\"]*trip-card[^\'\"]*[\'\"][^>]*?data-category=)[\'\"][^\'\"]*[\'\"]([^>]*?href=[\'\"][^\'\"]*{slug}\.html[\'\"])'
        
        # In case href is later in the article:
        # Match <article class="trip-card..." ...> ... href="...slug..." </article>
        article_pattern = rf'(<article\s+class=[\'\"][^\'\"]*trip-card[^\'\"]*[\'\"][^>]*?)data-category=[\'\"][^\'\"]*[\'\"](.*?(?:tours/)?{slug}\.html.*?)(?=</article>)'
        content = re.sub(article_pattern, rf'\1data-category="{tags}"\2', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_cards('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro')
update_cards('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/index.astro')

print("Updated static trip-card data-category attributes in index.astro and en/index.astro!")
