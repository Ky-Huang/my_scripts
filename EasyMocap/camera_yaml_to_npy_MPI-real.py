## 把easymocap的yaml格式相机转为npy格式
import numpy as np
import cv2
from pathlib import Path

# ----------------------------------修改------------------------------------------------------
intri_yaml_path = r'F:\MyDataF\DataSet\synth\smpl2_dance_multiView_singleFrame\easymocap\intri.yml'
extri_yaml_path = r'F:\MyDataF\DataSet\synth\smpl2_dance_multiView_singleFrame\easymocap\extri.yml'

data_path = r'F:\MyDataF\DataSet\synth\smpl2_dance_multiView_singleFrame\easymocap'
start_frame = 0
total_frame = 1
image_ext = "png"
skip_frames = []

# -------------------------------------------------------------------------------------------------

intri_yaml = cv2.FileStorage(intri_yaml_path, cv2.FILE_STORAGE_READ)
extri_yaml = cv2.FileStorage(extri_yaml_path, cv2.FILE_STORAGE_READ)
output_npy = {"cams":{}, "ims":[]}

cam_num = intri_yaml.getNode("names").size()
cam_names = [intri_yaml.getNode("names").at(i).string() for i in range(cam_num)]


# ----------------------------------------------------------------------------------------------------
# 相机“cams”
K = []
R = []
T = []
D = []
for cam_name in cam_names:
    K.append(intri_yaml.getNode(f"K_{cam_name}").mat().tolist())
    R.append(extri_yaml.getNode(f"Rot_{cam_name}").mat().tolist())
    T.append(extri_yaml.getNode(f"T_{cam_name}").mat().tolist())
    D.append(intri_yaml.getNode(f"dist_{cam_name}").mat().tolist())
output_npy["cams"]["K"] = np.array(K)
output_npy["cams"]["R"] = np.array(R)
output_npy["cams"]["T"] = np.array(T) * 1000
output_npy["cams"]["D"] = np.array(D)

# img路径“ims”
for i in range(total_frame):
    if i in skip_frames:
        continue
    output_npy["ims"].append({"ims":[f"{cam_name}/{start_frame+i:04d}.{image_ext}" for cam_name in cam_names]})

# 检查imgs路径是否存在
for i in output_npy["ims"]:
    for j in i["ims"]:
        tmp_data_path = Path(data_path)
        img_path = Path.joinpath(tmp_data_path, "images", j)
        # if not img_path.exists():
        #     raise
        assert img_path.exists()

np.save(data_path + r'\annots.npy', output_npy)