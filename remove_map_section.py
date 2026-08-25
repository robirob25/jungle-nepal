import re

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the entire section 4.5 and its script
content = re.sub(
    r'\s*<!-- ========================================================================= -->\s*<!-- 4\.5 CARTE GÉOGRAPHIQUE.*?<!-- ========================================================================= -->\s*<!-- 5\. GALERIE',
    '\n\n  <!-- ========================================================================= -->\n  <!-- 5. GALERIE',
    content,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)

print("Completely removed map section from index.astro!")
