import cv2
img = cv2.imread(r'F:\MyDataF\xzx\23.12.20\D5\instantNGP\images\JI_0235.JPG')
cv2.imshow('1', img)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('2', img2)
cv2.waitKey(0)