with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    c = f.read()

favicon_tags = """  <!-- Adaptive Favicons (Dark for light theme, Light for dark theme) -->
  <link rel="icon" href="/favicon-dark.png" media="(prefers-color-scheme: light)" type="image/png" />
  <link rel="icon" href="/favicon-light.png" media="(prefers-color-scheme: dark)" type="image/png" />
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />"""

if 'favicon-dark.png' not in c:
    c = c.replace('<meta name="description" content={description} />', '<meta name="description" content={description} />\n\n' + favicon_tags)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated Layout.astro with adaptive favicons!")
