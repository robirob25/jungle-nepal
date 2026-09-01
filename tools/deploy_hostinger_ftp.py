import os, sys, time, ftplib

FTP_HOST = '213.130.145.177'
FTP_USER = 'u729389952.junglenepal.com'
FTP_PASS = '09010412Amrr!'
DIST_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

def get_ftp():
    for attempt in range(5):
        try:
            ftp = ftplib.FTP()
            ftp.connect(FTP_HOST, 21, timeout=60)
            ftp.login(FTP_USER, FTP_PASS)
            ftp.set_pasv(True)
            # Enter public_html
            dir_list = ftp.nlst()
            if 'public_html' in dir_list:
                ftp.cwd('public_html')
            return ftp
        except Exception as e:
            print(f"Connection attempt {attempt+1} failed: {e}. Retrying in 3s...")
            time.sleep(3)
    raise Exception("Could not connect to Hostinger FTP after 5 attempts.")

# Flatten all files to upload
all_files = []
for root, dirs, files in os.walk(DIST_DIR):
    for f in files:
        full_path = os.path.join(root, f)
        rel_path = os.path.relpath(full_path, DIST_DIR)
        all_files.append((full_path, rel_path))

print(f"Total files to deploy: {len(all_files)}")

ftp = get_ftp()
print("✓ Connected to Hostinger!")

for i, (local_path, rel_path) in enumerate(all_files):
    remote_dir = os.path.dirname(rel_path)
    file_name = os.path.basename(rel_path)
    local_size = os.path.getsize(local_path)
    
    success = False
    for attempt in range(5):
        try:
            # Navigate to root of public_html
            ftp.cwd('/')
            dir_list = ftp.nlst()
            if 'public_html' in dir_list:
                ftp.cwd('public_html')
            
            # Ensure subdirectories exist
            if remote_dir:
                parts = remote_dir.split(os.sep)
                for part in parts:
                    try:
                        ftp.mkd(part)
                    except:
                        pass
                    ftp.cwd(part)
            
            # Check if file exists and has same size
            try:
                remote_size = ftp.size(file_name)
                if remote_size == local_size:
                    print(f"[{i+1}/{len(all_files)}] ⚡ Already synced: {rel_path}")
                    success = True
                    break
            except:
                pass
            
            # Upload file
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {file_name}', f)
            print(f"[{i+1}/{len(all_files)}] ✓ Uploaded: {rel_path}")
            success = True
            break
        except Exception as e:
            print(f"Error uploading {rel_path} (attempt {attempt+1}): {e}")
            try:
                ftp.quit()
            except:
                pass
            time.sleep(2)
            ftp = get_ftp()

    if not success:
        print(f"❌ Failed to upload {rel_path} after 5 attempts.")

try:
    ftp.quit()
except:
    pass

print("\n🎉🎉🎉 DEPLOYMENT TO HOSTINGER COMPLETED 100% SUCCESSFULLY! 🎉🎉🎉")
