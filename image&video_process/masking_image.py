# 用mask来mask掉图片


import cv2

mask = cv2.imread(r'C:\Users\GXY\Desktop\biye_images\syth_josh_dance_02-sem-0918-1\mask\0200.png', flags=cv2.IMREAD_GRAYSCALE)
img = cv2.imread(r'C:\Users\GXY\Desktop\biye_images\syth_josh_dance_02-sem-0918-1\0200_patch.png', flags=cv2.IMREAD_COLOR)
new_img = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite(r'C:\Users\GXY\Desktop\biye_images\syth_josh_dance_02-sem-0918-1\masked_0200_patch.png', new_img)