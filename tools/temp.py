# import numpy as np

# R1 = np.array([-1.000, 0.000, 0.000, 0.000, 0.243, -0.970, 0.000, -0.970, -0.243]).reshape(3,3)
# R2 = np.array([-0.000, -1.000, -0.000, -0.243, 0.000, -0.970, 0.970, 0.000, -0.243]).reshape(3,3)
# R3 = np.array([1.000, 0.000, 0.000, 0.000, -0.243, -0.970, -0.000, 0.970, -0.243]).reshape(3,3)
# R4 = np.array([-0.000, 1.000, -0.000, 0.243, 0.000, -0.970, -0.970, 0.000, -0.243]).reshape(3,3)

# T = np.array([0.000, 0.970, 4.366]).reshape(3,1)
# o1 = np.linalg.inv(R1) @ (-T)
# o2 = np.linalg.inv(R2) @ (-T)
# o3 = np.linalg.inv(R3) @ (-T)
# o4 = np.linalg.inv(R4) @ (-T)
# print(f'\n{o1}')
# print(f'\n{o2}')
# print(f'\n{o3}')
# print(f'\n{o4}')

# 用于smpl dance multiView singleFrame数据的图片自动分目录
from pathlib import Path

rootdir = Path(r'E:\BaiduNetdiskDownload\synth\josh_dance_02\PhySG\josh_dance_02\depth')
for img in rootdir.glob('*.png'):
    cam_id = img.stem.split('_')[0]
    img_id = img.stem.split('_')[1]
    new_path = img.parent.joinpath('mask', cam_id, f'{img_id}.png')
    new_path.parent.mkdir(parents=True, exist_ok=True)
    new_path.write_bytes(img.read_bytes())