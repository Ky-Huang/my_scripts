# MIP-real的数据到annots.npy

import os
import numpy as np
import cv2
from functools import cmp_to_key

data_path = r'E:\BaiduNetdiskDownload\MPI\for_texture500'
calib_file_path = os.path.join(data_path,'cameras.calibration')
images_path = os.path.join(data_path,'images')
output_path = os.path.join(data_path,r'output\smpl')
camera_params = {}
with open(calib_file_path) as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith('name'):
            camera_id = line.split()[-1]
            camera_params[camera_id] = {}
        elif line.startswith('intrinsic'):
            intrinsic = np.asarray(line.split()[1:],dtype=float).reshape((4,4))
            camera_params[camera_id]['K'] = intrinsic[:3,:3].flatten()
            camera_params[camera_id]['D'] = np.zeros((5,1))
        elif line.startswith('extrinsic'):
            extrinsic = np.asarray(line.split()[1:],dtype=float).reshape((4,4))
            Rot = extrinsic[:3,:3]
            camera_params[camera_id]['Rot'] = Rot.flatten()
            camera_params[camera_id]['R'] = cv2.Rodrigues(Rot)[0].flatten()
            camera_params[camera_id]['T'] = extrinsic[:3,3].flatten()
        elif line.startswith('radial'):
            radial = float(line.split()[1])
            camera_params[camera_id]['radial'] = radial


# param_path = r'H:\dataset\A-NeRF\human3.6m\h36m\S1\Posing\annots.npy'
# params = np.load(param_path, allow_pickle=True).item()
start_frame = 15275
image_num = 600
image_path = []
K = []
R = []
T = []
D = []

camera_ids = sorted(os.listdir(images_path),key=cmp_to_key(lambda a, b: int(a) - int(b)))
params = {'cams':{},'ims':[]}
for camera_id in camera_ids:
    K.append(camera_params[camera_id]['K'].reshape((3,3)))
    R.append(camera_params[camera_id]['Rot'].reshape((3, 3)))
    T.append(camera_params[camera_id]['T'].reshape((3, 1)))
    D.append(camera_params[camera_id]['D'].reshape((5, 1)))


for i in range(image_num):
    image_path = []
    for camera_id in camera_ids:
        image_path.append(camera_id + '/{}.png'.format(start_frame+i))
    params['ims'].append({'ims': image_path})


params['cams']['K'] = K
params['cams']['R'] = R
params['cams']['T'] = T
params['cams']['D'] = D

np.save(os.path.join(output_path,'annots.npy'),params)