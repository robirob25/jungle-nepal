import os, json

# Mapping of all 100% historical URLs from old WordPress junglenepal.com to the new Astro site:
redirect_map = {
    # Core pages
    "/agence-de-safaris-au-nepal/": "/a-propos/",
    "/agence-de-safaris-au-nepal": "/a-propos/",
    "/contact/": "/contact/",
    "/contact": "/contact/",
    "/nos-destinations/": "/destinations/",
    "/nos-destinations": "/destinations/",
    "/nos-aventures/": "/tours/carnet-de-voyage/",
    "/nos-aventures": "/tours/carnet-de-voyage/",
    "/nos-offres/": "/#circuits",
    "/nos-offres": "/#circuits",
    "/nos-recommandations/": "/#faq",
    "/nos-recommandations": "/#faq",
    "/nos-tours-a-venir/": "/#circuits",
    "/nos-tours-a-venir": "/#circuits",
    "/mentions-legales/": "/a-propos/",
    "/mentions-legales": "/a-propos/",

    # Destination pages
    "/parc-national-de-bardia/": "/destinations/bardia/",
    "/parc-national-de-bardia": "/destinations/bardia/",
    "/parc-national-de-chitwan/": "/destinations/chitwan/",
    "/parc-national-de-chitwan": "/destinations/chitwan/",
    "/parc-national-de-suklaphanta/": "/destinations/suklaphanta/",
    "/parc-national-de-suklaphanta": "/destinations/suklaphanta/",
    "/katmandou/": "/destinations/katmandou/",
    "/katmandou": "/destinations/katmandou/",
    "/annapurna-region/": "/destinations/annapurna/",
    "/annapurna-region": "/destinations/annapurna/",

    # Tour pages (WordPress slugs -> new clean Astro slugs)
    "/tour/nepal-sauvage-de-la-jungle-aux-montagnes-sacrees/": "/tours/nepal-sauvage/",
    "/tour/nepal-sauvage-de-la-jungle-aux-montagnes-sacrees": "/tours/nepal-sauvage/",
    "/tour/bardia-explorateur-5-jours-dans-la-jungle/": "/tours/bardia-explorateur/",
    "/tour/bardia-explorateur-5-jours-dans-la-jungle": "/tours/bardia-explorateur/",
    "/tour/jungle-extreme-special-faune-sauvage/": "/tours/jungle-extreme/",
    "/tour/jungle-extreme-special-faune-sauvage": "/tours/jungle-extreme/",
    "/tour/bardia-aventure-immersive-en-jungle-et-camping-sauvage/": "/tours/bardia-nuit-sauvage/",
    "/tour/bardia-aventure-immersive-en-jungle-et-camping-sauvage": "/tours/bardia-nuit-sauvage/",
    "/tour/bardia-babai-vallee-camping-sauvage-au-coeur-dune-nature-vierge-et-isolee/": "/tours/bardia-babai-camping/",
    "/tour/bardia-babai-vallee-camping-sauvage-au-coeur-dune-nature-vierge-et-isolee": "/tours/bardia-babai-camping/",
    "/tour/chitwan-bardia-laventure-jungle-complete/": "/tours/chitwan-bardia-complete/",
    "/tour/chitwan-bardia-laventure-jungle-complete": "/tours/chitwan-bardia-complete/",
    "/tour/nepal-immersion-totale-culture-vie-sauvage-et-aventure/": "/tours/nepal-immersion-totale/",
    "/tour/nepal-immersion-totale-culture-vie-sauvage-et-aventure": "/tours/nepal-immersion-totale/",
    "/tour/deep-into-the-wild-babai-special-experience-5-jours/": "/tours/babai-special/",
    "/tour/deep-into-the-wild-babai-special-experience-5-jours": "/tours/babai-special/",
    "/tour/chitwan-culture-et-jungle-sauvage/": "/tours/chitwan-culture/",
    "/tour/chitwan-culture-et-jungle-sauvage": "/tours/chitwan-culture/",
    "/tour/immersion-spirituelle-en-himalaya/": "/tours/immersion-spirituelle/",
    "/tour/immersion-spirituelle-en-himalaya": "/tours/immersion-spirituelle/",
    "/tour/rivieres-sauvages-et-patrimoines-caches-expedition-et-rafting/": "/tours/rafting-safari/",
    "/tour/rivieres-sauvages-et-patrimoines-caches-expedition-et-rafting": "/tours/rafting-safari/",
    "/tour/rara-lake-bardia-expedition-lultime-aventure-hors-sentiers-battus/": "/tours/rara-lake-bardia/",
    "/tour/rara-lake-bardia-expedition-lultime-aventure-hors-sentiers-battus": "/tours/rara-lake-bardia/",
    "/tour/tiji-festival-tour-upper-mustang/": "/tours/tiji-mustang/",
    "/tour/tiji-festival-tour-upper-mustang": "/tours/tiji-mustang/",
    "/tour/nepal-special-carnet-de-voyage/": "/tours/carnet-de-voyage/",
    "/tour/nepal-special-carnet-de-voyage": "/tours/carnet-de-voyage/",

    # Blog posts & SEO guides (retaining search traffic by directing to relevant authoritative hubs)
    "/safari-tigre-nepal/": "/destinations/bardia/",
    "/safari-tigre-nepal": "/destinations/bardia/",
    "/safari-dans-le-parc-national-de-bardia-au-nepal/": "/destinations/bardia/",
    "/safari-dans-le-parc-national-de-bardia-au-nepal": "/destinations/bardia/",
    "/bardia-ou-chitwan-safari-nepal/": "/destinations/",
    "/bardia-ou-chitwan-safari-nepal": "/destinations/",
    "/babai-valley-la-vallee-oubliee-du-nepal-sauvage/": "/tours/bardia-babai-camping/",
    "/babai-valley-la-vallee-oubliee-du-nepal-sauvage": "/tours/bardia-babai-camping/",
    "/culture-tharu-a-bardia-traditions-villages-et-vie-locale/": "/tours/chitwan-culture/",
    "/culture-tharu-a-bardia-traditions-villages-et-vie-locale": "/tours/chitwan-culture/",
    "/la-faune-du-nepal-a-la-rencontre-du-big-5-de-bardia/": "/#galerie-faune",
    "/la-faune-du-nepal-a-la-rencontre-du-big-5-de-bardia": "/#galerie-faune",
    "/safari-a-pied-au-nepal-est-ce-dangereux/": "/a-propos/",
    "/safari-a-pied-au-nepal-est-ce-dangereux": "/a-propos/",
    "/safari-au-nepal-vivre-la-jungle-autrement-loin-des-circuits-touristiques/": "/#histoire",
    "/safari-au-nepal-vivre-la-jungle-autrement-loin-des-circuits-touristiques": "/#histoire",
    "/camping-jungle-nepal/": "/tours/bardia-nuit-sauvage/",
    "/camping-jungle-nepal": "/tours/bardia-nuit-sauvage/",
    "/quand-partir-au-nepal/": "/#faq",
    "/quand-partir-au-nepal": "/#faq",
    "/voyage-nature-au-nepal-safari-et-aventures-hors-sentiers-battus/": "/tours/carnet-de-voyage/",
    "/voyage-nature-au-nepal-safari-et-aventures-hors-sentiers-battus": "/tours/carnet-de-voyage/"
}

