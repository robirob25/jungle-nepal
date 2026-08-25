import os
import re

base_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'
src_pages = os.path.join(base_dir, 'src/pages')

def extract_head_and_body(html_content):
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.DOTALL | re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else 'Jungle Nepal Adventure'
    
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL | re.IGNORECASE)
    if body_match:
        body_content = body_match.group(1)
    else:
        body_content = html_content

    # Clean assets path to absolute /assets/
    body_content = re.sub(r'(\.\./)+assets/', '/assets/', body_content)
    body_content = re.sub(r'(?<![/\w])assets/', '/assets/', body_content)

    return title, body_content

# Clean out old dynamic [slug].astro templates so individual exact pages take precedence
for old_slug_file in [
    os.path.join(src_pages, 'tours/[slug].astro'),
    os.path.join(src_pages, 'en/tours/[slug].astro'),
    os.path.join(src_pages, 'destinations/[slug].astro'),
    os.path.join(src_pages, 'en/destinations/[slug].astro')
]:
    if os.path.exists(old_slug_file):
        os.remove(old_slug_file)

html_files = []
for root, dirs, files in os.walk(base_dir):
    # Only skip src, dist, node_modules inside jungle-nepal
    rel_root = os.path.relpath(root, base_dir)
    if rel_root.startswith('src') or rel_root.startswith('dist') or rel_root.startswith('node_modules') or rel_root.startswith('docs'):
        continue
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f"Found {len(html_files)} original HTML files to convert to exact Astro pages.")

for fpath in html_files:
    rel_path = os.path.relpath(fpath, base_dir)
    astro_rel = rel_path[:-5] + '.astro'
    target_astro_file = os.path.join(src_pages, astro_rel)
    os.makedirs(os.path.dirname(target_astro_file), exist_ok=True)

    with open(fpath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    is_en = rel_path.startswith('en/')
    lang = 'en' if is_en else 'fr'

    depth = astro_rel.count('/')
    layout_import = '../' * (depth + 1) + 'layouts/Layout.astro'

    title, body = extract_head_and_body(html_content)

    body = body.replace('<script>', '<script is:inline>').replace('<script src=', '<script is:inline src=')
    body = body.replace('is:inline is:inline', 'is:inline')

    astro_page_content = f"""---
import Layout from '{layout_import}';
---

<Layout title="{title}" lang="{lang}">
{body}
</Layout>
"""

    with open(target_astro_file, 'w', encoding='utf-8') as f:
        f.write(astro_page_content)

print(f"Successfully migrated all {len(html_files)} pages to exact 1:1 Astro pages!")
