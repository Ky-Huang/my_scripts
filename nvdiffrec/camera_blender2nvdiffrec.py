# 用于把blender画的的相机camera_record参数转成nvdiffrec需要的格式
import json
import numpy as np

file_path = r'E:\BaiduNetdiskDownload\synth\josh_dance_02\josh_dance_02_cqf_nvdiff\camera_record.json'
output_path = r'E:\BaiduNetdiskDownload\synth\josh_dance_02\josh_dance_02_cqf_nvdiff\nvdiffrec_transform_512.json'

image_width = 512
bottom = np.array([0.0, 0.0, 0.0, 1.0]).reshape([1, 4])
with open(file_path) as f:
    data = json.load(f)
    Ks, Rs, Ts = [], [], []
    for key, value in data.items():
        Ks.append(np.array(value['K']))
        Rs.append(np.array(value['RT'])[:3, :3].reshape(3,3))
        # Ts.append(np.array(data['cams']['20190823']['T']) / 1000)
        Ts.append(np.array(value['RT'])[:3, 3].reshape(3,1))
    Ks, Rs, Ts = np.array(Ks), np.array(Rs), np.array(Ts)
    Ks[:, :2] = Ks[:, :2] / 2                                                       # 从1024到512分辨率，内参也要改
output_json = {}
output_json["camera_angle_x"] = math.atan(image_width / (Ks[0, 0, 0] * 2)) * 2      # 用第一个相机的fx作为所有相机的x和y方向的焦距
output_json["frames"] = []
for i in range(len(Ks)):
    w2c = np.concatenate([np.concatenate([Rs[i], Ts[i]], 1), bottom], 0)
    c2w = np.linalg.inv(w2c)
    c2w[0:3,2] *= -1 # flip the y and z axis
    c2w[0:3,1] *= -1
    output_json["frames"].append({
        "file_path": f"./train/{i:02d}",
        "transform_matrix": c2w.tolist(),
        "K":Ks[i].tolist()                                                          # nvdiffrect默认相机是xy对称的，这里为了符合真实世界相机xy不对称的情况，给json多写进一个K，用于nvdiff后续使用
    })

with open(output_path, 'w') as fd:
        json.dump(output_json, fd)
