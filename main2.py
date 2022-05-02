import cv2

img = cv2.imread('assets/simp.jpg', -1)

#in cv2, instead of the standard RGB representation, it uses BGR
print(img.shape)


