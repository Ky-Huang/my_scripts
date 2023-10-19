## 把blender的camera_record.json格式相机参数转为PySG需要的cam_dict_norm.json相机参数

import json
import copy
import os
import time
import numpy as np

file_path = r'E:\BaiduNetdiskDownload\synth\megan_dance_03\PhySG\megan_dance_03\camera_record.json'
output_path = r'E:\BaiduNetdiskDownload\synth\megan_dance_03\PhySG\megan_dance_03\PhySG_megan\cam_dict_norm.json'
with open(file_path) as f:
    data = json.load(f)
    output_json = {}
    for key, value in data.items():
        K = np.array(value['K'])
        K = np.c_[K, np.array([0., 0., 0.])]
        K = np.r_[K, np.array([[0., 0., 0., 1.]])]
        W2C = np.array(value['RT'])
        W2C = np.r_[W2C, np.array([[0., 0., 0., 1.]])]
        output_json[f"{int(key[:-4]):06d}.png"] = {}
        output_json[f"{int(key[:-4]):06d}.png"]["K"] = K.flatten().tolist()
        output_json[f"{int(key[:-4]):06d}.png"]["W2C"] = W2C.flatten().tolist()
        output_json[f"{int(key[:-4]):06d}.png"]["img_size"] = [1024, 1024]
with open(output_path, 'w') as output_file:
    json.dump(output_json, output_file)
# time.sleep()
# os.system("pause")