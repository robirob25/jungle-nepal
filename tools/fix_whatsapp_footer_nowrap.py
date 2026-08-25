import re, glob

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

updated = 0
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # Fix footer logo to transparent white logo if present
    c = c.replace('src="/assets/logo.png" alt="Jungle Nepal Adventure" class="h-16', 'src="/assets/logo_nav_white.png" alt="Jungle Nepal Adventure" class="h-12')

    # Fix any WhatsApp button or text in footers or headers to prevent wrapping
    c = re.sub(
        r'<a\s+href=[\'"]https://wa\.me/33695413227[^\'"]*[\'"]([^>]*)>\s*(<svg[^>]*>.*?</svg>)\s*<span>(.*?)</span>\s*</a>',
        r'<a href="https://wa.me/33695413227" target="_blank" \1 whitespace-nowrap">\2<span class="whitespace-nowrap">\3</span></a>',
        c,
        flags=re.DOTALL
    )

    # Ensure whitespace-nowrap on WhatsApp spans
    c = c.replace('<span>WhatsApp : +33 6 95 41 32 27</span>', '<span class="whitespace-nowrap">WhatsApp : +33 6 95 41 32 27</span>')
    c = c.replace('<span>WhatsApp Direct (+33 6 95 41 32 27)</span>', '<span class="whitespace-nowrap">WhatsApp Direct (+33 6 95 41 32 27)</span>')
    c = c.replace('<span>WhatsApp Direct</span>', '<span class="whitespace-nowrap">WhatsApp Direct</span>')

    # Fix duplicate whitespace-nowrap classes if any
    c = re.sub(r'whitespace-nowrap\s+whitespace-nowrap', 'whitespace-nowrap', c)

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated += 1

print(f"Enforced strict single-line whitespace-nowrap for WhatsApp across {updated} files!")
