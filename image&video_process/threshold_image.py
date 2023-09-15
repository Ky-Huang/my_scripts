import cv2
from pathlib import Path

root_p = Path(r'F:\MyDataF\DataSet\kate_dance_01\test')
ext = "png"


# ---------------------------------------------------------
for img_path in root_p.rglob(f'*.{ext}'):
    img = cv2.imread(str(img_path), cv2.IMREAD_GRAYSCALE)
    ret, img = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY)
    cv2.imshow("1", img)
    cv2.imwrite(str(img_path), img)