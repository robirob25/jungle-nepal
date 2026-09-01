import ftplib, os

FTP_HOST = '213.130.145.177'
FTP_USER = 'u729389952.junglenepal.com'
FTP_PASS = '09010412Amrr!'
DIST_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

ftp = ftplib.FTP(FTP_HOST, timeout=60)
ftp.login(FTP_USER, FTP_PASS)
ftp.set_pasv(True)

def sync_dir(local_dir, remote_prefix=''):
    for item in os.listdir(local_dir):
        local_path = os.path.join(local_dir, item)
        if os.path.isdir(local_path):
            ftp.cwd('/')
            # Create remote path
            rel_dir = remote_prefix + item
            for part in rel_dir.split('/'):
                try:
                    ftp.mkd(part)
                except:
                    pass
                ftp.cwd(part)
            sync_dir(local_path, rel_dir + '/')
        elif os.path.isfile(local_path):
            ftp.cwd('/')
            if remote_prefix:
                for part in remote_prefix.rstrip('/').split('/'):
                    ftp.cwd(part)
            with open(local_path, 'rb') as f:
                ftp.storbinary(f'STOR {item}', f)
            print(f"✓ Synced: {remote_prefix}{item}")

sync_dir(DIST_DIR)
ftp.quit()
print("🎉 Full recursive sync completed!")
