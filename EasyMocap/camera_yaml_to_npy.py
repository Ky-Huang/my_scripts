## 把yaml格式相机转为npy格式

import os
import numpy as np
import cv2
from functools import cmp_to_key

import re

camera_params = {}

# intri_yaml = r'G:\MyData\XieData\intri.yml'
#23.2.13
intri_yaml = r'G:\MyData\EasyMocap\XieData\intri.yml'

intri_file = open(intri_yaml)
lines = intri_file.readlines()
for i, line in enumerate(lines):
    line = line.strip()
    if line.startswith('- "'):
        camera_id = re.findall(r"\d+\.?\d*", line)[0]
        print('camera_id:', camera_id)
        camera_params[camera_id] = {}
    elif line.startswith('K_'):
        current_id = re.findall(r"\d+\.?\d*", line)[0]
        data = lines[i + 8]
        data_digital = re.findall(r"-?\d+\.?\d*", data)
        print('K data_digital:', data_digital)
        camera_params[current_id]['K'] = np.array(data_digital, dtype=float).flatten()
        print('camera_params[{}][K]:'.format(current_id), camera_params[current_id]['K'])
    elif line.startswith('dist_'):
        current_id = re.findall(r"\d+\.?\d*", line)[0]
        data = lines[i + 8]
        data_digital = re.findall(r"-?\d+\.?\d*", data)
        print('D data_digital:', data_digital)
        camera_params[current_id]['D'] = np.array(data_digital, dtype=float).flatten()
        print('camera_params[{}][D]:'.format(current_id), camera_params[current_id]['D'])

# extri_yaml = r'G:\MyData\XieData\extri.yml'
#23.2.13
extri_yaml = r'G:\MyData\EasyMocap\XieData\extri.yml'
extri_file = open(extri_yaml)
lines = extri_file.readlines()
for i, line in enumerate(lines):
    line = line.strip()
    if line.startswith('- "'):
        camera_id = re.findall(r"\d+\.?\d*", line)[0]
        print('camera_id:', camera_id)
        # camera_params[camera_id] = {}
    elif line.startswith('Rot_'):
        current_id = re.findall(r"\d+\.?\d*", line)[0]
        data = lines[i + 8]
        data_digital = re.findall(r"-?\d+\.?\d*", data)
        print('Rot data_digital:', data_digital)
        camera_params[current_id]['Rot'] = np.array(data_digital, dtype=float).flatten()
        print('camera_params[{}][Rot]:'.format(current_id), camera_params[current_id]['Rot'])
    elif line.startswith('T_'):
        current_id = re.findall(r"\d+\.?\d*", line)[0]
        data = lines[i + 8]
        data_digital = re.findall(r"-?\d+\.?\d*", data)
        print('T data_digital:', data_digital)
        camera_params[current_id]['T'] = np.array(data_digital, dtype=float).flatten() * 1000
        print('camera_params[{}][T]:'.format(current_id), camera_params[current_id]['T'])



# data_path = r'G:\MyData\XieData\10_9mv1pout7'
#23.2.13
data_path = r'G:\MyData\EasyMocap\XieData\10_9mv1pout7'
images_path = os.path.join(data_path, 'images')
output_path = data_path
start_frame = 1
image_num = 4757






# param_path = r'H:\dataset\A-NeRF\human3.6m\h36m\S1\Posing\annots.npy'
# params = np.load(param_path, allow_pickle=True).item()

# start_frame = 15275
# start_frame = 0
# image_num = 600
# image_num = 800
image_path = []
K = []
R = []
T = []
D = []

camera_ids = sorted(os.listdir(images_path), key=cmp_to_key(lambda a, b: int(a) - int(b)))
params = {'cams': {}, 'ims': []}
for camera_id in camera_ids:
    K.append(camera_params[camera_id]['K'].reshape((3, 3)))
    R.append(camera_params[camera_id]['Rot'].reshape((3, 3)))
    T.append(camera_params[camera_id]['T'].reshape((3, 1)))
    D.append(camera_params[camera_id]['D'].reshape((5, 1)))

for i in range(image_num):
    image_path = []
    for camera_id in camera_ids:
        # image_path.append(camera_id + '/{}.png'.format(start_frame+i))
        image_path.append(camera_id + '/{}.jpg'.format(start_frame + i))

    params['ims'].append({'ims': image_path})

params['cams']['K'] = K
params['cams']['R'] = R
params['cams']['T'] = T
params['cams']['D'] = D

# np.save(os.path.join(output_path, 'annots.npy'), params)
#23.2.13
np.save(r'G:\MyData\EasyMocap\XieData\annots.npy', params)