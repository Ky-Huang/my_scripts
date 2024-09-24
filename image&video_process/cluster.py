import cv2
import numpy as np
from sklearn.cluster import AgglomerativeClustering

root_dir = r'C:\Users\GXY\Desktop\biye_images\syth_jody_dance_for_lightgraid_03'
image_path = root_dir + '\\' + r'semantic_image_frame150_cam0.png'  # 替换为你的图片路径
mask_path = root_dir + '\\' + r'mask\0150.png'    # 替换为你的掩膜图像路径

# 读取原始图像
image = cv2.imread(image_path)

# 将图像缩小到50%
height, width = image.shape[:2]
new_height, new_width = height // 2, width // 2
image_small = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

# 读取4通道掩膜图像
mask = cv2.imread(mask_path, cv2.IMREAD_UNCHANGED)  # 读取为4通道图像

# 如果掩膜为4通道，提取Alpha通道（第四通道）
if len(mask. shape) > 2 and  mask.shape[2] == 4:
    mask = mask[:, :, 3]  # 提取Alpha通道
else:
    mask = cv2.imread(mask_path, 0)  # 以灰度模式读取

# 缩小掩膜的Alpha通道
mask_small = cv2.resize(mask, (new_width, new_height), interpolation=cv2.INTER_NEAREST)

# # 定义腐蚀核的大小（可以根据需要调整大小，3x3是一个常用的选择）
# kernel = np.ones((3, 3), np.uint8)

# # 对掩膜进行腐蚀操作，使掩膜收缩
# mask_small = cv2.erode(mask_small, kernel, iterations=1)

# 创建掩膜的布尔数组，值大于0的区域为True
mask_bool = mask_small > 0

# 提取掩膜区域的像素
pixels = image_small[mask_bool].reshape(-1, 3)

# 定义距离阈值
distance_threshold = 30

# 使用Agglomerative Clustering进行聚类
clustering = AgglomerativeClustering(
    n_clusters=None,
    metric='euclidean',
    linkage='ward',
    distance_threshold=distance_threshold
)
clustering.fit(pixels)

# 获取每个像素所属的聚类标签
labels = clustering.labels_

# 计算每个聚类的中心（均值）
cluster_centers = np.array([pixels[labels == i].mean(axis=0) for i in np.unique(labels)])

# 用聚类中心的值替换原始像素值
new_pixels = cluster_centers[labels]

# 创建一个新的图像数组，初始为原图像（或全零）
new_image_small = np.zeros_like(image_small)

# 仅在掩膜区域替换像素值
new_image_small[mask_bool] = new_pixels.astype('uint8')

# 如果需要，将图像放大回原始尺寸
new_image = cv2.resize(new_image_small, (width, height), interpolation=cv2.INTER_NEAREST)

# 保存并显示图像
image_name = image_path.split('\\')[-1][:-4]
output_path = root_dir + '\\' + f'{image_name}_discret.jpg'
cv2.imwrite(output_path , new_image)
