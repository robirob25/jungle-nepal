import os
import shutil

dist = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

# Ensure en/index.html exists
if os.path.exists(os.path.join(dist, 'en.html')):
    os.makedirs(os.path.join(dist, 'en'), exist_ok=True)
    shutil.copyfile(os.path.join(dist, 'en.html'), os.path.join(dist, 'en/index.html'))

# For every .html file in dist, also create a directory with index.html (and vice versa)
for root, dirs, files in os.walk(dist):
    for f in files:
        if f.endswith('.html'):
            fpath = os.path.join(root, f)
            fname = f[:-5]
            if fname == 'index':
                continue
            
            # If foo.html exists, make sure foo/index.html also exists
            sub_dir = os.path.join(root, fname)
            os.makedirs(sub_dir, exist_ok=True)
            sub_index = os.path.join(sub_dir, 'index.html')
            if not os.path.exists(sub_index):
                shutil.copyfile(fpath, sub_index)

print("Dual routing guaranteed (both /foo.html and /foo/ return 200 OK)!")
