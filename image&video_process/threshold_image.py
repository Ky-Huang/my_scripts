import cv2
import numpy as np
from pathlib import Path

# 把图片二值化，用途是把合成数据的depth做成mask

# ----------------------------修改-----------------------------------------
root_p = Path(r'E:\BaiduNetdiskDownload\synth\megan_dance_04_xie\megan_dance_04_cqf\physg\mask')
ext = "png"
flood_fill = False
morphologyEx = False

# ---------------------------------------------------------
for img_path in root_p.rglob(f'*.{ext}'):
    img = cv2.imread(str(img_path), cv2.IMREAD_GRAYSCALE)
    ret, img = cv2.threshold(img, 0.5, 255, cv2.THRESH_BINARY)
    if flood_fill:
        h, w = img.shape[:2]
        img_flood = img.copy()
        flood_mask = np.zeros((h+2, w+2), np.uint8)
        cv2.floodFill(img_flood, flood_mask, (0, 0), 255)
        img_flood = cv2.bitwise_not(img_flood)
        img = img | img_flood
    if morphologyEx:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
        img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(str(img_path), img)