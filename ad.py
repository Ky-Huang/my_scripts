# !/usr/bin/env python
# -*-encoding: utf-8-*-
# author:LiYanwei
# version:0.1


import numpy as np
import cv2

import numpy as np
import glob
import os
import cv2
import re

import sys, os
import imageio.v2 as imageio
import skimage.io



def read_exr(exr_file):
    if not os.path.isfile(exr_file):
        return False

    filename, extension = os.path.splitext(exr_file)
    if not extension.lower().endswith('.exr'):
        return False

    img = imageio.imread(exr_file)
    # img = cv2.imread(exr_file)
    return img

# root_dir = r'E:\BaiduNetdiskDownload\for relighting quan  1128\rrengine_result_gt_1024_4k'
# for dir_4k in os.listdir(root_dir):
#     data_path = os.path.join(root_dir, dir_4k)
#     output_path = os.path.join(root_dir, '_PNG', dir_4k)
#     os.makedirs(output_path,exist_ok=True)
#     for file_path in glob.glob(data_path+'\*_gpu.exr'):
#         filename = os.path.basename(file_path).split('.')[0]
#         re_g = re.match('(.*)-(.*)_gpu',filename)
#         file_id = int(re_g.group(1))
#         cam_id = re_g.group(2)
#         out_file_path = os.path.join(output_path, '{}_{}'.format(file_id, cam_id) + '.png')
#         if os.path.exists(out_file_path):
#             continue
#         img = read_exr(file_path)
#         img = img[..., :3]
#
#         im_gamma_correct = np.clip(np.power(img, 0.45), 0, 1)
#         img = np.uint8(im_gamma_correct * 255)
#         img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)  #到这里相当于得到了rgb图，拼到下面去
#         os.makedirs(os.path.join(output_path, cam_id), exist_ok=True)
#
#
#         cv2.imwrite(out_file_path,img)


# 用上面一段代码吧exr转png试试，看转出来的颜色跟comparsion里面画出来的是否接近，差的多的话，用下面的代码调一下饱和度，下面的代码是ldr的，所以上面的代码先把hdr转ldr

def preprocess(image):
    fImg = image.astype(np.float32)
    fImg = fImg / 255.0
    hlsImg = cv2.cvtColor(fImg, cv2.COLOR_BGR2HLS)
    # hlsCopy = np.copy(hlsImg)
    # hlsCopy = cv2.cvtColor(hlsCopy, cv2.COLOR_HLS2BGR)
    # cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("image", 800, 800)
    # cv2.imshow("image", hlsCopy)
    # cv2.waitKey(0)
    return hlsImg


