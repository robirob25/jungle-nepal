import json
import re
import os

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Trustpilot in Navbar
html = re.sub(
    r'<a href=\"#avis\"[^>]*><span>Avis.*?</a>',
    '<a href="#avis" class="hover:text-amber-300 transition-colors flex items-center gap-1.5 whitespace-nowrap"><span class="flex items-center text-[#00b67a] font-black">★</span><span>Trustpilot 5.0 (19 avis)</span></a>',
    html
)

# 2. Update Trustpilot in Hero Pill
html = re.sub(
    r'<span class=\"text-slate-200 flex items-center gap-1 font-bold\">.*?</span>',
    '<span class="text-slate-200 flex items-center gap-1.5 font-bold"><span class="inline-flex items-center justify-center w-4 h-4 bg-[#00b67a] text-white text-[10px] font-black rounded-sm">★</span><span>Trustpilot 5.0 / 5 (19 avis)</span></span>',
    html
)

# 3. Update Reassurance Bar
html = re.sub(
    r'<p class=\"font-black text-2xl text-amber-700 tracking-tight\">100% Local</p>\s*<p class=\"text-xs text-slate-500 font-medium mt-1\">Retombées directes pour les villages</p>',
    '<p class="font-black text-2xl text-[#00b67a] tracking-tight flex items-center justify-center gap-1"><span class="bg-[#00b67a] text-white text-xs px-1.5 py-0.5 rounded">★</span> 5.0 / 5</p><p class="text-xs text-slate-500 font-medium mt-1">19 avis vérifiés sur Trustpilot</p>',
    html
)

# 4. Update the complete Reviews Section with authentic Trustpilot styling
trustpilot_stars_html = """
<div class="flex items-center justify-center gap-1">
  <span class="w-7 h-7 bg-[#00b67a] text-white font-black text-sm flex items-center justify-center rounded-sm shadow-sm">★</span>
  <span class="w-7 h-7 bg-[#00b67a] text-white font-black text-sm flex items-center justify-center rounded-sm shadow-sm">★</span>
  <span class="w-7 h-7 bg-[#00b67a] text-white font-black text-sm flex items-center justify-center rounded-sm shadow-sm">★</span>
  <span class="w-7 h-7 bg-[#00b67a] text-white font-black text-sm flex items-center justify-center rounded-sm shadow-sm">★</span>
  <span class="w-7 h-7 bg-[#00b67a] text-white font-black text-sm flex items-center justify-center rounded-sm shadow-sm">★</span>
</div>
"""

