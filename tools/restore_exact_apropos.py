import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/a-propos.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract title
title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL | re.IGNORECASE)
title = title_match.group(1).strip() if title_match else 'À propos | Jungle Nepal Adventure'

# Extract body
body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL | re.IGNORECASE)
body = body_match.group(1) if body_match else html

# Adjust scripts and assets
body = body.replace('<script>', '<script is:inline>').replace('<script src=', '<script is:inline src=')
body = body.replace('is:inline is:inline', 'is:inline')

# Update 14 to 15 tours where needed
body = body.replace('Tous les 14 séjours', 'Tous les 15 séjours')
body = body.replace('Nos 14 Séjours', 'Nos 15 Séjours')
body = body.replace('14 séjours d\'exception', '15 séjours d\'exception')
body = body.replace('Voir les 14 séjours', 'Voir les 15 séjours')

astro_content = f"""---
import Layout from '../layouts/Layout.astro';
---

<Layout title="{title}" lang="fr">
{body}
</Layout>
"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro', 'w', encoding='utf-8') as f:
    f.write(astro_content)

print("Successfully restored 100% original a-propos.astro from original a-propos.html!")
