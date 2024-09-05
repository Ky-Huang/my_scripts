# 计算psnr lpips

import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
import lpips

def align_images(image1, image2):
    # 将图像转换为灰度图
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    
    # 使用ORB特征检测器
    orb = cv2.ORB_create()
    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)
    
    # 使用BFMatcher进行特征匹配
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)
    matches = sorted(matches, key=lambda x: x.distance)
    
    # 提取匹配的关键点
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)
    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt
    
    # 使用RANSAC估计变换矩阵
    h, mask = cv2.findHomography(points2, points1, cv2.RANSAC)
    
    # 对图像进行对齐
    height, width, channels = image1.shape
    aligned_image2 = cv2.warpPerspective(image2, h, (width, height))
    
    return aligned_image2

def main():
    # 读取两张图像
    image1 = cv2.imread(r'E:\tongxue\xrg\psnr_cal\goat\goat_p_2.png', cv2.IMREAD_UNCHANGED)
    image2 = cv2.imread(r'E:\tongxue\xrg\psnr_cal\goat\goat_albedo_p.png', cv2.IMREAD_UNCHANGED)

    # image1 = cv2.imread(r'E:\tongxue\xrg\psnr_cal\elephont\gt_albedo_elephont_p11.png', cv2.IMREAD_UNCHANGED)
    # image2 = cv2.imread(r'E:\tongxue\xrg\psnr_cal\elephont\pred_albedo_p11.png', cv2.IMREAD_UNCHANGED)

    # 确保两张图像的尺寸相同
    if image1.shape != image2.shape:
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]), interpolation=cv2.INTER_AREA)
        # cv2.imwrite(r'E:\tongxue\xrg\psnr_cal\elephont\gt_albedo_elephont_pcvcvcv.png', image2)

    # # 对齐图像
    # image2 = align_images(image1, image2)
    
    # 计算PSNR
    psnr_value = psnr(image1, image2, data_range=255)
    print(f"PSNR值: {psnr_value} dB")
    
    # 计算LPIPS
    loss_fn = lpips.LPIPS(net='alex')  # 使用AlexNet作为基础网络
    image1_tensor = lpips.im2tensor(image1)  # 将图像转换为tensor
    image2_tensor = lpips.im2tensor(image2)  # 将图像转换为tensor
    lpips_value = loss_fn(image1_tensor, image2_tensor)
    print(f"LPIPS值: {lpips_value.item()}")

if __name__ == "__main__":
    main()

