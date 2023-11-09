# 用于把zjumocap313 的相机参数转成nvdiffrec需要的格式,稍微改一改可以用作easymocap定标出来的
import math
import json
import numpy as np

file_path = r'F:\MyDataF\DataSet\zju-mocap\CoreView_313\annots.json'
output_path = r'F:\MyDataF\DataSet\zju-mocap\CoreView_313\nvdiffrec_transform.json'

image_width = 1024
bottom = np.array([0.0, 0.0, 0.0, 1.0]).reshape([1, 4])
with open(file_path) as f:
    data = json.load(f)
    # print(data)
    Ks = np.array(data['cams']['20190823']['K'])
    Rs = np.array(data['cams']['20190823']['R'])
    Ts = np.array(data['cams']['20190823']['T']) / 1000
    Ds = np.array(data['cams']['20190823']['D'])
output_json = {}
output_json["camera_angle_x"] = math.atan(image_width / (Ks[0, 0, 0] * 2)) * 2      # 用第一个相机的fx作为所有相机的fx
output_json["frames"] = []
for i in range(len(Ks)):
    w2c = np.concatenate([np.concatenate([Rs[i], Ts[i]], 1), bottom], 0)
    c2w = np.linalg.inv(w2c)
    c2w[0:3,2] *= -1 # flip the y and z axis
    c2w[0:3,1] *= -1
    output_json["frames"].append({
        "file_path": f"./train/{i:02d}",
        "transform_matrix": c2w.tolist()
    })

with open(output_path, 'w') as fd:
        json.dump(output_json, fd)
