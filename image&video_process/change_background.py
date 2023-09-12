import glob
import os

import cv2

# ### 把mask以外的地方（背景）换成gt
# gt_dir = r'G:\MyData\PhySG\CoreView_313\PySGoutput\default-zju313_10_30png\test1\change_background\gt'
# mask_dir = r'G:\MyData\PhySG\CoreView_313\PySGoutput\default-zju313_10_30png\test1\change_background\mask'
# tobe_changed_dir = r'G:\MyData\PhySG\CoreView_313\PySGoutput\default-zju313_10_30png\test1\change_background\tobe_changed'
#
# for mask_path in glob.glob(mask_dir + '/*.png'):
#     mask = cv2.imread(mask_path)
#     mask_id = os.path.basename(mask_path).split('.')[0]
#     gt = None
#     tobe = None
#     for gt_path in glob.glob(gt_dir + '/*.png'):
#         if mask_id in gt_path:
#             gt = cv2.imread(gt_path)
#             break
#     for tobe_path in glob.glob(tobe_changed_dir + '/*.png'):
#         if mask_id in tobe_path:
#             tobe = cv2.imread(tobe_path)
#             output_path = tobe_path
#             break
#     if gt is None or tobe is None:
#         raise RuntimeError('no gt or tobe')
#
#     for i in range(mask.shape[0]):
#         for j in range(mask.shape[1]):
#             if int(mask[i][j].sum()) == 0:
#                 tobe[i][j] = gt[i][j]
#     cv2.imwrite(output_path, tobe)


## 把全白的地方换成全黑
image_dir = r'G:\MyData\PhySG\CoreView_313\PySGoutput\default-zju313_10_30png\test1_relight_studio_garden_4k'
for image_path in glob.glob(image_dir + '/*.png'):
    image = cv2.imread(image_path)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if int(image[i][j].sum()) == 255*3:
                image[i][j] = (0, 0, 0)
    cv2.imwrite(image_path, image)

# ### 写roughness
# image_dir = r'G:\MyData\PhySG\CoreView_313\PySGoutput\default-zju313_10_30png\test1\change_background\CoreView313_eval_frame0'
# # roughness = 0.823
# roughness = 0.9617
# for image_path in glob.glob(image_dir + '/depth_*.png'):
#     image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#     image_id = os.path.basename(image_path).split('.')[0].split('_')[1]
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             if int(image[i][j].sum()) != 0:
#                 image[i][j] = roughness*255
#             else:
#                 image[i][j] = 0
#     cv2.imwrite(os.path.join(image_dir, f'roughness_{image_id}.png'), image)