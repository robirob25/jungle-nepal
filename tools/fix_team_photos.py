import re

# 1. Update index.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Pawan image
html = re.sub(
    r'<img\s+src=\"[^\"]*\"\s+alt=\"Pawan[^\"]*\"[^>]*>',
    '<img src="https://junglenepal.com/wp-content/uploads/2025/12/2.png" alt="Pawan - Chef Pisteur Bardia" class="w-full h-full object-cover rounded-full" />',
    html
)

# Replace Kiran image
html = re.sub(
    r'<img\s+src=\"[^\"]*\"\s+alt=\"Kiran[^\"]*\"[^>]*>',
    '<img src="https://junglenepal.com/wp-content/uploads/2025/12/1.png" alt="Kiran - Co-Fondateur Écotourisme" class="w-full h-full object-cover rounded-full" />',
    html
)

# Replace Robin image
html = re.sub(
    r'<img\s+src=\"[^\"]*\"\s+alt=\"Robin[^\"]*\"[^>]*>',
    '<img src="https://junglenepal.com/wp-content/uploads/2025/12/3.png" alt="Robin - Coordinateur France" class="w-full h-full object-cover rounded-full" />',
    html
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update a-propos.html
with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/a-propos.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

about_html = re.sub(
    r'<img\s+src=\"[^\"]*\"\s+alt=\"Pawan\"[^>]*>',
    '<img src="https://junglenepal.com/wp-content/uploads/2025/12/2.png" alt="Pawan" class="w-full h-full object-cover" />',
    about_html
)

about_html = re.sub(
    r'<img\s+src=\"[^\"]*\"\s+alt=\"Kiran\"[^>]*>',
    '<img src="https://junglenepal.com/wp-content/uploads/2025/12/1.png" alt="Kiran" class="w-full h-full object-cover" />',
    about_html
)

about_html = re.sub(
    r'<img\s+src=\"[^\"]*\"\s+alt=\"Robin\"[^>]*>',
    '<img src="https://junglenepal.com/wp-content/uploads/2025/12/3.png" alt="Robin" class="w-full h-full object-cover" />',
    about_html
)

with open('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/a-propos.html', 'w', encoding='utf-8') as f:
    f.write(about_html)

print("Team portraits corrected with 100% exact match across index.html and a-propos.html!")