new_reviews_section = f"""  <!-- ========================================================================= -->
  <!-- 9. AVIS TRUSTPILOT VÉRIFIÉS (5.0/5 • 19 AVIS) -->
  <!-- ========================================================================= -->
  <section id="avis" class="py-20 sm:py-28 bg-safari-100 border-t border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white border border-slate-200 shadow-sm mb-4">
          <span class="text-[#00b67a] font-black text-sm">Trustpilot</span>
          <span class="text-slate-300">|</span>
          <div class="flex items-center gap-0.5">
            <span class="w-3.5 h-3.5 bg-[#00b67a] text-white text-[9px] font-black flex items-center justify-center rounded-[2px]">★</span>
            <span class="w-3.5 h-3.5 bg-[#00b67a] text-white text-[9px] font-black flex items-center justify-center rounded-[2px]">★</span>
            <span class="w-3.5 h-3.5 bg-[#00b67a] text-white text-[9px] font-black flex items-center justify-center rounded-[2px]">★</span>
            <span class="w-3.5 h-3.5 bg-[#00b67a] text-white text-[9px] font-black flex items-center justify-center rounded-[2px]">★</span>
            <span class="w-3.5 h-3.5 bg-[#00b67a] text-white text-[9px] font-black flex items-center justify-center rounded-[2px]">★</span>
          </div>
          <span class="font-extrabold text-xs text-slate-900">5.0 / 5</span>
        </div>

        <h2 class="font-black text-3xl sm:text-5xl text-slate-900 tracking-tight">
          Ce que disent nos voyageurs sur Trustpilot
        </h2>
        <p class="mt-3 text-base text-slate-600 font-medium">
          Note globale <strong class="text-slate-900">5.0 / 5</strong> basée sur <strong class="text-slate-900">19 avis vérifiés</strong> • 100% d'avis 5 étoiles ⭐
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- Review 1 -->
        <div class="rounded-3xl p-8 bg-white border border-slate-200/90 shadow-sm flex flex-col justify-between hover:shadow-md transition-shadow">
          <div>
            <div class="flex items-center justify-between mb-4">
              <div class="flex gap-1">
                <span class="w-5 h-5 bg-[#00b67a] text-white text-xs font-black flex items-center justify-center rounded-sm">★</span>
                <span class="w-5 h-5 bg-[#00b67a] text-white text-xs font-black flex items-center justify-center rounded-sm">★</span>
                <span class="w-5 h-5 bg-[#00b67a] text-white text-xs font-black flex items-center justify-center rounded-sm">★</span>
                <span class="w-5 h-5 bg-[#00b67a] text-white text-xs font-black flex items-center justify-center rounded-sm">★</span>
                <span class="w-5 h-5 bg-[#00b67a] text-white text-xs font-black flex items-center justify-center rounded-sm">★</span>
              </div>
              <span class="text-[11px] font-bold text-slate-400">Vérifié Trustpilot ✓</span>
            </div>
            <h4 class="font-black text-base text-slate-950 mb-2">Une aventure gravée à vie dans la jungle !</h4>
            <p class="text-slate-700 text-sm leading-relaxed italic font-medium">
              « Choisir Jungle Nepal Adventure pour découvrir ce pays sous l'angle de sa vie sauvage, c'est la meilleure décision. Voir des tigres et des rhinos en liberté avec Pawan est un moment absolument magique ! »
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-jungle-950 text-amber-300 font-bold flex items-center justify-center text-sm shadow">SG</div>
            <div>
              <p class="font-bold text-sm text-slate-900">Samantha Gonthier</p>
              <p class="text-xs text-slate-500">Expédition Bardia Sauvage</p>
            </div>
          </div>
        </div>

        <!-- Review 2 -->
        <div class="rounded-3xl p-8 bg-white border border-slate-200/90 shadow-sm flex flex-col justify-between hover:shadow-md transition-shadow">
          <div>
            <div class="flex items-center justify-between mb-4">
              <div class="flex gap-1">
                <span class="w-5 h-5 bg-[#00b67a] text-white text-xs font-black flex items-center justify-center rounded-sm">★</span>
                <span class="w-5 h-5 bg-[#00b67a] text-white text-xs font-black flex items-center justify-center rounded-sm">★</span>
                <span class="w-5 h-5 bg-[#00b67a] text-white text-xs font-black flex items-center justify-center rounded-sm">★</span>
                <span class="w-5 h-5 bg-[#00b67a] text-white text-xs font-black flex items-center justify-center rounded-sm">★</span>
                <span class="w-5 h-5 bg-[#00b67a] text-white text-xs font-black flex items-center justify-center rounded-sm">★</span>
              </div>
              <span class="text-[11px] font-bold text-slate-400">Vérifié Trustpilot ✓</span>
            </div>
            <h4 class="font-black text-base text-slate-950 mb-2">L'humain et l'authenticité avant tout</h4>
            <p class="text-slate-700 text-sm leading-relaxed italic font-medium">
              « Je reviens de 15 jours au Népal... ce que je retiens avant tout, c'est l'humain. Une équipe sincère, passionnée et dévouée. On ne se sent jamais comme un simple client. Une expérience rare ! »
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-[#0e8354] text-white font-bold flex items-center justify-center text-sm shadow">AN</div>
            <div>
              <p class="font-bold text-sm text-slate-900">Adrien Noat</p>
              <p class="text-xs text-slate-500">Circuit Népal Sauvage 15 jours</p>
            </div>
          </div>
        </div>

        <!-- Review 3 -->
        <div class="rounded-3xl p-8 bg-white border border-slate-200/90 shadow-sm flex flex-col justify-between hover:shadow-md transition-shadow">
          <div>
            <div class="flex items-center justify-between mb-4">
              <div class="flex gap-1">
                <span class="w-5 h-5 bg-[#00b67a] text-white text-xs font-black flex items-center justify-center rounded-sm">★</span>
                <span class="w-5 h-5 bg-[#00b67a] text-white text-xs font-black flex items-center justify-center rounded-sm">★</span>
                <span class="w-5 h-5 bg-[#00b67a] text-white text-xs font-black flex items-center justify-center rounded-sm">★</span>
                <span class="w-5 h-5 bg-[#00b67a] text-white text-xs font-black flex items-center justify-center rounded-sm">★</span>
                <span class="w-5 h-5 bg-[#00b67a] text-white text-xs font-black flex items-center justify-center rounded-sm">★</span>
              </div>
              <span class="text-[11px] font-bold text-slate-400">Vérifié Trustpilot ✓</span>
            </div>
            <h4 class="font-black text-base text-slate-950 mb-2">Immersion en village et respect des animaux</h4>
            <p class="text-slate-700 text-sm leading-relaxed italic font-medium">
              « Un voyage exceptionnel. Séjourner chez l'habitant au milieu de la jungle de Bardia et bivouaquer dans la vallée secrète de Babai est une expérience hors du commun. Merci à Robin et Pawan ! »
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-slate-100 flex items-center gap-3">
            <div class="w-10 h-10 rounded-full bg-emerald-800 text-white font-bold flex items-center justify-center text-sm shadow">AP</div>
            <div>
              <p class="font-bold text-sm text-slate-900">Alice Palasti</p>
              <p class="text-xs text-slate-500">Immersion Tharu & Bivouac Babai</p>
            </div>
          </div>
        </div>

      </div>

      <!-- Trustpilot Footer Badge -->
      <div class="mt-12 text-center">
        <a href="https://wa.me/33695413227?text=Bonjour%20Robin%2C%20je%20souhaite%20des%20renseignements%20sur%20vos%20séjours" target="_blank" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-white border border-slate-200 shadow-sm hover:shadow text-xs font-extrabold text-slate-800 hover:text-[#0e8354] transition-all">
          <span class="w-2 h-2 rounded-full bg-[#00b67a]"></span>
          <span>Consulter tous les 19 avis vérifiés sur Trustpilot (5.0 / 5.0)</span>
          <i data-lucide="arrow-up-right" class="w-4 h-4"></i>
        </a>
      </div>

    </div>
  </section>"""

