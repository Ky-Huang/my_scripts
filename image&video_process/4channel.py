# 把三通道的jpg加上mask组成四通道的png
import glob
import os.path

import cv2
import numpy as np

img_dir = r''
mask_dir = r''
out_dir = r''
for img_path in sorted(glob.glob(img_dir + r'\*.JPG')):
    img = cv2.imread(img_path)
    mask_path = os.path.join(mask_dir,os.path.basename(img_path)[:-4] + '.jpg')
    mask = cv2.imread(mask_path)[..., :1]
    new_img = np.concatenate((img, mask), axis=-1)
    new_img_path = os.path.join(out_dir, os.path.basename(img_path)[:-4] + '.png')
    cv2.imwrite(new_img_path, new_img)
