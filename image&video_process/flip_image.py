import cv2

image = cv2.imread(r'G:\MyData\_20221116095429.jpg')
img = cv2.flip(image, 1, dst=None)
cv2.imwrite(r'G:\MyData\20221116095429.jpg', img)