import ftplib

ftp = ftplib.FTP('213.130.145.177', timeout=30)
ftp.login('u729389952.junglenepal.com', '09010412Amrr!')

print("Default PWD:", ftp.pwd())
try:
    ftp.cwd('..')
    print("Parent PWD:", ftp.pwd())
    print("Parent items:", ftp.nlst())
except Exception as e:
    print("Cannot cd ..:", e)

ftp.quit()
