import cv2
import numpy as np
checker_img = np.zeros((4096, 4096, 3))
block_width = 4096 // 16
deepred_block = np.full((block_width,block_width, 3),(255, 0, 255))
white_block = np.full((block_width,block_width, 3),(255, 255, 255))

for row in range(16):
    for col in range(16):
        row_begin = row*block_width
        row_end = row_begin+block_width
        col_begin = col*block_width
        col_end = col_begin+block_width
        if (row+col)%2==0:
            checker_img[row_begin:row_end,col_begin:col_end] = deepred_block
        else:
            checker_img[row_begin:row_end,col_begin:col_end] = white_block
cv2.imwrite(r"C:\Users\Administrator\Desktop\temp_img\checker_board.png",checker_img)
