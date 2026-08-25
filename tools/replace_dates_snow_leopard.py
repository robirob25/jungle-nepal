import re

fr_box = """          <!-- Informations Flexibilité & Période (Pas de dates fixes) -->
          <div class="space-y-3 pt-2">
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
              <div class="flex items-center gap-2 text-xs font-black text-slate-900">
                <span class="w-6 h-6 rounded-lg bg-emerald-500/20 text-[#0e8354] flex items-center justify-center text-xs shrink-0">📅</span>
                <span>Départs sur-mesure & Sur demande</span>
              </div>
              <p class="text-xs text-slate-600 leading-relaxed font-normal">
                Cette expédition exclusive est organisée selon vos dates et disponibilités durant la <strong>saison hivernale optimale (Novembre à Mars)</strong>, en micro-groupe ou en formule privatisée.
              </p>
              <div class="pt-1 flex items-center gap-2">
                <span class="inline-flex items-center gap-1 text-[11px] font-extrabold text-amber-700 bg-amber-50 border border-amber-200 px-2.5 py-0.5 rounded-md">
                  ❄️ Saison idéale : Nov – Mars
                </span>
                <span class="inline-flex items-center gap-1 text-[11px] font-extrabold text-emerald-800 bg-emerald-50 border border-emerald-200 px-2.5 py-0.5 rounded-md">
                  👥 4 à 8 pers. max
                </span>
              </div>
            </div>
          </div>"""

en_box = """          <!-- Flexibility & Season Information (No fixed dates) -->
          <div class="space-y-3 pt-2">
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
              <div class="flex items-center gap-2 text-xs font-black text-slate-900">
                <span class="w-6 h-6 rounded-lg bg-emerald-500/20 text-[#0e8354] flex items-center justify-center text-xs shrink-0">📅</span>
                <span>Custom & On-Demand Departures</span>
              </div>
              <p class="text-xs text-slate-600 leading-relaxed font-normal">
                This exclusive expedition is tailored to your schedule during the <strong>optimal winter tracking season (November to March)</strong>, for private departures or small groups.
              </p>
              <div class="pt-1 flex items-center gap-2">
                <span class="inline-flex items-center gap-1 text-[11px] font-extrabold text-amber-700 bg-amber-50 border border-amber-200 px-2.5 py-0.5 rounded-md">
                  ❄️ Best Season: Nov – March
                </span>
                <span class="inline-flex items-center gap-1 text-[11px] font-extrabold text-emerald-800 bg-emerald-50 border border-emerald-200 px-2.5 py-0.5 rounded-md">
                  👥 4 to 8 pers. max
                </span>
              </div>
            </div>
          </div>"""

# 1. Update French page
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/panthere-des-neiges.astro', 'r', encoding='utf-8') as f:
    fr = f.read()

# Replace the departure selector block
fr = re.sub(
    r'<!-- Departures Selector -->\s*<div class="space-y-2\.5">.*?</div>\s*<!-- CTA Button -->',
    '<!-- Départs Sur Mesure -->\n' + fr_box + '\n\n          <!-- CTA Button -->',
    fr,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/panthere-des-neiges.astro', 'w', encoding='utf-8') as f:
    f.write(fr)

# 2. Update English page
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/tours/panthere-des-neiges.astro', 'r', encoding='utf-8') as f:
    en = f.read()

en = re.sub(
    r'<!-- Departures Selector -->\s*<div class="space-y-2\.5">.*?</div>\s*<!-- CTA Button -->',
    '<!-- Départs Sur Mesure -->\n' + en_box + '\n\n          <!-- CTA Button -->',
    en,
    flags=re.DOTALL
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/tours/panthere-des-neiges.astro', 'w', encoding='utf-8') as f:
    f.write(en)

print("Replaced fixed date radio buttons with on-demand / custom season block in FR & EN!")
