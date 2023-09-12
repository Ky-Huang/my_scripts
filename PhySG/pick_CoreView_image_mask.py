## 从CoreView系列数据集取帧和mask，用作PySG输入
import os
import shutil

input_path = r'G:\MyData\PhySG\CoreView_313\image'
output_path = r'G:\MyData\PhySG\zju313_10_30\test2\image'
target_frame = '0100'


## 用于CoreView313,377  image,mask
CoreView_313 = False
CoreView_377 = False
if 'CoreView_377' in input_path:
    CoreView_377 = True
if 'CoreView_313' in input_path:
    CoreView_313 = True
camera_id = None

cameras = os.listdir(input_path)
for camera in cameras:
    if CoreView_377:
        camera_id = int(camera.split('B')[1])
    elif CoreView_313:
        camera_id = int(camera.split('(')[1].split(')')[0])
    for image_name in os.listdir(os.path.join(input_path, camera)):
        if target_frame in image_name:
            target_frame_name = image_name
            shutil.copyfile(os.path.join(input_path, camera, target_frame_name),
                            os.path.join(output_path, '{:06d}.png'.format(camera_id - 1)))
