import cv2
grayImage = cv2.imread('tipu_png.png', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('tipu_gray.png', grayImage)