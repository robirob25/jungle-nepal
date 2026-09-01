import ftplib

ftp = ftplib.FTP('213.130.145.177', timeout=30)
ftp.login('u729389952.junglenepal.com', '09010412Amrr!')

print("=== FTP ROOT LISTING ===")
ftp.cwd('/')
print("PWD:", ftp.pwd())
for item in ftp.nlst():
    print(" -", item)

# Check if there are other directories
try:
    ftp.cwd('/public_html')
    print("\n=== /public_html LISTING ===")
    for item in ftp.nlst():
        print(" -", item)
except Exception as e:
    print("Error in /public_html:", e)

ftp.quit()
