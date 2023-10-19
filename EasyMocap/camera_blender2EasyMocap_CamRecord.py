## 把blender的camera_record.json格式相机参数转为EasyMocap需要的intri.yml, extri.yml格式
# 似乎是c2w的
import json
import numpy as np
from EasyMocap.easymocap_tools.camera_utils import write_intri, write_extri
from os.path import join
import numpy
import cv2
from os import makedirs

# -------------------------------------修改----------------------------------------------------
camera_file_path = r'F:\MyDataF\DataSet\synth\smpl2_dance_multiView_singleFrame\smpl2_dance_mistyfarmroad\camera_record.json'
# ----------------------------------------------------------------------------------------------
with open(camera_file_path) as f:
    data = json.load(f)
    output_json = {}
    for key, value in data.items():
        K = np.array(value['K'])
        RT = np.array(value['RT'])
        output_json[f"{int(key[:-4]):02d}"] = {}
        output_json[f"{int(key[:-4]):02d}"]["K"] = K
        output_json[f"{int(key[:-4]):02d}"]["Rot"] = RT[:3, :3].reshape(3,3)
        output_json[f"{int(key[:-4]):02d}"]["T"] = RT[:3, 3].reshape(3,1)





### 准备
# -------------------------------------修改----------------------------------------------------
output_path = r'F:\MyDataF\DataSet\synth\smpl2_dance_multiView_singleFrame\easymocap'
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
makedirs(join(output_path, 'intri_extri_output'), exist_ok=True)
write_intri(join(output_path, 'intri_extri_output', 'intri.yml'), cameras)

### calib_extri部分
extri = {}
for ic, cam in enumerate(camnames):
    extri[cam] = {}
    extri[cam]['R'] = output_json[cam]["Rot"]
    temp = cv2.Rodrigues(extri[cam]['R'])[0]
    extri[cam]['Rvec'] = cv2.Rodrigues(extri[cam]['R'])[0].reshape((3, 1))
    extri[cam]['T'] = output_json[cam]["T"]
write_extri(join(output_path, 'intri_extri_output', 'extri.yml'), extri)