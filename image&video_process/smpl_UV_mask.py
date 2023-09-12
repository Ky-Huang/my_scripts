# 根据smpluv的到它的mask

import cv2
import numpy as np
uv_img_path = r'F:\MyDataF\SMPL_files\SMPL\UV map in OBJ format\smpl_uv_20200910.png'
uv_img = cv2.imread(uv_img_path, cv2.IMREAD_UNCHANGED)
mask = np.zeros((uv_img.shape[0], uv_img.shape[1]), dtype=int)
mask[uv_img[:, :, 3] != 0] = 255
cv2.imwrite(uv_img_path[:-4] + '_mask' + uv_img_path[-4:], mask)