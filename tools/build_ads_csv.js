import fs from 'fs';
import path from 'path';

// Character validation helpers
function checkLen(str, max, label) {
  if (str.length > max) {
    throw new Error(`[OVER LIMIT] "${str}" has ${str.length} chars (max: ${max}) in ${label}`);
  }
}

// 1. DATA DEFINITION

const CAMPAIGN_FR = "FR_SNIPER_BARDIA_SAFARI";
const CAMPAIGN_EN = "EN_SNIPER_BARDIA_SAFARI";

const groups = [
  // ==========================================
  // GROUPE 1 FR: BARDIA LOCAL DMC
  // ==========================================
  {
    campaign: CAMPAIGN_FR,
    budget: "6.50",
    lang: "fr",
    location: "France;Switzerland;Belgium",
    adGroup: "1_Bardia_Local_DMC",
    cpc: "1.20",
    status: "Enabled",
    finalUrl: "https://junglenepal.com/destinations/bardia/",
    path1: "Bardia",
    path2: "Safari",
    keywords: [
      { text: "safari bardia", type: "Exact" },
      { text: "parc national de bardia", type: "Exact" },
      { text: "visiter le parc de bardia", type: "Phrase" },
      { text: "agence locale bardia népal", type: "Phrase" },
      { text: "guide francophone bardia", type: "Phrase" },
      { text: "bardia népal safari", type: "Phrase" },
      { text: "parc bardia agence locale", type: "Phrase" },
      { text: "séjour parc bardia", type: "Phrase" }
    ],
    headlines: [
      "Parc National de Bardia",       // 23
      "Agence Locale au Népal",       // 22
      "Pisteurs Tharu Natifs",        // 21
      "Safaris Bardia en Direct",     // 24
      "Loin du Tourisme de Masse",    // 25
      "Micro-Groupes de 4 à 10",      // 23
      "Pistage du Tigre à Pied",      // 23
      "Circuit Bardia sur Mesure",    // 25
      "Écolodges Authentiques",       // 22
      "Fondateur Francophone",        // 21
      "0% Éléphant • 100% Éthique",   // 26
      "Bardia Sauvage et Préservé",   // 26
      "Devis Gratuit en 24h",         // 20
      "Séjours dès 490 € au Sol",     // 24
      "Contact Direct sur WhatsApp"   // 27
    ],
    descriptions: [
      "Agence réceptive locale spécialiste de Bardia. Safaris à pied avec maîtres pisteurs Tharu.", // 89
      "Vivez le Népal sauvage en micro-groupe de 4 à 10 pers. Écotourisme 100% éthique à Bardia.", // 89
      "Pistez le tigre du Bengale en liberté loin de la foule. Échangez avec Robin sur WhatsApp.", // 89
      "Circuits sur-mesure ou départs garantis. Hébergement en lodge de charme et guides locaux."  // 89
    ]
  },

  // ==========================================
  // GROUPE 2 FR: SAFARI TIGRE ÉTHIQUE
  // ==========================================
  {
    campaign: CAMPAIGN_FR,
    budget: "6.50",
    lang: "fr",
    location: "France;Switzerland;Belgium",
    adGroup: "2_Safari_Tigre_Ethique",
    cpc: "1.20",
    status: "Enabled",
    finalUrl: "https://junglenepal.com/tours/bardia-explorateur/",
    path1: "Safari",
    path2: "Tigre",
    keywords: [
      { text: "safari tigre népal", type: "Exact" },
      { text: "voir tigre du bengale népal", type: "Exact" },
      { text: "pister le tigre à pied", type: "Exact" },
      { text: "safari éthique népal", type: "Phrase" },
      { text: "observer le tigre sans éléphant", type: "Phrase" },
      { text: "bardia ou chitwan", type: "Phrase" },
      { text: "safari animalier népal", type: "Exact" },
      { text: "safari a pied népal", type: "Exact" },
      { text: "voyage tigre népal", type: "Exact" }
    ],
    headlines: [
      "Safari Tigre au Népal",        // 21
      "Pistez le Tigre à Pied",       // 22
      "Parc de Bardia Sauvage",       // 22
      "Tigre du Bengale en Liberté",  // 27
      "100% à Pied • 0% Éléphant",    // 25
      "Guides Pisteurs d'Élite",      // 23
      "Bardia vs Chitwan : Le Choix", // 28
      "Séjour 5 Jours dès 490 €",     // 24
      "Alternative Sauvage à l'Inde", // 28
      "Micro-Groupes de 4 à 10",      // 23
      "85% Chances en Saison Sèche",  // 27
      "Safari Animalier Éthique",     // 24
      "Loin des Jeeps et de la Foule",// 29
      "Agence Locale Francophone",    // 25
      "Devis Rapide sur WhatsApp"     // 25
    ],
    descriptions: [
      "Pistez le tigre du Bengale à pied à Bardia. 0% éléphant, 100% éthique et respect animal.",   // 88
      "L'alternative sauvage et silencieuse aux safaris en jeep en Inde. Pisteurs Tharu réputés.", // 89
      "Séjour 5 jours au camp de base écolodge dès 490 €. Micro-groupes de 4 à 10 voyageurs.",       // 86
      "La meilleure fenêtre de tir : février à mai. Posez vos questions en direct sur WhatsApp."     // 88
    ]
  },

  // ==========================================
  // GROUPE 3 FR: VOYAGE PHOTO ANIMALLIER
  // ==========================================
  {
    campaign: CAMPAIGN_FR,
    budget: "6.50",
    lang: "fr",
    location: "France;Switzerland;Belgium",
    adGroup: "3_Voyage_Photo_Animalier",
    cpc: "1.20",
    status: "Enabled",
    finalUrl: "https://junglenepal.com/tours/jungle-extreme/",
    path1: "Safari",
    path2: "Photo",
    keywords: [
      { text: "voyage photo animalier népal", type: "Phrase" },
      { text: "safari photo tigre népal", type: "Phrase" },
      { text: "stage photo animalier népal", type: "Phrase" },
      { text: "voyage photo bardia", type: "Phrase" },
      { text: "voyage photo népal", type: "Exact" },
      { text: "safari photo népal", type: "Exact" },
      { text: "voyage photographie faune népal", type: "Phrase" }
    ],
    headlines: [
      "Voyage Photo Faune Népal",     // 24
      "Safari Photo Tigre Népal",     // 24
      "Affûts Photo à Bardia",        // 21
      "Immersion 100% Faune Sauvage", // 28
      "Tigre, Rhinocéros & Gavial",   // 26
      "Rythme Dédié Photographes",    // 25
      "Lumières d'Aube et Crépuscule",// 29
      "Micro-Groupe 4 à 8 Pers Max",  // 27
      "Expédition 15 Jours 2 490 €",  // 27
      "Chitwan, Bardia, Suklaphanta", // 28
      "Pisteurs Experts en Faune",    // 25
      "Marche et Affûts Silencieux",  // 27
      "Voyage Naturaliste Exclusif",  // 27
      "Créé par Passionnés Faune",    // 25
      "Échangez avec l'Équipe",       // 22
    ],
    descriptions: [
      "Voyage photo animalier 15 jours au Népal. Affûts à l'aube, pistage du tigre et rhinos.",     // 86
      "Rythme sur-mesure pour photographes exigeants : Chitwan, Bardia et Suklaphanta sauvage.",      // 87
      "Micro-groupe exclusif dès 2 490 €. Accompagnement par les maîtres-pisteurs Tharu.",            // 83
      "Immersion nature sans compromis loin des foules. Discutez de votre projet sur WhatsApp."      // 87
    ]
  },

  // ==========================================
  // GROUPES ANGLAIS (EN PAUSE PAR DÉFAUT POUR PROTÉGER LE BUDGET)
  // ==========================================
  {
    campaign: CAMPAIGN_EN,
    budget: "3.50",
    lang: "en",
    location: "United Kingdom;Netherlands;Germany;United States",
    adGroup: "1_EN_Bardia_Local_DMC",
    cpc: "1.40",
    status: "Paused",
    finalUrl: "https://junglenepal.com/en/destinations/bardia/",
    path1: "Bardia",
    path2: "Safari",
    keywords: [
      { text: "bardia national park safari", type: "Exact" },
      { text: "walking safari bardia", type: "Exact" },
      { text: "bardia tiger safari", type: "Exact" },
      { text: "local agency bardia nepal", type: "Phrase" },
      { text: "tharu guide bardia", type: "Phrase" },
      { text: "bardia vs chitwan safari", type: "Phrase" }
    ],
    headlines: [
      "Bardia National Park Safari",  // 27
      "Local Nepal Wildlife Agency",  // 27
      "Native Tharu Expert Guides",   // 25
      "Track Tigers on Foot",         // 20
      "Authentic Jungle Ecolodges",   // 25
      "Small Groups 4 to 10",         // 20
      "Far From Mass Tourism",        // 21
      "0% Elephant Riding",           // 19
      "Custom Bardia Itineraries",    // 25
      "Bardia Specialist Operator",   // 26
      "Direct WhatsApp Contact",      // 23
      "5-Day Safaris from 490€",      // 23
      "Pure Wilderness Experience",   // 26
      "Ethical Wildlife Tracking",    // 25
      "Chat with Robin Today"         // 21
    ],
    descriptions: [
      "Direct local safari operator in Bardia. Walking safaris with renowned Tharu trackers.", // 87
      "Experience untamed Nepal in small groups of 4-10 travelers. 100% ethical wildlife tours.", // 89
      "Track wild Bengal tigers on foot far from crowds. Chat directly with us on WhatsApp.", // 86
      "Tailor-made itineraries and guaranteed departures. Authentic lodges and expert guides." // 87
    ]
  },
  {
    campaign: CAMPAIGN_EN,
    budget: "3.50",
    lang: "en",
    location: "United Kingdom;Netherlands;Germany;United States",
    adGroup: "2_EN_Walking_Tiger_Safari",
    cpc: "1.40",
    status: "Paused",
    finalUrl: "https://junglenepal.com/en/tours/bardia-tiger-safari-5-days/",
    path1: "Tiger",
    path2: "Safari",
    keywords: [
      { text: "walking tiger safari nepal", type: "Exact" },
      { text: "track tigers on foot nepal", type: "Exact" },
      { text: "ethical wildlife tour nepal", type: "Phrase" },
      { text: "bengal tiger tracking nepal", type: "Exact" },
      { text: "nepal tiger safari small group", type: "Phrase" }
    ],
    headlines: [
      "Nepal Tiger Safari on Foot",   // 26
      "Track Bengal Tigers on Foot",  // 27
      "Wild Bardia National Park",    // 25
      "100% on Foot • 0% Elephant",   // 26
      "Expert Tharu Trackers",        // 20
      "85% Sighting Rate in Season",  // 27
      "Small Groups 4 to 10",         // 20
      "Wild Alternative to India",    // 25
      "5-Day Safari From 490€",       // 22
      "Ethical Animal Observation",   // 26
      "No Crowded Jeeps",             // 16
      "Direct WhatsApp Support",      // 23
      "Bardia vs Chitwan Choice",     // 24
      "Tailor-Made Tiger Tours",      // 23
      "Plan Your 2027 Safari"         // 22
    ],
    descriptions: [
      "Track wild Bengal tigers on foot in Bardia National Park. 100% ethical walking safaris.", // 89
      "The wild, silent alternative to Indian jeep crowds. Guided by elite native Tharu scouts.", // 90
      "5-day ecolodge basecamp package from 490€. Exclusive small groups of 4 to 10 travelers.", // 89
      "Prime tiger tracking season: February to May. Chat with our founder Robin on WhatsApp."  // 88
    ]
  },
  {
    campaign: CAMPAIGN_EN,
    budget: "3.50",
    lang: "en",
    location: "United Kingdom;Netherlands;Germany;United States",
    adGroup: "3_EN_Wildlife_Photo_Tour",
    cpc: "1.40",
    status: "Paused",
    finalUrl: "https://junglenepal.com/en/tours/nepal-wildlife-safari-15-days/",
    path1: "Wildlife",
    path2: "Photo",
    keywords: [
      { text: "wildlife photography tour nepal", type: "Phrase" },
      { text: "tiger photography tour nepal", type: "Phrase" },
      { text: "bardia photography safari", type: "Phrase" },
      { text: "nepal wildlife photo tour", type: "Exact" },
      { text: "nepal wildlife photography", type: "Phrase" }
    ],
    headlines: [
      "Nepal Wildlife Photo Safari",  // 27
      "Tiger Photo Tour in Bardia",   // 26
      "Dawn and Dusk River Hides",    // 25
      "Designed for Photographers",   // 26
      "Tigers, Rhinos & Gharials",    // 25
      "Chitwan, Bardia, Suklaphanta", // 28
      "15-Day Ultimate Expedition",   // 26
      "Small Group 4-8 Pax Max",      // 23
      "Master Native Trackers",       // 21
      "Pure Naturalist Immersion",    // 25
      "From 2,490€ All-Inclusive",    // 25
      "Far From Mass Tourism",        // 21
      "Custom Photo Expeditions",     // 24
      "Silent Foot Approaches",       // 23
      "Contact Expert Team Direct"    // 26
    ],
    descriptions: [
      "15-day wildlife photography expedition in Nepal. Dawn hides, tiger and rhino tracking.",  // 89
      "Paced specifically for demanding photographers: Chitwan, wild Bardia and Suklaphanta.",   // 88
      "Exclusive micro-group from 2,490€. Led by the most experienced Tharu tracking masters.",  // 89
      "Uncompromising nature immersion far from crowds. Chat directly with us on WhatsApp."      // 85
    ]
  }
];

