import ftplib, os

ftp = ftplib.FTP('213.130.145.177', timeout=60)
ftp.login('u729389952.junglenepal.com', '09010412Amrr!')
ftp.set_pasv(True)

DIST_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

# Sync all html files and .htaccess
for root, dirs, files in os.walk(DIST_DIR):
    for f in files:
        if f.endswith('.html') or f == '.htaccess':
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, DIST_DIR)
            remote_dir = os.path.dirname(rel_path)
            
            ftp.cwd('/')
            dir_list = ftp.nlst()
            if 'public_html' in dir_list:
                ftp.cwd('public_html')
            
            if remote_dir:
                for part in remote_dir.split(os.sep):
                    try:
                        ftp.mkd(part)
                    except:
                        pass
                    ftp.cwd(part)
            
            with open(full_path, 'rb') as fp:
                ftp.storbinary(f'STOR {f}', fp)
            print(f"✓ Synced clean link: {rel_path}")

ftp.quit()
print("✓ All HTML files & .htaccess synced to Hostinger!")
