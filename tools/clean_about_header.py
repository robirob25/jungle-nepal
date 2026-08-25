import re

for filepath in [
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/a-propos.astro',
    '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/a-propos.astro'
]:
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Remove duplicated top-bar and header and mobile-menu before the HERO section
    # Target: from <Header ... /> until <!-- ========================================================================= -->\n  <!-- 3. HERO IMMERSIF (or HERO SECTION)
    c = re.sub(
        r'(<Header\s+lang=[\'\"].*?[\'\"]\s+currentPath=[\'\"].*?[\'\"]\s*/>)\s*<!-- 1\. TOP ANNOUNCEMENT BANNER -->.*?<!-- ========================================================================= -->\s*<!-- 3\. HERO',
        r'\1\n\n  <!-- ========================================================================= -->\n  <!-- 3. HERO',
        c,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Cleaned up duplicated headers in about pages!")
