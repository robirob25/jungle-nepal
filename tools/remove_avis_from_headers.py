import os
import re

def remove_avis_from_header(html):
    # Find <nav ...> ... </nav> inside <header ...> ... </header>
    def clean_nav(match):
        nav_content = match.group(0)
        # Remove any link inside nav that contains Avis
        # Pattern 1: <a ...>Avis ★ 5.0</a> or <a ...>★ Avis 5.0</a> or <a ...>Avis</a> or <a ...>Reviews</a>
        nav_content = re.sub(r'<a\s+href=[\"\'][^\"\']*[\"\'][^>]*>\s*(?:<span[^>]*>.*?</span>\s*)?(?:Avis(?:\s*★\s*5\.0)?|Reviews(?:\s*★\s*5\.0)?|★\s*Avis\s*5\.0)\s*</a>\s*', '', nav_content)
        return nav_content

    # Apply only inside <header>...</header>
    def clean_header(match):
        header_block = match.group(0)
        return re.sub(r'<nav[^>]*>.*?</nav>', clean_nav, header_block, flags=re.DOTALL)

    return re.sub(r'<header[^>]*>.*?</header>', clean_header, html, flags=re.DOTALL)

# 1. Update root pages
root_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'
for root, dirs, files in os.walk(root_dir):
    for f in files:
        if not f.endswith('.html'):
            continue
        fpath = os.path.join(root, f)
        with open(fpath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        new_content = remove_avis_from_header(content)
        if new_content != content:
            with open(fpath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Removed Avis from header in: {os.path.relpath(fpath, root_dir)}")

print("Completed removing Avis from all headers across the site!")
