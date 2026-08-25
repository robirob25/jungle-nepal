import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Find the tours grid container
# Starts around `<div id="trips-grid"` and ends before `</div>` and pagination/sur-mesure CTA
grid_start_idx = c.find('id="trips-grid"')
if grid_start_idx == -1:
    grid_start_idx = c.find('class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"')

# Extract all `<article ... class="trip-card ..."> ... </article>` blocks
article_regex = re.compile(r'(<article\s+class="[^"]*trip-card[^"]*"[\s\S]*?</article>)', re.MULTILINE)

# Find all matches in the trips grid section
grid_section = c[grid_start_idx:c.find('<!-- ========================================================================= -->\n  <!-- 7.', grid_start_idx)]
articles = article_regex.findall(grid_section)

print(f"Found {len(articles)} tour articles in index.astro")

# Map articles by their tour link
tour_articles = {}
for art in articles:
    match = re.search(r'href="/tours/([^"\.]+)\.html"', art)
    if match:
        slug = match.group(1)
        tour_articles[slug] = art

# Reorder articles according to user request:
# 1. jungle-extreme
# 2. nepal-sauvage
# 3. chitwan-bardia-complete
# Followed by all others

priority_slugs = ['jungle-extreme', 'nepal-sauvage', 'chitwan-bardia-complete']
ordered_articles = []

for slug in priority_slugs:
    if slug in tour_articles:
        ordered_articles.append(tour_articles[slug])

for slug, art in tour_articles.items():
    if slug not in priority_slugs:
        ordered_articles.append(art)

# Replace the original articles sequence with the new ordered sequence
new_grid_content = "\n\n        ".join(ordered_articles)

# Replace in index.astro
orig_articles_block = "\n\n        ".join(articles)
# Or replace the section between grid opening and closing
start_tag_idx = grid_section.find('>') + 1
end_tag_idx = grid_section.rfind('</div>')

new_grid_section = grid_section[:start_tag_idx] + "\n        " + new_grid_content + "\n      " + grid_section[end_tag_idx:]
c = c[:grid_start_idx] + new_grid_section + c[grid_start_idx + len(grid_section):]

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Successfully placed the 3 requested tours at the top of the homepage grid!")