// 2. VALIDATION RUN
console.log("Validating character limits...");
groups.forEach(g => {
  checkLen(g.path1, 15, `${g.adGroup} path1`);
  checkLen(g.path2, 15, `${g.adGroup} path2`);
  g.headlines.forEach((h, i) => checkLen(h, 30, `${g.adGroup} Headline ${i+1}`));
  g.descriptions.forEach((d, i) => checkLen(d, 90, `${g.adGroup} Description ${i+1}`));
});
console.log("All character limits verified 100% compliant!");

// 3. GENERATE GOOGLE ADS EDITOR CSV
const csvHeaders = [
  "Campaign",
  "Campaign Daily Budget",
  "Campaign Type",
  "Networks",
  "Languages",
  "Location",
  "Ad Group",
  "Max CPC",
  "Keyword",
  "Criterion Type",
  "Headline 1", "Headline 2", "Headline 3", "Headline 4", "Headline 5",
  "Headline 6", "Headline 7", "Headline 8", "Headline 9", "Headline 10",
  "Headline 11", "Headline 12", "Headline 13", "Headline 14", "Headline 15",
  "Description 1", "Description 2", "Description 3", "Description 4",
  "Final URL",
  "Path 1",
  "Path 2",
  "Status"
];

function escapeCsv(val) {
  if (val === undefined || val === null) return "";
  const str = String(val);
  if (str.includes(",") || str.includes("\"") || str.includes("\n") || str.includes(";")) {
    return `"${str.replace(/"/g, '""')}"`;
  }
  return str;
}

