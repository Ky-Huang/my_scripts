import cv2
img = cv2.imread(r'E:\tmp\physgmegan\sg_specular_rgb_000108.png') * 2
img[(img == (0, 0, 0)).all(axis = 2)] = (255, 255, 255)
cv2.imwrite(r'E:\tmp\physgmegan\sg_specular_rgb_000108w.png', img)