import cv2
import numpy as np
import os
import tqdm
import rawpy
import matplotlib.pyplot as plt
import glob


imrows = 2048
imcols = 2448
imsize = imrows*imcols


raw_path = r'F:\MyDataF\camera_data\Raw_Img_extrix_small'
# rgb_path = r''
target_format = 'png'

for raw_dir in tqdm.tqdm(os.listdir(raw_path), desc='dir'):
    raw_dir_path = os.path.join(raw_path, raw_dir)
    for raw_file_name in tqdm.tqdm(os.listdir(raw_dir_path), desc='images'):
        raw_file_path = os.path.join(raw_dir_path, raw_file_name)
        rgb_file_path = raw_file_path.replace('Raw_Img', 'Rgb_Img').replace('raw', target_format)
        os.makedirs(os.path.dirname(rgb_file_path), exist_ok=True)

        with open(raw_file_path, 'rb') as raw_img:
            bayer_img = np.fromfile(raw_img, np.dtype(np.uint8), imsize).reshape((imrows, imcols))
            color = cv2.cvtColor(bayer_img, cv2.COLOR_BAYER_BG2BGR)
            cv2.imwrite(rgb_file_path, color)




# file_path = r'C:\Users\Administrator\Desktop\temp\raw\Image_20230407101651669_w2448_h2048_pBayerRG8.raw'
# imrows = 2048
# imcols = 2448
# imsize = imrows*imcols
# with open(file_path, "rb") as rawimage:
#     bayer_img = np.fromfile(rawimage, np.dtype(np.uint8), imsize).reshape((imrows, imcols))
#     # bayer_img = np.fromfile(rawimage, np.dtype('u1')).reshape((imrows, imcols))
# colour = cv2.cvtColor(bayer_img, cv2.COLOR_BAYER_BG2BGR)
# cv2.namedWindow('cv2_colour', 0)
# cv2.imshow("cv2_colour", colour)
# cv2.waitKey()







# def pixel (img):
#     img = img.astype(np.float64)
#     pixel = lambda x,y : {
#         0: [ img[x][y] , (img[x][y-1] + img[x-1][y] + img[x+1][y] + img[x][y+1]) / 4 ,  (img[x-1][y-1] + img[x+1][y-1] + img[x-1][y+1] + img[x+1][y+1]) / 4 ] ,
#         1: [ (img[x-1][y] + img[x+1][y])  / 2,img[x][y] , (img[x][y-1] + img[x][y+1]) / 2 ],
#         2: [(img[x][y-1] + img[x][y+1]) / 2 ,img[x][y], (img[x-1][y] + img[x+1][y]) / 2],
#         3: [(img[x-1][y-1] + img[x+1][y-1] + img[x-1][y+1] + img[x+1][y+1]) / 4 , (img[x][y-1] + img[x-1][y] + img[x+1][y] + img[x][y+1]) / 4 ,img[x][y] ]
#     } [  x % 2 + (y % 2)*2]
#     res = np.zeros ( [    np.size(img,0) , np.size(img,1)  , 3] )
#     for x in range (1,np.size(img,0)-2):
#         for y in range (1,np.size(img,1)-2):
#             p = pixel(x,y)
#             p.reverse();
#             res[x][y] = p
#     res = res.astype(np.uint8)
#     return res
#
# def channel_break (img):
#     img = img.astype(np.float64)
#     red=np.copy (img);red [1::2,:]=0;red[:,1::2]=0
#     blue=np.copy (img);blue [0::2,:]=0;blue[:,0::2]=0
#     green=np.copy (img);green [0::2,0::2]=0;green [1::2,1::2]=0;
#     red = red.astype(np.float64)
#     blue = blue.astype(np.float64)
#     green = green.astype(np.float64)
#     return (red,green,blue)
#
# def rgb2gray(img):
#     res = np.zeros ( [    np.size(img,0) , np.size(img,1)  , 3] )
#     res = res.astype(np.float64)
#     for x in range (1,np.size(img,0)-1):
#         for y in range (1,np.size(img,1)-1):
#             res[x][y]=img[x][y][0]*0 + img[x][y][1]*0.5 + img[x][y][2]*0.5;
#     res = res.astype(np.uint8)
#     return res

# file_path = r'C:\Users\Administrator\Desktop\temp\raw\Image_20230407101651669_w2448_h2048_pBayerRG8.raw'
# imrows = 2048
# imcols = 2448
# imsize = imrows*imcols
# with open(file_path, "rb") as rawimage:
#     bayer_img = np.fromfile(rawimage, np.dtype('u1'), imsize).reshape((imrows, imcols))
#     # bayer_img = np.fromfile(rawimage, np.dtype('u1')).reshape((imrows, imcols))


# plot bayer imager
# plt.imshow(bayer_img)
# cv2.imshow('cv2bayer_img', bayer_img)
# cv2.waitKey()
# plt.title ('bayer img')
# plt.imsave('bayer_img.png', bayer_img)
#plt.show()


