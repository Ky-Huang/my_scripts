## 使用opencv转换图片格式

import glob
import os.path

import numpy as np
import cv2

os.environ["OPENCV_IO_ENABLE_OPENEXR"] = "1"

input_dir = r'G:\MyData\PhySG\kitty_copy\train\image'
output_dir = r'G:\MyData\PhySG\kitty_copy\train\image2'
for image_path in glob.glob(input_dir + '/*.exr'):
    image_name = os.path.basename(image_path)
    new_image_name = image_name.split('.')[0] + '.png'
    image = cv2.imread(image_path, -1)
    image = image * 65535
    image[image > 65535] = 65535
    image = np.uint16(image)
    cv2.imwrite(os.path.join(output_dir, new_image_name), image)
    # im = cv2.imread("torus.exr", -1)
    # im = im * 65535
    # im[im > 65535] = 65535
    # im = np.uint16(im)
    # cv2.imwrite("torus.png", im)

input_dir = r'G:\MyData\PhySG\kitty_copy\train\image2'
output_dir = r'G:\MyData\PhySG\kitty_copy\train\image2'
for image_path in glob.glob(input_dir + '/*.png'):
    image_name = os.path.basename(image_path)
    new_image_name = image_name.split('.')[0] + '.jpg'
    image = cv2.imread(image_path, -1)
    cv2.imwrite(os.path.join(output_dir, new_image_name), image)

#
# # !/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# import sys
#
# import numpy
#
# import OpenEXR
# import Imath
# import Image
#
#
# # refer:
# # * [OpenEXR interfacing with other packages][1]
# # * [Converting Linear EXR to sRGB JPEG with Python?][2]
# #
# # [1]: http://excamera.com/articles/26/doc/intro.html
# # [2]: http://tech-artists.org/forum/showthread.php?2339-Converting-Linear-EXR-to-sRGB-JPEG-with-Python
# #
#
# def ConvertEXRToJPG(exrfile, jpgfile):
#     File = OpenEXR.InputFile(exrfile)
#     PixType = Imath.PixelType(Imath.PixelType.FLOAT)
#     DW = File.header()['dataWindow']
#     Size = (DW.max.x - DW.min.x + 1, DW.max.y - DW.min.y + 1)
#
#     rgb = [numpy.fromstring(File.channel(c, PixType), dtype=numpy.float32) for c in 'RGB']
#     for i in range(3):
#         rgb[i] = numpy.where(rgb[i] <= 0.0031308,
#                              (rgb[i] * 12.92) * 255.0,
#                              (1.055 * (rgb[i] ** (1.0 / 2.4)) - 0.055) * 255.0)
#
#     rgb8 = [Image.fromstring("F", Size, c.tostring()).convert("L") for c in rgb]
#     # rgb8 = [Image.fromarray(c.astype(int)) for c in rgb]
#     Image.merge("RGB", rgb8).save(jpgfile, "JPEG", quality=95)
#
#
# def EncodeToSRGB(v):
#     if (v <= 0.0031308):
#         return (v * 12.92) * 255.0
#     else:
#         return (1.055 * (v ** (1.0 / 2.4)) - 0.055) * 255.0
#
#
# def main(argv=sys.argv[:]):
#     # print 'from %s to %s' % (argv[1], argv[2])
#     ConvertEXRToJPG(argv[1], argv[2])
#     return 0
#
#
# if __name__ == '__main__':
#     sys.exit(main())


### 转视频格式

input = r''
output = r''

from tqdm import tqdm

video_path = r'F:\video_rgb.mp4'
out_path = r'F:\video_rgb_t.mp4'


cap = cv2.VideoCapture(video_path)
frame_cnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
weight = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(cap.get(cv2.CAP_PROP_FPS))

size = (weight, height)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(out_path, fourcc, fps, size)  # fourcc是编码格式，size是图片尺寸
for n in tqdm(range(frame_cnt)):
    # print('视频合成进度:', n, frame_cnt)
    ret, frame = cap.read()
    # cv2.imshow('frame', frame)
    out.write(frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
out.release()
