import os, glob, re

en_tour_files = glob.glob('/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/src/pages/en/tours/*.astro')

replacements = [
    ('Ce voyage est-il fait pour moi ?', 'Is this trip right for you?'),
    ('Ce voyage est-il fait pour moi', 'Is this trip right for you'),
    ('Profil Voyage', 'Trip Profile'),
    ('Les temps forts du voyage', 'Trip Highlights'),
    ('Les temps forts', 'Trip Highlights'),
    ('Itinéraire détaillé', 'Detailed Itinerary'),
    ('Itinéraire Jour par Jour', 'Day-by-Day Itinerary'),
    ('Programme jour par jour encadré par nos pisteurs natifs de Bardia et guides d’expédition.', 'Day-by-day itinerary led by our native master trackers and certified expedition guides.'),
    ('Programme jour par jour encadré par nos pisteurs natifs de Bardia et guides d\'expédition.', 'Day-by-day itinerary led by our native master trackers and certified expedition guides.'),
    ('Tout déplier / replier', 'Expand all / Collapse'),
    ('Ce qui est inclus dans votre séjour', 'What is included in your expedition'),
    ('Inclus dans le tarif', 'Included in the rate'),
    ('Non inclus', 'Not included'),
    ('Vos questions fréquentes', 'Frequently Asked Questions'),
    ('Avis voyageurs vérifiés', 'Verified Explorer Reviews'),
    ('Vous pourriez aussi aimer ces expéditions', 'You might also love these expeditions'),
    ('Poursuivre l\'exploration', 'Continue Exploring'),
    ('Partager ce séjour', 'Share this trip'),
    ('Copier le lien direct', 'Copy direct link'),
    ('Envoyer sur WhatsApp', 'Send via WhatsApp'),
    ('Partager par Email', 'Share via Email'),
    ('Tous les 15 séjours', 'All 15 Expeditions'),
    ('Tous les 14 séjours', 'All 15 Expeditions'),
    ('Nos 15 Séjours', 'All 15 Expeditions'),
    ('Nos 14 Séjours', 'All 15 Expeditions'),
    ('Inclus & Extras', 'Inclusions & Extras'),
    ('À propos', 'About us'),
    ('Départs & Prix', 'Departures & Rates'),
    ('Faune & Pistage', 'Wildlife & Tracking'),
    ('Nature & Aventure', 'Nature & Adventure'),
    ('Culture & Vie locale', 'Culture & Local Life'),
    ('Relax & Contemplation', 'Relaxation & Scenery'),
    ('Soirées & Fête', 'Evenings & Social'),
    ('Rythme & Effort :', 'Pace & Effort:'),
    ('Rythme & Effort', 'Pace & Effort'),
    ('À PARTIR DE', 'STARTING FROM'),
    ('À partir de', 'Starting from'),
    ('À PARTIR DE :', 'STARTING FROM:'),
    ('SÉLECTIONNEZ VOTRE DÉPART :', 'SELECT YOUR DEPARTURE DATE:'),
    ('Sélectionnez votre départ :', 'Select your departure date:'),
    ('Sélectionnez votre départ', 'Select your departure date'),
    ('Réserver ma place →', 'Reserve your spot →'),
    ('Réserver ma place', 'Reserve your spot'),
    ('places restantes', 'spots left'),
    ('places disponibles', 'spots available'),
    ('Dernières places', 'Last spots'),
    ('Confirmé', 'Guaranteed'),
    ('Saison tigres', 'Tiger season'),
    ('Acompte de 30% seulement à l\'inscription', 'Only 30% deposit at registration'),
    ('Annulation flexible jusqu\'à 30 jours', 'Flexible cancellation up to 30 days'),
    ('Paiement sécurisé en plusieurs fois sans frais', 'Secure fee-free installment payments'),
    ('Un conseiller d\'expédition dédié vous accompagne', 'Dedicated expedition specialist to assist you'),
    ('Une question sur ce séjour ?', 'Have questions about this expedition?'),
    ('Échangez directement avec Robin sur WhatsApp pour affiner votre projet :', 'Chat directly with Robin on WhatsApp to customize your project:'),
    ('Discuter sur WhatsApp', 'Chat on WhatsApp'),
    ('Voir toutes les photos', 'View all photos'),
    ('Voir les 15 séjours →', 'View all 15 expeditions →'),
    ('Voir les 14 séjours →', 'View all 15 expeditions →'),
    ('Toutes les inclusions', 'All inclusions'),
    ('Questions fréquentes', 'FAQ')
]

for p in en_tour_files:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()

    # Apply all general replacements
    for fr_text, en_text in replacements:
        c = c.replace(fr_text, en_text)

    # Translate Day labels like "Jour 1", "Jour 2", etc.
    c = re.sub(r'\bJour\s+(\d+)\b', r'Day \1', c)
    c = re.sub(r'\bJours\s+(\d+)\b', r'Days \1', c)

    # Translate "4 jours", "5 jours", "15 jours", etc. in headers/badges
    c = re.sub(r'\((\d+)\s*jours\)', r'(\1 Days)', c)
    c = re.sub(r'\((\d+)\s*j\)', r'(\1 Days)', c)
    c = re.sub(r'(\d+)\s*jours', r'\1 days', c)

    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)

print(f"Successfully translated template and section headers across all {len(en_tour_files)} English tour pages!")
