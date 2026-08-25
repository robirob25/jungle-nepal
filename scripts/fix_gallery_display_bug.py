import re

fpath = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro'

with open(fpath, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Remove loading="lazy" from all wildlife-card images so they never get blocked when unhidden
# Match all img tags inside wildlife cards and ensure decoding="async" without lazy blocking
c = re.sub(
    r'(<div class="wildlife-card.*?<img[^>]*?)\s+loading="lazy"',
    r'\1 loading="eager"',
    c,
    flags=re.DOTALL
)

# 2. Update renderWildlifeCards script to ensure all unhidden images are immediately forced to display and layout reflowed
old_render = """      if (matchesCat) {
        totalInCurrentCategory++;
        if (window.currentWildlifeCategory === 'all') {
          if (visibleInCurrentCategory < window.wildlifeVisibleLimit) {
            card.style.display = 'block';
            visibleInCurrentCategory++;
          } else {
            card.style.display = 'none';
          }
        } else {
          card.style.display = 'block';
          visibleInCurrentCategory++;
        }
      } else {
        card.style.display = 'none';
      }"""

new_render = """      if (matchesCat) {
        totalInCurrentCategory++;
        if (window.currentWildlifeCategory === 'all') {
          if (visibleInCurrentCategory < window.wildlifeVisibleLimit) {
            card.style.display = 'block';
            var imgEl = card.querySelector('img');
            if (imgEl && !imgEl.complete) {
              imgEl.loading = 'eager';
            }
            visibleInCurrentCategory++;
          } else {
            card.style.display = 'none';
          }
        } else {
          card.style.display = 'block';
          var imgEl = card.querySelector('img');
          if (imgEl && !imgEl.complete) {
            imgEl.loading = 'eager';
          }
          visibleInCurrentCategory++;
        }
      } else {
        card.style.display = 'none';
      }"""

c = c.replace(old_render, new_render)

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated index.astro: lazy loading removed on wildlife gallery and eager loading forced on display.")
