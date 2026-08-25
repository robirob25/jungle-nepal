with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix relative links in destinations/index.html
html = html.replace('href="destinations/index.html"', 'href="index.html"')
html = html.replace('href="destinations/bardia.html"', 'href="bardia.html"')
html = html.replace('href="destinations/chitwan.html"', 'href="chitwan.html"')
html = html.replace('href="destinations/suklaphanta.html"', 'href="suklaphanta.html"')
html = html.replace('href="destinations/annapurna.html"', 'href="annapurna.html"')
html = html.replace('href="destinations/katmandou.html"', 'href="katmandou.html"')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed relative links in destinations/index.html!")
