import ftplib

ftp = ftplib.FTP('213.130.145.177', timeout=30)
ftp.login('u729389952.junglenepal.com', '09010412Amrr!')

for folder in ['wp-content', 'wp-includes', 'wp-admin']:
    try:
        ftp.rename(folder, folder + '_old_backup')
        print(f"✓ Renamed {folder} to {folder}_old_backup")
    except Exception as e:
        print(f"{folder}: {e}")

ftp.quit()
print("✓ Finished isolating old WordPress folders!")
