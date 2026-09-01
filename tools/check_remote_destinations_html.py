import ftplib

ftp = ftplib.FTP('213.130.145.177', timeout=30)
ftp.login('u729389952.junglenepal.com', '09010412Amrr!')
ftp.cwd('/public_html')

# Check destinations.html and destinations/index.html on the server
import io
buf = io.BytesIO()
ftp.retrbinary('RETR destinations.html', buf.write)
c1 = buf.getvalue().decode('utf-8')
print("destinations.html has 'Nos guides':", 'Nos guides' in c1)
print("destinations.html has 'Galerie':", 'Galerie' in c1)

buf2 = io.BytesIO()
try:
    ftp.cwd('destinations')
    ftp.retrbinary('RETR index.html', buf2.write)
    c2 = buf2.getvalue().decode('utf-8')
    print("destinations/index.html has 'Nos guides':", 'Nos guides' in c2)
    print("destinations/index.html has 'Galerie':", 'Galerie' in c2)
except Exception as e:
    print("destinations/index.html check:", e)

ftp.quit()
