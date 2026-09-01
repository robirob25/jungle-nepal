import ftplib

ftp = ftplib.FTP('213.130.145.177', timeout=30)
ftp.login('u729389952.junglenepal.com', '09010412Amrr!')

print("PWD:", ftp.pwd())
root_items = ftp.nlst()
print("Root NLST:", root_items)

# Check if there is another directory or if public_html is inside
if 'domains' in root_items:
    print("Found 'domains' directory! Listing domains:")
    ftp.cwd('domains')
    print(ftp.nlst())
    for d in ftp.nlst():
        if 'junglenepal' in d:
            ftp.cwd(d)
            print(f"Inside domains/{d}:", ftp.nlst())
            if 'public_html' in ftp.nlst():
                ftp.cwd('public_html')
                print(f"Inside domains/{d}/public_html:", ftp.nlst()[:10])

ftp.quit()
