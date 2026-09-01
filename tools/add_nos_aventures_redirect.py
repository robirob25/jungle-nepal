with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/.htaccess', 'r', encoding='utf-8') as f:
    c = f.read()

# Add 301 redirects for legacy URLs like /nos-aventures, /nos-aventures/, /nos-destinations, etc.
redirects = """# 7. 301 REDIRECTS (Legacy WordPress Slugs Preservation)
Redirect 301 /nos-aventures/ /#prochains-departs
Redirect 301 /nos-aventures /#prochains-departs
Redirect 301 /nos-destinations/ /destinations
Redirect 301 /nos-destinations /destinations
"""

c = c.replace('# 7. 301 REDIRECTS (Legacy WordPress Slugs Preservation)\n', redirects)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/.htaccess', 'w', encoding='utf-8') as f:
    f.write(c)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist/.htaccess', 'w', encoding='utf-8') as f:
    f.write(c)

# Upload updated .htaccess immediately to Hostinger
import ftplib
ftp = ftplib.FTP('213.130.145.177', timeout=30)
ftp.login('u729389952.junglenepal.com', '09010412Amrr!')
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist/.htaccess', 'rb') as fp:
    ftp.storbinary('STOR .htaccess', fp)
ftp.quit()

print("✓ Updated .htaccess on Hostinger with /nos-aventures redirect!")
