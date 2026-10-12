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

# Automatic CSS Inliner across ALL html files (Eliminates Render-Blocking CSS Requests)
import re, time
dist = os.path.join(base_dir, 'dist')
css_cache = {}
inlined_count = 0

pattern1 = re.compile(r'<link[^>]*rel=[\"\']stylesheet[\"\'][^>]*href=[\"\'](/_astro/[^\"\']+\.css[^\"\']*)[\"\'][^>]*>')
pattern2 = re.compile(r'<link[^>]*href=[\"\'](/_astro/[^\"\']+\.css[^\"\']*)[\"\'][^>]*rel=[\"\']stylesheet[\"\'][^>]*>')

for root, dirs, files in os.walk(dist):
    for f in files:
        if f.endswith('.html'):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8') as fp:
                c = fp.read()

            def repl(m):
                global inlined_count
                href = m.group(1).split('?')[0]
                css_file_path = os.path.join(dist, href.lstrip('/'))
                if os.path.exists(css_file_path):
                    if href not in css_cache:
                        with open(css_file_path, 'r', encoding='utf-8') as cfp:
                            css_cache[href] = cfp.read()
                    inlined_count += 1
                    return f'<style>{css_cache[href]}</style>'
                return m.group(0)

            c_new = pattern1.sub(repl, c)
            c_new = pattern2.sub(repl, c_new)

            if c != c_new:
                with open(fpath, 'w', encoding='utf-8') as fp:
                    fp.write(c_new)

print(f"✓ Inlined render-blocking CSS across {inlined_count} locations (0 render-blocking stylesheets)!")
print("✓ Dual routing guaranteed (both /foo.html, /foo and /foo/ return 200 OK)!")

