## 复制自谢博的json转npy的脚本

import numpy as np
import json
import os
import glob

# data_root = r'H:\dataset\realtime\Vlad\output\smpl'
# data_root = r'G:\MyData\PhySG\CoreView_313\mv1pout'
data_root = r'F:\MyDataF\DataSet\megan\easymocap\mv1pout1'
smpl_input_path = os.path.join(data_root,'smpl')
output_path = os.path.join(data_root,'new_params')
os.makedirs(output_path,exist_ok=True)
# strart_frame = 15275
strart_frame = 0
for file_path in glob.glob(smpl_input_path+'\*.json'):
    with open(file_path) as f:
        smpl_data = json.load(f)[0]
        file_id = int(os.path.basename(file_path).split('.')[0])+strart_frame
        del smpl_data['id']
        smpl_data['Rh'] = np.asarray(smpl_data['Rh'])
        smpl_data['Th'] = np.asarray(smpl_data['Th'])
        smpl_data['shapes'] = np.asarray(smpl_data['shapes'])
        smpl_data['poses'] = np.asarray(smpl_data['poses'])
        np.save(os.path.join(output_path,'{}.npy'.format(file_id)),smpl_data)

# param_path = r'H:\dataset\A-NeRF\zju_mocap\CoreView_313\new_params\1.npy'
# params = np.load(param_path, allow_pickle=True).item()
# print(params.keys())
#
# vertice_path = r'H:\dataset\A-NeRF\zju_mocap\CoreView_313\new_vertices\1.npy'
# vertices = np.load(vertice_path)
# print(vertices.shape)