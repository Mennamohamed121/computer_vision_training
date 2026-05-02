import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("C:/Users/Menna Mohamed/Downloads/fruits-with-protein-help-boost-intake-pomegranate-1440x810.webp")

# Convert spaces
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# Store spaces
spaces = {
    'BGR': cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
    'Gray': gray,
    'HSV': hsv,
    'LAB': lab,
    'YCrCb': ycrcb
}

# Plot
fig, axes = plt.subplots(1, 5, figsize=(20, 5))

for ax, (title, image) in zip(axes, spaces.items()):
    if image.ndim == 2:
        ax.imshow(image, cmap='gray')
    else:
        ax.imshow(image)

    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.savefig('color_spaces.png')
plt.show()

# Center pixel
cy, cx = img.shape[0] // 2, img.shape[1] // 2

print("BGR:", img[cy, cx])
print("Gray:", gray[cy, cx])
print("HSV:", hsv[cy, cx])
print("LAB:", lab[cy, cx])
print("YCrCb:", ycrcb[cy, cx])