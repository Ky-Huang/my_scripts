import numpy as np
import cv2
from pathlib import Path

dir = Path(r'F:\MyDataF\xzx\23.12.20\dwzx\instant-ngp\LR2')
for img_path in dir.rglob('*.[jp][pn]g'):
    img = cv2.imread(img_path.as_posix(), cv2.IMREAD_UNCHANGED)
    # if img.shape[0] > 500 or img.shape[1] > 500:
    img = cv2.resize(img, (img.shape[1] // 4, img.shape[0] // 4))
    cv2.imwrite(img_path.as_posix(), img)
    print(img_path.name)