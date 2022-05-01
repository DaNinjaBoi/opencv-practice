import cv2

img = cv2.imread('assets/simp.jpg', 1)
img = cv2.resize(img, (0, 0), fx=1, fy=1)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('new_img.jpg', img)

cv2.imshow('Image', img)

cv2.waitKey(0)
# Wait infinite amount of times until a button is pressed to move on from the line
cv2.destroyAllWindows()
# Destroy all windows

