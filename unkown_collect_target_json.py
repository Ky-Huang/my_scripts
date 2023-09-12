##

import os.path
import shutil

image_dir = r'G:\MyData\9_22_new_data\src_xxtrix_data\extrix_data\output\calibration\round1\round2\round3\round4'
json_dir = r'G:\MyData\9_22_new_data\src_xxtrix_data\extrix_data\chessboard'
save_dir = r'G:\MyData\9_22_new_data\src_xxtrix_data\extrix_data\output\calibration\round1\round2\round3\round4\chessboard'

for i in range(4):
    current_image_path = os.path.join(image_dir, "{}".format(i + 1))
    current_json_path = os.path.join(json_dir, '{}'.format(i + 1))
    current_save_path = os.path.join(save_dir, '{}'.format(i + 1))
    for image_name in os.listdir(current_image_path):
        json_name = image_name.replace('jpg', 'json')
        shutil.copyfile(os.path.join(current_json_path, json_name), os.path.join(current_save_path, json_name))
