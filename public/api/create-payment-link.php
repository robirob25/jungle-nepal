<?php
/**
 * Jungle Nepal Adventure - Collectif My Way Payment Link Generator
 * Secure server-side proxy for Payzen / Collectif My Way payment links
 */

header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, X-Requested-With');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'Method Not Allowed']);
    exit;
}

// 1. API Configuration
$API_KEY = getenv('MYWAY_API_KEY') ?: '';
$API_URL = 'https://api.collectifmyway.com/v1/api/payments/links';
$DEFAULT_PROJECT_REF = getenv('MYWAY_PROJECT_REF') ?: 'TMP161026RRR';

// Load external config file if available
$configFile = __DIR__ . '/config.php';
if (file_exists($configFile)) {
    $cfg = include $configFile;
    if (is_array($cfg)) {
        if (!empty($cfg['project_ref'])) {
            $DEFAULT_PROJECT_REF = $cfg['project_ref'];
        }
        if (!empty($cfg['api_key'])) {
            $API_KEY = $cfg['api_key'];
        }
    }
}

if (empty($API_KEY)) {
    http_response_code(500);
    echo json_encode(['error' => 'API Key Collectif My Way non configurée']);
    exit;
}

// 2. Parse JSON Input
$rawInput = file_get_contents('php://input');
$data = json_decode($rawInput, true);

if (!$data) {
    http_response_code(400);
    echo json_encode(['error' => 'Invalid JSON input']);
    exit;
}

// 3. Extract & Validate Fields
$activityTitle = trim($data['activityTitle'] ?? 'Activité Jungle Nepal');
$activitySlug  = trim($data['activitySlug'] ?? '');
$travelers     = max(1, min(20, intval($data['travelers'] ?? 1)));
$date          = trim($data['date'] ?? '');
$hasGuideRoom  = !empty($data['hasGuideRoom']);
$firstname     = trim($data['firstname'] ?? '');
$lastname      = trim($data['lastname'] ?? '');
$email         = trim($data['email'] ?? '');
$phone         = trim($data['phone'] ?? '');
$notes         = trim($data['notes'] ?? '');
$customRef     = trim($data['projectRef'] ?? '');

$projectRef = !empty($customRef) ? $customRef : $DEFAULT_PROJECT_REF;

if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['error' => 'Adresse email invalide']);
    exit;
}

if (empty($date)) {
    http_response_code(400);
    echo json_encode(['error' => 'Veuillez sélectionner une date pour l\'activité']);
    exit;
}

// 4. Server-Side Price Calculation & Verification
// Known official base rates for day activities
$basePrices = [
    'safari-pied-bardia'     => ['type' => 'per_person', 'price' => 50,  'night' => 12],
    'bardia-walking-safari'  => ['type' => 'per_person', 'price' => 50,  'night' => 12],
    'safari-jeep-bardia'     => ['type' => 'flat_group', 'price' => 190, 'night' => 12],
    'bardia-jeep-safari'     => ['type' => 'flat_group', 'price' => 190, 'night' => 12],
    'safari-pied-chitwan'    => ['type' => 'per_person', 'price' => 70,  'night' => 0],
    'chitwan-walking-safari' => ['type' => 'per_person', 'price' => 70,  'night' => 0],
    'safari-jeep-chitwan'    => ['type' => 'flat_group', 'price' => 190, 'night' => 0],
    'chitwan-jeep-safari'    => ['type' => 'flat_group', 'price' => 190, 'night' => 0],
    'rafting-safari-bardia'  => ['type' => 'flat_group', 'price' => 190, 'night' => 0],
    'bardia-rafting-safari'  => ['type' => 'flat_group', 'price' => 190, 'night' => 0],
];

