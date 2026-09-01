import ftplib

ftp = ftplib.FTP('213.130.145.177', timeout=30)
ftp.login('u729389952.junglenepal.com', '09010412Amrr!')

def delete_recursive(dir_name):
    try:
        ftp.cwd(dir_name)
    except:
        return
    for item in ftp.nlst():
        if item in ('.', '..'):
            continue
        try:
            ftp.delete(item)
        except Exception:
            delete_recursive(item)
    ftp.cwd('..')
    try:
        ftp.rmd(dir_name)
        print(f"✓ Removed dir: {dir_name}")
    except Exception as e:
        pass

# Delete wp-content, wp-includes, wp-admin, lscache
for d in ['wp-content', 'wp-includes', 'wp-admin']:
    print(f"Deleting legacy {d}...")
    delete_recursive(d)

ftp.quit()
print("✓ Full legacy cleanup finished!")
