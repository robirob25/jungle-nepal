import os
import re
import glob

def clean_tour_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    is_en = '/en/' in filepath
    return_link = "https://junglenepal.com/en/legal-mentions/" if is_en else "https://junglenepal.com/mentions-legales/"

    # Replace dead conditions-generales link
    content = content.replace("https://junglenepal.com/conditions-generales", return_link)

    # In Schema.org, ensure country is FR for financial/cancellation policy with French operator
    content = re.sub(r'"applicableCountry":\s*"NP"', '"applicableCountry": "FR"', content)
    content = re.sub(r'"returnPolicyCountry":\s*"NP"', '"returnPolicyCountry": "FR"', content)

    # Remove returnMethod ReturnByMail if present
    content = re.sub(r'\s*"returnMethod":\s*"https://schema.org/ReturnByMail",?', '', content)

    # Remove shippingDetails block from offers if present
    # regex matches "shippingDetails": { ... },
    shipping_pattern = re.compile(
        r'\s*"shippingDetails":\s*\{\s*"@type":\s*"OfferShippingDetails".*?\}\s*\},',
        re.DOTALL
    )
    content = shipping_pattern.sub('', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

tour_files = glob.glob('src/pages/tours/*.astro') + glob.glob('src/pages/en/tours/*.astro')
for tf in tour_files:
    clean_tour_file(tf)

print(f"Cleaned {len(tour_files)} tour files successfully.")
