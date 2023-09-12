import os
import glob
import shutil
import tqdm


data_path = r'C:\Users\Administrator\Desktop\temp\repose\manuel\new_params'

for file_path in glob.glob(data_path + '/*.npy'):
    filename = os.path.basename(file_path)
    fileid = int(filename.split('.')[0])
    new_filename = '{}.npy'.format(fileid)
    os.replace(file_path, os.path.join(data_path, new_filename))

# ## for image
# data_path = r'/workspace/xrg/animatable_nerf/data/zjlab_mocap/red/images'
# data_path = r'/workspace/xrg/animatable_nerf/data/zjlab_mocap/red__resized_images_10_24'
# views = os.listdir(data_path)
# print(views)
# for view in views:
#     print("unzero")
#     print(view)
#     view_path = os.path.join(data_path,view)
#     for file_path in glob.glob(view_path+'/*.jpg'):
#         filename = os.path.basename(file_path)
#         if 'vis' in filename:
#             os.remove(file_path)
#         else:
#             fileid = int(filename.split('.')[0])
#             new_filename = '{}.jpg'.format(fileid)
#             os.replace(file_path,os.path.join(view_path,new_filename))



## for mask
# data_path = r'/workspace/xrg/animatable_nerf/data/zjlab_mocap/red/mask'
# views = os.listdir(data_path)
# print(views)
# for view in views:
#     print("unzero")
#     print(view)
#     view_path = os.path.join(data_path,view)
#     for file_path in glob.glob(view_path+'/cihp_parsing_maps/*.png'):
#         filename = os.path.basename(file_path)
#         if 'vis' in filename:
#             pass
#         else:
#             fileid = int(filename.split('.')[0])
#             new_filename = '{}.png'.format(fileid)
#             shutil.copyfile(file_path,os.path.join(view_path,new_filename))