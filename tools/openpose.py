import numpy as np
import os
import subprocess


openpose_path=r'D:\environment\Openpose\openpose'
# data_path = r'G:\MyData\XieData\todo_images\red\images'
# output_path = r'G:\MyData\XieData\todo_images\red\openpose'
data_path = r'E:\BaiduNetdiskDownload\MPI\for_texture\images'
output_path = os.path.join(data_path, '..\openpose')
os.makedirs(output_path,exist_ok=True)

views = os.listdir(data_path)
for view in views:
    view_path = os.path.join(data_path,view)
    p1 = '--hand'
    p2 = '--face'
    p3 = '--image_dir'
    p4 = view_path
    p5 = '--write_json'
    outjson_path=os.path.join(output_path,view)
    os.makedirs(outjson_path,exist_ok=True)
    p6=outjson_path
    p7='-display'
    p8='0'
    p9='-render_pose'
    p10='0'
    #运行参数格式化
    para = "%s \"%s\" \"%s\" \"%s\" \"%s\" \"%s\" \"%s\" \"%s\" \"%s\" \"%s\" \"%s\""%('bin\OpenPoseDemo', p1, p2, p3, p4, p5, p6,
                                                                                       p7, p8, p9, p10)
    # para = "%s \"%s\" \"%s\" \"%s\" \"%s\" \"%s\" \"%s\" \"%s\" \"%s\""%('bin\OpenPoseDemo', p1, p2, p3, p4, p5, p6, p7, p8)
    #os.system(para)
    subprocess.check_call(para, shell=True, cwd=openpose_path)


