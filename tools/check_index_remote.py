import ftplib

ftp = ftplib.FTP('213.130.145.177', timeout=30)
ftp.login('u729389952.junglenepal.com', '09010412Amrr!')
ftp.cwd('public_html')
files = ftp.nlst()
print("Files in public_html:", [f for f in files if 'index' in f or 'wp-' in f][:15])
ftp.quit()
