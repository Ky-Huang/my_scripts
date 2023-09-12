##

import os.path
import shutil

image_path = r'C:\Users\Administrator\Desktop\camera_data\intrix_data\output\calibration'
json_path = r'C:\Users\Administrator\Desktop\9_28calibration_data\intrix_data\images'
target_json_path = r'C:\Users\Administrator\Desktop\camera_data\intrix_data\images'

if 0:
    for i in range(2):
        current_sub_image_path = os.path.join(image_path, '{}'.format(i + 1))
        current_sub_json_path = os.path.join(json_path, '{}'.format(i + 1))
        current_target_json_path = os.path.join(target_json_path, '{}'.format(i + 1))
        for image_name in os.listdir(current_sub_image_path):
            json_name = image_name.split('.')[0] + '.json'
            shutil.copyfile(os.path.join(current_sub_json_path, json_name),
                            os.path.join(current_target_json_path, json_name))


for i in range(2):
    current_sub_image_path = os.path.join(image_path, '{}'.format(i + 1))
    current_sub_json_path = os.path.join(json_path, '{}'.format(i + 1))
    current_target_json_path = os.path.join(target_json_path, '{}'.format(i + 1))
    for image_name in os.listdir(current_sub_image_path):
        shutil.copyfile(os.path.join(current_sub_json_path, image_name),
                        os.path.join(current_target_json_path, image_name))
