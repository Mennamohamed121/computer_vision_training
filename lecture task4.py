import cv2
import numpy as np

# Load images
img = cv2.imread(r"C:\Users\Menna Mohamed\Downloads\fruits-with-protein-help-boost-intake-pomegranate-1440x810.webp")
iimg = cv2.imread(r"C:\Users\Menna Mohamed\Downloads\download (2).jpeg")
mask = cv2.imread(r"C:\Users\Menna Mohamed\Downloads\download.png", cv2.IMREAD_GRAYSCALE)

# Safety check
if img is None or iimg is None or mask is None:
    print("❌ Error: One of the images did not load")
    exit()

H, W = img.shape[:2]

# 🔹 Crop image
new1 = img[250:600, 300:500]
cv2.imshow("Cropped", new1)
cv2.imshow("Original", img)

# 🔹 Resize image
resized = cv2.resize(img, (W//2, H//2), interpolation=cv2.INTER_AREA)
resized2 = cv2.resize(img, (W*2, H*2), interpolation=cv2.INTER_CUBIC)
resized3 = cv2.resize(img, (W+200, H+200), interpolation=cv2.INTER_LINEAR)

cv2.imshow("Area resized", resized)
cv2.imshow("Cubic resized", resized2)
cv2.imshow("Linear resized", resized3)

# 🔹 Rotate image
center = (W//2, H//2)
rot = cv2.getRotationMatrix2D(center, 30, 1.0)
rotated = cv2.warpAffine(img, rot, (W, H))
cv2.imshow("Rotation", rotated)

# 🔹 Flip
cv2.imshow("Flip X", cv2.flip(img, 0))
cv2.imshow("Flip Horizontal", cv2.flip(img, 1))
cv2.imshow("Flip Both", cv2.flip(img, -1))

# 🔹 Image blending
iimg = cv2.resize(iimg, (W, H))

blend1 = cv2.addWeighted(img, 0.75, iimg, 0.25, 0)
blend2 = cv2.addWeighted(img, 0.50, iimg, 0.50, 0)
blend3 = cv2.addWeighted(img, 0.25, iimg, 0.75, 0)

cv2.imshow("Blend 1", blend1)
cv2.imshow("Blend 2", blend2)
cv2.imshow("Blend 3", blend3)

# 🔹 MASK PROCESSING (FIXED)

# Resize mask to match image
mask = cv2.resize(mask, (W, H))

# Convert to binary
mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

# Inverse mask
mask_inv = cv2.bitwise_not(mask)

# Extract object
object_only = cv2.bitwise_and(img, img, mask=mask)

# Extract background
background_only = cv2.bitwise_and(img, img, mask=mask_inv)

cv2.imshow("Mask", mask)
cv2.imshow("Mask Inverse", mask_inv)
cv2.imshow("Object Only", object_only)
cv2.imshow("Background Only", background_only)

# Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()