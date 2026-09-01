with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace remote avatar URLs with local assets
c = c.replace('https://junglenepal.com/wp-content/uploads/2025/12/2.png', '/assets/pawan_webp.webp')
c = c.replace('https://junglenepal.com/wp-content/uploads/2025/12/1.png', '/assets/kiran_webp.webp')
c = c.replace('https://junglenepal.com/wp-content/uploads/2025/12/3.png', '/assets/banner_duo.webp')

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Fixed all team avatar URLs in index.astro!")
