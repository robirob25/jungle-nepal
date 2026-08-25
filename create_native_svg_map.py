import re

# We will generate a rich native interactive SVG map of Nepal recreating all the features of the user's reference:
# - Nepal geographic silhouette
# - Topographic mountain relief and snowcaps
# - Wildlife parks (Bardia, Chitwan) in green with animal silhouettes
# - Cities & culture (Kathmandu with red star, Pokhara, Lumbini with Buddha, Rara Lake)
# - Mountain peaks with elevations (Everest 8848M, Annapurna 8090M, Dhaulagiri 8167M, etc.)

svg_map_code = """<div class="relative w-full aspect-[1000/520] rounded-2xl overflow-hidden bg-gradient-to-b from-[#fbf9f4] via-[#f5f1e8] to-[#eee9dc] border border-amber-950/10 shadow-2xl select-none">
  
  <!-- Subtle Topographic Contour Background Grid -->
  <svg class="absolute inset-0 w-full h-full opacity-30 pointer-events-none" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <pattern id="topo-grid" width="40" height="40" patternUnits="userSpaceOnUse">
        <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#bfa67a" stroke-width="0.5" stroke-dasharray="2 4"/>
      </pattern>
    </defs>
    <rect width="100%" height="100%" fill="url(#topo-grid)" />
  </svg>

  <!-- Main Vector SVG Map of Nepal -->
  <svg viewBox="0 0 1000 520" class="w-full h-full" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <!-- Drop Shadows & Filters -->
      <filter id="map-shadow" x="-5%" y="-5%" width="115%" height="115%">
        <feDropShadow dx="2" dy="6" stdDeviation="6" flood-color="#000000" flood-opacity="0.12"/>
      </filter>
      <filter id="park-glow" x="-10%" y="-10%" width="120%" height="120%">
        <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#059669" flood-opacity="0.25"/>
      </filter>
      
      <!-- Snow / Glacier Gradients -->
      <linearGradient id="snow-grad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#ffffff" stop-opacity="0.95"/>
        <stop offset="100%" stop-color="#f0ebe1" stop-opacity="0.2"/>
      </linearGradient>
      <linearGradient id="park-grad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#74c365"/>
        <stop offset="100%" stop-color="#4a934a"/>
      </linearGradient>
    </defs>

    <!-- 1. NEPAL BASE COUNTRY SHAPE (High Precision Boundary) -->
    <path 
      d="M 45 190 
         C 55 170, 75 140, 115 110 
         C 150 85, 200 45, 260 25 
         C 300 15, 340 35, 380 65 
         C 420 95, 460 115, 510 135 
         C 560 155, 600 175, 650 200 
         C 700 225, 740 250, 780 270 
         C 830 290, 880 305, 915 325 
         C 925 335, 920 360, 910 390 
         C 900 420, 890 450, 875 475 
         C 860 495, 840 500, 810 495 
         C 770 490, 730 480, 690 460 
         C 655 440, 620 425, 580 415 
         C 540 405, 500 400, 460 380 
         C 425 365, 390 350, 350 340 
         C 300 330, 260 315, 210 290 
         C 170 270, 130 255, 90 235 
         C 60 220, 45 205, 45 190 Z" 
      fill="#fdfbf7" 
      stroke="#dfd7c6" 
      stroke-width="2.5" 
      filter="url(#map-shadow)"
    />

    <!-- 2. INTERNAL TOPOGRAPHIC ELEVATION / PLATEAU SHADING -->
    <!-- Mid-hills elevation layer -->
    <path 
      d="M 120 120 
         C 200 65, 300 50, 420 110 
         C 500 145, 600 185, 750 260 
         C 830 300, 880 320, 900 340 
         C 880 390, 850 430, 810 440 
         C 740 430, 660 390, 580 370 
         C 500 350, 420 320, 330 290 
         C 240 260, 170 210, 120 120 Z" 
      fill="#f5eee0" 
      opacity="0.65"
    />

    <!-- High Himalayan Snow & Glacier Shading Zone -->
    <path 
      d="M 115 110 
         C 160 80, 240 35, 300 40 
         C 360 45, 420 90, 490 125 
         C 560 160, 630 190, 720 235 
         C 800 275, 870 300, 915 325 
         C 900 340, 850 330, 780 300 
         C 700 265, 620 230, 550 200 
         C 470 165, 400 140, 320 110 
         C 240 80, 170 85, 115 110 Z" 
      fill="url(#snow-grad)"
    />

    <!-- 3. RIVERS (Blue meandering waterlines) -->
    <!-- Karnali River in the West -->
    <path d="M 210 50 Q 230 110 200 160 T 195 240 Q 190 280 180 310" fill="none" stroke="#a3c7d6" stroke-width="1.8" stroke-linecap="round" opacity="0.8"/>
    <!-- Babai River (Bardia) -->
    <path d="M 225 215 Q 210 235 185 245 T 160 260" fill="none" stroke="#7eb8d4" stroke-width="1.6" stroke-linecap="round" opacity="0.85"/>
    <!-- Narayani / Rapti River in Chitwan -->
    <path d="M 440 180 Q 470 230 490 290 T 520 380 Q 535 410 540 430" fill="none" stroke="#7eb8d4" stroke-width="2" stroke-linecap="round" opacity="0.85"/>
    <!-- Koshi River in the East -->
    <path d="M 770 260 Q 790 320 780 380 T 770 470" fill="none" stroke="#a3c7d6" stroke-width="1.8" stroke-linecap="round" opacity="0.8"/>

    <!-- 4. LAKES (Blue water bodies) -->
    <!-- Rara Lake -->
    <g transform="translate(250, 105)">
      <path d="M 0 0 C 4 -6, 12 -4, 15 2 C 18 8, 10 14, 4 12 C -2 10, -4 6, 0 0 Z" fill="#38bdf8" stroke="#0284c7" stroke-width="1"/>
      <text x="18" y="2" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369a1">Rara Lake</text>
    </g>
    <!-- Phoksundo Lake -->
    <g transform="translate(340, 150)">
      <path d="M 0 0 C 3 -5, 10 -3, 11 3 C 12 8, 6 11, 2 9 C -2 7, -3 4, 0 0 Z" fill="#38bdf8" stroke="#0284c7" stroke-width="1"/>
      <text x="14" y="2" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#0369a1">Phoksundo Lake</text>
    </g>
    <!-- Pokhara Lakes (Phewa, Begnas, Rupa) -->
    <g transform="translate(460, 275)">
      <ellipse cx="0" cy="0" rx="6" ry="4" fill="#38bdf8" stroke="#0284c7" stroke-width="0.8"/>
      <text x="-4" y="14" font-family="system-ui, sans-serif" font-size="8.5" font-weight="600" fill="#64748b">Phewa Lake</text>
    </g>

    <!-- 5. HIMALAYAN MOUNTAIN PEAKS (Symbols + Altitude Labels) -->
    <!-- Api Himal -->
    <g transform="translate(115, 75)">
      <path d="M -8 10 L 0 -4 L 8 10 Z" fill="#93c5fd" opacity="0.6"/>
      <path d="M -6 10 L 0 0 L 6 10 Z" fill="#ffffff"/>
      <text x="10" y="4" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#64748b">Api Himal</text>
    </g>
    <!-- Dhaulagiri (8167M) -->
    <g transform="translate(385, 195)">
      <path d="M -10 12 L 0 -5 L 10 12 Z" fill="#60a5fa" opacity="0.7"/>
      <path d="M -8 12 L 0 0 L 8 12 Z" fill="#ffffff"/>
      <text x="-15" y="-9" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" fill="#334155">Dhaulagiri</text>
      <text x="-12" y="2" font-family="system-ui, sans-serif" font-size="8" font-weight="700" fill="#64748b">8167M</text>
    </g>
    <!-- Annapurna (8090M) & Annapurna Conservation Area -->
    <g transform="translate(440, 225)">
      <path d="M -12 14 L 0 -6 L 12 14 Z" fill="#60a5fa" opacity="0.75"/>
      <path d="M -9 14 L 0 -1 L 9 14 Z" fill="#ffffff"/>
      <text x="14" y="-12" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#1e293b">Annapurna</text>
      <text x="14" y="-1" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#475569">Conservation Area</text>
      <text x="14" y="10" font-family="system-ui, sans-serif" font-size="8" font-weight="700" fill="#64748b">8090M</text>
    </g>
    <!-- Manaslu (8163M) -->
    <g transform="translate(515, 230)">
      <path d="M -9 11 L 0 -4 L 9 11 Z" fill="#60a5fa" opacity="0.7"/>
      <path d="M -7 11 L 0 0 L 7 11 Z" fill="#ffffff"/>
      <text x="-8" y="22" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#334155">Manaslu 8163M</text>
    </g>
    <!-- Ganesh Himal (7046M) -->
    <g transform="translate(565, 255)">
      <path d="M -8 10 L 0 -3 L 8 10 Z" fill="#93c5fd" opacity="0.6"/>
      <text x="-6" y="20" font-family="system-ui, sans-serif" font-size="8" font-weight="600" fill="#64748b">Ganesh 7046M</text>
    </g>
    <!-- Langtang (7234M) -->
    <g transform="translate(610, 260)">
      <path d="M -8 10 L 0 -3 L 8 10 Z" fill="#93c5fd" opacity="0.6"/>
      <text x="-6" y="20" font-family="system-ui, sans-serif" font-size="8" font-weight="600" fill="#64748b">Langtang 7234M</text>
    </g>
    <!-- Mt. Everest (8848M) & Choyu (8201M) -->
    <g transform="translate(760, 310)">
      <!-- Everest Peak Symbol (Largest) -->
      <path d="M -14 16 L 0 -8 L 14 16 Z" fill="#3b82f6" opacity="0.8"/>
      <path d="M -10 16 L 0 -2 L 10 16 Z" fill="#ffffff"/>
      <text x="-12" y="-12" font-family="system-ui, sans-serif" font-size="11" font-weight="900" fill="#0f172a">Mt. Everest</text>
      <text x="-6" y="0" font-family="system-ui, sans-serif" font-size="9" font-weight="800" fill="#2563eb">8848M</text>
      <text x="-40" y="10" font-family="system-ui, sans-serif" font-size="7.5" font-weight="600" fill="#64748b">Choyu 8201M</text>
    </g>
    <!-- Makalu (8463M) -->
    <g transform="translate(820, 345)">
      <path d="M -8 10 L 0 -4 L 8 10 Z" fill="#60a5fa" opacity="0.7"/>
      <text x="-4" y="20" font-family="system-ui, sans-serif" font-size="8" font-weight="700" fill="#475569">Makalu 8463M</text>
    </g>
    <!-- Kanchenjunga (8598M) -->
    <g transform="translate(895, 365)">
      <path d="M -9 11 L 0 -4 L 9 11 Z" fill="#60a5fa" opacity="0.7"/>
      <text x="-20" y="22" font-family="system-ui, sans-serif" font-size="8" font-weight="700" fill="#475569">Kanchenjunga 8598M</text>
    </g>

    <!-- 6. CITIES & CULTURAL SITES -->
    <!-- Pokhara -->
    <g transform="translate(440, 290)">
      <circle cx="0" cy="0" r="4.5" fill="#475569"/>
      <circle cx="0" cy="0" r="2" fill="#ffffff"/>
      <text x="8" y="4" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" fill="#1e293b">Pokhara</text>
    </g>

    <!-- Lumbini (Buddha Birthplace) -->
    <g transform="translate(370, 360)">
      <!-- Little Buddha Silhouette icon -->
      <path d="M 0 -8 C 2 -8 3 -7 3 -5 C 3 -4 2 -3 0 -3 C -2 -3 -3 -4 -3 -5 C -3 -7 -2 -8 0 -8 Z M -5 0 C -5 -2 -2 -3 0 -3 C 2 -3 5 -2 5 0 L 6 4 C 6 6 4 7 0 7 C -4 7 -6 6 -6 4 Z" fill="#475569"/>
      <text x="10" y="3" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" fill="#334155">Lumbini</text>
    </g>

    <!-- Kathmandu (Capital - Iconic Red Circle with Star) -->
    <g transform="translate(605, 350)" class="cursor-pointer" onclick="selectMapLocation('katmandou')">
      <!-- Outer red badge -->
      <circle cx="0" cy="0" r="14" fill="#991b1b" filter="url(#map-shadow)"/>
      <circle cx="0" cy="0" r="12" fill="#dc2626"/>
      <!-- Star -->
      <path d="M 0 -7 L 2 -2 L 7 -2 L 3 1 L 5 6 L 0 3 L -5 6 L -3 1 L -7 -2 L -2 -2 Z" fill="#ffffff"/>
      <text x="20" y="5" font-family="system-ui, sans-serif" font-size="13" font-weight="900" fill="#0f172a" letter-spacing="0.5">KATHMANDU</text>
    </g>

    <!-- ========================================================================= -->
    <!-- 7. NATIONAL PARKS HIGHLIGHTED IN RICH GREEN WITH FAUNA SILHOUETTES -->
    <!-- ========================================================================= -->

    <!-- A. BARDIA NATIONAL PARK ZONE (West) -->
    <g id="park-bardia-group" class="cursor-pointer group/bardia" onclick="selectMapLocation('bardia')">
      <!-- Green Park Shape with soft contour -->
      <path 
        d="M 160 215 
           C 185 205, 225 210, 235 235 
           C 245 255, 235 285, 215 295 
           C 195 305, 165 295, 155 270 
           C 145 250, 150 225, 160 215 Z" 
        fill="url(#park-grad)" 
        stroke="#2e7d32" 
        stroke-width="1.5"
        filter="url(#park-glow)"
        class="group-hover/bardia:brightness-110 transition-all"
      />
      
      <!-- Wildlife Silhouettes inside Bardia -->
      <!-- Tiger Silhouette (SVG vector) -->
      <path d="M 180 226 C 182 224, 186 224, 189 226 L 194 227 C 196 226, 198 227, 200 229 L 202 233 L 199 235 L 198 238 L 196 238 L 196 235 L 191 235 L 190 238 L 188 238 L 189 233 C 187 232, 184 231, 181 233 L 178 231 C 176 229, 178 227, 180 226 Z" fill="#1e293b"/>
      <!-- Rhino Silhouette -->
      <path d="M 203 234 C 205 232, 208 231, 211 233 L 216 234 C 218 234, 220 236, 221 239 L 220 244 L 217 244 L 216 241 L 212 241 L 211 244 L 208 244 L 209 238 Z" fill="#1e293b"/>
      <!-- Elephant Silhouette (Large Asian Bull) -->
      <path d="M 202 248 C 206 244, 215 244, 222 247 C 228 250, 233 255, 234 262 L 232 272 L 227 272 L 226 266 L 220 266 L 219 272 L 214 272 L 215 264 L 210 264 L 209 272 L 205 272 L 206 260 C 204 262, 203 268, 203 271 L 200 271 C 200 265, 201 257, 203 252 Z" fill="#1e293b"/>

      <!-- Park Label -->
      <text x="140" y="185" font-family="system-ui, sans-serif" font-size="15" font-weight="900" fill="#0f172a">Bardia</text>
      <text x="140" y="202" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#1e293b">National</text>
      <text x="140" y="219" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#1e293b">Park</text>

      <!-- Interactive Plus Button Pin -->
      <g transform="translate(185, 255)">
        <circle cx="0" cy="0" r="13" fill="#b08958" stroke="#ffffff" stroke-width="2" filter="url(#map-shadow)"/>
        <text x="0" y="4.5" font-family="system-ui, sans-serif" font-size="14" font-weight="900" fill="#ffffff" text-anchor="middle">+</text>
      </g>
    </g>

    <!-- B. CHITWAN NATIONAL PARK ZONE (South-Central) -->
    <g id="park-chitwan-group" class="cursor-pointer group/chitwan" onclick="selectMapLocation('chitwan')">
      <!-- Green Park Shape extending along the Rapti River -->
      <path 
        d="M 450 365 
           C 480 355, 525 365, 555 390 
           C 565 400, 555 415, 530 415 
           C 495 415, 465 400, 445 385 
           C 435 375, 440 370, 450 365 Z" 
        fill="url(#park-grad)" 
        stroke="#2e7d32" 
        stroke-width="1.5"
        filter="url(#park-glow)"
        class="group-hover/chitwan:brightness-110 transition-all"
      />

      <!-- Wildlife Silhouettes inside Chitwan -->
      <!-- Rhino Silhouette -->
      <path d="M 470 358 C 473 355, 477 355, 481 357 L 488 358 C 491 359, 493 361, 494 365 L 493 371 L 489 371 L 487 367 L 482 367 L 481 371 L 477 371 L 478 364 Z" fill="#1e293b"/>
      <!-- Elephant Silhouette -->
      <path d="M 500 352 C 504 348, 513 348, 519 351 C 524 354, 529 359, 530 365 L 528 374 L 524 374 L 523 369 L 518 369 L 517 374 L 513 374 L 514 367 L 510 367 L 509 374 L 505 374 L 506 363 C 504 365, 503 370, 503 373 L 500 373 Z" fill="#1e293b"/>
      <!-- Deer / Chital with Antlers Silhouette -->
      <path d="M 535 368 C 536 364, 538 361, 541 363 L 542 360 L 544 360 L 543 363 L 546 365 C 548 367, 549 370, 548 376 L 546 384 L 544 384 L 543 378 L 540 378 L 539 384 L 537 384 L 538 372 Z" fill="#1e293b"/>

      <!-- Park Label -->
      <text x="460" y="428" font-family="system-ui, sans-serif" font-size="15" font-weight="900" fill="#0f172a">Chitwan</text>
      <text x="460" y="445" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#1e293b">National</text>
      <text x="460" y="462" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#1e293b">Park</text>

      <!-- Interactive Plus Button Pin -->
      <g transform="translate(460, 375)">
        <circle cx="0" cy="0" r="13" fill="#b08958" stroke="#ffffff" stroke-width="2" filter="url(#map-shadow)"/>
        <text x="0" y="4.5" font-family="system-ui, sans-serif" font-size="14" font-weight="900" fill="#ffffff" text-anchor="middle">+</text>
      </g>
    </g>

  </svg>
</div>"""

print("SVG map template successfully designed!")
