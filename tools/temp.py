from PIL import Image

# 读取原始图像
original_image = Image.open(r'E:\tongxue\xrg\psnr_cal\goat\goat_albedo_p.png')

# 获取原始图像的尺寸
original_width, original_height = original_image.size

# 创建一个新的1920x1080的空白图像，使用RGBA模式
new_width, new_height = 1920, 1080
new_image = Image.new('RGBA', (new_width, new_height), (0, 0, 0, 0))

# 计算粘贴位置，使原图像的中心与新图像的中心对齐
paste_x = (new_width - original_width) // 2
paste_y = (new_height - original_height) // 2

# 将原始图像粘贴到新图像的中心位置
new_image.paste(original_image, (paste_x, paste_y))

# 保存新图像
new_image.save(r'E:\tongxue\xrg\psnr_cal\goat\goat_albedo_p3.png')