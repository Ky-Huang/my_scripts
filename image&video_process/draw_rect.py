# 在uv img上画矩形
import cv2

img = cv2.imread(r'C:\Users\Administrator\Desktop\temp_img\9-4uv.png', cv2.IMREAD_COLOR)
# left_top = (150, 2200)
# right_bottom = (2300, 3200)
# cv2.rectangle(img, left_top, right_bottom, (0, 0, 255), 64)
# cv2.imwrite(r'C:\Users\Administrator\Desktop\temp_img\9-4uv_rect.png', img)
# left_top = (200, 715)
# right_bottom = (2200, 1140)
# cv2.rectangle(img, left_top, right_bottom, (0, 0, 255), 64)
# cv2.imwrite(r'C:\Users\Administrator\Desktop\temp_img\9-4uv_rect2.png', img)

left_top = (900, 3200)
cv2.putText(img, '8', left_top, cv2.FONT_HERSHEY_COMPLEX, 40, (0,0,255), 60)
cv2.imwrite(r'C:\Users\Administrator\Desktop\temp_img\9-4uv_text8.png', img)