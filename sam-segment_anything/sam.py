
import numpy as np
import cv2
from pathlib import Path
from segment_anything import sam_model_registry, SamPredictor
import matplotlib.pyplot as plt

# def show_points(coords, labels, ax, marker_size=375):
#     pos_points = coords[labels==1]
#     neg_points = coords[labels==0]
#     ax.scatter(pos_points[:, 0], pos_points[:, 1], color='green', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)
#     ax.scatter(neg_points[:, 0], neg_points[:, 1], color='red', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)   
    
# def show_box(box, ax):
#     x0, y0 = box[0], box[1]
#     w, h = box[2] - box[0], box[3] - box[1]
#     ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0,0,0,0), lw=2)) 

def show_mask(param, random_color=False):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([30, 144, 255], dtype=np.uint8)
    h, w = param['mask'].shape[-2:]
    mask_image = param['mask'].reshape(h, w, 1) * color.reshape(1, 1, -1)
    full_image = cv2.addWeighted(param['image'], 0.5, mask_image, 0.5, 0)
    cv2.imshow(WIN_NAME, full_image)
    
def onmouse_pick_points(event, x, y, flags, param):
    x, y = float(x), float(y)

    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'L: x = {x}, y = {y}')
        predict(x, y, 1, param)

    if event == cv2.EVENT_RBUTTONDOWN:
        print(f'R: x = {x}, y = {y}')
        predict(x, y, 0, param)

def predict(x, y, label, param):
        param['input_point'] = np.append(param['input_point'], np.array([[x, y]]), axis=0)
        param['input_label'] = np.append(param['input_label'], label)
        print(f'input_point:{param["input_point"]}, input_label:{param["input_label"]}')
        
        if len(param['input_point']) == 1:
            print('single prompt')
            masks, scores, logits = predictor.predict(
                point_coords=param['input_point'],
                point_labels=param['input_label'],
                multimask_output=True,
            )
            param['scores'], param['logits'] = scores, logits
            param['mask'] = masks[None, np.argmax(scores), :, :]
        elif len(param['input_point']) > 1:
            print('multiple prompt')
            mask_input = param['logits'][np.argmax(param['scores']), :, :]
            mask, _, _ = predictor.predict(
                point_coords=param['input_point'],
                point_labels=param['input_label'],
                mask_input=mask_input[None, :, :],
                multimask_output=False,
            )
            param['mask'] = mask
        else:
            raise
        show_mask(param)
        return

if __name__ == "__main__":
    WIN_NAME = 'masked_image'
    WIN_NAME2 = 'ori_image'

    image_dir = Path(r'F:\MyDataF\xzx\23.12.20\D5\instantNGP-mask\images')
    mask_dir = Path(r'F:\MyDataF\xzx\23.12.20\D5\instantNGP-mask\masks')
    sam_checkpoint = r"F:\Codes\Python\my_scripts\sam-segment_anything\sam_vit_h_4b8939.pth"
    model_type = "vit_h"
    device = "cuda"
    print('loading model.........')
    sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
    sam.to(device=device)
    predictor = SamPredictor(sam)
    print('start predict')

    for image_path in image_dir.glob('*.[JjPp][PpNn][Gg]'):
        image = cv2.imread(image_path.as_posix())
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        predictor.set_image(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.namedWindow(WIN_NAME, 0)
        cv2.namedWindow(WIN_NAME2, 0)
        param = dict()
        param['input_point'] = np.empty((0,2))
        param['input_label'] = np.empty((0,2))
        param['image'] = image
        param['mask'] = np.ones((1, image.shape[0], image.shape[1]), dtype=np.uint8)
        param['scores'] = None
        param['logits'] = None

        cv2.setMouseCallback(WIN_NAME, onmouse_pick_points, param)

        cv2.imshow(WIN_NAME, param['image'])
        cv2.imshow(WIN_NAME2, param['image'])

        while True:

            key = cv2.waitKey(30)

            if key == 32:  # 空格确认
                mask_name = f'dynamic_mask_{image_path.stem}.png'
                cv2.imwrite(mask_dir.joinpath(mask_name).as_posix(), (~param['mask']).transpose(1, 2, 0).astype(np.uint8) * 255)
                cv2.destroyAllWindows()
                break

            if key == 27:  # Esc取消，重做
                param['input_point'] = np.empty((0,2))
                param['input_label'] = np.empty((0,2))
