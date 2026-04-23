import cv2 
import numpy as np #Functiond for the arrays 

# Read images (use forward slashes to avoid unicode error)
img1 = cv2.imread("C:/Users/Menna Mohamed/Downloads/download.jpeg")
img2 = cv2.imread("C:/Users/Menna Mohamed/Downloads/images.jpeg")
img3 = cv2.imread("C:/Users/Menna Mohamed/Downloads/images (1).jpeg")

# Check if images loaded correctly
if img1 is None or img2 is None or img3 is None:
 print("Error: One or more images not loaded. Check file paths!")
else:
# Print shapes
 print("shape1:", img1.shape)
 print("shape2:", img2.shape)
 print("shape3:", img3.shape)

# Print data types
 print("dtype1:", img1.dtype)
 print("dtype2:", img2.dtype)
 print("dtype3:", img3.dtype)

#      #print channels
 print("img1:", img1.ndim)
 print("img2:", img2.ndim)
 print("img3:", img3.ndim)

#      #print size
 print("img1:", img1.size)
 print("img2:", img2.size)
 print("img3:", img3.size)

W,H =img1.shape[:2]
F,L  =img2.shape[:2]
M,A  =img3.shape[:2]

# Split channels
B1, G1, R1 = cv2.split(img1)
B2, G2, R2 = cv2.split(img2)
B3, G3, R3 = cv2.split(img3)

#Acces pixels for img
cx,cy =W//3, H//2
cx1,cy2 =F//5, L//4
cx2,cy1 =M//2, A//2
print(img1[cy,cx])  #BGR print 
print(img1[cy,cx,0]) #Layer 1
print(img1[cy,cx,1]) #layer2
print(img1[cy,cx,2]) #layer3

# Show img1 channels
cv2.imshow("Img1 Blue", B1)
cv2.imshow("Img1 Green", G1)
cv2.imshow("Img1 Red", R1)

# Show img2 channels
cv2.imshow("Img2 Blue", B2)
cv2.imshow("Img2 Green", G2)
cv2.imshow("Img2 Red", R2)

# Show img3 channels
cv2.imshow("Img3 Blue", B3)
cv2.imshow("Img3 Green", G3)
cv2.imshow("Img3 Red", R3)

# Show img
cv2.imshow("Img1 ", img1)
cv2.imshow("Img2", img2)
cv2.imshow("Img3", img3)

grey = cv2.imread("C:/Users/Menna Mohamed/Downloads/download.jpeg",0)
rgba = cv2.imread("C:/Users/Menna Mohamed/Downloads/download.jpeg",-1)
color = cv2.imread("C:/Users/Menna Mohamed/Downloads/download.jpeg",1) 
cv2.imshow("Img_grey", grey)
cv2.imshow("Img_rgba", rgba)
cv2.imshow("Img_color", color)




# Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()
