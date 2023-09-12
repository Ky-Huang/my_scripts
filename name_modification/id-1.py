import os
import glob



##  id - 1
data_path = r'C:\Users\Administrator\Desktop\temp\repose\manuel\new_params'

for file_path in glob.glob(data_path + '/*.npy'):
    filename = os.path.basename(file_path)
    fileid = int(filename.split('.')[0])
    new_filename = '{}.npy'.format(fileid - 1)
    os.replace(file_path, os.path.join(data_path, new_filename))