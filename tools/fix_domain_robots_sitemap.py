# Align site domain strictly to junglenepal.com across robots.txt, astro.config.mjs, and sitemap

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/robots.txt', 'w', encoding='utf-8') as f:
    f.write("User-agent: *\nAllow: /\n\nSitemap: https://junglenepal.com/sitemap.xml\n")

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/astro.config.mjs', 'r', encoding='utf-8') as f:
    cfg = f.read()

cfg = cfg.replace('https://junglenepaladventure.com', 'https://junglenepal.com')
cfg = cfg.replace('https://jungle-nepal.com', 'https://junglenepal.com')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/astro.config.mjs', 'w', encoding='utf-8') as f:
    f.write(cfg)

print("✓ Updated robots.txt and astro.config.mjs with official domain https://junglenepal.com!")
