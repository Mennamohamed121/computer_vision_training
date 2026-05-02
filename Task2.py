import cv2, numpy as np
from PIL import Image
import matplotlib.pyplot as plt
# Print versions
print("OpenCV:  " + cv2._version_)
print("NumPy:   " + np._version_)
print("Pillow:  " + Image._version_)
# Create & display a test image
img = np.zeros((300, 400, 3), dtype=np.uint8)
img[50:250, 100:300] = [0, 194, 203]
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Setup Successful!")
plt.show()