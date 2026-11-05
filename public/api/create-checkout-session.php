<?php
/**
 * Jungle Nepal Adventure - Stripe Checkout Session Endpoint
 * Creates a secure Stripe Checkout session for day tours.
 */

header('Content-Type: application/json; charset=UTF-8');
header('X-Content-Type-Options: nosniff');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Method Not Allowed']);
    exit;
}

require_once __DIR__ . '/stripe-config.php';

$rawInput = file_get_contents('php://input');
$data = json_decode($rawInput, true);

if (!$data) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Invalid JSON input']);
    exit;
}

$tourId = trim($data['tourId'] ?? '');
$date = trim($data['date'] ?? '');
$travelers = max(1, intval($data['travelers'] ?? 1));
$customerName = trim($data['customerName'] ?? '');
$customerEmail = trim($data['customerEmail'] ?? '');
$whatsapp = trim($data['whatsapp'] ?? '');
$hotel = trim($data['hotel'] ?? '');
$hasPawanRoom = !empty($data['hasPawanRoom']);
$lang = ($data['lang'] ?? 'fr') === 'en' ? 'en' : 'fr';
$cancelUrl = trim($data['cancelUrl'] ?? '');

if (empty($tourId) || empty($date) || empty($customerName) || empty($customerEmail) || empty($whatsapp)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => $lang === 'en' ? 'Please fill all required fields.' : 'Veuillez remplir tous les champs obligatoires.']);
    exit;
}

// Server-side tour definitions & prices (EUR cents)
$catalog = [
    'safari-pied-bardia' => [
        'title_fr' => 'Safari à pied — Parc national de Bardia (1 jour)',
        'title_en' => 'Walking Safari — Bardia National Park (1 day)',
        'type' => 'per_person',
        'unit_price' => 5000, // 50€
        'allows_pawan' => true,
    ],
    'safari-jeep-bardia' => [
        'title_fr' => 'Safari Jeep privée — Parc national de Bardia (1 jour)',
        'title_en' => 'Private Jeep Safari — Bardia National Park (1 day)',
        'type' => 'fixed_group',
        'unit_price' => 19000, // 190€
        'allows_pawan' => true,
    ],
    'safari-pied-chitwan' => [
        'title_fr' => 'Safari à pied — Parc national de Chitwan (1 jour)',
        'title_en' => 'Walking Safari — Chitwan National Park (1 day)',
        'type' => 'per_person',
        'unit_price' => 7000, // 70€
        'allows_pawan' => false,
    ],
    'safari-jeep-chitwan' => [
        'title_fr' => 'Safari Jeep privée — Parc national de Chitwan (1 jour)',
        'title_en' => 'Private Jeep Safari — Chitwan National Park (1 day)',
        'type' => 'fixed_group',
        'unit_price' => 19000, // 190€
        'allows_pawan' => false,
    ],
    'rafting-safari-bardia' => [
        'title_fr' => 'Rafting & Safari sauvage Bardia / Karnali (1 jour)',
        'title_en' => 'Karnali River Rafting & Wildlife Safari Bardia (1 day)',
        'type' => 'fixed_group',
        'unit_price' => 19000, // 190€
        'allows_pawan' => true,
    ],
];

$aliases = [
    'bardia-walking-safari' => 'safari-pied-bardia',
    'bardia-jeep-safari' => 'safari-jeep-bardia',
    'chitwan-walking-safari' => 'safari-pied-chitwan',
    'chitwan-jeep-safari' => 'safari-jeep-chitwan',
    'bardia-rafting-safari' => 'rafting-safari-bardia',
];
if (isset($aliases[$tourId])) {
    $tourId = $aliases[$tourId];
}

if (!isset($catalog[$tourId])) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => $lang === 'en' ? 'Invalid tour selected.' : 'Tour non valide.']);
    exit;
}

$tour = $catalog[$tourId];
$tourTitle = $lang === 'en' ? $tour['title_en'] : $tour['title_fr'];

$lineItems = [];

// Line 1: Main Tour Activity
if ($tour['type'] === 'per_person') {
    $lineItems[] = [
        'price_data' => [
            'currency' => 'eur',
            'unit_amount' => $tour['unit_price'],
            'product_data' => [
                'name' => $tourTitle,
                'description' => ($lang === 'en' ? 'Date: ' : 'Date : ') . $date . ' • ' . $travelers . ' ' . ($lang === 'en' ? ($travelers > 1 ? 'travelers' : 'traveler') : ($travelers > 1 ? 'personnes' : 'personne')),
            ],
        ],
        'quantity' => $travelers,
    ];
} else {
    // Fixed vehicle / boat group
    $lineItems[] = [
        'price_data' => [
            'currency' => 'eur',
            'unit_amount' => $tour['unit_price'],
            'product_data' => [
                'name' => $tourTitle,
                'description' => ($lang === 'en' ? 'Date: ' : 'Date : ') . $date . ' • ' . ($lang === 'en' ? 'Privatized vehicle/boat for up to ' : 'Véhicule/embarcation privatisée pour ') . $travelers . ' ' . ($lang === 'en' ? ($travelers > 1 ? 'travelers' : 'traveler') : ($travelers > 1 ? 'personnes' : 'personne')),
            ],
        ],
        'quantity' => 1,
    ];
}

