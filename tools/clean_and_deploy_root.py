import ftplib, os, time

FTP_HOST = '213.130.145.177'
FTP_USER = 'u729389952.junglenepal.com'
FTP_PASS = '09010412Amrr!'
DIST_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

ftp = ftplib.FTP(FTP_HOST, timeout=60)
ftp.login(FTP_USER, FTP_PASS)
ftp.set_pasv(True)

print("PWD:", ftp.pwd())

# Clean old WordPress index.php if exists
try:
    ftp.delete('index.php')
    print("✓ Removed old index.php")
except Exception as e:
    print("index.php delete:", e)

# Upload .htaccess & all root files directly
for f in os.listdir(DIST_DIR):
    local_f = os.path.join(DIST_DIR, f)
    if os.path.isfile(local_f):
        with open(local_f, 'rb') as fp:
            ftp.storbinary(f'STOR {f}', fp)
        print(f"✓ Uploaded root file: {f}")

ftp.quit()
print("✓ Root synchronization complete!")
