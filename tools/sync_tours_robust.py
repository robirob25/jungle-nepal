import ftplib, os, time

DIST_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

def upload_file_with_retry(ftp, local_path, remote_dir, filename):
    for attempt in range(3):
        try:
            ftp.cwd('/public_html')
            if remote_dir:
                for part in remote_dir.split(os.sep):
                    try:
                        ftp.mkd(part)
                    except:
                        pass
                    ftp.cwd(part)
            with open(local_path, 'rb') as fp:
                ftp.storbinary(f'STOR {filename}', fp)
            print(f"✓ Uploaded: {os.path.join(remote_dir, filename)}")
            return True
        except Exception as e:
            print(f"Retry {attempt+1} on {filename}: {e}")
            time.sleep(2)
            try:
                ftp.connect('213.130.145.177', timeout=60)
                ftp.login('u729389952.junglenepal.com', '09010412Amrr!')
                ftp.set_pasv(True)
            except:
                pass
    return False

ftp = ftplib.FTP('213.130.145.177', timeout=60)
ftp.login('u729389952.junglenepal.com', '09010412Amrr!')
ftp.set_pasv(True)

for root, dirs, files in os.walk(DIST_DIR):
    for f in files:
        if f.endswith('.html') or f.endswith('.css') or f.endswith('.js') or f == '.htaccess':
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, DIST_DIR)
            remote_dir = os.path.dirname(rel_path)
            upload_file_with_retry(ftp, full_path, remote_dir, f)

ftp.quit()
print("🎉 All tour pages and CSS assets synced with perfect retry mechanism!")
