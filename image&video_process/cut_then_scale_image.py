## 裁剪然后resize图片


# coding: utf-8
from PIL import Image
import os
import numpy as np
import cv2
import glob

input_root =  r'F:\MyDataF\6ae3096788db279f5cc2b79e8aef2da.jpg'
output_root = r'F:\MyDataF\6ae3096788db279f5cc2b79e8aef2da.jpg'


### humannerf
input_dir = r'G:\MyData\HumanNeRF\jinitaimei_images'
for input_image in glob.glob(input_dir + '/*.png'):
    ori_img = cv2.imread(input_image)
    # crop_img = ori_img[:, :1280, :]                                                             # 裁切[高，宽，rgb]
    resized_image = cv2.resize(ori_img, (ori_img.size[1]//2, ori_img.size[0]//2), interpolation=cv2.INTER_LINEAR)           # resize
    cv2.imwrite(input_image, resized_image)




# #### using opencv resize
# for input_image in glob.glob(input_root + '/*.png'):
#     ori_img = cv2.imread(input_image)
#     resized_image = cv2.resize(ori_img, (512, 512), interpolation=cv2.INTER_LINEAR)
#     cv2.imwrite(output_root + '/' + os.path.basename(input_image), resized_image)

# ### using opencv crop 给最后的结果画红框框用的
# input_image0 = r'G:\MyData\temp\lightprobes_ablation\single836_0.png'
# output_image0 = r'G:\MyData\temp\lightprobes_ablation\final_single836_0.png'
# input_image1 = r'G:\MyData\temp\lightprobes_ablation\single836_1.png'
# output_image1 = r'G:\MyData\temp\lightprobes_ablation\final_single836_1.png'
# ori_img0 = cv2.imread(input_image0)
# ori_img1 = cv2.imread(input_image1)
# head1 = ori_img1[125:190, 225:270]
# arm1 = ori_img1[205:270, 155:210]
# head0 = ori_img0[105:170, 220:265]
# arm0 = ori_img0[185:250, 150:205]
# print(f'\nhead:{head0.shape}\narm:{arm0.shape}')
# head0 = cv2.resize(head0, (0, 0), fx=55.0/45.0, fy=55.0/45.0)
# # cv2.resize(head0, (90, 110))
# head1 = cv2.resize(head1, (0, 0), fx=55.0/45.0, fy=55.0/45.0)
# print(f'\nhead:{head0.shape}\narm:{arm0.shape}')
# cv2.imshow('head0', head0)
# cv2.waitKey(0)
# cv2.imshow('arm0', arm0)
# cv2.waitKey(0)
# cv2.imshow('head1', head1)
# cv2.waitKey(0)
# cv2.imshow('arm1', arm1)
# cv2.waitKey(0)
# head_arm0 = np.concatenate((head0, arm0), axis=0)
# head_arm1 = np.concatenate((head1, arm1), axis=0)
# cv2.imshow('head_arm0', head_arm0)
# cv2.waitKey(0)
# cv2.rectangle(ori_img1, (225, 125), (270, 190), (0, 0, 255), 2)
# cv2.rectangle(ori_img1, (155, 205), (210, 270), (0, 97, 255), 2)
# cv2.rectangle(ori_img0, (220, 105), (265, 170), (0, 0, 255), 2)
# cv2.rectangle(ori_img0, (150, 185), (205, 250), (0, 97, 255), 2)
# # cv2.imwrite(output_image0, ori_img0)
# # cv2.imwrite(output_image1, ori_img1)
# croped_img0 = ori_img0[100:410, 140:340]
# croped_img1 = ori_img1[115:425, 140:340]
# head_arm0 = cv2.resize(head_arm0, None, fx=310.0/144.0, fy=310/144.0)
# head_arm1 = cv2.resize(head_arm1, None, fx=310.0/144.0, fy=310/144.0)
# final_img0 = np.concatenate((croped_img0, head_arm0), axis=1)
# final_img1 = np.concatenate((croped_img1, head_arm1), axis=1)
# cv2.imshow('final img0', final_img0)
# cv2.waitKey()
# cv2.imwrite(output_image0, final_img0)
# cv2.imwrite(output_image1, final_img1)
# black_img = np.zeros((310,200,3), np.uint8)





#####   using PIL.Image
# views = os.listdir(input_root)
# for view in views:
#     current_dir = os.path.join(input_root, view)
#     output_dir = os.path.join(output_root, view)
#     for parent, dirnames, filenames in os.walk(current_dir):
#         for filename in filenames:
#             # print('parent is :' + parent)
#             # print('filename is :' + filename)
#             currentPath = os.path.join(parent, filename)
#             # print('the fulll name of the file is :' + currentPath)
#
#             img = Image.open(currentPath)
#             # print(img.format, img.size, img.mode)
#             # img.show()
#
#             box1 = (840, 0, 3000, 2160)
#             image1 = img.crop(box1)
#             image1_resize = image1.resize((1080, 1080))
#             image1_resize.save(output_dir + '\\' + filename)
#             print(f"{filename} done.")



# ########   using opencv
# views = os.listdir(input_root)
# target_num = [x for x in range(190, 811)]
# print("target_num:", target_num)
# for view in views:
#     current_dir = os.path.join(input_root, view)
#     output_dir = os.path.join(output_root, view)
#     os.makedirs(output_dir, exist_ok=True)
#     for parent, dirnames, filenames in os.walk(current_dir):
#         for filename in filenames:
#             # print('parent is :' + parent)
#             # print('filename is :' + filename)
#             if int(filename.split('.')[0]) not in target_num:
#                 print(int(filename.split('.')[0]))
#                 continue
#             currentPath = os.path.join(parent, filename)
#             # print('the fulll name of the file is :' + currentPath)
#
#             img = cv2.imread(currentPath)
#             # print(img.format, img.size, img.mode)
#             # img.show()
#
#             cropped_image = img[0:2160, 840:3000]
#             resized_image = cv2.resize(cropped_image, (1080, 1080), interpolation=cv2.INTER_LINEAR)
#             cv2.imwrite(output_dir + '\\' + filename, resized_image)
#             print(f"{filename} done.")


# img = cv2.imread(r"G:\MyData\10_10_new_data\10101644\red\images\1\000001.jpg")
# # print(img.shape)
# # cv2.imshow("img", img)
# # cv2.waitKey(0)
# cropped_image = img[0:2160, 840:3000]
# # cv2.imshow("cropped", cropped_image)
# # cv2.waitKey(0)
# # print(cropped_image.shape)
# resized_image = cv2.resize(cropped_image, (1080, 1080), interpolation=cv2.INTER_LINEAR)
# # cv2.imshow("resized", cropped_image)
# # cv2.waitKey(0)
# # print(resized_image.shape)
# cv2.imwrite(r"G:\MyData\10_10_new_data\10101644\red\images\1\1.jpg", resized_image)
