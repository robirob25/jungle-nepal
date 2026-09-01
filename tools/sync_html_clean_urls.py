import ftplib, os

ftp = ftplib.FTP('213.130.145.177', timeout=60)
ftp.login('u729389952.junglenepal.com', '09010412Amrr!')
ftp.set_pasv(True)

DIST_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

# Only sync HTML files and .htaccess
for root, dirs, files in os.walk(DIST_DIR):
    for f in files:
        if f.endswith('.html') or f == '.htaccess' or f.endswith('.xml'):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, DIST_DIR)
            remote_dir = os.path.dirname(rel_path)
            
            ftp.cwd('/public_html')
            if remote_dir:
                for part in remote_dir.split(os.sep):
                    try:
                        ftp.mkd(part)
                    except:
                        pass
                    ftp.cwd(part)
            
            with open(full_path, 'rb') as fp:
                ftp.storbinary(f'STOR {f}', fp)
            print(f"✓ Synced clean URL file: {rel_path}")

ftp.quit()
print("🎉 All HTML pages with clean URL bars deployed!")
