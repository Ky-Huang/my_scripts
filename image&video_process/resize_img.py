import numpy as np
import cv2
from pathlib import Path

dir = Path(r'E:\tmp\physgmegan')
for img_path in dir.rglob('*.[jp][pn]g'):
    img = cv2.imread(img_path.as_posix(), cv2.IMREAD_UNCHANGED)
    if img.shape[0] > 500 or img.shape[1] > 500:
        img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
    cv2.imwrite(img_path.as_posix(), img)