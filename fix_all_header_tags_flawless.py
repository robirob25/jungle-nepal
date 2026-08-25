import os
import re
from html.parser import HTMLParser

class StrictTagValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link', 'source']:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in ['img', 'br', 'hr', 'input', 'meta', 'link', 'source']:
            return
        if self.stack:
            expected = self.stack.pop()
            if expected != tag:
                self.errors.append(f'Mismatched </{tag}>, expected </{expected}>')
        else:
            self.errors.append(f'Unexpected </{tag}> with empty stack')

base = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal'

for rel in ['destinations/index.html', 'en/index.html', 'en/destinations/index.html']:
    fpath = os.path.join(base, rel)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Replace 4 closing divs with 3 closing divs around destinations dropdown
    c = re.sub(r'(\s*</div>\s*</div>\s*</div>)\s*</div>(\s*<a href="[^"]*#(?:concept|prochains-departs))', r'\1\2', c)
    c = re.sub(r'(\s*</div>\s*</div>\s*</div>)\s*</div>(\s*<a href="[^"]*a-propos\.html)', r'\1\2', c)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

# Now check all html files in entire repo
all_files = []
for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.html'):
            all_files.append(os.path.join(root, f))

errors = 0
for fpath in all_files:
    rel = os.path.relpath(fpath, base)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    v = StrictTagValidator()
    v.feed(content)
    if v.stack or v.errors:
        print(f"❌ {rel}: Stack={v.stack}, Errors={v.errors[:3]}")
        errors += 1

if errors == 0:
    print(f"\n🎉 100% of ALL {len(all_files)} HTML pages in the website have STRICTLY PERFECT, BALANCED DOM!")
else:
    print(f"\nRemaining errors in {errors} files.")
