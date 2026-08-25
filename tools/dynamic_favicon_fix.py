with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace static links with a dynamic JavaScript listener on matchMedia('(prefers-color-scheme: dark)')
# that swaps the favicon immediately and flawlessly in Chrome/Safari/Firefox tabs!

old_fav = """  <!-- Dynamic Adaptive Favicon (Auto Dark/Light Theme Detection via Media Query + High-Res PNG) -->
  <link rel="icon" href="/favicon-dark.png" media="(prefers-color-scheme: light)" type="image/png" />
  <link rel="icon" href="/favicon-light.png" media="(prefers-color-scheme: dark)" type="image/png" />
  <link rel="icon" href="/favicon-dark.png" type="image/png" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />"""

new_fav = """  <!-- Dynamic Adaptive Favicon (Instant DOM Switcher for Chrome/Safari/Edge) -->
  <link id="dynamic-favicon" rel="icon" href="/favicon-light.png" type="image/png" />
  <link rel="icon" href="/favicon-dark.png" media="(prefers-color-scheme: light)" type="image/png" />
  <link rel="icon" href="/favicon-light.png" media="(prefers-color-scheme: dark)" type="image/png" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />

  <script is:inline>
    (function() {
      function updateFavicon() {
        var isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
        var favicon = document.getElementById('dynamic-favicon');
        if (favicon) {
          favicon.href = isDark ? '/favicon-light.png?v=2' : '/favicon-dark.png?v=2';
        }
      }
      updateFavicon();
      if (window.matchMedia) {
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', updateFavicon);
      }
    })();
  </script>"""

c = c.replace(old_fav, new_fav)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Dynamic JavaScript & CSS adaptive favicon switcher installed in Layout.astro!")
