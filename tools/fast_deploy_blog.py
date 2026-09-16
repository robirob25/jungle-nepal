import os
import sys
import time
import ftplib
from concurrent.futures import ThreadPoolExecutor

FTP_HOST = '213.130.145.177'
FTP_USER = 'u729389952.junglenepal.com'
FTP_PASS = '09010412Amrr!'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST_DIR = os.path.join(BASE_DIR, 'dist')

def make_ftp():
    for attempt in range(5):
        try:
            ftp = ftplib.FTP()
            ftp.connect(FTP_HOST, 21, timeout=60)
            ftp.login(FTP_USER, FTP_PASS)
            ftp.set_pasv(True)
            ftp.cwd('/public_html')
            return ftp
        except Exception as e:
            time.sleep(2)
    raise Exception("Could not connect to FTP")

# Get list of all files in DIST_DIR
all_files = []
for root, dirs, files in os.walk(DIST_DIR):
    for f in files:
        full_path = os.path.join(root, f)
        rel_path = os.path.relpath(full_path, DIST_DIR)
        all_files.append((full_path, rel_path))

print(f"Total files to deploy to Hostinger: {len(all_files)}")

# First ensure all directories exist on FTP
main_ftp = make_ftp()
print("✓ Connected to Hostinger FTP /public_html")

# Collect unique remote dirs
unique_dirs = sorted(list(set(os.path.dirname(rel) for _, rel in all_files if os.path.dirname(rel))))

for d in unique_dirs:
    parts = d.split(os.sep)
    current = '/public_html'
    for p in parts:
        current = f"{current}/{p}"
        try:
            main_ftp.cwd(current)
        except:
            try:
                main_ftp.cwd('/public_html')
                parent = os.path.dirname(d)
                main_ftp.mkd(current)
            except Exception as e:
                pass

print(f"✓ Ensured {len(unique_dirs)} remote directories exist.")
main_ftp.quit()

def upload_file_task(item):
    local_path, rel_path = item
    file_size = os.path.getsize(local_path)
    remote_path = rel_path.replace(os.sep, '/')
    
    for attempt in range(4):
        try:
            ftp = ftplib.FTP()
            ftp.connect(FTP_HOST, 21, timeout=60)
            ftp.login(FTP_USER, FTP_PASS)
            ftp.set_pasv(True)
            ftp.cwd('/public_html')
            
            # Check if remote file exists and same size (skip if same)
            try:
                rem_size = ftp.size(remote_path)
                if rem_size == file_size:
                    ftp.quit()
                    return f"SKIPPED (already up to date): {remote_path}"
            except Exception:
                pass
            
            # Upload
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {remote_path}', f)
            ftp.quit()
            return f"✓ UPLOADED: {remote_path} ({file_size} bytes)"
        except Exception as e:
            time.sleep(2)
            if attempt == 3:
                return f"✗ FAILED: {remote_path} ({e})"

print("Starting parallel upload (10 workers)...")
start_t = time.time()
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(upload_file_task, all_files))

uploaded = sum(1 for r in results if r and r.startswith("✓"))
skipped = sum(1 for r in results if r and r.startswith("SKIPPED"))
failed = sum(1 for r in results if r and r.startswith("✗"))

print(f"\n🎉 Deployment completed in {round(time.time() - start_t, 1)}s!")
print(f"Uploaded: {uploaded} files | Skipped (already identical): {skipped} | Failed: {failed}")
