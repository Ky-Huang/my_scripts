import os
from PIL import Image

def convert_webp_to_png(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.webp'):
            img = Image.open(os.path.join(directory, filename))
            png_filename = os.path.splitext(filename)[0] + '.png'
            img.save(os.path.join(directory, png_filename), 'PNG')

# 使用你的目录替换 'your_directory'
convert_webp_to_png(r'C:\Users\Administrator\Desktop\owl1\2ddata\CRM-main\examples')