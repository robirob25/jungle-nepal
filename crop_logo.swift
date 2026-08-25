import Cocoa

let srcURL = URL(fileURLWithPath: "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/assets/logo.png")
guard let image = NSImage(contentsOf: srcURL),
      let tiffData = image.tiffRepresentation,
      let bitmap = NSBitmapImageRep(data: tiffData) else {
    print("Could not load image")
    exit(1)
}

let width = bitmap.pixelsWide
let height = bitmap.pixelsHigh

var minX = width
var maxX = 0
var minY = height
var maxY = 0

for y in 0..<height {
    for x in 0..<width {
        let color = bitmap.colorAt(x: x, y: y)
        if let alpha = color?.alphaComponent, alpha > 0.05 {
            // Also check if not pure white
            if let r = color?.redComponent, let g = color?.greenComponent, let b = color?.blueComponent {
                if r < 0.95 || g < 0.95 || b < 0.95 {
                    if x < minX { minX = x }
                    if x > maxX { maxX = x }
                    if y < minY { minY = y }
                    if y > maxY { maxY = y }
                }
            }
        }
    }
}

print("Bounds: X: \(minX) to \(maxX), Y: \(minY) to \(maxY)")
let cropRect = NSRect(x: minX, y: minY, width: maxX - minX + 1, height: maxY - minY + 1)

let croppedImage = NSImage(size: cropRect.size)
croppedImage.lockFocus()
image.draw(in: NSRect(origin: .zero, size: cropRect.size),
           from: cropRect,
           operation: .copy,
           fraction: 1.0)
croppedImage.unlockFocus()

guard let croppedTiff = croppedImage.tiffRepresentation,
      let croppedBitmap = NSBitmapImageRep(data: croppedTiff),
      let pngData = croppedBitmap.representation(using: .png, properties: [:]) else {
    print("Failed to save cropped image")
    exit(1)
}

let outURL = URL(fileURLWithPath: "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/assets/logo_cropped.png")
try pngData.write(to: outURL)
print("Cropped logo saved to logo_cropped.png successfully!")
