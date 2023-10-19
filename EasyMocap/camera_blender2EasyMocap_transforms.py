## 把blender的transforms.json格式相机参数转为EasyMocap需要的intri.yml, extri.yml格式
# 似乎是w2c的，暂时没用
import json
import numpy as np
from EasyMocap.easymocap_tools.camera_utils import write_intri, write_extri
from os.path import join
import numpy
import cv2
from os import makedirs

# -------------------------------------修改----------------------------------------------------
file_path = r'E:\BaiduNetdiskDownload\synth\megan_dance_04_xie\megan_dance_04\transforms.json'
camera_record_path = r'E:\BaiduNetdiskDownload\synth\megan_dance_04_xie\megan_dance_04\camera_record.json'
# ----------------------------------------------------------------------------------------------
K = 0
with open(camera_record_path) as f:
    data = json.load(f)
    K = data["0.png"]["K"]
with open(file_path) as f:
    data = json.load(f)
    output_json = {}
    for i in data['frames']:
        cam_name = i['file_path'].split('/')[-1].split('_')[0]                        # 按需修改
        mat = np.array(i['transform_matrix'])
        output_json[f"{int(cam_name):02d}"] = {}
        output_json[f"{int(cam_name):02d}"]["K"] = np.array(K)
        output_json[f"{int(cam_name):02d}"]["Rot"] = mat[:3, :3].reshape(3,3)
        output_json[f"{int(cam_name):02d}"]["T"] = mat[:3, 3].reshape(3,1)





### 准备
# -------------------------------------修改----------------------------------------------------
path = r'E:\BaiduNetdiskDownload\synth\megan_dance_04_xie'
# ----------------------------------------------------------------------------------------------
camnames = [key for key in output_json.keys()]

### calib_intri部分
cameras = {}
for ic, cam in enumerate(camnames):
    K = output_json[cam]["K"]
    cameras[cam] = {
        'K': K,
        'dist': numpy.zeros((1, 5), dtype=numpy.float64)  # dist: (1, 5)
    }
makedirs(join(path, 'intri_extri_output'), exist_ok=True)
write_intri(join(path, 'intri_extri_output', 'intri.yml'), cameras)

### calib_extri部分
extri = {}
for ic, cam in enumerate(camnames):
    extri[cam] = {}
    extri[cam]['R'] = output_json[cam]["Rot"]
    temp = cv2.Rodrigues(extri[cam]['R'])[0]
    extri[cam]['Rvec'] = cv2.Rodrigues(extri[cam]['R'])[0].reshape((3, 1))
    extri[cam]['T'] = output_json[cam]["T"]
write_extri(join(path, 'intri_extri_output', 'extri.yml'), extri)