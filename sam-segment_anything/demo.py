# 使用SAM conda环境。
# 左键点击提供正面prompt，右键点击提供负面prompt，空格确认，ESC清除prompt

import numpy as np
import torch
import matplotlib.pyplot as pltpi
import cv2
import os
import glob
from segment_anything import sam_model_registry, SamPredictor



def predict(x, y, label, param):

        param['input_point'] = np.append(param['input_point'], np.array([[x, y]]), axis=0)

        param['input_label'] = np.append(param['input_label'], label)

        print(f'input_point:{param["input_point"]}, input_label:{param["input_label"]}')
        mask, _, _ = predictor.predict(

            point_coords=param['input_point'],

            point_labels=param['input_label'],

            multimask_output=False,
        )

        mask = mask[0].astype(np.uint8) * 255

        # cv2.imshow("mask_name", mask)

        # cv2.waitKey()
        masked_image = cv2.add(param['image'], np.zeros(np.shape(param['image']), dtype=np.uint8), mask=mask)

        cv2.imshow(WIN_NAME, masked_image)

        mask_name = f'dynamic_mask_{os.path.basename(image_path)[:-4]}'

        cv2.imwrite(os.path.join(mask_dir, mask_name) + '.png', mask)
        return mask




def onmouse_pick_points(event, x, y, flags, param):


    x, y = float(x), float(y)

    if event == cv2.EVENT_LBUTTONDOWN:

        print(f'L: x = {x}, y = {y}')

        mask = predict(x, y, 1, param)


    if event == cv2.EVENT_RBUTTONDOWN:

        print(f'R: x = {x}, y = {y}')

        mask = predict(x, y, 0, param)



WIN_NAME = 'masked_image'

WIN_NAME2 = 'ori_image'


image_dir = r'F:\MyDataF\xzx\23.12.20\D5\instantNGP-mask\images'
mask_dir = r'F:\MyDataF\xzx\23.12.20\D5\instantNGP-mask\images'
sam_checkpoint = r"F:\Codes\Python\my_scripts\sam-segment_anything\sam_vit_h_4b8939.pth"

model_type = "vit_h"

device = "cuda"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)

sam.to(device=device)

predictor = SamPredictor(sam)

for image_path in sorted(glob.glob(image_dir + r'\*.JPG')):



    image = cv2.imread(image_path)
  

    predictor.set_image(image)


    cv2.namedWindow(WIN_NAME, 0)
    cv2.namedWindow(WIN_NAME2, 0)
    param = dict()

    param['input_point'] = np.empty((0,2))

    param['input_label'] = np.empty((0,2))

    param['image'] = image

    cv2.setMouseCallback(WIN_NAME, onmouse_pick_points, param)

    cv2.imshow(WIN_NAME, image)

    cv2.imshow(WIN_NAME2, image)

    while True:

        key = cv2.waitKey(30)

        if key == 32:  # 空格确认

            break

        if key == 27:  # Esc取消，重做

            param['input_point'] = np.empty((0,2))

            param['input_label'] = np.empty((0,2))

    cv2.destroyAllWindows()




      























# WIN_NAME = 'pick_points'



# def onmouse_pick_points(event, x, y, flags, param):

#     x, y = float(x), float(y)

#     if event == cv2.EVENT_LBUTTONDOWN:

#         # print('x = %d, y = %d' % (x, y))

#         print(f'L: x = {x}, y = {y}')

#         # cv2.drawMarker(param, (x, y), (0, 255, 0))

#         # param[0] = np.append(param[0], [x, y], axis=0)

#         # param[1] = np.append(param[1], 1)

#         param[0].append([x, y])

#         param[1].append(1)

#         print(f'0:{param[0]}, 1:{param[1]}')

#     if event == cv2.EVENT_RBUTTONDOWN:

#         print(f'R: x = {x}, y = {y}')

#         # param[0] = np.append(param[0], [x, y], axis=0)

#         # param[1] = np.append(param[1], 0)

#         param[0].append([x, y])

#         param[1].append(0)






# image_dir = r'F:\MyDataF\xzx\2'

# mask_dir = r'F:\MyDataF\xzx\mask2'



# sam_checkpoint = r"F:\Codes\Python\sam-segment_anything\sam_vit_h_4b8939.pth"

# model_type = "vit_h"


# device = "cuda"


# sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)

# sam.to(device=device)


# predictor = SamPredictor(sam)



# for image_path in glob.glob(image_dir + r'\*.JPG'):



#     image = cv2.imread(image_path)

#     # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     # import sys

#     # sys.path.append("..")
    




#     predictor.set_image(image)


#     # input_point = np.array([])

#     # input_label = np.array([])

#     input_point = []

#     input_label = []



#     cv2.namedWindow(WIN_NAME, 0)

#     cv2.setMouseCallback(WIN_NAME, onmouse_pick_points, [input_point, input_label])

#     while True:

#         cv2.imshow(WIN_NAME, image)

#         key = cv2.waitKey(30)

#         if key == 27:  # ESC

#             break

#     cv2.destroyAllWindows()



#     input_point = np.array(input_point)

#     input_label = np.array(input_label)


#     print(f'input_point:{input_point}')



#     masks, scores, logits = predictor.predict(
#         point_coords=input_point,

#         point_labels=input_label,

#         multimask_output=False,
#     )


#     mask = mask.astype(np.uint8) * 255


#     # masks, scores, logits = predictor.predict(

#     #     point_coords=input_point[0],

#     #     point_labels=input_label[0],

#     #     multimask_output=True,
#     # )



#     # mask_input = logits[np.argmax(scores), :, :]  # Choose the model's best mask

#     # for i, in range(len(masks)):
#     #     masks, _, mask_input = predictor.predict(

#     #     point_coords=input_point[:i],

#     #     point_labels=input_label[:i],

#     #     mask_input=mask_input[None, :, :],

#     #     multimask_output=False,
#     # )


#     # for i, mask in enumerate(masks):

#     #     mask_name = f'{os.path.basename(image_path)[:-4]}_Mask{i}'

#     #     mask = mask.astype(np.uint8) * 255

#     #     cv2.imshow("mask_name", mask)

#     #     cv2.waitKey()

#     #     cv2.imwrite(os.path.join(mask_dir, mask_name) + '.jpg', mask)
        