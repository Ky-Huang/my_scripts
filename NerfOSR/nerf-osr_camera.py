import json

import numpy as np
def convert_pose(C2W):
    flip_yz = np.eye(4)
    flip_yz[1, 1] = -1
    flip_yz[2, 2] = -1
    C2W = np.matmul(C2W, flip_yz)
    return C2W

camera_record = r'H:\xzx\building_1\camera_record.json'
out_camera_record = r'H:\xzx\building_1\camera_record_convert.json'
with open(camera_record, 'r') as f:
    cameras = json.load(f)
    for camera_name, camera_para in cameras.items():
        m_numpy = np.array(camera_para['m'])
        b = np.array([0,0,0,1])
        m_numpy = np.insert(m_numpy, 3, values=b, axis=0)
        m_numpy = convert_pose(m_numpy)
        m_numpy = np.linalg.inv(m_numpy)

        camera_para['m'] = m_numpy.tolist()
    with open(out_camera_record, 'w') as fd:
        json.dump(cameras, fd)