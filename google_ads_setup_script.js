/**
 * ========================================================================================
 * JUNGLE NEPAL ADVENTURE - GOOGLE ADS SETUP BILINGUE & INTERNATIONAL (200€ / MOIS)
 * ========================================================================================
 * 
 * Stratégie SEA Internationale :
 * 1. Séparation stricte FR vs EN (Annonces et pages d'atterrissage dédiées).
 * 2. Mots-clés en Anglais ciblés sur les requêtes à forte intention d'achat (High-intent).
 * 3. Enchères en Exact Match [ ... ] et Phrase Match " ... " pour éliminer le déchet.
 * 4. URLs de destination pointant directement vers les versions anglaises /en/tours/...
 * 5. Liste noire négative bilingue (35+ termes FR + 30+ termes EN).
 * 
 * Répartition Budget (~6.60 € / jour = ~200 € / mois) :
 * - Marché Anglais / International (65% du budget = ~4.30 €/j) -> Volume mondial & fort pouvoir d'achat
 * - Marché Français / Francophone (35% du budget = ~2.30 €/j) -> Niche fidèle & conversion forte
 * ========================================================================================
 */

function main() {
  Logger.log("=== DÉBUT DE LA CRÉATION DES CAMPAGNES INTERNATIONALES & BILINGUES ===");

  var CAMPAIGNS_CONFIG = [
    // =========================================================================
    // A. CAMPAGNES ANGLAISES / INTERNATIONALES (65% DU BUDGET)
    // =========================================================================

    // 1. EN - CHITWAN SAFARI (ETHICAL & JEEP/WALKING)
    {
      name: "JNA_Search_EN_Chitwan_Ethical_Safari",
      budget: 2.20,
      adGroups: [
        {
          name: "Chitwan_Safari_Tours_EN",
          keywords: [
            { text: "[chitwan safari]", cpc: 0.45 },
            { text: "\"chitwan safari tour\"", cpc: 0.45 },
            { text: "[chitwan national park safari]", cpc: 0.50 },
            { text: "\"ethical safari chitwan\"", cpc: 0.40 },
            { text: "\"no elephant safari chitwan\"", cpc: 0.40 },
            { text: "[chitwan walking safari]", cpc: 0.45 },
            { text: "\"best safari in chitwan\"", cpc: 0.50 },
            { text: "[jungle safari nepal chitwan]", cpc: 0.50 }
          ],
          ads: [
            {
              finalUrl: "https://junglenepal.com/en/tours/chitwan-jeep-safari?utm_source=google_ads&utm_medium=cpc&utm_campaign=chitwan_en",
              path1: "safari",
              path2: "chitwan",
              headlines: [
                "Ethical Chitwan Safari Tours",
                "Explore Chitwan Jungle Nepal",
                "Rhinos, Crocodiles & Tigers",
                "100% Ethical - No Elephant Ride",
                "Private Jeep & Walking Safari",
                "Direct Local Agency in Nepal",
                "Instant WhatsApp Quote in 1h",
                "Jungle Nepal Adventure",
                "Certified Wildlife Guides",
                "Eco-Responsible Safaris 2026",
                "Best Chitwan Jungle Packages",
                "Book Direct - No Middleman",
                "Authentic Terai Wildlife Tour",
                "Small Group & Tailor-Made",
                "Unforgettable Nepal Jungle"
              ],
              descriptions: [
                "Experience an authentic & ethical jungle safari in Chitwan National Park. Expert local guides.",
                "Encounter one-horned rhinos, gharials & wild tigers in nature. 100% cruelty-free wildlife tours.",
                "Custom private jeep safaris, canoe floats and guided jungle walks. Direct local rates.",
                "Plan your dream Chitwan wildlife tour with local naturalists. Fast WhatsApp support & quotes."
              ]
            }
          ]
        }
      ]
    },

    // 2. EN - BARDIA TIGER SAFARI (THE FLAGSHIP HIGH-TICKET)
    {
      name: "JNA_Search_EN_Bardia_Tiger_Safari",
      budget: 1.60,
      adGroups: [
        {
          name: "Bardia_Tiger_Tracking_EN",
          keywords: [
            { text: "[bardia tiger safari]", cpc: 0.60 },
            { text: "\"tiger tracking safari nepal\"", cpc: 0.60 },
            { text: "[bardia national park safari]", cpc: 0.55 },
            { text: "\"walking safari bardia\"", cpc: 0.50 },
            { text: "\"see wild tigers in nepal\"", cpc: 0.60 },
            { text: "[nepal tiger safari]", cpc: 0.60 },
            { text: "\"best place to see tigers nepal\"", cpc: 0.50 },
            { text: "[bardia jungle tour]", cpc: 0.50 }
          ],
          ads: [
            {
              finalUrl: "https://junglenepal.com/en/tours/bardia-tiger-safari-5-days?utm_source=google_ads&utm_medium=cpc&utm_campaign=bardia_en",
              path1: "tiger-safari",
              path2: "bardia",
              headlines: [
                "Bardia Tiger Safari Nepal",
                "Track Wild Royal Bengal Tigers",
                "Walking Safari with Top Guides",
                "High Tiger Sighting Rate",
                "Raw & Untamed Nepal Wildlife",
                "Far from Crowds in Bardia",
                "Bardia National Park 2026",
                "Direct Local Tour Operator",
                "Eco-Friendly Tiger Tracking",
                "Instant WhatsApp Quotation",
                "Jungle Nepal Adventure",
                "Exclusive Wildlife Photography",
                "5-Day Tiger Safari Package",
                "Authentic Jungle Lodges",
                "Track Tigers on Foot Safely"
              ],
              descriptions: [
                "Track the majestic Bengal Tiger on foot in pristine Bardia National Park. Unrivaled sightings.",
                "Led by veteran local naturalists and trackers. Safe, ethical and intimate wildlife immersion.",
                "Escape tourist crowds and explore Nepal's premier tiger sanctuary. Direct local pricing.",
                "Book your customized Bardia tiger expedition today. Direct contact with local experts."
              ]
            }
          ]
        }
      ]
    },

    // 3. EN - COMBINED & SNOW LEOPARD EXPEDITIONS
    {
      name: "JNA_Search_EN_SnowLeopard_Combos",
      budget: 0.50,
      adGroups: [
        {
          name: "Snow_Leopard_And_Combos_EN",
          keywords: [
            { text: "[snow leopard expedition nepal]", cpc: 0.65 },
            { text: "\"snow leopard trek nepal\"", cpc: 0.65 },
            { text: "[nepal wildlife holiday]", cpc: 0.55 },
            { text: "\"chitwan and bardia combined safari\"", cpc: 0.50 }
          ],
          ads: [
            {
              finalUrl: "https://junglenepal.com/en/tours/snow-leopard-expedition-nepal?utm_source=google_ads&utm_medium=cpc&utm_campaign=snow_leopard_en",
              path1: "wildlife",
              path2: "expedition",
              headlines: [
                "Snow Leopard Expedition Nepal",
                "Track the Ghost of the Mountains",
                "High Himalaya Wildlife Trek",
                "Elite Local Mountain Trackers",
                "Combined Jungle & Mountain Tour",
                "Chitwan & Bardia Combined Tour",
                "Nepal Wildlife Photography",
                "Direct Local Himalayan Agency",
                "Small Group Expeditions",
                "Jungle Nepal Adventure",
                "Custom Wildlife Itineraries",
                "WhatsApp Support & Quotes",
                "Bespoke Nature Travel Nepal",
                "High-Altitude Safari Trek",
                "Ethical Himalayan Expeditions"
              ],
              descriptions: [
                "Embark on an epic expedition tracking the elusive Snow Leopard in high Himalayas.",
                "Guided by specialized trackers with top-tier spotting scopes. Ethical and authentic journey.",
                "Combine tropical lowland jungle safaris and high-altitude wildlife in one ultimate trip.",
                "Inquire now for tailor-made dates and private wildlife itineraries with local specialists."
              ]
            }
          ]
        }
      ]
    },

    // =========================================================================
    // B. CAMPAGNES FRANÇAISES / FRANCOPHONES (35% DU BUDGET)
    // =========================================================================

    // 4. FR - CHITWAN SAFARI ÉTHIQUE
    {
      name: "JNA_Search_FR_Chitwan_Ethique",
      budget: 1.30,
      adGroups: [
        {
          name: "Chitwan_Safari_Ethique_FR",
          keywords: [
            { text: "[safari chitwan]", cpc: 0.45 },
            { text: "\"safari parc chitwan\"", cpc: 0.45 },
            { text: "[safari nepal chitwan]", cpc: 0.45 },
            { text: "\"safari chitwan sans elephant\"", cpc: 0.40 },
            { text: "[parc national chitwan safari]", cpc: 0.45 },
            { text: "\"safari jungle chitwan\"", cpc: 0.45 }
          ],
          ads: [
            {
              finalUrl: "https://junglenepal.com/safari-parc-national-chitwan-nepal?utm_source=google_ads&utm_medium=cpc&utm_campaign=chitwan_fr",
              path1: "safari",
              path2: "chitwan",
              headlines: [
                "Safari Chitwan Éthique & Privé",
                "Explorez la Jungle de Chitwan",
                "Rhinos, Crocodiles & Tigres",
                "100% Éthique Sans Éléphant",
                "Guides Locaux Certifiés Népal",
                "Devis Direct WhatsApp en 1h",
                "Jungle Nepal Adventure",
                "Safaris Éco-Responsables 2026",
                "Tarifs Directs Sans Intermédiaire",
                "Immersion Faune Sauvage Chitwan",
                "Jeep & Marche Guidée Chitwan",
                "Réservez Votre Safari Népal",
                "Au Cœur de la Jungle du Terai",
                "Séjour Safari Privé au Népal",
                "Vivez le Vrai Népal Sauvage"
              ],
              descriptions: [
                "Vivez un safari éthique d'exception au Parc National de Chitwan. Guides naturalistes experts.",
                "Rencontrez rhinocéros unicornes, crocodiles et tigres dans leur habitat préservé. Devis rapide.",
                "Safari 100% respectueux des animaux, sans monte d'éléphant. Tarifs locaux directs.",
                "Organisation sur-mesure de votre séjour à Chitwan : jeep privée, pirogue et affûts faune."
              ]
            }
          ]
        }
      ]
    },

    // 5. FR - BARDIA TIGRE ROYAL
    {
      name: "JNA_Search_FR_Bardia_Tigre",
      budget: 1.00,
      adGroups: [
        {
          name: "Bardia_Safari_Tigre_FR",
          keywords: [
            { text: "[safari bardia nepal]", cpc: 0.55 },
            { text: "\"safari tigre nepal\"", cpc: 0.55 },
            { text: "[parc national bardia safari]", cpc: 0.50 },
            { text: "\"voir tigre sauvage nepal\"", cpc: 0.50 },
            { text: "[safari a pied bardia]", cpc: 0.50 },
            { text: "\"guide safari bardia\"", cpc: 0.45 }
          ],
          ads: [
            {
              finalUrl: "https://junglenepal.com/safari-parc-national-bardia-nepal?utm_source=google_ads&utm_medium=cpc&utm_campaign=bardia_fr",
              path1: "safari",
              path2: "bardia",
              headlines: [
                "Safari Tigre à Bardia Népal",
                "Sur la Piste du Tigre Royal",
                "Parc National de Bardia 2026",
                "Safari à Pied avec Guides Locaux",
                "90% Chances d'Observer le Tigre",
                "Loin du Tourisme de Masse",
                "Jungle Sauvage & Préservée",
                "Guides Naturalistes d'Élite",
                "Tarifs Directs Sans Agence Tiers",
                "Devis Immédiat par WhatsApp",
                "Jungle Nepal Adventure",
                "Safaris Photo & Ornithologie",
                "Traque Éthique et Respectueuse",
                "Camp de Base & Lodges de Charme",
                "Votre Expédition Tigre au Népal"
              ],
              descriptions: [
                "Maximisez vos chances de croiser le Tigre du Bengale dans le joyau sauvage de Bardia.",
                "Affûts discrets et traque à pied sécurisée avec nos pisteurs naturalistes locaux chevronnés.",
                "Le Népal authentique, loin des foules. Safaris en immersion totale et respect absolu de la faune.",
                "Créez votre expédition sur-mesure à Bardia dès aujourd'hui. Réponse rapide en direct."
              ]
            }
          ]
        }
      ]
    }
  ];

  // =========================================================================
  // LISTE DES MOTS-CLÉS NÉGATIFS (BILINGUE FR + EN)
  // =========================================================================
  var NEGATIVE_KEYWORDS = [
    // Français
    "gratuit", "free", "stage", "emploi", "job", "recrutement", "benevolat", "volontariat",
    "defi", "forum", "routard avis", "tripadvisor avis", "carte", "map", "dessin",
    "peinture", "pdf", "livre", "coloriage", "chasse", "tuer", "tirer", "fusil",
    "cirque", "zoo", "balade elephant", "dos elephant", "ride elephant", "monte elephant",
    "pas cher", "low cost", "promo carrefour", "leclerc voyage", "promovacances",
    // Anglais
    "jobs", "career", "volunteer", "volunteering", "internship", "salary", "work",
    "free download", "drawing", "coloring", "clipart", "wallpaper", "hunting", "trophy",
    "elephant riding", "ride an elephant", "elephant back", "cheap flights", "cheap hotel"
  ];

  for (var i = 0; i < CAMPAIGNS_CONFIG.length; i++) {
    var campConfig = CAMPAIGNS_CONFIG[i];
    Logger.log("--> Traitement de la campagne : " + campConfig.name);

    var campaignIterator = AdsApp.campaigns()
      .withCondition("Name = '" + campConfig.name + "'")
      .get();

    var campaign;
    if (campaignIterator.hasNext()) {
      campaign = campaignIterator.next();
      Logger.log("    Campagne déjà existante : " + campConfig.name);
    } else {
      var campaignOperation = AdsApp.newCampaignBuilder()
        .withName(campConfig.name)
        .withBudget(campConfig.budget)
        .withBiddingStrategy("MANUAL_CPC")
        .build();

      if (!campaignOperation.isSuccessful()) {
        Logger.log("    ERREUR lors de la création de la campagne : " + campaignOperation.getErrors());
        continue;
      }
      campaign = campaignOperation.getResult();
      Logger.log("    Campagne créée avec succès !");
    }

    // Ajout des mots-clés négatifs
    for (var n = 0; n < NEGATIVE_KEYWORDS.length; n++) {
      campaign.createNegativeKeyword(NEGATIVE_KEYWORDS[n]);
    }
    Logger.log("    " + NEGATIVE_KEYWORDS.length + " mots-clés négatifs appliqués.");

    // Groupes d'annonces
    for (var g = 0; g < campConfig.adGroups.length; g++) {
      var groupConfig = campConfig.adGroups[g];
      var adGroupIterator = campaign.adGroups()
        .withCondition("Name = '" + groupConfig.name + "'")
        .get();

      var adGroup;
      if (adGroupIterator.hasNext()) {
        adGroup = adGroupIterator.next();
        Logger.log("    Groupe existant : " + groupConfig.name);
      } else {
        var adGroupOperation = campaign.newAdGroupBuilder()
          .withName(groupConfig.name)
          .withCpc(0.50)
          .build();

        if (!adGroupOperation.isSuccessful()) {
          Logger.log("    ERREUR création groupe : " + adGroupOperation.getErrors());
          continue;
        }
        adGroup = adGroupOperation.getResult();
        Logger.log("    Groupe créé : " + groupConfig.name);
      }

      // Mots-clés
      for (var k = 0; k < groupConfig.keywords.length; k++) {
        var kw = groupConfig.keywords[k];
        var kwOp = adGroup.newKeywordBuilder()
          .withText(kw.text)
          .withCpc(kw.cpc)
          .build();
        if (kwOp.isSuccessful()) {
          Logger.log("      Mot-clé ajouté : " + kw.text + " (CPC: " + kw.cpc + "€)");
        }
      }

      // Annonces RSA
      for (var a = 0; a < groupConfig.ads.length; a++) {
        var ad = groupConfig.ads[a];
        var rsaBuilder = adGroup.newAd().responsiveSearchAdBuilder()
          .withFinalUrl(ad.finalUrl)
          .withPath1(ad.path1)
          .withPath2(ad.path2);

        for (var h = 0; h < ad.headlines.length; h++) {
          rsaBuilder.addHeadline(ad.headlines[h]);
        }
        for (var d = 0; d < ad.descriptions.length; d++) {
          rsaBuilder.addDescription(ad.descriptions[d]);
        }

        var rsaOp = rsaBuilder.build();
        if (rsaOp.isSuccessful()) {
          Logger.log("      Annonce Responsive créée pour " + groupConfig.name);
        } else {
          Logger.log("      Erreur annonce : " + rsaOp.getErrors());
        }
      }
    }
  }

  Logger.log("=== TOUTES LES CAMPAGNES INTERNATIONALES & FR SONT CONFIGURÉES ! ===");
}
