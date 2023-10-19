# 把两个depth合成一个没有灯柱的depth

from pathlib import Path
import cv2
import numpy as np

depthA_path = Path(r'E:\BaiduNetdiskDownload\synth\kate_dance_for_lightgraid_01\easymocap\depthA')
depthH_path = Path(r'E:\BaiduNetdiskDownload\synth\kate_dance_for_lightgraid_01\easymocap\depthH')

for img_path in depthA_path.glob('*.png'):
    img_name = img_path.name
    dir_name = img_path.parent.parent
    depthA_img = cv2.imread(img_path.as_posix(), cv2.IMREAD_GRAYSCALE)
    depthH_img = cv2.imread(depthH_path.joinpath(img_name).as_posix(), cv2.IMREAD_GRAYSCALE)
    # cv2.imshow('A', depthA_img)
    # cv2.imshow('H', depthH_img)
    # cv2.waitKey(0)
    mask = depthH_img.copy()
    mask[depthA_img != depthH_img] = 0
    dir_name.joinpath('mask').mkdir(parents=True, exist_ok=True)
    cv2.imwrite(dir_name.joinpath('mask', img_name).as_posix(), mask)