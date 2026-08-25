import os, re, glob
from urllib.parse import urlparse

DIST_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

def audit():
    print("=" * 60)
    print("🚀 AUDIT COMPLET DU SITE (DIST & SOURCE)")
    print("=" * 60)

    html_files = glob.glob(f"{DIST_DIR}/**/*.html", recursive=True)
    print(f"📄 Total pages HTML dans dist/ : {len(html_files)}")

    broken_links = []
    broken_images = []
    total_links_checked = 0
    total_images_checked = 0

    for html_path in html_files:
        rel_page = os.path.relpath(html_path, DIST_DIR)
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Check Links
        links = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\']', content, re.IGNORECASE)
        for link in links:
            link_clean = link.split('#')[0].split('?')[0].strip()
            if not link_clean or link_clean.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#')):
                continue
            total_links_checked += 1

            if link_clean.startswith('/'):
                target_path = os.path.join(DIST_DIR, link_clean.lstrip('/'))
            else:
                target_path = os.path.normpath(os.path.join(os.path.dirname(html_path), link_clean))

            # Check if file or directory/index.html exists
            if not (os.path.isfile(target_path) or os.path.isfile(os.path.join(target_path, 'index.html')) or (not link_clean.endswith('.html') and os.path.isfile(target_path + '.html'))):
                broken_links.append((rel_page, link, target_path))

        # 2. Check Images
        imgs = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\']', content, re.IGNORECASE)
        for img in imgs:
            img_clean = img.split('?')[0].strip()
            if not img_clean or img_clean.startswith(('http://', 'https://', 'data:')):
                continue
            total_images_checked += 1

            if img_clean.startswith('/'):
                target_img = os.path.join(DIST_DIR, img_clean.lstrip('/'))
            else:
                target_img = os.path.normpath(os.path.join(os.path.dirname(html_path), img_clean))

            if not os.path.isfile(target_img):
                broken_images.append((rel_page, img, target_img))

    print(f"\n🔗 Liens internes vérifiés : {total_links_checked}")
    print(f"🖼️ Images locales vérifiées : {total_images_checked}")

    if broken_links:
        print(f"\n❌ {len(broken_links)} LIEN(S) MORT(S) DÉTECTÉ(S) :")
        for page, link, target in broken_links:
            print(f"  • Dans [{page}] -> href='{link}' (Cible introuvable: {target})")
    else:
        print("\n✅ AUCUN LIEN MORT ! Tous les liens internes pointent vers des pages existantes.")

    if broken_images:
        print(f"\n❌ {len(broken_images)} IMAGE(S) MANQUANTE(S) :")
        for page, img, target in broken_images:
            print(f"  • Dans [{page}] -> src='{img}'")
    else:
        print("✅ TOUTES LES IMAGES LOCALES SONT PRÉSENTES ET CHARGÉES !")

    print("=" * 60)

if __name__ == '__main__':
    audit()
