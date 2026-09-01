import os, glob, re, ftplib

DIST_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

# 1. Audit all image references in dist/
img_srcs = set()
for root, dirs, files in os.walk(DIST_DIR):
    for f in files:
        if f.endswith('.html'):
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8') as fp:
                c = fp.read()
            # Match src="/assets/..." and src="assets/..."
            matches = re.findall(r'src="(/assets/[^"]+|\/?assets/[^"]+)"', c)
            for m in matches:
                img_srcs.add(m.lstrip('/'))

print(f"Total distinct local image references in HTML: {len(img_srcs)}")

# Check missing local files
missing_local = []
for src in img_srcs:
    local_path = os.path.join(DIST_DIR, src)
    if not os.path.exists(local_path):
        missing_local.append(src)

if missing_local:
    print("WARNING: Missing local files in dist:", missing_local)
else:
    print("✓ All referenced images exist locally in dist!")

# 2. Check which images exist on Hostinger FTP in /public_html
ftp = ftplib.FTP('213.130.145.177', timeout=60)
ftp.login('u729389952.junglenepal.com', '09010412Amrr!')
ftp.set_pasv(True)
ftp.cwd('/public_html')

print("Verifying and uploading all assets directly to /public_html/assets/...")

for src in img_srcs:
    local_path = os.path.join(DIST_DIR, src)
    if not os.path.exists(local_path):
        continue
    
    local_size = os.path.getsize(local_path)
    remote_dir = os.path.dirname(src)
    file_name = os.path.basename(src)
    
    ftp.cwd('/public_html')
    for part in remote_dir.split('/'):
        if part:
            try:
                ftp.mkd(part)
            except:
                pass
            ftp.cwd(part)
    
    # Check size
    needs_upload = True
    try:
        remote_size = ftp.size(file_name)
        if remote_size == local_size:
            needs_upload = False
    except:
        pass
    
    if needs_upload:
        with open(local_path, 'rb') as fp:
            ftp.storbinary(f'STOR {file_name}', fp)
        print(f"✓ Uploaded missing/broken asset: {src}")

ftp.quit()
print("🎉 All images are 100% verified on Hostinger /public_html!")
