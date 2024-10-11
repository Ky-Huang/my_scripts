# 根据animSeg出来的二维纹理进行纹理编辑（选中分割图中同色部分，修改对应位置纹理）

import cv2
import numpy as np
import os


def visualize_and_modify_pixels(root_dir, image_path, target_rgb, new_rgb, threshold, second_image_path):
    # 读取图像
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 读取第二张同尺寸的图像
    second_image = cv2.imread(second_image_path)
    second_image_rgb = cv2.cvtColor(second_image, cv2.COLOR_BGR2RGB)

    # 将图像转换为浮点数并归一化
    image_float = image_rgb.astype(np.float32) / 255.0
    target_rgb_float = np.array(target_rgb, dtype=np.float32)



    masks = []
    for i in range(len(target_rgb)):
        # 计算与目标RGB值的差距
        diff = np.abs(image_float - target_rgb_float[i])
        # 找到差距在阈值之内的像素
        mask = np.all(diff<= threshold, axis=-1)
        masks.append(mask)
    masks = np.logical_or.reduce(masks)

    # 创建半透明的蒙版
    alpha = 0.5  # 透明度
    highlighted_image = image_rgb.copy()
    
    # 将未选中区域设为半透明的白色
    highlighted_image[~masks] = (255, 255, 255)  # 设置未选中区域为白色
    
    # 使未选中区域变为半透明
    highlighted_image = cv2.addWeighted(image_rgb, 1 - alpha, highlighted_image, alpha, 0)

    # 修改第二张图像的选中像素
    second_image_rgb[masks] = np.array(new_rgb) * 255  # 将选中像素的RGB值替换为new_rgb

    # 将图像转换回BGR以用于OpenCV显示
    highlighted_image_bgr = cv2.cvtColor(highlighted_image, cv2.COLOR_RGB2BGR)
    second_image_bgr = cv2.cvtColor(second_image_rgb, cv2.COLOR_RGB2BGR)

    # 使用OpenCV显示图像
    cv2.imshow("Original Image", image)
    cv2.imshow("Highlighted Selected Pixels", highlighted_image_bgr)
    cv2.imshow("Modified Second Image", second_image_bgr)
    cv2.waitKey(0)
    cv2.imwrite(os.path.join(root_dir, 'modified_image3.png') , second_image_bgr)
    cv2.imwrite(os.path.join(root_dir, 'highlighted_image3.png') , highlighted_image_bgr)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    root_dir = r'C:\Users\GXY\Desktop\biye_images\blender\edit\syth_kate_dance_03-sem-0918-1'
    # 示例用法
    image_path = os.path.join(root_dir, 'LDMtexture_frame_0_sem.png')     # semUV图
    second_image_path = os.path.join(root_dir, 'LDMtexture_frame_0.png')   # 纹理UV图
    # target_rgb1 = [0.839, 0.082, 0.345]
    # target_rgb2 = [0.937, 0.941, 0.498]
    # target_rgb3 = [0.6156863 ,0.3372549, 0.85882354]
    target_rgb = [[0.6117647, 0.972549, 0.81960785], [0.9307843, 0.09215687, 0.80686276], [0.7529412, 0.5254902, 0.18431373]]
    new_rgb = [0.1,0.9,0.1]
    threshold = 0.20  # 阈值

    visualize_and_modify_pixels(root_dir, image_path, target_rgb, new_rgb, threshold, second_image_path)


