## 把杂乱数字的图片名字按顺序改为顺序数字的名字


import glob
import os


###  通用



path = r'G:\MyData\PhySG\male_3\male_3_casual\male_3_casual_workspace\train_10_29\mask2'
file_format = '.png'
## 通用改名
for file_path in glob.glob(path + '/*' + file_format):
    filename = os.path.basename(file_path)
    fileid = int(filename.split('.')[0])
    new_filename = '{:06d}'.format(fileid) + file_format
    os.replace(file_path, os.path.join(path, new_filename))

# ## zju313改名
# for file_path in glob.glob(path + '/*' + file_format):
#     filename = os.path.basename(file_path)
#     temp = filename.split('(')[1]
#     fileid = int(temp.split(')')[0])
#     new_filename = '{:06d}'.format(fileid) + file_format
#     os.replace(file_path, os.path.join(path, new_filename))


file_names = os.listdir(path)
file_names.sort()
print(file_names)
new_id = 0
for i in range(len(file_names)):
    # file_id = int(file_names[i].split('.')[0])
    new_file_name = '{:06d}'.format(new_id) + file_format
    os.replace(os.path.join(path, file_names[i]), os.path.join(path, new_file_name))
    new_id += 1