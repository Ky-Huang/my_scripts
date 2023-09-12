from Colmap.colmap_read_write_model import read_cameras_binary, read_images_binary, qvec2rotmat, read_cameras_text, read_images_text
import numpy as np
import os
data_dir = 'image_select_resize_2/'

cameras=read_cameras_text(data_dir+"cameras.txt")
images=read_images_text(data_dir+"images.txt")
K = np.eye(3)
K[0, 0] = cameras['1'].params[0]
K[1, 1] = cameras['1'].params[0]
K[0, 2] = cameras['1'].params[1]
K[1, 2] = cameras['1'].params[2]

cameras_npz_format = {}

image_ids = [id for id in images]

for id in range(len(image_ids)):
    print('scp {} image_select_2/{:04d}.JPG'.format(data_dir+images[image_ids[id]].name, id))
    os.system('scp {} image_select_2/{:04d}.JPG'.format(data_dir+images[image_ids[id]].name, id))
for ii in range(len(images)):
    cur_image=images[image_ids[ii]]

    M=np.zeros((3,4))
    M[:,3]=cur_image.tvec
    M[:3,:3]=qvec2rotmat(cur_image.qvec)
    M = M[:,[0,2,1,3]]
    M[:,2] = -M[:,2]
    
    P=np.eye(4)
    P[:3,:] = K@M
    cameras_npz_format['world_mat_%d' % ii] = P
    
np.savez(
        "image_select_2/camera.npz",
        **cameras_npz_format)