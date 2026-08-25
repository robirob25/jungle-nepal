import glob, re

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # Replace 24h / 24 heures mentions regarding quotes and replies with 48h / 48 heures:
    c = c.replace('Réponse garantie sous 24 heures', 'Réponse garantie sous 48 heures')
    c = c.replace('réponse sous 24h', 'réponse sous 48h')
    c = c.replace('répondront sous 24h', 'répondront sous 48h')
    c = c.replace('répondront personnellement sous 24h', 'répondront personnellement sous 48h')
    c = c.replace('Étude personnalisée sous 24h', 'Étude personnalisée sous 48h')
    c = c.replace('réponse garantie sous 24h', 'réponse garantie sous 48h')
    c = c.replace('vous répondent sous 24h', 'vous répondent sous 48h')
    c = c.replace('devis sous 24h', 'devis sous 48h')
    c = c.replace('Devis sous 24h', 'Devis sous 48h')
    c = c.replace('Response within 24h', 'Response within 48h')
    c = c.replace('within 24 hours', 'within 48 hours')
    c = c.replace('within 24h', 'within 48h')

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"✓ Updated quote response delay to 48h in {fpath.split('/')[-1]}")

print("Done updating all quote response guarantees to 48h!")
