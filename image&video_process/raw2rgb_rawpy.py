import numpy as np
import imageio
import rawpy
import sys
import os
import cv2


def extract_bayer_channels(raw):
    ch_B = raw[1::2, 1::2]
    ch_Gb = raw[0::2, 1::2]
    ch_R = raw[0::2, 0::2]
    ch_Gr = raw[1::2, 0::2]

    return ch_R, ch_Gr, ch_B, ch_Gb


if __name__ == "__main__":

    raw_file = r"C:\Users\Administrator\Desktop\temp\raw\Image_20230407101651669_w2448_h2048_pBayerRG8.raw"
    print("Converting file " + raw_file)

    if not os.path.isfile(raw_file):
        print("The file doesn't exist!")
        sys.exit()

    raw = rawpy.imread(raw_file)
    raw_image = raw.raw_image
    del raw

    """# extract_bayer_channels将raw数据按4通道提取，至于为何是4通道这里就不介绍了
    raw_image = raw_image.astype(np.float32)
    print(np.max(raw_image))
    ch_R, ch_Gr, ch_B, ch_Gb = extract_bayer_channels(raw_image)
    # 拼合四通道一起
    out = np.stack((R, Gr, Gb, B))"""

# raw数据一般是16位，有效位可能为16,14,12,10等。常见位12位
png_image = raw_image.astype(np.uint16)
new_name = raw_file.replace(".dng", ".png")
imageio.imwrite(new_name, png_image)
