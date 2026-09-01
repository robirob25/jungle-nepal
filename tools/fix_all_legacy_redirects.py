with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/.htaccess', 'r', encoding='utf-8') as f:
    c = f.read()

# Comprehensive list of old WordPress URLs to redirect to the new pages
legacy_redirects = """# 301 REDIRECTS (Legacy WordPress Slugs Preservation)
Redirect 301 /agence-de-safaris-au-nepal/ /a-propos
Redirect 301 /agence-de-safaris-au-nepal /a-propos
Redirect 301 /nos-aventures/ /#prochains-departs
Redirect 301 /nos-aventures /#prochains-departs
Redirect 301 /nos-destinations/ /destinations
Redirect 301 /nos-destinations /destinations
Redirect 301 /safaris/ /tours/jungle-extreme
Redirect 301 /safaris /tours/jungle-extreme
Redirect 301 /parc-national-de-bardia/ /destinations/bardia
Redirect 301 /parc-national-de-bardia /destinations/bardia
Redirect 301 /parc-national-de-chitwan/ /destinations/chitwan
Redirect 301 /parc-national-de-chitwan /destinations/chitwan
Redirect 301 /parc-national-de-suklaphanta/ /destinations/suklaphanta
Redirect 301 /parc-national-de-suklaphanta /destinations/suklaphanta
Redirect 301 /annapurnas-pokhara/ /destinations/annapurna
Redirect 301 /annapurnas-pokhara /destinations/annapurna
Redirect 301 /katmandou-vallee-des-rois/ /destinations/katmandou
Redirect 301 /katmandou-vallee-des-rois /destinations/katmandou
Redirect 301 /contact-us/ /contact
Redirect 301 /contact-us /contact
Redirect 301 /about-us/ /a-propos
Redirect 301 /about-us /a-propos
Redirect 301 /about/ /a-propos
Redirect 301 /about /a-propos
Redirect 301 /notre-histoire/ /a-propos
Redirect 301 /notre-histoire /a-propos
"""

import re
c = re.sub(r'# 301 REDIRECTS \(Legacy WordPress Slugs Preservation\).*', legacy_redirects, c, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/public/.htaccess', 'w', encoding='utf-8') as f:
    f.write(c)
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/dist/.htaccess', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Updated .htaccess with all legacy WordPress redirects!")
