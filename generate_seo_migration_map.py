import json, glob, re, os

# Map current built pages in dist to WordPress URL paths
dist_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

pages = []
for root, dirs, files in os.walk(dist_dir):
    for f in files:
        if f.endswith('.html') and not f.startswith('.'):
            full_p = os.path.join(root, f)
            rel_p = os.path.relpath(full_p, dist_dir)
            pages.append(rel_p)

print(f"Total HTML endpoints generated in dist: {len(pages)}")

# Generate .htaccess with 301 redirects for Apache / LiteSpeed / Coolify / Nginx
htaccess_content = """# =========================================================================
# JUNGLE NEPAL ADVENTURE - 301 REDIRECTS & SEO CONSERVATION ENGINE
# =========================================================================
RewriteEngine On
RewriteBase /

# 1. Force HTTPS and Non-WWW (or WWW depending on preferred domain)
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} ^www\.junglenepal\.com [NC]
RewriteRule ^(.*)$ https://junglenepal.com/$1 [L,R=301]

# 2. Universal Trailing Slash & Clean URL Mapping
# Redirect /page.html to /page
RewriteCond %{THE_REQUEST} /([^.]+)\.html [NC]
RewriteRule ^ /%1 [NC,L,R=301]

# Serve existing file or directory directly
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME}.html -f
RewriteRule ^(.*)$ $1.html [L]

# 3. 301 Redirects from Old WordPress Slugs to New Clean Slugs
Redirect 301 /safaris/ /tours/jungle-extreme
Redirect 301 /parc-national-de-bardia/ /destinations/bardia
Redirect 301 /parc-national-de-chitwan/ /destinations/chitwan
Redirect 301 /parc-national-de-suklaphanta/ /destinations/suklaphanta
Redirect 301 /annapurnas-pokhara/ /destinations/annapurna
Redirect 301 /katmandou-vallee-des-rois/ /destinations/katmandou
Redirect 301 /contact-us/ /contact
Redirect 301 /about-us/ /a-propos
Redirect 301 /about/ /a-propos
Redirect 301 /notre-histoire/ /a-propos
"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/.htaccess', 'w', encoding='utf-8') as f:
    f.write(htaccess_content)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist/.htaccess', 'w', encoding='utf-8') as f:
    f.write(htaccess_content)

print("✓ Generated production-ready .htaccess with 301 redirects and clean URLs!")
