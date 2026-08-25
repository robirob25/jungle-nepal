import Foundation
import CoreGraphics
import ImageIO

let srcURL = URL(fileURLWithPath: "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/assets/logo_dark_raw.png")
guard let imageSource = CGImageSourceCreateWithURL(srcURL as CFURL, nil),
      let cgImage = CGImageSourceCreateImageAtIndex(imageSource, 0, nil) else {
    print("Failed to load image")
    exit(1)
}

let width = cgImage.width
let height = cgImage.height
let colorSpace = CGColorSpaceCreateDeviceRGB()
let bytesPerPixel = 4
let bytesPerRow = bytesPerPixel * width
let rawData = UnsafeMutablePointer<UInt8>.allocate(capacity: height * bytesPerRow)
defer { rawData.deallocate() }

guard let context = CGContext(data: rawData,
                              width: width,
                              height: height,
                              bitsPerComponent: 8,
                              bytesPerRow: bytesPerRow,
                              space: colorSpace,
                              bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue | CGBitmapInfo.byteOrder32Big.rawValue) else {
    print("Failed to create context")
    exit(1)
}

context.draw(cgImage, in: CGRect(x: 0, y: 0, width: width, height: height))

// Process pixels in memory
var byteIndex = 0
for _ in 0..<height {
    for _ in 0..<width {
        let r = rawData[byteIndex]
        let g = rawData[byteIndex + 1]
        let b = rawData[byteIndex + 2]
        
        // If near white, set alpha to 0
        if r > 235 && g > 235 && b > 235 {
            rawData[byteIndex] = 0
            rawData[byteIndex + 1] = 0
            rawData[byteIndex + 2] = 0
            rawData[byteIndex + 3] = 0
        }
        byteIndex += 4
    }
}

guard let outCGImage = context.makeImage() else {
    print("Failed to make output image")
    exit(1)
}

let outURL = URL(fileURLWithPath: "/Users/robinrozier/.gemini/antigravity/scratch/jungle-nepal/assets/logo_dark.png") as CFURL
guard let destination = CGImageDestinationCreateWithURL(outURL, "public.png" as CFString, 1, nil) else {
    print("Failed to create destination")
    exit(1)
}

CGImageDestinationAddImage(destination, outCGImage, nil)
CGImageDestinationFinalize(destination)
print("Successfully generated transparent logo_dark.png in instant speed!")
