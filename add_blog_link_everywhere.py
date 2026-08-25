import re, glob

astro_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/**/*.astro', recursive=True)

blog_link_desktop_transparent = '<a href="https://safarinepal.com" target="_blank" rel="noopener noreferrer" class="hover:text-amber-300 transition-colors whitespace-nowrap">Blog</a>'
blog_link_desktop_light = '<a href="https://safarinepal.com" target="_blank" rel="noopener noreferrer" class="hover:text-[#0e8354] transition-colors whitespace-nowrap">Blog</a>'

blog_link_mobile = """      <!-- Blog (safarinepal.com) -->
      <a href="https://safarinepal.com" target="_blank" rel="noopener noreferrer" class="px-3.5 py-2.5 rounded-2xl hover:bg-white/10 flex items-center gap-2.5 text-slate-200 hover:text-white transition-colors">
        <span>📝</span>
        <span>Blog</span>
        <span class="text-[10px] bg-white/10 text-slate-300 px-1.5 py-0.5 rounded font-mono ml-auto">↗</span>
      </a>"""

updated = 0
for fpath in astro_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    orig = c
    is_tour = '/tours/' in fpath
    target_desktop_link = blog_link_desktop_light if is_tour else blog_link_desktop_transparent

    # 1. Add Blog to desktop <nav> if missing
    if 'href="https://safarinepal.com"' not in c:
        # Insert before À propos or Contact in <nav>
        c = re.sub(
            r'(\s*)(<a\s+href=[\'"]/a-propos\.html[\'"])',
            rf'\1{target_desktop_link}\1\2',
            c,
            count=1
        )

    # 2. Add Blog to mobile-menu drawer if missing
    if 'safarinepal.com' in c and blog_link_mobile not in c:
        # Check if already in mobile menu
        if '<a href="https://safarinepal.com"' not in c.split('id="mobile-menu"')[1] if 'id="mobile-menu"' in c else True:
            c = re.sub(
                r'(\s*)(<!--\s*(?:5\.\s*)?À propos\s*-->)',
                rf'\1{blog_link_mobile}\1\2',
                c,
                count=1
            )

    if c != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        updated += 1

print(f"Added Blog link (https://safarinepal.com) across {updated} files!")
