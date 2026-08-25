import os
import re

src_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src'

def clean_links(content):
    # Convert ../../en/ or ../en/ to /en/
    content = re.sub(r'href=[\'\"](?:\.\./)+en/', 'href="/en/', content)
    
    # Convert ../index.html or ../../index.html to /index.html
    content = re.sub(r'href=[\'\"](?:\.\./)+index\.html', 'href="/index.html', content)
    
    # Convert ../destinations/ to /destinations/
    content = re.sub(r'href=[\'\"](?:\.\./)+destinations/', 'href="/destinations/', content)
    
    # Convert ../tours/ to /tours/
    content = re.sub(r'href=[\'\"](?:\.\./)+tours/', 'href="/tours/', content)

    # Convert ../a-propos.html to /a-propos.html
    content = re.sub(r'href=[\'\"](?:\.\./)+a-propos\.html', 'href="/a-propos.html', content)
    
    # Convert ../contact.html to /contact.html
    content = re.sub(r'href=[\'\"](?:\.\./)+contact\.html', 'href="/contact.html', content)

    # Convert ../destinations.html to /destinations.html
    content = re.sub(r'href=[\'\"](?:\.\./)+destinations\.html', 'href="/destinations.html', content)

    # In destination hub pages (destinations/index.astro & en/destinations/index.astro):
    # replace href="bardia.html" with href="/destinations/bardia.html" or href="/en/destinations/bardia.html"
    return content

count = 0
for root, dirs, files in os.walk(src_dir):
    for f in files:
        if f.endswith('.astro') or f.endswith('.vue') or f.endswith('.jsx') or f.endswith('.tsx'):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8') as file:
                old_c = file.read()
            new_c = clean_links(old_c)
            
            # Specific fixes for hub pages
            if 'destinations/index.astro' in fpath:
                is_en = '/en/' in fpath
                prefix = '/en/destinations/' if is_en else '/destinations/'
                for d in ['bardia', 'chitwan', 'suklaphanta', 'annapurna', 'katmandou']:
                    new_c = re.sub(rf'href=[\'\"]{d}\.html[\'\"]', f'href="{prefix}{d}.html"', new_c)
                    new_c = re.sub(rf'href=[\'\"]\./{d}\.html[\'\"]', f'href="{prefix}{d}.html"', new_c)

            if old_c != new_c:
                with open(fpath, 'w', encoding='utf-8') as file:
                    file.write(new_c)
                count += 1

print(f"Fixed links across {count} Astro source files!")