def main2():

    root_dir = r'E:\BaiduNetdiskDownload\for relighting quan  1128\download\download'
    for dataset in os.listdir(root_dir):
        dataset_dir = os.path.join(root_dir, dataset)
        gt_dir = os.path.join(dataset_dir, 'gt')
        mask_dir = os.path.join(dataset_dir, 'mask')
        names = os.listdir(dataset_dir)
        psnr = []
        psnr_nums = []
        ssim = []
        ssim_nums = []
        for name in names:
            if name == 'gt' or name == 'mask' or name == 'bbox' or name == 'psnr_ssim.json':
                continue
            pred = cv2.imread(os.path.join(dataset_dir, name), cv2.IMREAD_COLOR)
            gt = cv2.imread(os.path.join(gt_dir, name), cv2.IMREAD_COLOR)
            gt_copy = np.copy(gt)
            mask = cv2.imread(os.path.join(mask_dir, name), cv2.IMREAD_GRAYSCALE)
            x, y, w, h = cv2.boundingRect(mask)
            # x, y, w, h = cv2.boundingRect(mask.astype(np.uint8))
            crop_img_pred = pred[y:y + h, x:x + w]
            crop_img_gt = gt[y:y +h, x:x + w]

            # l_ratio = preprocess(gt_image)[0, 0, 1] / preprocess(render_image)[0, 0, 1]
            # s_ratio = preprocess(gt_image)[0, 0, 2] / preprocess(render_image)[0, 0, 2]
            # l_ratio = preprocess(crop_img_gt)[0, :, 1] / preprocess(crop_img_pred)[0, :, 1]
            # s_ratio = preprocess(crop_img_gt)[0, :, 2][preprocess(crop_img_pred)[0, :, 2] != 0] / preprocess(crop_img_pred)[0, :, 2][preprocess(crop_img_pred)[0, :, 2] != 0]
            l_ratio = preprocess(crop_img_gt)[..., 1][preprocess(crop_img_pred)[..., 1] > 0.1] / preprocess(crop_img_pred)[..., 1][preprocess(crop_img_pred)[..., 1] > 0.1]
            s_ratio = preprocess(crop_img_gt)[..., 2][preprocess(crop_img_pred)[..., 2] > 0.1] / preprocess(crop_img_pred)[..., 2][preprocess(crop_img_pred)[..., 2] > 0.1]
            l_ratio = np.mean(l_ratio)
            s_ratio = np.mean(s_ratio)
            print(l_ratio, s_ratio)
            out_image_hls = np.copy(preprocess(crop_img_gt))
            out_image_hls[..., 1] = out_image_hls[..., 1] / l_ratio
            out_image_hls[..., 2] = out_image_hls[..., 2] / s_ratio
            out_image_hls = cv2.cvtColor(out_image_hls, cv2.COLOR_HLS2BGR)
            cv2.namedWindow("out image", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("out image", 800, 800)
            cv2.imshow("out image", out_image_hls)
            cv2.waitKey(0)
            gt_hls = np.copy(preprocess(gt))
            # l_ratio = 1.0
            # s_ratio = 1.0
            gt_hls[..., 1] = np.clip(gt_hls[..., 1] / l_ratio, 0, 1)
            gt_hls[..., 2] = np.clip(gt_hls[..., 2] / s_ratio, 0, 1)
            gt_hls = cv2.cvtColor(gt_hls, cv2.COLOR_HLS2BGR)
            cv2.namedWindow("out image gt", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("out image gt", 800, 800)
            cv2.imshow("out image gt", gt_hls)
            for_save = (gt_hls * 255).astype(np.uint8)
            cv2.imwrite(os.path.join(gt_dir, 'ratio' + name), for_save)

    # gt_image = cv2.imread(r'E:\BaiduNetdiskDownload\for relighting quan\for relighting quan\png\circus\5\00121.png',
    #                           cv2.IMREAD_COLOR)
    # 
    # render_image = cv2.imread(
    #     r'E:\BaiduNetdiskDownload\for relighting quan\for relighting quan\comparison-4k-spareview\circus_arena_4k\frame0121_view0005_rgb_render.png',
    #     cv2.IMREAD_COLOR)
    # gt_image = cv2.resize(gt_image, (512, 512))
    # # l_ratio = preprocess(gt_image)[0, 0, 1] / preprocess(render_image)[0, 0, 1]
    # # s_ratio = preprocess(gt_image)[0, 0, 2] / preprocess(render_image)[0, 0, 2]
    # l_ratio = preprocess(gt_image)[0, :, 1] / preprocess(render_image)[0, :, 1]
    # s_ratio = preprocess(gt_image)[0, :, 2][preprocess(render_image)[0, :, 2] != 0] / preprocess(render_image)[0, :, 2][preprocess(render_image)[0, :, 2] != 0]
    # # l_ratio = preprocess(gt_image)[..., 1] / preprocess(render_image)[..., 1]
    # # s_ratio = preprocess(gt_image)[..., 2][preprocess(render_image)[..., 2] != 0] / preprocess(render_image)[..., 2][preprocess(render_image)[..., 2] != 0]
    # l_ratio = np.mean(l_ratio)
    # s_ratio = np.mean(s_ratio)
    # print( l_ratio, s_ratio)
    # out_image_hls = np.copy(preprocess(render_image))
    # out_image_hls[..., 1] = out_image_hls[..., 1] * l_ratio
    # out_image_hls[..., 2] = out_image_hls[..., 2] * s_ratio
    # out_image_hls = cv2.cvtColor(out_image_hls, cv2.COLOR_HLS2BGR)
    # cv2.namedWindow("out image", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("out image", 800, 800)
    # cv2.imshow("out image", out_image_hls)
    # cv2.waitKey(0)


def main():
    # 加载图片 读取彩色图像
    # image = cv2.imread('./couryard/121-7_gpu.png', cv2.IMREAD_COLOR)
    image = cv2.imread(r'G:\MyData\evl\for relighting quan  1128\rrengine_result_gt_1024_4k\_PNG\venice\121_9.png',
                       cv2.IMREAD_COLOR)
    # print(image)
    # cv2.imshow("image", image)
    # 图像归一化，且转换为浮点型
    fImg = image.astype(np.float32)
    fImg = fImg / 255.0
    # 颜色空间转换 BGR转为HLS
    hlsImg = cv2.cvtColor(fImg, cv2.COLOR_BGR2HLS)
    l = 100
    s = 100
    MAX_VALUE = 100
    # 调节饱和度和亮度的窗口
    cv2.namedWindow("l and s", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("l and s", 1000, 1000)

    def nothing(*arg):
        pass

    # 滑动块
    cv2.createTrackbar("l", "l and s", l, MAX_VALUE, nothing)
    cv2.createTrackbar("s", "l and s", s, MAX_VALUE, nothing)
    # 调整饱和度和亮度后的效果
    lsImg = np.zeros(image.shape, np.float32)
    # 调整饱和度和亮度
    while True:
        # 复制
        hlsCopy = np.copy(hlsImg)
        # 得到 l 和 s 的值
        l = cv2.getTrackbarPos('l', 'l and s')
        s = cv2.getTrackbarPos('s', 'l and s')
        # 1.调整亮度（线性变换) , 2.将hlsCopy[:, :, 1]和hlsCopy[:, :, 2]中大于1的全部截取
        hlsCopy[:, :, 1] = (0.1 + l / float(MAX_VALUE)) * hlsCopy[:, :, 1]
        hlsCopy[:, :, 1][hlsCopy[:, :, 1] > 1] = 1
        # 饱和度
        hlsCopy[:, :, 2] = (0.1 + s / float(MAX_VALUE)) * hlsCopy[:, :, 2]
        hlsCopy[:, :, 2][hlsCopy[:, :, 2] > 1] = 1
        # HLS2BGR
        lsImg = cv2.cvtColor(hlsCopy, cv2.COLOR_HLS2BGR)
        # 显示调整后的效果
        cv2.imshow("l and s", lsImg)

        ch = cv2.waitKey(5)
        # 按 ESC 键退出
        if ch == 27:
            break
        elif ch == ord('s'):
            # 按 s 键保存并退出
            # 保存结果
            lsImg = lsImg * 255
            lsImg = lsImg.astype(np.uint8)
            cv2.imwrite("lsImg.jpg", lsImg)
            break

    # 关闭所有的窗口
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
