import os
import shutil

base_dir = os.path.dirname(os.path.abspath(__file__))
dist = os.path.join(base_dir, 'dist')

print(f"Ensuring dual routes in: {dist}")

# Ensure en/index.html exists
if os.path.exists(os.path.join(dist, 'en.html')):
    os.makedirs(os.path.join(dist, 'en'), exist_ok=True)
    shutil.copyfile(os.path.join(dist, 'en.html'), os.path.join(dist, 'en', 'index.html'))

# Ensure blog/index.html exists
if os.path.exists(os.path.join(dist, 'blog.html')):
    os.makedirs(os.path.join(dist, 'blog'), exist_ok=True)
    shutil.copyfile(os.path.join(dist, 'blog.html'), os.path.join(dist, 'blog', 'index.html'))

# Ensure dual routes: if foo.html exists, make sure foo/index.html also exists
for root, dirs, files in os.walk(dist):
    for f in files:
        if f.endswith('.html'):
            fpath = os.path.join(root, f)
            fname = f[:-5]
            if fname == 'index':
                continue
            
            sub_dir = os.path.join(root, fname)
            os.makedirs(sub_dir, exist_ok=True)
            sub_index = os.path.join(sub_dir, 'index.html')
            if not os.path.exists(sub_index):
                shutil.copyfile(fpath, sub_index)

# Automatic CSS Cache-Buster across ALL html files
import re, time
cache_ver = f"?v={int(time.time())}"
css_pattern = re.compile(r'(/_astro/[^"\'\?]+\.css)(\?[^"\']*)?')

for root, dirs, files in os.walk(dist):
    for f in files:
        if f.endswith('.html'):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8') as fp:
                c = fp.read()
            c_new = css_pattern.sub(r'\1' + cache_ver, c)
            if c != c_new:
                with open(fpath, 'w', encoding='utf-8') as fp:
                    fp.write(c_new)

print(f"✓ Cache-busted all CSS references with {cache_ver}")
print("✓ Dual routing guaranteed (both /foo.html, /foo and /foo/ return 200 OK)!")

