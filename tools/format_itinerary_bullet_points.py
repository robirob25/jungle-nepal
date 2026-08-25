import glob, re

tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/tours/*.astro')

def clean_and_format_itinerary(match):
    content = match.group(1)
    
    # Split content by bullets '•', '*', '-' or sentences
    # First normalize bullet characters
    raw_text = content.replace('&bull;', '•')
    
    # Extract items
    if '•' in raw_text:
        items = [x.strip() for x in raw_text.split('•') if x.strip()]
    elif '<p>' in raw_text:
        # Extract text inside p tags
        items = re.findall(r'<p[^>]*>(.*?)</p>', raw_text, re.DOTALL)
        if len(items) == 1 and '•' in items[0]:
            items = [x.strip() for x in items[0].split('•') if x.strip()]
        else:
            items = [x.strip() for x in items if x.strip()]
    else:
        items = [x.strip() for x in raw_text.split('\n') if x.strip()]

    if not items:
        return match.group(0)

    # Build clean modern unordered list with custom green/slate bullet icons
    ul_html = '<ul class="pt-3 space-y-2 text-slate-700 text-xs sm:text-sm font-normal leading-relaxed">\n'
    for it in items:
        # Clean text
        it_clean = re.sub(r'^[•\-\*\s]+', '', it).strip()
        if it_clean:
            ul_html += f"""                  <li class="flex items-start gap-2.5">
                    <span class="w-1.5 h-1.5 rounded-full bg-[#0e5c3e] mt-1.5 shrink-0"></span>
                    <span>{it_clean}</span>
                  </li>\n"""
    ul_html += '                </ul>'

    return f'<div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">\n                {ul_html}\n              </div>'

pattern = r'<div class="p-4 sm:p-5 pt-0 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 font-normal">\s*(.*?)\s*</div>'

for fpath in tour_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()

    new_c = re.sub(pattern, clean_and_format_itinerary, c, flags=re.DOTALL)

    if new_c != c:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"✓ Formatted bullet points in {fpath.split('/')[-1]}")

print("Done formatting all tour itineraries into elegant, aligned vertical bullet lists!")
