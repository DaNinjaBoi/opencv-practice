import cv2
import random

img = cv2.imread('assets/simp.jpg', -1)

#in cv2, instead of the standard RGB representation, it uses BGR
#print(img.shape)
print(img.shape)

for i in range(50):
    for j in range(50):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

glitch = img[0:50, 0:50]
img[100:150, 100:150] = glitch

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()