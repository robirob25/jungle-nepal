import urllib.request, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls_to_test = [
    'https://junglenepal.com/',
    'https://junglenepal.com/a-propos',
    'https://junglenepal.com/destinations',
    'https://junglenepal.com/contact',
    'https://junglenepal.com/destinations/bardia',
    'https://junglenepal.com/destinations/chitwan',
    'https://junglenepal.com/destinations/suklaphanta',
    'https://junglenepal.com/destinations/annapurna',
    'https://junglenepal.com/destinations/katmandou',
    'https://junglenepal.com/tours/jungle-extreme',
    'https://junglenepal.com/tours/bardia-nuit-sauvage',
    'https://junglenepal.com/tours/panthere-des-neiges',
    'https://junglenepal.com/sitemap.xml',
    'https://junglenepal.com/robots.txt',
    'https://junglenepal.com/assets/img_3.webp',
    'https://junglenepal.com/assets/pawan_webp.webp',
    'https://junglenepal.com/assets/kiran_webp.webp'
]

print("=== FINAL LIVE HEALTH CHECK ===")
all_good = True
for u in urls_to_test:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 HealthCheck'})
        resp = urllib.request.urlopen(req, context=ctx, timeout=10)
        status = resp.getcode()
        if status == 200:
            print(f"✓ {status} OK: {u}")
        else:
            print(f"⚠ {status}: {u}")
            all_good = False
    except Exception as e:
        print(f"❌ ERROR on {u}: {e}")
        all_good = False

if all_good:
    print("\n🎉 ALL 17 CHECKPOINTS PASSED WITH 200 OK STATUS!")
