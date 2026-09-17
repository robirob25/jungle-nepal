import ftplib
import os
import time

DIST_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

def connect_ftp():
    for attempt in range(5):
        try:
            ftp = ftplib.FTP('213.130.145.177', timeout=60)
            ftp.login('u729389952.junglenepal.com', '09010412Amrr!')
            ftp.set_pasv(True)
            return ftp
        except Exception as e:
            print(f"FTP Connect attempt {attempt+1} failed: {e}")
            time.sleep(2)
    raise Exception("Could not connect to FTP after 5 attempts")

ftp = connect_ftp()

uploaded_count = 0
error_count = 0

for root, dirs, files in os.walk(DIST_DIR):
    for f in files:
        # Include all relevant assets, including .css, .js, .html, .woff2, .webp, .png, .jpg, .svg, .json, .htaccess
        full_path = os.path.join(root, f)
        rel_path = os.path.relpath(full_path, DIST_DIR)
        
        # Skip temp / map files
        if f.endswith('.map'):
            continue

        remote_dir = os.path.dirname(rel_path)

        success = False
        for attempt in range(3):
            try:
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

                with open(full_path, 'rb') as fp:
                    ftp.storbinary(f'STOR {f}', fp)
                
                uploaded_count += 1
                success = True
                break
            except Exception as e:
                print(f"Retry {attempt+1} uploading {rel_path}: {e}")
                time.sleep(1)
                try:
                    ftp = connect_ftp()
                except Exception:
                    pass

        if not success:
            print(f"❌ FAILED to upload: {rel_path}")
            error_count += 1

try:
    ftp.quit()
except Exception:
    pass

print(f"🎉 Sync Complete! Successfully uploaded {uploaded_count} files. Errors: {error_count}")
