import os
import glob



##  id - 1
data_path = r'E:\BaiduNetdiskDownload\synth\megan_dance_04_xie\easymocp\mv1pout2\new_vertices'

for file_path in sorted(glob.glob(data_path + '/*.npy'), reverse=False):             # 注意reverse
    filename = os.path.basename(file_path)
    fileid = int(filename.split('.')[0])
    new_filename = '{}.npy'.format(fileid -10)
    if os.path.exists(os.path.join(data_path, new_filename)):
        raise
    os.replace(file_path, os.path.join(data_path, new_filename))