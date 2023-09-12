## 复制自谢博的json转npy的脚本

import numpy as np
import json
import os
import glob

# data_root = r'H:\dataset\realtime\Vlad\output\smpl'
# data_root = r'G:\MyData\PhySG\CoreView_313\mv1pout'
data_root = r'G:\MyData\repose\repose_2023.2.28\coreview_313'
smpl_input_path = os.path.join(data_root,'vertices')
output_path = os.path.join(data_root,'new_vertices')
# strart_frame = 15275
strart_frame = 0
os.makedirs(output_path,exist_ok=True)
for file_path in glob.glob(smpl_input_path+'\*.json'):
    with open(file_path) as f:
        smpl_data = json.load(f)[0]
        file_id = int(os.path.basename(file_path).split('.')[0])+strart_frame
        np.save(os.path.join(output_path,'{}.npy'.format(file_id)),np.asarray(smpl_data['vertices']))