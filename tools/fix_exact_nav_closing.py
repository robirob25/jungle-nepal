import os
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

# Fix destinations/index.html
dest_idx = os.path.join(base, 'destinations/index.html')
with open(dest_idx, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace("""              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="destinations/index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  Voir toutes les destinations →
                </a>
              </div>

            </div>
          </div>
        <a href="../index.html#concept""", """              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="destinations/index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  Voir toutes les destinations →
                </a>
              </div>

            </div>
          </div>
        </div>
        <a href="../index.html#concept""")

with open(dest_idx, 'w', encoding='utf-8') as f:
    f.write(c)

# Fix en/index.html
en_idx = os.path.join(base, 'en/index.html')
with open(en_idx, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace("""              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="destinations/index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  All Destinations →
                </a>
              </div>

            </div>
          </div>
      </div>
      <a href="#concept""", """              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="destinations/index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  All Destinations →
                </a>
              </div>

            </div>
          </div>
        </div>
      <a href="#concept""")

with open(en_idx, 'w', encoding='utf-8') as f:
    f.write(c)

# Fix en/destinations/index.html
en_dest_idx = os.path.join(base, 'en/destinations/index.html')
with open(en_dest_idx, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace("""              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="destinations/index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  All Destinations →
                </a>
              </div>

            </div>
          </div>
        <a href="../index.html#concept""", """              <div class="pt-2 border-t border-white/10 mt-1">
                <a href="destinations/index.html" class="block w-full text-center py-2 rounded-xl bg-[#0e8354] hover:bg-[#0c6d46] text-white font-black text-xs transition-colors shadow">
                  All Destinations →
                </a>
              </div>

            </div>
          </div>
        </div>
        <a href="../index.html#concept""")

with open(en_dest_idx, 'w', encoding='utf-8') as f:
    f.write(c)

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
    print(f"\n🎉 100% OF ALL {len(all_files)} HTML PAGES IN THE REPOSITORY HAVE PERFECT ZERO-ERROR DOM STRUCTURE!")
else:
    print(f"\nRemaining errors in {errors} files.")
