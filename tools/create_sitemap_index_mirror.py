import shutil

# Copy sitemap.xml to sitemap_index.xml as well for compatibility with legacy WordPress/Yoast expectations
shutil.copy('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/sitemap.xml', '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/sitemap_index.xml')
shutil.copy('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist/sitemap.xml', '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist/sitemap_index.xml')

import ftplib
ftp = ftplib.FTP('213.130.145.177', timeout=30)
ftp.login('u729389952.junglenepal.com', '09010412Amrr!')
ftp.cwd('/public_html')
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist/sitemap_index.xml', 'rb') as fp:
    ftp.storbinary('STOR sitemap_index.xml', fp)
ftp.quit()

print("✓ Created and uploaded sitemap_index.xml to Hostinger!")
