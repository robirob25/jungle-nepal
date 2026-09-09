import ftplib, os

ftp = ftplib.FTP('213.130.145.177', timeout=60)
ftp.login('u729389952.junglenepal.com', '09010412Amrr!')
ftp.set_pasv(True)

DIST_DIR = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist'

# 1. Sync entire _astro directory (All CSS and JS bundles)
astro_dir = os.path.join(DIST_DIR, '_astro')
if os.path.exists(astro_dir):
    ftp.cwd('/public_html')
    try:
        ftp.mkd('_astro')
    except:
        pass
    ftp.cwd('_astro')
    for f in os.listdir(astro_dir):
        fp = os.path.join(astro_dir, f)
        if os.path.isfile(fp):
            with open(fp, 'rb') as file_obj:
                ftp.storbinary(f'STOR {f}', file_obj)
            print(f"✓ Uploaded CSS/JS bundle: _astro/{f}")

ftp.quit()
print("🎉 All _astro CSS & JS bundles uploaded!")
