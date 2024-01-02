# 用于给谢子玄做数据的时候sam扣mask的结果逆转
import cv2
from pathlib import Path

dir = Path(r'F:\MyDataF\xzx\23.12.20\D5\instantNGP-mask\masks')
dst_dir = Path(r'F:\MyDataF\xzx\23.12.20\D5\instantNGP-mask\masks2')
for img_path in dir.glob('*.png'):
    img = cv2.imread(img_path.as_posix(), cv2.IMREAD_GRAYSCALE)
    if (img - 2).any() != 0:
        img = cv2.bitwise_not(img)
    cv2.imwrite(dst_dir.joinpath(img_path.name).as_posix(), img)