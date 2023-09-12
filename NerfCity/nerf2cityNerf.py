# 把nerf转成cityNerf需要的格式

from Colmap.colmap_read_write_model import read_cameras_binary, read_images_binary, qvec2rotmat, read_cameras_text, read_images_text
import numpy as np
import json

transforms_path = r'F:\MyDataF\xihu_square\colmap\transforms.json'
poses_enu_path = r'F:\MyDataF\xihu_square\colmap\poses_enu2.json'

with open(transforms_path, 'r') as f:
    data = json.load(f)
poses = []
t = []
for i in range(len(data['frames'])):
    transform_matrix = data['frames'][i]['transform_matrix']
    cur_pose = transform_matrix[0] + [999] + transform_matrix[1] + [999] + transform_matrix[2] + [4301.937092164707, 1000, 1001]
    poses.append(cur_pose)
    t.append(transform_matrix[0][3])
    t.append(transform_matrix[1][3])
    t.append(transform_matrix[2][3])

t = np.array(t)
scale = 2**3 * np.pi / max(t.max(), -t.min())
t = max(t.max(), -t.min())
scene_origin = [
        0.0,
        0.0,
        -6371011.0
    ]
scale_split = [
        325,
        195,
        65,
        0
    ]
cam_pose = {'poses' : poses,
            'scene_scale' : scale,
            'scene_origin' : [0., 0., -6371011.], # earth center is fixed in ENU coord
            'scale_split' : scale_split,
            't' : t,
            }
with open(poses_enu_path, 'w') as f:
    json.dump(cam_pose, f)