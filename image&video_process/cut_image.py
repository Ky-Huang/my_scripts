# 把1920*1080的图片cut成1080*1080的 
import cv2
import glob
import os

def crop_center_and_save(image_path):
    # 读取图片
    img = cv2.imread(image_path)
    
    # 检查图片是否成功加载
    if img is None:
        print(f"无法读取图片: {image_path}")
        return
    
    # 获取图片的尺寸
    height, width, _ = img.shape
    
    # 确保图片尺寸为1920x1080
    if width == 1920 and height == 1080:
        # 计算裁剪区域，保留中间1080x1080的部分
        x_start = (width - 1080) // 2
        y_start = 0
        x_end = x_start + 1080
        y_end = 1080
        
        # 裁剪图片
        cropped_img = img[y_start:y_end, x_start:x_end]
        
        # 保存裁剪后的图片，覆盖原图片
        cv2.imwrite(image_path, cropped_img)
        # print(f"图片已处理并覆盖: {image_path}")
    else:
        print(f"跳过图片（尺寸不是1920x1080）: {image_path}")

def process_images_in_directory_with_glob(directory):
    # 使用glob递归查找目录下的所有图片文件
    image_paths = glob.glob(os.path.join(directory, '**', '*.*'), recursive=True)
    
    # 支持的图片格式
    valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')

    # 遍历所有找到的文件
    for image_path in image_paths:
        # 检查文件扩展名是否为图片格式
        if image_path.lower().endswith(valid_extensions):
            crop_center_and_save(image_path)
        else:
            print(f"跳过非图片文件: {image_path}")

# 指定图片所在根目录
directory_path = r'C:\Users\GXY\Desktop\shipin\images\push'

# 调用处理函数
process_images_in_directory_with_glob(directory_path)
