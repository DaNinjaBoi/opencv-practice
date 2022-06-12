import cv2
import numpy as np

img = cv2.imread('assets/board.jpg')
crop_img = img[88:612, 88:612]
cv2.imwrite('assets/board_fixed.jpg', img)
cv2.imshow('crop', crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
