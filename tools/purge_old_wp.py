import ftplib

ftp = ftplib.FTP('213.130.145.177', timeout=30)
ftp.login('u729389952.junglenepal.com', '09010412Amrr!')

# List of obsolete WordPress root files that trigger LiteSpeed/CDN cache
wp_files = [
    'wp-config.php', 'wp-settings.php', 'wp-login.php', 'xmlrpc.php', 
    'default.php', 'wp-cron.php', 'wp-load.php', 'wp-activate.php',
    'wp-mail.php', 'wp-signup.php', 'wp-links-opml.php', 'wp-trackback.php'
]

for wf in wp_files:
    try:
        ftp.delete(wf)
        print(f"✓ Deleted legacy WP file: {wf}")
    except Exception as e:
        pass

ftp.quit()
print("✓ WP cleanup finished!")