# Replace the reviews section in html
pattern = r'<!-- ========================================================================= -->\s*<!-- 9\. AVIS CLIENTS -->.*?<!-- ========================================================================= -->\s*<!-- 10\. FOOTER -->'
html = re.sub(pattern, new_reviews_section + "\n\n  <!-- ========================================================================= -->\n  <!-- 10. FOOTER -->", html, flags=re.DOTALL)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 5. Update all 14 Tour Pages with Trustpilot 5.0 and 19 reviews
tours_dir = '/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/tours'
for fname in os.listdir(tours_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(tours_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Update top badge in tour
    c = re.sub(
        r'<div class=\"inline-flex items-center gap-1\.5 bg-emerald-50 text-emerald-900 font-extrabold px-3 py-1 rounded-full border border-emerald-200\">.*?</div>',
        '<div class="inline-flex items-center gap-1.5 bg-emerald-50 text-emerald-950 font-extrabold px-3 py-1 rounded-full border border-emerald-200"><span class="w-3.5 h-3.5 bg-[#00b67a] text-white text-[9px] font-black flex items-center justify-center rounded-[2px]">★</span><span>5.0 / 5 (19 avis Trustpilot)</span></div>',
        c
    )

    # Update Tour Reviews Section
    c = re.sub(
        r'Note globale <strong>.*?</strong> sur Google Reviews \(.*? avis vérifiés\)',
        'Note globale <strong class="text-slate-900">5.0 / 5</strong> sur <strong class="text-[#00b67a]">Trustpilot</strong> (19 avis 100% vérifiés)',
        c
    )
    c = re.sub(r'Google Reviews', 'Trustpilot', c)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Applied Trustpilot 5.0 / 5 (19 reviews) across all pages successfully!")