# this algorithm conversion
# rgb_res = pixel (bayer_img)
# plt.imshow(rgb_res)
# plt.title ('the article conversion')
# plt.imsave('the_article_conversion.png', rgb_res)
#plt.show()

# open cv conversion

# cv2.namedWindow('cv2_bayer_img', 0)
# cv2.imshow('cv2_bayer_img', bayer_img)
# cv2.waitKey()
# colour = cv2.cvtColor(bayer_img, cv2.COLOR_BAYER_BG2BGR)
# colour = cv2.cvtColor(bayer_img, cv2.COLOR_BAYER_RG2BGR)
# cv2.namedWindow('cv2_colour', 0)
# # cv2.resizeWindow('cv2_colour', 2048//2, 2448//2)
# cv2.imshow("cv2_colour", colour)
# cv2.waitKey()
# plt.imshow(colour)
# plt.title ('color image by open cv')
# plt.imsave('color_image_by_opencv.png', colour)
#plt.show()

# # convert to gray level
# gray = rgb2gray(rgb_res)
# plt.imshow(gray)
# plt.title ('gray conversion')
# plt.imsave('gray_level.png', gray)
# #plt.show()
#
#
# # break to RGB  channels
# RGB = channel_break(bayer_img)
# blue_only = pixel (RGB[0])
# plt.imshow(blue_only)
# plt.title ('blue only')
# plt.imsave('blue_only.png',blue_only)
# plt.show()
#
# green_only = pixel (RGB[1])
# plt.imshow(green_only)
# plt.title ('green only')
# plt.imsave('green_only.png',green_only)
# plt.show()
#
# red_only = pixel (RGB[2])
# plt.imshow(red_only)
# plt.title ('red only')
# plt.imsave('red_only.png',red_only)
# plt.show()




# 以下都不行





# file = r'C:\Users\Administrator\Desktop\temp\raw\Image_20230407101651669_w2448_h2048_pBayerRG8.raw'
# rawimg = np.fromfile(file, dtype=np.uint8).reshape(2048, 2448, 4)
# R = rawimg[0::2, 0::2]
# G0 = rawimg[0::2, 1::2]
# G1 = rawimg[1::2, 0::2]
# B = rawimg[1::2, 1::2]
# G = (G0 + G1) // 2
# out = np.dstack((B,G,R))
# out = cv2.cvtColor(out, cv2.COLOR_BAYER_RG2BGR)
# cv2.imshow('BGR', out)
# cv2.waitKey(0)
# # img = cv2.cvtColor(rawimg, cv2.COLOR_BAYER_RG2BGR)
# # rawimg = cv2.merge([rawimg[..., 0], rawimg[..., 1], rawimg[..., 2]])
# cv2.imshow("rawimg", rawimg[..., 3])
# cv2.waitKey(0)
# # cv2.imshow("img", img)
# # cv2.waitKey(0)






# path = "F:\IMAGE\small_orial_color".replace('\\', '/')
# save_path = "F:\IMAGE\small_orial_ir_png".replace('\\', '/')
# file_names = os.listdir(path)
#
# for name in file_names:
#     if "raw" in name:
#         print(path + "/" + name)
#         if "orial_rgb" in name:
#             #将raw格式的rgb转成png
#             rawImg = np.fromfile(path + "/" + name, dtype=np.uint8)
#             try:
#                 print('rawImg.shape', rawImg.shape)
#                 rawImg1 = rawImg[:635904].reshape(864, 736)
#                 rawImg2 = rawImg[635904:1271808].reshape(864, 736)
#                 rawImg3 = rawImg[1271808:].reshape(864, 736)
#                 rawImg = cv2.merge([rawImg1, rawImg2, rawImg3])
#                 h, w, d = rawImg.shape
#                 print(h, w, d)
#                 cv2.imshow("img", rawImg)
#                 cv2.waitKey(5)
#                 newName = name.replace("raw", "png")
#                 cv2.imwrite(save_path + "/" + newName, rawImg)
#             except:
#                 continue
#         elif "orial_depth" in name:
#             rawImg = np.fromfile(path + "/" + name, dtype=np.uint8)
#             try:
#                 rawImg = rawImg.reshape(112, 112)
#                 h, w = rawImg.shape
#                 print(h, w)
#                 cv2.imshow("img", rawImg)
#                 cv2.waitKey(5)
#                 newName = name.replace("raw", "png")
#                 cv2.imwrite(save_path + "/" + newName, rawImg)
#             except:
#                 continue
#         elif "orial_ir" in name:
#             rawImg = np.fromfile(path + "/" + name, dtype=np.uint16)
#             try:
#                 rawImg = rawImg.reshape(112, 112)
#                 h, w = rawImg.shape
#                 print(h, w)
#                 cv2.imshow("img", rawImg/4)
#                 cv2.waitKey(5)
#                 newName = name.replace("raw", "png")
#                 cv2.imwrite(save_path + "/" + newName, rawImg/4)
#             except:
#                 continue

