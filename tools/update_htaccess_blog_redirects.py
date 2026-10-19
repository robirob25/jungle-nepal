import os
import sys

BASE_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'
HTACCESS_PATH = os.path.join(BASE_DIR, 'public/.htaccess')

sys.path.insert(0, '.')
from tools.fix_english_blog_slugs import SLUG_MAP

with open(HTACCESS_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Build the 301 redirect rules
rules = ["    # English Blog Posts SEO Permanent 301 Redirects (French slugs -> English slugs)"]
for fr, en in sorted(SLUG_MAP.items()):
    rules.append(f"    RewriteRule ^en/blog/{fr}/?$ https://junglenepal.com/en/blog/{en} [R=301,L,NE]")

rules_block = "\n".join(rules) + "\n"

target_anchor = "    RewriteRule ^en/tours/tiji-mustang/?$ https://junglenepal.com/en/tours/tiji-festival-upper-mustang-trek [R=301,L,NE]\n"

if target_anchor in content:
    content = content.replace(target_anchor, target_anchor + "\n" + rules_block)
    with open(HTACCESS_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added 60 blog 301 redirects to public/.htaccess!")
else:
    print("Could not find target anchor in .htaccess!")
