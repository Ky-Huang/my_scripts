import cv2
from pathlib import Path
import numpy as np
# path = r'F:\MyDataF\DataSet\synth\megan_dance_02\000_0000_0000.png'
# img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
# mask = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
# tem = np.all(img == [137, 137, 137, 255], axis=2)
# mask[~tem] = 255
# cv2.imwrite(r'F:\MyDataF\DataSet\synth\megan_dance_02\1.png', mask)
# rbg = cv2.imread(r'F:\MyDataF\DataSet\synth\megan_dance_02\000_0000.png', cv2.IMREAD_COLOR)
# rbg[tem] = 0
# cv2.imwrite(r'F:\MyDataF\DataSet\synth\megan_dance_02\2.png', rbg)

img_rgb = cv2.imread(r'F:\MyDataF\DataSet\synth\megan_dance_02\000_0000.png', cv2.IMREAD_COLOR)
img_mask = cv2.imread(r'F:\MyDataF\DataSet\synth\megan_dance_02\EM000_0000_0000.png', cv2.IMREAD_GRAYSCALE)
img_rgb[img_mask<100] = 0
cv2.imwrite(r'F:\MyDataF\DataSet\synth\megan_dance_02\7.png', img_rgb)