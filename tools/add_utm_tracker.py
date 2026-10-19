# Enhances src/pages/tours/dashain-immersion-culturelle.astro with:
# 1. Automatic UTM detection (utm_source, utm_medium, utm_campaign)
# 2. Dynamic WhatsApp message customized if coming from Adrien's Instagram
# 3. Google Analytics GA4 custom event tracking (tracks clicks on WhatsApp & Booking Modal from Adrien's campaign)

dashain_path = 'src/pages/tours/dashain-immersion-culturelle.astro'

with open(dashain_path, 'r', encoding='utf-8') as f:
    content = f.read()

tracker_script = '''
  <!-- ADRIEN INSTAGRAM UTM & GA4 TRACKING SCRIPT -->
  <script is:inline>
    document.addEventListener('DOMContentLoaded', function() {
      var params = new URLSearchParams(window.location.search);
      var source = params.get('utm_source') || '';
      var medium = params.get('utm_medium') || '';
      var campaign = params.get('utm_campaign') || '';

      var isFromAdrien = source.toLowerCase().includes('adrien') || 
                         medium.toLowerCase().includes('adrien') || 
                         source.toLowerCase().includes('instagram');

      if (isFromAdrien) {
        // 1. Send dedicated GA4 custom event
        if (typeof gtag === 'function') {
          gtag('event', 'campaign_visit_adrien', {
            event_category: 'Influencer_Campaign',
            event_label: 'Adrien_Instagram_100k',
            utm_source: source,
            utm_medium: medium
          });
        }

        // 2. Personalize WhatsApp buttons with specialized pre-filled text
        var customWaText = encodeURIComponent("Bonjour Robin, je viens de la part d'Adrien (Instagram) pour le voyage exceptionnel Dashain 2027 à Bardia !");
        var customWaUrl = "https://wa.me/33695413227?text=" + customWaText;

        var waButtons = document.querySelectorAll('a[href*="wa.me"]');
        waButtons.forEach(function(btn) {
          btn.href = customWaUrl;
          btn.addEventListener('click', function() {
            if (typeof gtag === 'function') {
              gtag('event', 'whatsapp_click_adrien', {
                event_category: 'Lead_Conversion',
                event_label: 'Dashain_Tour_Adrien_Story'
              });
            }
          });
        });

        // 3. Track modal booking button clicks specifically from this campaign
        var bookButtons = document.querySelectorAll('button[onclick*="openTourBookingModal"]');
        bookButtons.forEach(function(btn) {
          btn.addEventListener('click', function() {
            if (typeof gtag === 'function') {
              gtag('event', 'booking_modal_adrien', {
                event_category: 'Lead_Conversion',
                event_label: 'Dashain_Booking_Modal_Opened'
              });
            }
          });
        });

        // Store campaign in sessionStorage for persistent attribution
        sessionStorage.setItem('referral_campaign', 'adrien_instagram_100k');
      }
    });
  </script>
'''

if 'ADRIEN INSTAGRAM UTM & GA4 TRACKING SCRIPT' not in content:
    # Inject before </Layout>
    content = content.replace('</Layout>', tracker_script + '\n</Layout>')
    with open(dashain_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Successfully injected Adrien Campaign Tracker & GA4 Events in dashain-immersion-culturelle.astro")
else:
    print("Already injected.")
