## 把coreview的anotion.json格式相机参数转为PySG需要的cam_dict_norm.json相机参数

import json
import copy
import os
import time

file_path = r'F:\MyDataF\DataSet\zju-mocap\CoreView_313\annots.json'
output_path = r'F:\MyDataF\DataSet\zju-mocap\CoreView_313\cam_dict_norm.json'
with open(file_path) as f:
    data = json.load(f)
    # print(data)
    Ks = data['cams']['20190823']['K']
    Rs = data['cams']['20190823']['R']
    Ts = data['cams']['20190823']['T']
    Ds = data['cams']['20190823']['D']
    # print(Ks , Rs, Ts, Ds)
    newKs = copy.deepcopy(Ks)
    newRs = copy.deepcopy(Rs)
    newTs = copy.deepcopy(Ts)

    K = [None for i in range(21)]
    W2C = [None for i in range(21)]
    for i in range(21):
        newKs[i][0].append(0.0)
        newKs[i][1].append(0.0)
        newKs[i][2].append(0.0)
        newKs[i].append([0.0, 0.0, 0.0, 1.0])
        K[i] = newKs[i][0] + newKs[i][1] + newKs[i][2] + newKs[i][3]

        newRs[i][0].append(Ts[i][0][0]/1000)
        newRs[i][1].append(Ts[i][1][0]/1000)
        newRs[i][2].append(Ts[i][2][0]/1000)
        newRs[i].append([0.0, 0.0, 0.0, 1.0])
        W2C[i] = newRs[i][0] + newRs[i][1] + newRs[i][2] + newRs[i][3]
        # newRs[i][]
output_json = {}
for i in range(21):
    output_json["{:06d}.jpg".format(i)] = {}
    output_json["{:06d}.jpg".format(i)] = {}
    output_json["{:06d}.jpg".format(i)] = {}
    output_json["{:06d}.jpg".format(i)]["K"] = K[i]
    output_json["{:06d}.jpg".format(i)]["W2C"] = W2C[i]
    output_json["{:06d}.jpg".format(i)]["img_size"] = [1024, 1024]
with open(output_path, 'w') as output_file:
    json.dump(output_json, output_file)
# time.sleep()
# os.system("pause")