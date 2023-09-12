## 给图片的名字填0


import os
import glob



# ##  修改image.jpg的名字      PySG用
# data_path = r'C:\Users\Administrator\Desktop\temp\repose\m2c\new_vertices'
#
# for file_path in glob.glob(data_path + '/*.npy'):
#     filename = os.path.basename(file_path)
#     fileid = int(filename.split('.')[0])
#     new_filename = '{:06d}.npy'.format(fileid)
#     os.replace(file_path, os.path.join(data_path, new_filename))

##  修改image.jpg的名字
# data_path = r'G:\MyData\repose\manuel_dancing\images'
# views = os.listdir(data_path)
# for view in views:
#     view_path = os.path.join(data_path, view)
#     for file_path in glob.glob(view_path + '/*.png'):
#         filename = os.path.basename(file_path)
#         fileid = int(filename.split('.')[0])
#         new_filename = '{:06d}.jpg'.format(fileid)
#         os.replace(file_path, os.path.join(view_path, new_filename))




# #   修改openpose.json的名字
data_path = r'G:\MyData\repose\manuel_dancing\openpose'
views = os.listdir(data_path)
for view in views:
    view_path = os.path.join(data_path, view)
    for file_path in glob.glob(view_path + '/*.json'):
        filename = os.path.basename(file_path)
        fileid = int(filename.split('_')[0])
        new_filename = '{:06d}_keypoints.json'.format(fileid)
        os.replace(file_path, os.path.join(view_path, new_filename))
        # TODO
        pass



##   修改chessboard.json的名字
# data_path = r'G:\MyData\camera_data\extrix_data\chessboard'
# views = os.listdir(data_path)
# for view in views:
#     view_path = os.path.join(data_path, view)
#     for file_path in glob.glob(view_path + '/*.json'):
#         filename = os.path.basename(file_path)
#         fileid = int(filename.split('.')[0])
#         new_filename = '{:06d}.json'.format(fileid)
#         os.replace(file_path, os.path.join(view_path, new_filename))