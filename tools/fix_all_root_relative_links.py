import os
import re

base_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'

def fix_links_in_content(content, is_english=False):
    # Fix Destinations links
    # destinations/bardia.html or ../destinations/bardia.html -> /destinations/bardia.html (or /en/destinations/bardia.html)
    if is_english:
        content = re.sub(r'href=[\'\"](?:\.\./)*destinations/([a-zA-Z0-9_\-]+)\.html[\'\"]', r'href="/en/destinations/\1.html"', content)
        content = re.sub(r'href=[\'\"](?:\.\./)*destinations/?[\'\"]', r'href="/en/destinations.html"', content)
        content = re.sub(r'href=[\'\"](?:\.\./)*destinations/index\.html[\'\"]', r'href="/en/destinations.html"', content)
        content = re.sub(r'href=[\'\"](?:\.\./)*tours/([a-zA-Z0-9_\-]+)\.html[\'\"]', r'href="/en/tours/\1.html"', content)
        content = re.sub(r'href=[\'\"](?:\.\./)*a-propos\.html[\'\"]', r'href="/en/a-propos.html"', content)
        content = re.sub(r'href=[\'\"](?:\.\./)*contact\.html[\'\"]', r'href="/en/contact.html"', content)
        content = re.sub(r'href=[\'\"](?:\.\./)*index\.html[\'\"]', r'href="/en/index.html"', content)
    else:
        content = re.sub(r'href=[\'\"](?:\.\./)*destinations/([a-zA-Z0-9_\-]+)\.html[\'\"]', r'href="/destinations/\1.html"', content)
        content = re.sub(r'href=[\'\"](?:\.\./)*destinations/?[\'\"]', r'href="/destinations.html"', content)
        content = re.sub(r'href=[\'\"](?:\.\./)*destinations/index\.html[\'\"]', r'href="/destinations.html"', content)
        content = re.sub(r'href=[\'\"](?:\.\./)*tours/([a-zA-Z0-9_\-]+)\.html[\'\"]', r'href="/tours/\1.html"', content)
        content = re.sub(r'href=[\'\"](?:\.\./)*a-propos\.html[\'\"]', r'href="/a-propos.html"', content)
        content = re.sub(r'href=[\'\"](?:\.\./)*contact\.html[\'\"]', r'href="/contact.html"', content)
        content = re.sub(r'href=[\'\"](?:\.\./)*index\.html[\'\"]', r'href="/index.html"', content)

    # Clean double prefixes if any (e.g. /en/en/ or /destinations/destinations/)
    content = content.replace('/en/en/', '/en/')
    content = content.replace('/destinations/destinations/', '/destinations/')
    content = content.replace('/tours/tours/', '/tours/')
    return content

updated = 0
for root, dirs, files in os.walk(base_dir):
    if any(p in root for p in ['node_modules', '.git']):
        continue
    for f in files:
        if f.endswith('.astro') or f.endswith('.html'):
            fpath = os.path.join(root, f)
            rel_path = os.path.relpath(fpath, base_dir)
            is_en = '/en/' in fpath or rel_path.startswith('en') or 'en_' in f
            
            with open(fpath, 'r', encoding='utf-8') as file:
                old_c = file.read()
            
            new_c = fix_links_in_content(old_c, is_english=is_en)
            if old_c != new_c:
                with open(fpath, 'w', encoding='utf-8') as file:
                    file.write(new_c)
                updated += 1

print(f"Fixed root-relative links in {updated} files!")
