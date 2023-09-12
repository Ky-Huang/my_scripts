# 用mask来mask掉图片


import cv2

mask = cv2.imread(r'F:\MyDataF\SMPL_files\SMPL\UV map in OBJ format\smpl_uv_20200910_mask.png', flags=cv2.IMREAD_GRAYSCALE)
img = cv2.imread(r'F:\MyDataF\SMPL_files\SMPL\UV map in OBJ format\Honeyview_t.png', flags=cv2.IMREAD_COLOR)
new_img = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite(r'F:\MyDataF\SMPL_files\SMPL\UV map in OBJ format\Honeyview_t1.png', new_img)