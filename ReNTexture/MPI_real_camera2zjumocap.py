# 把MPI real数据集的camera.calibration转成easymocap能读取的相机形式intri.yml、extri.yml

import numpy as np
import yaml
import cv2
from ReNTexture.camera_utils import write_intri, write_extri
from os import makedirs
from os.path import join
# from camera_utils import write_intri, write_extri

camera_calibration_path = r'E:\BaiduNetdiskDownload\MPI\Vlad\cameras.calibration'
camera_easymocap_path = r'E:\BaiduNetdiskDownload\MPI\Vlad'
with open(camera_calibration_path, 'r') as f:
    cameras = {}
    lines = f.readlines()
    for i, line in enumerate(lines):
        if line.startswith("name"):
            cam_id = int(line.split()[1])
            cameras[f"c_{cam_id:02}"] = {}
            cameras[f"c_{cam_id:02}"]["sensor"] = lines[i+1].split()[1:]
            cameras[f"c_{cam_id:02}"]["size"] = lines[i+2].split()[1:]
            cameras[f"c_{cam_id:02}"]["animated"] = lines[i+3].split()[1:]
            cameras[f"c_{cam_id:02}"]["intrinsic"] = lines[i+4].split()[1:]
            cameras[f"c_{cam_id:02}"]["extrinsic"] = lines[i+5].split()[1:]
            cameras[f"c_{cam_id:02}"]["radial"] = lines[i+6].split()[1:]

### calib_intri部分
camera_easymocap_intri = {}
for ic, cam in enumerate(cameras):
    K = np.array(cameras[cam]["intrinsic"]).astype(float).reshape(4, 4)[:3, :3]
    camera_easymocap_intri[cam] = {
        'K': K,
        'dist': np.zeros((1, 5), dtype=np.float64)  # dist: (1, 5)
    }
makedirs(join(camera_easymocap_path, 'intri_extri_output'), exist_ok=True)
write_intri(join(camera_easymocap_path, 'intri_extri_output', 'intri.yml'), camera_easymocap_intri)

### calib_extri部分
camera_easymocap_extri = {}
for ic, cam in enumerate(cameras):
    camera_easymocap_extri[cam] = {}
    camera_easymocap_extri[cam]['R'] = np.array(cameras[cam]["extrinsic"]).astype(float).reshape(4, 4)[:3, :3]
    camera_easymocap_extri[cam]['Rvec'] = cv2.Rodrigues(camera_easymocap_extri[cam]['R'])[0].reshape((3, 1))
    camera_easymocap_extri[cam]['T'] = np.array(cameras[cam]["extrinsic"]).astype(float).reshape(4, 4)[:3, 3].reshape(3, 1) / 1000.0
write_extri(join(camera_easymocap_path, 'intri_extri_output', 'extri.yml'), camera_easymocap_extri)