# 1. Generate Nginx 301 redirection blocks
nginx_redirects = []
for old_path, new_path in redirect_map.items():
    if old_path.endswith('/'):
        clean = old_path.rstrip('/')
        nginx_redirects.append(f"    rewrite ^{clean}/?$ {new_path} permanent;")

nginx_redirect_str = "\n".join(sorted(list(set(nginx_redirects))))

nginx_conf = f"""server {{
    listen 80;
    listen [::]:80;
    server_name _;

    root /usr/share/nginx/html;
    index index.html index.htm;

    # Gzip Compression
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_proxied expired no-cache no-store private auth;
    gzip_types text/plain text/css text/xml text/javascript application/x-javascript application/xml application/javascript application/json image/svg+xml;
    gzip_disable "MSIE [1-6]\.";

    # Security Headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    # ==========================================
    # SEO 301 PERMANENT REDIRECTS (ZERO LOSS MIGRATION)
    # ==========================================
{nginx_redirect_str}

    # Redirect WordPress wp-content image links to root assets if needed
    rewrite ^/wp-content/uploads/(.*)$ /assets/$1 permanent;

    # Static Assets Caching (1 Year)
    location ~* \.(?:ico|css|js|gif|jpe?g|png|webp|svg|woff2?|ttf|eot)$ {{
        expires 1y;
        add_header Cache-Control "public, max-age=31536000, immutable";
        access_log off;
    }}

    # Clean URL handling (.html, directory, or fallback)
    location / {{
        try_files $uri $uri/ $uri.html /index.html =404;
    }}

    # Custom 404 Page
    error_page 404 /index.html;
}}
"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/nginx.conf', 'w', encoding='utf-8') as f:
    f.write(nginx_conf)

# 2. Generate Netlify / Cloudflare _redirects file for static hostings
redirects_content = []
for old_path, new_path in redirect_map.items():
    redirects_content.append(f"{old_path} {new_path} 301")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/_redirects', 'w', encoding='utf-8') as f:
    f.write("\n".join(redirects_content) + "\n")

# 3. Generate static HTML meta-refresh fallback pages inside dist for maximum compatibility
dist_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'
for old_path, new_path in redirect_map.items():
    clean_p = old_path.strip('/')
    target_dir = os.path.join(dist_dir, clean_p)
    os.makedirs(target_dir, exist_ok=True)
    meta_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url={new_path}">
  <link rel="canonical" href="https://junglenepal.com{new_path}">
  <title>Redirection...</title>
</head>
<body style="background:#020617;color:white;font-family:sans-serif;text-align:center;padding:50px;">
  <p>Redirection vers <a href="{new_path}" style="color:#10b981;">{new_path}</a>...</p>
  <script>window.location.href = "{new_path}";</script>
</body>
</html>"""
    with open(os.path.join(target_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(meta_html)

print("Generated comprehensive 301 SEO redirects across Nginx, _redirects, and static HTML fallbacks!")
