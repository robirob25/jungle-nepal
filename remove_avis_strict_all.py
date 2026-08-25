import os
import re

# Remove Avis / Reviews link from ANY header nav
tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
dest_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/destinations'
root_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'

all_files = []
for r, d, files in os.walk(root_dir):
    for f in files:
        if f.endswith('.html'):
            all_files.append(os.path.join(r, f))

pattern = r'<a\s+href=[\"\'][^\"\']*[\"\'][^>]*>(?:(?!</a>).)*?(?:Avis|Reviews).*?</a>\s*'

count = 0
for fpath in all_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find header and clean only inside nav
    def clean_header_nav(match):
        header = match.group(0)
        def clean_nav(nmatch):
            nav = nmatch.group(0)
            return re.sub(pattern, '', nav, flags=re.DOTALL | re.IGNORECASE)
        return re.sub(r'<nav[^>]*>.*?</nav>', clean_nav, header, flags=re.DOTALL)

    new_content = re.sub(r'<header[^>]*>.*?</header>', clean_header_nav, content, flags=re.DOTALL)
    
    if new_content != content:
        count += 1
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned header in: {os.path.relpath(fpath, root_dir)}")

print(f"\nRemoved Avis from {count} files across the entire project!")
