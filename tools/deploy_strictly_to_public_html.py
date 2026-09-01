import ftplib, os

FTP_HOST = '213.130.145.177'
FTP_USER = 'u729389952.junglenepal.com'
FTP_PASS = '09010412Amrr!'
DIST_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

ftp = ftplib.FTP(FTP_HOST, timeout=60)
ftp.login(FTP_USER, FTP_PASS)
ftp.set_pasv(True)

# Always go into /public_html
ftp.cwd('/public_html')
print("Active deploy directory:", ftp.pwd())

# Clean any rogue php files in public_html
for item in ftp.nlst():
    if item.endswith('.php') or item.endswith('.bk') or item.endswith('.bk_old') or 'old_backup' in item:
        try:
            ftp.delete(item)
            print(f"Deleted rogue file: {item}")
        except Exception:
            pass

def upload_recursive(local_path, remote_prefix=''):
    for item in os.listdir(local_path):
        local_item = os.path.join(local_path, item)
        if os.path.isdir(local_item):
            try:
                ftp.mkd(item)
            except:
                pass
            ftp.cwd(item)
            upload_recursive(local_item, remote_prefix + item + '/')
            ftp.cwd('..')
        elif os.path.isfile(local_item):
            with open(local_item, 'rb') as f:
                ftp.storbinary(f'STOR {item}', f)
            print(f"✓ Uploaded to /public_html/{remote_prefix}{item}")

print("Uploading entire distribution directly into /public_html...")
upload_recursive(DIST_DIR)

ftp.quit()
print("🎉 Clean deployment directly into /public_html complete!")
