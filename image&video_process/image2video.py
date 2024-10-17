# import cv2
# from pathlib import Path
# from collections import defaultdict
# import numpy as np
# import numpy as np

# def add_background(image_path, background_color=(255, 255, 255)):
#     image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
#     if image.shape[2] == 4:
#         alpha_channel = image[:,:,3]
#         rgb_channels = image[:,:,:3]

#         # White Background Image
#         background_image = np.ones_like(rgb_channels, dtype=np.uint8) * background_color

#         # Alpha factor
#         alpha_factor = alpha_channel[:,:,np.newaxis].astype(np.float32) / 255.0
#         alpha_factor = np.concatenate((alpha_factor,alpha_factor,alpha_factor), axis=2)

#         # Transparent Elements
#         base = rgb_channels.astype(np.float32) * alpha_factor
#         white = background_image.astype(np.float32) * (1 - alpha_factor)
#         final_image = base + white
#         return final_image.astype(np.uint8)

#     else:
#         return image
    
# def add_background2(image_path, background_color=(255, 255, 255)):
#     image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
#     if image.shape[2] == 4:
#         alpha_channel = image[:,:,3]
#         rgb_channels = image[:,:,:3]

#         # White Background Image
#         background_image = np.ones_like(rgb_channels, dtype=np.uint8) * background_color

#         # Replace all pixels with transparency of 0 with the background color
#         mask = alpha_channel == 0
#         rgb_channels[mask] = background_image[mask]

#         # Set the alpha channel to 1
#         alpha_channel[mask] = 255

#         final_image = cv2.merge([rgb_channels, alpha_channel])
#         return final_image

#     else:
#         return image
    
# def images_to_video(image_folder, output_folder):
#     image_folder = Path(image_folder)
#     output_folder = Path(output_folder)
#     output_folder.mkdir(exist_ok=True)

#     images = sorted(image_folder.rglob('*.png'))

#     videos = defaultdict(list)

#     for image in images:
#         # video_name = image.stem.split('_')[0].split('.')[0]
#         video_name = image.stem.rsplit('_', 1)[0]
#         videos[video_name].append(image)

#     for video_name, images in videos.items():
#         frame = cv2.imread(str(images[0]))
#         height, width, layers = frame.shape

#         video = cv2.VideoWriter(str(output_folder / f"{video_name}.mp4"), cv2.VideoWriter_fourcc(*'mp4v'), 30, (width,height))

#         for image in images:
#             video.write(add_background(str(image)))

#         video.release()

#     cv2.destroyAllWindows()

# # 使用你的目录和视频名替换 'image_folder' 和 'output_folder'
# images_to_video(r'E:\around\shading\render',
#                 r'E:\video\shade')


###########################################2024/10/11 xrg LDM cvm##################################################################
import os
import cv2
from tqdm import tqdm

root_dir = r'C:\Users\GXY\Desktop\shipin\tem'


def images_to_video(image_folder, video_name, fps=60):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]
    images.sort()  # 排序图片，确保按照文件名顺序处理
    if not images:
        print(f"No images found in {image_folder}")
        return

    # 读取第一张图片以获得帧大小
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    # 定义视频编码和输出文件
    video_path = os.path.join(root_dir, video_name + ".mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 定义编码格式
    video = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

    # 将每张图片写入视频并显示进度条
    for image in tqdm(images, desc=f"Processing {video_name}"):
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        video.write(frame)

    video.release()
    print(f"Video saved as {video_path}")

def process_directories(root_dir):
    for subdir in os.listdir(root_dir):
        subdir_path = os.path.join(root_dir, subdir)
        for subsubdir in os.listdir(subdir_path):
            subsubdir_path = os.path.join(subdir_path, subsubdir)
            video_name = f"{subdir}_{subsubdir}"
            print(f"Processing subdirectory: {subdir}/{subsubdir}")
            images_to_video(subsubdir_path, video_name)

process_directories(root_dir)

