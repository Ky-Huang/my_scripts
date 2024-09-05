# 用于把blender的相机参数转成nerfstudio需要的格式
import math
import json
import numpy as np

file_path = r'F:\MyDataF\DataSet\synth\smpl2_dance_multiView_singleFrame\smpl2_dance_mistyfarmroad_lerf\camera_record.json'
output_path = r'F:\MyDataF\DataSet\synth\smpl2_dance_multiView_singleFrame\smpl2_dance_mistyfarmroad_lerf\lerf_transform_1024.json'

image_width = 1024
bottom = np.array([0.0, 0.0, 0.0, 1.0]).reshape([1, 4])
with open(file_path) as f:
    data = json.load(f)
    Ks, Rs, Ts = [], [], []
    for key, value in data.items():
        Ks.append(np.array(value['K']))
        Rs.append(np.array(value['RT'])[:3, :3].reshape(3,3))
        Ts.append(np.array(value['RT'])[:3, 3].reshape(3,1))
    Ks, Rs, Ts = np.array(Ks), np.array(Rs), np.array(Ts)
    # Ks[:, :2] = Ks[:, :2] / 2                                                       # 从1024到512分辨率，内参也要改
output_json = {}
output_json["camera_model"] = "OPENCV"
output_json["orientation_override"] = "none"
output_json["frames"] = []
for i in range(len(Ks)):
    w2c = np.concatenate([np.concatenate([Rs[i], Ts[i]], 1), bottom], 0)
    c2w = np.linalg.inv(w2c)
    c2w[0:3,2] *= -1 # flip the y and z axis
    c2w[0:3,1] *= -1
    output_json["frames"].append({
         "fl_x":Ks[0,0,0],
         "fl_y":Ks[1,1,1],
         "cx":image_width/2,
         "cy":image_width/2,
         "w":1024,
         "h":1024,
        "file_path": f"./image/{i:03d}_0147.png",
        "transform_matrix": c2w.tolist(),
    })

with open(output_path, 'w') as fd:
        json.dump(output_json, fd)