// Line 2: Optional Night at Pawan's
if ($hasPawanRoom && $tour['allows_pawan']) {
    $lineItems[] = [
        'price_data' => [
            'currency' => 'eur',
            'unit_amount' => 1200, // 12€
            'product_data' => [
                'name' => $lang === 'en' ? "Option: Night at guide's place (Pawan)" : "Option : Nuit chez Pawan (guide senior)",
                'description' => $lang === 'en' 
                    ? "Private AC room + homemade dinner + breakfast next morning" 
                    : "Chambre privée climatisée + dîner traditionnel maison + petit-déjeuner",
            ],
        ],
        'quantity' => $travelers,
    ];
}

$siteUrl = rtrim(SITE_URL, '/');
$successPath = $lang === 'en' ? '/en/booking-success/' : '/merci-reservation/';
$successUrl = $siteUrl . $successPath . '?session_id={CHECKOUT_SESSION_ID}';

if (empty($cancelUrl)) {
    $cancelUrl = $siteUrl . ($lang === 'en' ? '/en/' : '/');
}

// Build Stripe payload
$postFields = [
    'mode' => 'payment',
    'customer_email' => $customerEmail,
    'success_url' => $successUrl,
    'cancel_url' => $cancelUrl,
    'locale' => $lang === 'en' ? 'en' : 'fr',
    'metadata' => [
        'tour_id' => $tourId,
        'tour_title' => $tourTitle,
        'date_safari' => $date,
        'nombre_voyageurs' => (string)$travelers,
        'nom_client' => $customerName,
        'email_client' => $customerEmail,
        'telephone_whatsapp' => $whatsapp,
        'hotel_pickup' => $hotel ?: 'À confirmer sur WhatsApp',
        'nuit_pawan' => ($hasPawanRoom && $tour['allows_pawan']) ? 'OUI (+12€/pers)' : 'NON',
        'langue' => $lang,
    ],
];

// Helper to serialize nested array for Stripe Form-Urlencoded
function buildStripePayload($data, $prefix = '') {
    $result = [];
    foreach ($data as $key => $value) {
        $newKey = $prefix === '' ? $key : "{$prefix}[{$key}]";
        if (is_array($value)) {
            $result = array_merge($result, buildStripePayload($value, $newKey));
        } else {
            $result[$newKey] = (string)$value;
        }
    }
    return $result;
}

$flatPayload = buildStripePayload($postFields);

// Add line items
foreach ($lineItems as $idx => $item) {
    $flatPayload["line_items[{$idx}][price_data][currency]"] = $item['price_data']['currency'];
    $flatPayload["line_items[{$idx}][price_data][unit_amount]"] = (string)$item['price_data']['unit_amount'];
    $flatPayload["line_items[{$idx}][price_data][product_data][name]"] = $item['price_data']['product_data']['name'];
    $flatPayload["line_items[{$idx}][price_data][product_data][description]"] = $item['price_data']['product_data']['description'];
    $flatPayload["line_items[{$idx}][quantity]"] = (string)$item['quantity'];
}

$ch = curl_init('https://api.stripe.com/v1/checkout/sessions');
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => http_build_query($flatPayload),
    CURLOPT_USERPWD => STRIPE_SECRET_KEY . ':',
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
        'Stripe-Version: 2024-06-20',
        'Content-Type: application/x-www-form-urlencoded',
    ],
    CURLOPT_TIMEOUT => 20,
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$curlError = curl_error($ch);
curl_close($ch);

if ($curlError) {
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'Connection error: ' . $curlError]);
    exit;
}

$resData = json_decode($response, true);

if ($httpCode >= 200 && $httpCode < 300 && isset($resData['url'])) {
    echo json_encode([
        'success' => true,
        'url' => $resData['url'],
        'sessionId' => $resData['id'],
    ]);
} else {
    http_response_code(500);
    $errMsg = $resData['error']['message'] ?? 'Erreur Stripe lors de la création de la session';
    echo json_encode(['success' => false, 'error' => $errMsg]);
}
