# 用于从MPI的视频数据集里提取图片
import cv2
# import icecreame
from pathlib import Path

root_dir = Path('E:\BaiduNetdiskDownload\MPI\Vlad')
for vid_path in root_dir.rglob('*.avi'):
    vidcap = cv2.VideoCapture(str(vid_path))
    frame_count = 0
    print(f'当前avi:{str(vid_path)}')
    while True:
        ret, frame = vidcap.read()
        if ret:
            im_path = vid_path.parent.joinpath(vid_path.stem, f'{frame_count:05}.jpg')
            im_path.parent.mkdir(parents=True, exist_ok=True)
            cv2.imwrite(str(im_path), frame)
            frame_count += 1
            if frame_count >= 2000:
                break
        else:
            vidcap.release()
            break