const rows = [];

groups.forEach(g => {
  // A. Keyword Rows
  g.keywords.forEach(kw => {
    const row = new Array(csvHeaders.length).fill("");
    row[0] = g.campaign;
    row[1] = g.budget;
    row[2] = "Search";
    row[3] = "Google search";
    row[4] = g.lang;
    row[5] = g.location;
    row[6] = g.adGroup;
    row[7] = g.cpc;
    row[8] = kw.text;
    row[9] = kw.type;
    row[32] = g.status;
    rows.push(row);
  });

  // B. Responsive Search Ad Row
  const adRow = new Array(csvHeaders.length).fill("");
  adRow[0] = g.campaign;
  adRow[1] = g.budget;
  adRow[2] = "Search";
  adRow[3] = "Google search";
  adRow[4] = g.lang;
  adRow[5] = g.location;
  adRow[6] = g.adGroup;
  adRow[7] = g.cpc;
  
  // Headlines 1-15 (columns 10 to 24)
  g.headlines.forEach((h, idx) => {
    adRow[10 + idx] = h;
  });

  // Descriptions 1-4 (columns 25 to 28)
  g.descriptions.forEach((d, idx) => {
    adRow[25 + idx] = d;
  });

  adRow[29] = g.finalUrl;
  adRow[30] = g.path1;
  adRow[31] = g.path2;
  adRow[32] = g.status;
  rows.push(adRow);
});

const csvContent = [
  csvHeaders.map(escapeCsv).join(","),
  ...rows.map(r => r.map(escapeCsv).join(","))
].join("\n");

fs.writeFileSync("ads-strategy/google-ads-sniper-campaign.csv", csvContent, "utf8");
console.log("Successfully generated ads-strategy/google-ads-sniper-campaign.csv!");
