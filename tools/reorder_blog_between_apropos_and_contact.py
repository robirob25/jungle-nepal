import re, glob

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

updated = 0
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c

    # 1. Desktop Nav reordering:
    # Remove existing Blog link from before À propos if present
    c = re.sub(
        r'<a\s+href=[\'"]https://safarinepal\.fr[\'"][^>]*>Blog</a>\s*(<a\s+href=[\'"]/a-propos\.html[\'"])',
        r'\1',
        c
    )
    # Insert Blog between À propos and Contact if not already there
    # Check if À propos is immediately followed by Contact
    def insert_blog_desktop(match):
        a_prop = match.group(1)
        contact = match.group(2)
        # Check styling class in a_prop
        if 'text-slate-700' in a_prop or 'hover:text-[#0e8354]' in a_prop:
            blog_link = '<a href="https://safarinepal.fr" target="_blank" rel="noopener noreferrer" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">Blog</a>'
        else:
            blog_link = '<a href="https://safarinepal.fr" target="_blank" rel="noopener noreferrer" class="hover:text-amber-300 transition-colors whitespace-nowrap">Blog</a>'
        return f"{a_prop}\n          {blog_link}\n          {contact}"

    c = re.sub(
        r'(<a\s+href=[\'"]/a-propos\.html[\'"][^>]*>À propos</a>)\s*(<a\s+href=[\'"]/contact\.html[\'"][^>]*>Contact(?:ez-nous)?</a>)',
        insert_blog_desktop,
        c
    )

    # 2. Mobile Drawer reordering:
    # Ensure in mobile menu Blog is between À propos and Contact
    if 'id="mobile-menu"' in c:
        # If Blog is before À propos in mobile menu, move it
        mobile_blog_pattern = r'<!-- Blog \(safarinepal\.fr\) -->\s*<a\s+href=[\'"]https://safarinepal\.fr[\'"].*?</a>'
        mobile_blog_match = re.search(mobile_blog_pattern, c, re.DOTALL)
        if mobile_blog_match:
            mobile_blog_str = mobile_blog_match.group(0)
            # Remove it first
            c = c.replace(mobile_blog_str, '')
            # Insert between À propos block and Contact block
            c = re.sub(
                r'(<!--\s*(?:5\.\s*)?À propos\s*-->.*?</a>)\s*(<!--\s*(?:6\.\s*)?Contact\s*-->)',
                rf'\1\n\n      {mobile_blog_str}\n\n      \2',
                c,
                flags=re.DOTALL
            )

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated += 1

print(f"Re-ordered Blog between 'À propos' and 'Contact' across {updated} files!")
