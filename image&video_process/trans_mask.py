## 把各种颜色的mask变为只有0，255颜色的mask
# 废弃，不如用image&video_process\threshold_image.py

import glob
import os

import cv2
import pathlib

# mask_dir_path = r'C:\Users\Administrator\Desktop\temp\lightprobes_ablation\single\mask'
mask_dir_path = r'F:\MyDataF\DataSet\kate_dance_01\easymocap\depth'
# output_dir = r'C:\Users\Administrator\Desktop\temp\lightprobes_ablation\single\mask'
output_dir = r'F:\MyDataF\DataSet\kate_dance_01\easymocap\depth'
black = 0
grey = 0
other = 0
os.makedirs(output_dir, exist_ok=True)
for view in os.listdir(mask_dir_path):
    sub_mask_dir_path = os.path.join(mask_dir_path, view)
    for mask_path in glob.glob(sub_mask_dir_path + '/*.png'):
        mask = cv2.imread(mask_path)
        mask_name = os.path.basename(mask_path)
        for i in range(mask.shape[0]):
            for j in range(mask.shape[1]):
                if mask[i][j].sum() == 0:
                    black += 1
                    continue
                elif mask[i][j].sum() == 3:
                    grey += 1
                else:
                    other += 1
                mask[i][j] = (255, 255, 255)
        # pathlib.Path(os.mkdir(os.path.join(output_dir, sub_mask_dir_path))).mkdir(parents=True, exist_ok=True)
        cv2.imwrite(os.path.join(output_dir, sub_mask_dir_path, mask_name), mask)
print('\n', 'num_black:{}\n num_grey:{}\n, num_other:{}'.format(black, grey, other))