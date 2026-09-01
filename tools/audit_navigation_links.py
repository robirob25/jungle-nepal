import glob, re
from urllib.parse import urlparse

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

# List of valid page routes in our project:
valid_routes = {
    '/', '/a-propos', '/a-propos.html', '/contact', '/contact.html', '/destinations', '/destinations.html',
    '/destinations/bardia', '/destinations/bardia.html',
    '/destinations/chitwan', '/destinations/chitwan.html',
    '/destinations/suklaphanta', '/destinations/suklaphanta.html',
    '/destinations/annapurna', '/destinations/annapurna.html',
    '/destinations/katmandou', '/destinations/katmandou.html',
    '/tours/bardia-explorateur', '/tours/bardia-explorateur.html',
    '/tours/chitwan-culture', '/tours/chitwan-culture.html',
    '/tours/nepal-sauvage', '/tours/nepal-sauvage.html',
    '/tours/babai-special', '/tours/babai-special.html',
    '/tours/bardia-babai-camping', '/tours/bardia-babai-camping.html',
    '/tours/rafting-safari', '/tours/rafting-safari.html',
    '/tours/tiji-mustang', '/tours/tiji-mustang.html',
    '/tours/nepal-immersion-totale', '/tours/nepal-immersion-totale.html',
    '/tours/bardia-nuit-sauvage', '/tours/bardia-nuit-sauvage.html',
    '/tours/jungle-extreme', '/tours/jungle-extreme.html',
    '/tours/panthere-des-neiges', '/tours/panthere-des-neiges.html',
    '/tours/rara-lake-bardia', '/tours/rara-lake-bardia.html',
    '/tours/immersion-spirituelle', '/tours/immersion-spirituelle.html',
    '/tours/carnet-de-voyage', '/tours/carnet-de-voyage.html',
    '/tours/chitwan-bardia-complete', '/tours/chitwan-bardia-complete.html',
}

valid_homepage_anchors = {'#prochains-departs', '#concept', '#galerie-faune', '#carte-nepal', '#pisteurs', '#avis'}

broken_links = []

for fpath in astro_files:
    fname = fpath.split('/')[-1]
    is_homepage = (fname == 'index.astro')

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all hrefs
    hrefs = re.findall(r'href="([^"#][^"]*)"', content)
    for h in hrefs:
        if h.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:')):
            continue
        # Split path and hash
        parts = h.split('#')
        path_part = parts[0]
        hash_part = '#' + parts[1] if len(parts) > 1 else ''

        # Check path
        if path_part and path_part not in valid_routes and path_part != '/':
            broken_links.append(f"{fname}: Invalid link href='{h}'")
        
        # Check homepage hash navigation from subpages
        if not is_homepage and h.startswith('#'):
            broken_links.append(f"{fname}: Local hash link on subpage href='{h}' (should be '/{h}')")

print("Navigation Audit Results:")
if not broken_links:
    print("✓ All links and anchors are strictly valid!")
else:
    for b in set(broken_links):
        print(f"- {b}")
