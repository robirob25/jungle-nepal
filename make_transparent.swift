import Cocoa

let srcURL = URL(fileURLWithPath: "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/assets/logo_dark_raw.png")
guard let image = NSImage(contentsOf: srcURL),
      let tiffData = image.tiffRepresentation,
      let bitmap = NSBitmapImageRep(data: tiffData) else {
    print("Could not load image")
    exit(1)
}

let width = bitmap.pixelsWide
let height = bitmap.pixelsHigh

guard let newBitmap = NSBitmapImageRep(bitmapDataPlanes: nil,
                                       pixelsWide: width,
                                       pixelsHigh: height,
                                       bitsPerSample: 8,
                                       samplesPerPixel: 4,
                                       hasAlpha: true,
                                       isPlanar: false,
                                       colorSpaceName: .calibratedRGB,
                                       bytesPerRow: 0,
                                       bitsPerPixel: 32) else {
    print("Could not create new bitmap")
    exit(1)
}

for y in 0..<height {
    for x in 0..<width {
        if let color = bitmap.colorAt(x: x, y: y) {
            let r = color.redComponent
            let g = color.greenComponent
            let b = color.blueComponent
            // If it's near white background, make transparent
            if r > 0.92 && g > 0.92 && b > 0.92 {
                newBitmap.setColor(NSColor(red: 0, green: 0, blue: 0, alpha: 0), atX: x, y: y)
            } else {
                // Keep the crisp black/dark color with proper alpha
                let alpha = color.alphaComponent
                newBitmap.setColor(NSColor(red: r, green: g, blue: b, alpha: alpha), atX: x, y: y)
            }
        }
    }
}

guard let pngData = newBitmap.representation(using: .png, properties: [:]) else {
    print("Failed to encode PNG")
    exit(1)
}

let outURL = URL(fileURLWithPath: "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/assets/logo_dark.png")
try pngData.write(to: outURL)
print("Saved transparent logo_dark.png successfully!")
