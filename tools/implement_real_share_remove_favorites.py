import os
import re

# 1. Update index.html: Remove all heart favorite buttons
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern for heart buttons
heart_btn_pattern = r'<button\s+onclick=[\"\']event\.preventDefault\(\);\s*this\.classList\.toggle\(\'text-rose-500\'\);[^>]*aria-label=[\"\']Favoris[\"\']>.*?</button>'
html = re.sub(heart_btn_pattern, '', html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("1. Removed all favorite heart buttons from index.html!")

# 2. Design the Share Component for tours/*.html
share_component_html = """      <!-- BOUTON PARTAGER INTERACTIF -->
      <div class="relative">
        <button id="share-btn" onclick="handleShareTour()" class="flex items-center gap-2 px-4 py-2 rounded-xl border border-slate-200 bg-white text-xs font-extrabold text-slate-800 hover:text-[#0e8354] hover:border-[#0e8354] shadow-sm hover:shadow transition-all group cursor-pointer">
          <i data-lucide="share-2" class="w-4 h-4 text-slate-500 group-hover:text-[#0e8354] transition-colors"></i>
          <span>Partager ce séjour</span>
        </button>

        <!-- Dropdown Menu Partage -->
        <div id="share-menu" class="absolute right-0 top-full mt-2 w-64 bg-white/98 backdrop-blur-xl border border-slate-200 rounded-2xl p-2 shadow-2xl opacity-0 translate-y-2 pointer-events-none transition-all duration-200 z-50 space-y-1">
          <button onclick="copyTourLink()" class="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-emerald-50 hover:text-[#0e8354] transition-colors text-left">
            <i data-lucide="link" class="w-4 h-4 text-[#0e8354]"></i>
            <span>Copier le lien direct</span>
          </button>
          <a id="share-whatsapp" href="#" target="_blank" class="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-emerald-50 hover:text-[#0e8354] transition-colors text-left">
            <i data-lucide="message-circle" class="w-4 h-4 text-[#109363]"></i>
            <span>Envoyer sur WhatsApp</span>
          </a>
          <a id="share-email" href="#" class="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-bold text-slate-700 hover:bg-emerald-50 hover:text-[#0e8354] transition-colors text-left">
            <i data-lucide="mail" class="w-4 h-4 text-slate-600"></i>
            <span>Partager par Email</span>
          </a>
        </div>
      </div>"""

share_js_functions = """
    // REAL SHARE FUNCTIONALITY & TOAST NOTIFICATION
    function handleShareTour() {
      const pageUrl = window.location.href;
      const pageTitle = document.title || 'Séjour Jungle Nepal Adventure';
      
      // Update whatsapp & email links
      const waLink = document.getElementById('share-whatsapp');
      if (waLink) {
        waLink.href = `https://api.whatsapp.com/send?text=${encodeURIComponent('Découvre ce séjour au Népal : ' + pageTitle + ' ' + pageUrl)}`;
      }
      const emailLink = document.getElementById('share-email');
      if (emailLink) {
        emailLink.href = `mailto:?subject=${encodeURIComponent(pageTitle)}&body=${encodeURIComponent('Je voulais te partager ce séjour au Népal avec Jungle Nepal Adventure : ' + pageUrl)}`;
      }

      // Try native web share on mobile
      if (navigator.share && /mobile|android|iphone|ipad/i.test(navigator.userAgent)) {
        navigator.share({
          title: pageTitle,
          text: 'Découvre ce séjour d\'immersion au Népal avec Jungle Nepal Adventure',
          url: pageUrl
        }).catch(() => {});
        return;
      }

      // Toggle dropdown on desktop
      const menu = document.getElementById('share-menu');
      if (menu) {
        const isOpen = menu.classList.contains('opacity-100');
        if (isOpen) {
          menu.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
          menu.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
        } else {
          menu.classList.remove('opacity-0', 'translate-y-2', 'pointer-events-none');
          menu.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
        }
      }
    }

    function copyTourLink() {
      const pageUrl = window.location.href;
      navigator.clipboard.writeText(pageUrl).then(() => {
        showToast('✅ Lien du séjour copié dans le presse-papier !');
        const menu = document.getElementById('share-menu');
        if (menu) {
          menu.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
          menu.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
        }
      }).catch(() => {
        showToast('Lien : ' + pageUrl);
      });
    }

    function showToast(msg) {
      let toast = document.getElementById('toast-notification');
      if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toast-notification';
        toast.className = 'fixed bottom-8 left-1/2 -translate-x-1/2 bg-slate-950/95 backdrop-blur-xl text-white text-xs sm:text-sm font-black px-5 py-3 rounded-full border border-white/20 shadow-[0_20px_50px_rgba(0,0,0,0.4)] transition-all duration-300 z-50 opacity-0 translate-y-4 pointer-events-none flex items-center gap-2';
        document.body.appendChild(toast);
      }
      toast.innerHTML = `<span class="text-amber-300 font-bold">✨</span> <span>${msg}</span>`;
      toast.classList.remove('opacity-0', 'translate-y-4', 'pointer-events-none');
      toast.classList.add('opacity-100', 'translate-y-0', 'pointer-events-auto');
      
      setTimeout(() => {
        toast.classList.add('opacity-0', 'translate-y-4', 'pointer-events-none');
        toast.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }, 2800);
    }

    // Close share menu on outside click
    document.addEventListener('click', (e) => {
      const btn = document.getElementById('share-btn');
      const menu = document.getElementById('share-menu');
      if (menu && btn && !btn.contains(e.target) && !menu.contains(e.target)) {
        menu.classList.add('opacity-0', 'translate-y-2', 'pointer-events-none');
        menu.classList.remove('opacity-100', 'translate-y-0', 'pointer-events-auto');
      }
    });
"""

# 3. Update all 14 tours in tours/*.html
tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Replace the old Partager/Favoris buttons container
    old_buttons_pattern = r'<div class=\"flex items-center gap-2\">\s*<button onclick=\"navigator\.clipboard\.writeText.*?<span>Partager</span>\s*</button>\s*<button onclick=\"this\.classList\.toggle\(\'text-rose-500\'\).*?<span>Favoris</span>\s*</button>\s*</div>'
    c = re.sub(old_buttons_pattern, share_component_html, c, flags=re.DOTALL)

    # Insert the real share functions into JS
    if 'function handleShareTour' not in c:
        c = c.replace('</script>\n\n</body>', share_js_functions + '\n  </script>\n\n</body>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("2. Upgraded Share system and removed favorites across all 14 tour pages!")
