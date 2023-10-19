### 先用这个脚本 输入new_parames，repose生成新pose的new_parames，然后用EasyMocap0925的脚本写vertices，然后用这里的prepare vertices生成new_vertices，然后在2卡机testdev进行lbs

# 1、拿目标shape的new_params、目标pose的new_params,使用这个repose.py生成内含目标shape和pose的new_params，在new_params_new_pose目录下
# 2、运行vscode EasyMocap0925_version2/apps/demo/hk_write_vertices.py，生成对应于上述new_params的vertices
# 3、运行prepare_vertices生成new_vertices
# 4、把以上步骤得到的new_vertices，new_params（new_params_new_pose）上传到x76服务器，/data/xrg/a_nerf_testdev/tools/prepare_blend_weights.py 生成lbs
# 5、把lbs，new_vertices，new_params，annots.npy（谁的annots.npy?如果这里面是相机的话，似乎都一样？答：是相机，最好用pose提供者的相机）上传到x57服务器进行训练

import glob
import os

import numpy as np

# pose_data_dir = r'G:\MyData\repose\repose_2023.2.28\manuel\new_params'
# shape_data_path = r'G:\MyData\repose\repose_2023.2.28\coreview_313\new_params\0.npy'
# new_pose_dir = os.path.dirname(shape_data_path) + r'\..\new_params_new_pose'
pose_data_dir = r'F:\MyDataF\DataSet\manuel_dancing\mv1pout2\new_params'
shape_data_path = r'F:\MyDataF\DataSet\manuel_dancing\repose_male4casual_shape_manuel_pose\shape_new_params\0.npy'
new_pose_dir = os.path.dirname(shape_data_path) + r'\..\new_params_new_pose'
# --------------------------------------------------------------------------------------------------------------------------------------
done_pose = []

for pose_data_path in glob.glob(pose_data_dir + '/*.npy'):
    shape_data = np.load(shape_data_path, allow_pickle=True).item()
    pose_data = np.load(pose_data_path, allow_pickle=True).item()
    # print('\npose:', pose_data, '\nshape:', shape_data)
    shape_data['Rh'] = pose_data['Rh']
    shape_data['Th'] = pose_data['Th']
    shape_data['poses'] = pose_data['poses']
    os.makedirs(new_pose_dir, exist_ok=True)
    np.save(os.path.join(new_pose_dir, os.path.basename(pose_data_path)), shape_data)
    done_pose.append(os.path.basename(pose_data_path))
print('done pose:', done_pose,
      '\nskip pose:', list(set(list(os.listdir(pose_data_dir))) - set(done_pose)))

# pose_data = np.load(r'C:\Users\Administrator\Desktop\temp\repose\manuel\new_params\0.npy', allow_pickle=True).item()
# shape_data = np.load(r'C:\Users\Administrator\Desktop\temp\repose\m2c\new_params_new_pose\0.npy', allow_pickle=True).item()
# old_shape_data = np.load(r'C:\Users\Administrator\Desktop\temp\repose\m2c\new_params\0.npy', allow_pickle=True).item()
# print(shape_data)