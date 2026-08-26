with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    c = f.read()

old_durations = """              <select id="custom-duration" class="w-full p-3 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all cursor-pointer">
                <option value="5 à 7 jours (Court séjour intensif)">5 à 7 jours (Court séjour intensif)</option>
                <option value="8 à 12 jours (Safari complet)" selected>8 à 12 jours (Safari complet)</option>
                <option value="14 à 18 jours (Grand tour immersion)">14 à 18 jours (Grand tour immersion)</option>
                <option value="3 semaines ou plus">3 semaines ou plus</option>
              </select>"""

new_durations = """              <select id="custom-duration" class="w-full p-3 rounded-2xl border border-slate-200 bg-slate-50/50 font-medium focus:bg-white focus:ring-2 focus:ring-[#0e8354] focus:outline-none transition-all cursor-pointer">
                <option value="- de 3 jours">- de 3 jours</option>
                <option value="3 à 5 jours">3 à 5 jours</option>
                <option value="5 à 7 jours">5 à 7 jours</option>
                <option value="8 à 12 jours" selected>8 à 12 jours</option>
                <option value="14 à 18 jours">14 à 18 jours</option>
                <option value="3 semaines ou plus">3 semaines ou plus</option>
              </select>"""

c = c.replace(old_durations, new_durations)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(c)

print("✓ Updated duration options in custom trip modal in Layout.astro!")
