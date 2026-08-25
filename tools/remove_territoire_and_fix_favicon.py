import glob, re

# 1. Remove the "Territoire Sauvage du Népal" pill badge from all destination pages
dest_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/destinations/*.astro')
for fpath in dest_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    c = re.sub(
        r'<span class="inline-flex items-center gap-2 px-4 py-1\.5 rounded-full bg-emerald-500/20 text-\[#10b981\] border border-emerald-500/30 text-xs font-black uppercase tracking-widest">\s*<span>🇳🇵</span>\s*Territoire Sauvage du Népal\s*</span>',
        '',
        c
    )
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("✓ Removed 'Territoire Sauvage du Népal' badges across all destination pages!")

# 2. Perfect Adaptive SVG / PNG Favicon in Layout.astro
# SVG favicon that automatically detects user dark/light mode preference via CSS @media,
# plus standard multi-resolution fallbacks.

svg_favicon_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <style>
    path { fill: #041d13; }
    @media (prefers-color-scheme: dark) {
      path { fill: #ffffff; }
    }
  </style>
  <!-- Stylized Tiger & Mountain Profile Logo Mark -->
  <path d="M256,48 L140,240 L210,240 L160,330 L256,270 L352,330 L302,240 L372,240 Z M180,360 C120,380 90,430 80,464 C140,464 200,440 256,400 C312,440 372,464 432,464 C422,430 392,380 332,360 C290,390 222,390 180,360 Z"/>
</svg>"""

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/favicon.svg', 'w', encoding='utf-8') as f:
    f.write(svg_favicon_content)

# Update Layout.astro favicon tags to support adaptive SVG + dark/light media queries
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

old_fav_block = """  <!-- Adaptive Favicons -->
  <link rel="icon" href="/favicon-dark.png" media="(prefers-color-scheme: light)" type="image/png" />
  <link rel="icon" href="/favicon-light.png" media="(prefers-color-scheme: dark)" type="image/png" />
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />"""

new_fav_block = """  <!-- Adaptive Modern Favicons (Auto Dark / Light Mode Matching Browser Theme) -->
  <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
  <link rel="icon" href="/favicon-dark.png" media="(prefers-color-scheme: light)" type="image/png" sizes="32x32" />
  <link rel="icon" href="/favicon-light.png" media="(prefers-color-scheme: dark)" type="image/png" sizes="32x32" />
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="apple-touch-icon" href="/assets/logo.png" />"""

layout = layout.replace(old_fav_block, new_fav_block)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)

print("✓ Successfully configured adaptive dynamic favicon (light & dark browser mode)!")