$computedAmount = 0;
if (isset($basePrices[$activitySlug])) {
    $info = $basePrices[$activitySlug];
    if ($info['type'] === 'per_person') {
        $computedAmount = $info['price'] * $travelers;
    } else {
        $computedAmount = $info['price']; // forfait groupe privatisé
    }
    if ($hasGuideRoom && $info['night'] > 0) {
        $computedAmount += ($info['night'] * $travelers);
    }
} else {
    // Fallback if price is passed from frontend
    $computedAmount = max(50, min(5000, intval($data['amount'] ?? 50)));
}

$amountCents = $computedAmount * 100;

// 5. Construct Clean Customer-Facing Label
$clientFullName = trim("$firstname $lastname");
$labelParts = [];
$labelParts[] = mb_substr($activityTitle, 0, 40);
$labelParts[] = "$travelers pers.";
$labelParts[] = $date;
if (!empty($clientFullName)) {
    $labelParts[] = mb_substr($clientFullName, 0, 25);
}
$label = implode(' - ', $labelParts);
// Ensure label does not exceed 100 chars
if (mb_strlen($label) > 100) {
    $label = mb_substr($label, 0, 97) . '...';
}

// 6. Call Collectif My Way API
$postData = [
    'projectRef'  => $projectRef,
    'amountCents' => $amountCents,
    'label'       => $label
];

$ch = curl_init($API_URL);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'X-API-Key: ' . $API_KEY,
    'Content-Type: application/json'
]);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($postData));
curl_setopt($ch, CURLOPT_TIMEOUT, 20);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$curlError = curl_error($ch);
curl_close($ch);

if ($curlError) {
    http_response_code(500);
    echo json_encode(['error' => 'Erreur de connexion au serveur de paiement: ' . $curlError]);
    exit;
}

$apiResult = json_decode($response, true);

if ($httpCode !== 200 && $httpCode !== 201) {
    http_response_code($httpCode >= 400 && $httpCode < 600 ? $httpCode : 500);
    $errMsg = $apiResult['message'] ?? 'Erreur lors de la génération du lien de paiement';
    if (is_array($errMsg)) {
        $errMsg = implode(', ', $errMsg);
    }
    echo json_encode(['error' => $errMsg, 'details' => $apiResult]);
    exit;
}

$paymentUrl = $apiResult['url'] ?? '';
$paymentLinkId = $apiResult['id'] ?? '';

// 7. Send Instant Email Notification to Robin / Agency
$to = 'junglenepaladventure@gmail.com';
$subject = "💳 NOUVELLE RÉSERVATION & LIEN PAIEMENT : $activityTitle ($computedAmount €)";
$message = "Une nouvelle réservation d'activité à la journée a été initiée :\n\n"
         . "Activité : $activityTitle\n"
         . "Date souhaitée : $date\n"
         . "Nombre de voyageurs : $travelers\n"
         . "Option Nuit chez Pawan : " . ($hasGuideRoom ? "OUI (+12€/pers)" : "NON") . "\n"
         . "Montant total : $computedAmount €\n\n"
         . "CLIENT :\n"
         . "Nom : $clientFullName\n"
         . "Email : $email\n"
         . "Téléphone / WhatsApp : $phone\n"
         . "Remarques : $notes\n\n"
         . "PAIEMENT MY WAY / PAYZEN :\n"
         . "Lien de paiement généré : $paymentUrl\n"
         . "ID Paiement : $paymentLinkId\n"
         . "Dossier My Way (projectRef) : $projectRef\n"
         . "Statut : PENDING (en attente de règlement par le client)\n"
         . "Date/Heure : " . date('Y-m-d H:i:s') . "\n";

$headers = "From: Jungle Nepal Website <noreply@junglenepal.com>\r\n"
         . "Reply-To: $email\r\n"
         . "X-Mailer: PHP/" . phpversion();

@mail($to, $subject, $message, $headers);

// 8. Return Success Response
echo json_encode([
    'success'       => true,
    'paymentUrl'    => $paymentUrl,
    'paymentLinkId' => $paymentLinkId,
    'amount'        => $computedAmount,
    'currency'      => 'EUR',
    'label'         => $label
]);
