<?php
/**
 * Jungle Nepal Adventure - Native First-Party Form Handler
 * Handles booking requests, custom tour requests, and contact messages server-side.
 */

header('Content-Type: application/json; charset=UTF-8');
header('X-Content-Type-Options: nosniff');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Method Not Allowed']);
    exit;
}

$rawInput = file_get_contents('php://input');
$data = json_decode($rawInput, true);

if (!$data || !is_array($data)) {
    $data = $_POST;
}

if (empty($data)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Invalid request payload']);
    exit;
}

// Honeypot check
if (!empty($data['_honey'])) {
    echo json_encode(['success' => true]);
    exit;
}

$to = 'junglenepaladventure@gmail.com';
$subject = isset($data['_subject']) ? trim((string)$data['_subject']) : 'Nouveau message — Jungle Nepal Adventure';
$replyTo = isset($data['email']) && filter_var($data['email'], FILTER_VALIDATE_EMAIL)
    ? $data['email']
    : (isset($data['_replyto']) && filter_var($data['_replyto'], FILTER_VALIDATE_EMAIL) ? $data['_replyto'] : 'contact@junglenepal.com');

// Build clean HTML table for email
$rowsHtml = '';
$plainLines = [];
foreach ($data as $key => $val) {
    if (in_array($key, ['_template', '_captcha', '_honey', '_subject', '_replyto'], true)) {
        continue;
    }
    $label = ucwords(str_replace('_', ' ', (string)$key));
    $cleanVal = htmlspecialchars((string)$val, ENT_QUOTES, 'UTF-8');
    $rowsHtml .= "<tr><td style=\"padding:10px 14px;border:1px solid #e2e8f0;font-weight:bold;background:#f8fafc;width:35%;\">{$label}</td><td style=\"padding:10px 14px;border:1px solid #e2e8f0;\">{$cleanVal}</td></tr>";
    $plainLines[] = "{$label}: " . (string)$val;
}

$htmlBody = "<!DOCTYPE html><html><body style=\"font-family:Arial,sans-serif;color:#0f172a;line-height:1.5;\">"
    . "<h2 style=\"color:#0e5c3e;margin-bottom:16px;\">" . htmlspecialchars($subject, ENT_QUOTES, 'UTF-8') . "</h2>"
    . "<table style=\"border-collapse:collapse;width:100%;max-width:680px;font-size:14px;\">{$rowsHtml}</table>"
    . "</body></html>";

$headers = [
    'MIME-Version: 1.0',
    'Content-type: text/html; charset=UTF-8',
    'From: Jungle Nepal Adventure <contact@junglenepal.com>',
    'Reply-To: ' . $replyTo,
    'X-Mailer: PHP/' . phpversion()
];

$mailSent = @mail($to, '=?UTF-8?B?' . base64_encode($subject) . '?=', $htmlBody, implode("\r\n", $headers));

// Server-side relay fallback (invisible to browsers/crawlers)
$relaySuccess = false;
if (function_exists('curl_init')) {
    $ch = curl_init('https://formsubmit.co/ajax/' . $to);
    curl_setopt_array($ch, [
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => json_encode($data),
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER => [
            'Content-Type: application/json',
            'Accept: application/json',
            'Referer: https://junglenepal.com/',
            'Origin: https://junglenepal.com'
        ],
        CURLOPT_TIMEOUT => 12,
    ]);
    $resp = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    if ($code >= 200 && $code < 300) {
        $relaySuccess = true;
    }
}

if ($mailSent || $relaySuccess) {
    echo json_encode(['success' => true]);
} else {
    http_response_code(500);
    echo json_encode(['success' => false, 'error' => 'Failed to send message']);
}
