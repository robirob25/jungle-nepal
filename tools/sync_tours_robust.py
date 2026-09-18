import ftplib
import os
import time
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

DIST_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'
FTP_HOST = '213.130.145.177'
FTP_USER = 'u729389952.junglenepal.com'
FTP_PASS = '09010412Amrr!'
MANIFEST_FILE = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/.ftp_deploy_manifest.json'

def create_ftp_conn():
    for attempt in range(5):
        try:
            ftp = ftplib.FTP(FTP_HOST, timeout=60)
            ftp.login(FTP_USER, FTP_PASS)
            ftp.set_pasv(True)
            return ftp
        except Exception as e:
            time.sleep(1)
    raise Exception("Could not connect to FTP")

def ensure_remote_dir(ftp, remote_dir):
    ftp.cwd('/public_html')
    if remote_dir and remote_dir != '.':
        for part in remote_dir.split(os.sep):
            if not part:
                continue
            try:
                ftp.mkd(part)
            except Exception:
                pass
            ftp.cwd(part)

# Load existing manifest
manifest = {}
if os.path.exists(MANIFEST_FILE):
    try:
        with open(MANIFEST_FILE, 'r') as f:
            manifest = json.load(f)
    except Exception:
        manifest = {}

# Gather all files
files_to_upload = []
new_manifest = {}

for root, dirs, files in os.walk(DIST_DIR):
    for f in files:
        if f.endswith('.map'):
            continue
        full_path = os.path.join(root, f)
        rel_path = os.path.relpath(full_path, DIST_DIR)
        
        st = os.stat(full_path)
        file_key = f"{st.st_size}_{int(st.st_mtime)}"
        new_manifest[rel_path] = file_key

        if manifest.get(rel_path) != file_key:
            files_to_upload.append((full_path, rel_path))

print(f"Total files in dist: {len(new_manifest)} | Files to upload: {len(files_to_upload)}")

# Sort files: ASSETS FIRST (_astro, assets, fonts, css, js), THEN images, THEN HTML LAST!
def sort_priority(item):
    full_path, rel_path = item
    if rel_path.startswith('_astro'):
        return 0
    if rel_path.startswith('assets/fonts') or rel_path.startswith('assets/css') or rel_path.startswith('assets/js'):
        return 1
    if rel_path == '.htaccess':
        return 2
    if not rel_path.endswith('.html'):
        return 3
    # HTML files uploaded strictly last so all styles and scripts are guaranteed ready
    return 4

files_to_upload.sort(key=sort_priority)

def upload_single_file(item):
    full_path, rel_path = item
    f_name = os.path.basename(full_path)
    remote_dir = os.path.dirname(rel_path)
    
    for attempt in range(4):
        ftp = None
        try:
            ftp = create_ftp_conn()
            ensure_remote_dir(ftp, remote_dir)
            with open(full_path, 'rb') as fp:
                ftp.storbinary(f'STOR {f_name}', fp)
            ftp.quit()
            return True, rel_path, None
        except Exception as e:
            if ftp:
                try:
                    ftp.close()
                except Exception:
                    pass
            time.sleep(1)
            if attempt == 3:
                return False, rel_path, str(e)

uploaded_count = 0
errors = 0

with ThreadPoolExecutor(max_workers=6) as executor:
    futures = [executor.submit(upload_single_file, item) for item in files_to_upload]
    for future in as_completed(futures):
        success, rel_path, err = future.result()
        if success:
            uploaded_count += 1
        else:
            errors += 1
            print(f"❌ Failed: {rel_path} ({err})")

# Save updated manifest
try:
    with open(MANIFEST_FILE, 'w') as f:
        json.dump(new_manifest, f)
except Exception:
    pass

print(f"🎉 Atomic Sync Complete! Uploaded {uploaded_count}/{len(files_to_upload)} files. Errors: {errors}")
