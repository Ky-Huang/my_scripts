import cv2
import glob

in_path = r'F:\MyDataF\Calibration\4.20\sony intri'
# out_path = r'F:\MyDataF\new_sony\sony_intri_cut_resize'
for img_path in glob.glob(in_path + '/*.png'):
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img_cut = img[:1024, :1224]
    # img_resize = cv2.resize(img_cut, (612, 512))
    cv2.imwrite(img_path, img_cut)
    # cv2.imwrite(img_path.replace('sony_intri', 'sony_intri_cut_resize'), img_resize)

# for img_path in glob.glob(r'F:\MyDataF\new_sony\sony_extri\images\MV-CS050-10GC-PRO (K63900969)intrix_small' + '/*.png'):
#     # input_path = r'F:\MyDataF\new_sony\sony_extri\sony\LUCID_PHX050S-Q_223600112__20230410101917463_image0_45.png'
#     img = cv2.imread(img_path, cv2.IMREAD_COLOR)
#     img_resize = cv2.resize(img, (1224, 1024))
#     cv2.imwrite(img_path, img_resize)