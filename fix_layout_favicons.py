with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    c = f.read()

old_fav = """  <!-- Adaptive Modern Favicons (Auto Dark / Light Mode Matching Browser Theme) -->
  <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
  <link rel="icon" href="/favicon-dark.png" media="(prefers-color-scheme: light)" type="image/png" sizes="32x32" />
  <link rel="icon" href="/favicon-light.png" media="(prefers-color-scheme: dark)" type="image/png" sizes="32x32" />
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="apple-touch-icon" href="/assets/logo.png" />"""

new_fav = """  <!-- Dynamic Adaptive Favicon (Auto Dark/Light Theme Detection via Media Query + High-Res PNG) -->
  <link rel="icon" href="/favicon-dark.png" media="(prefers-color-scheme: light)" type="image/png" />
  <link rel="icon" href="/favicon-light.png" media="(prefers-color-scheme: dark)" type="image/png" />
  <link rel="icon" href="/favicon-dark.png" type="image/png" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />"""

c = c.replace(old_fav, new_fav)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Updated Layout.astro with exact user uploaded icons!")
