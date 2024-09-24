# 观察图像某个像素的rgb值


# PIL + matplotlib实现----------------------------------------------------------

# import matplotlib.pyplot as plt
# from PIL import Image
# import numpy as np

# # 读取图片
# image_path = r'C:\Users\GXY\Desktop\biye_images\test\LDMtexture_frame_0_sem.png'  # 替换为你的图片路径
# image = Image.open(image_path)

# # 将图片转换为浮点数格式的RGB数组
# image_rgb = image.convert('RGB')
# image_array = np.array(image_rgb) / 255.0  # 归一化到[0, 1]范围

# def on_click(event):
#     # 检查点击是否在图像范围内
#     if event.xdata is not None and event.ydata is not None:
#         x, y = int(event.xdata), int(event.ydata)
#         rgb = image_array[y, x]  # 注意y, x顺序
#         print(f'Clicked pixel RGB: ({rgb[0]:.4f}, {rgb[1]:.4f}, {rgb[2]:.4f})')

# # 显示图像
# plt.imshow(image_array)
# plt.title('Click on the image to get RGB values')
# plt.gca().set_title('Click on the image to get RGB values')
# plt.connect('button_press_event', on_click)
# plt.axis('off')  # 关闭坐标轴
# plt.show()



# opencv实现----------------------------------------------------------

import cv2
import numpy as np

# 回调函数，用于处理鼠标事件
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # 获取像素值
        bgr = img[y, x]
        # 转换为浮点数
        rgb_float = bgr[::-1].astype(np.float32) / 255.0
        print(f"RGB值（浮点数）: {rgb_float}")

# 读取图像
img = cv2.imread(r'C:\Users\GXY\Desktop\biye_images\test\LDMtexture_frame_0_sem.png', flags=cv2.IMREAD_COLOR)

# 显示图像
cv2.imshow('Image', img)

# 设置鼠标回调函数
cv2.setMouseCallback('Image', mouse_callback)

# 保持窗口打开，直到用户按下任意键
cv2.waitKey(0)
cv2.destroyAllWindows()