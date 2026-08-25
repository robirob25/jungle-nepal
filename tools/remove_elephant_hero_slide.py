import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove Slide 2: Éléphant sauvage en jungle (hero_6_elephant_jungle.webp)
pattern = r'<!-- Slide 2: Éléphant sauvage en jungle -->\s*<div class="hero-slide[^"]*" data-slide="1">.*?</div>\s*'
c = re.sub(pattern, '', c, flags=re.DOTALL)

# Re-index all remaining data-slide attributes sequentially from 0 to N-1
def reindex_slides(match):
    slides = re.findall(r'(<div class="hero-slide[^"]*" data-slide=")\d+(".*?>)', match.group(0), flags=re.DOTALL)
    res = match.group(0)
    # let's replace data-slide="X" in order
    idx = 0
    def replace_idx(m):
        nonlocal idx
        out = f'{m.group(1)}{idx}{m.group(2)}'
        idx += 1
        return out
    res = re.sub(r'(<div class="hero-slide[^"]*" data-slide=")\d+(".*?>)', replace_idx, res)
    return res

c = re.sub(r'<div class="absolute inset-0 z-0 overflow-hidden" id="hero-slider-container">.*?</div>\s*<!-- 1\.1 Subtle Dark Contrast Layer', reindex_slides, c, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Removed elephant close-up slide from homepage hero slider and re-indexed slides cleanly!")
