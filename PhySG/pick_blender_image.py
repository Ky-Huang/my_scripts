# 把blender的图按照帧序号分开放在不同目录，图片名字是相机序号
from pathlib import Path
img_path = Path(r'F:\MyDataF\DataSet\megan\depth')
out_path = Path(r'F:\MyDataF\DataSet\megan\mask')
for img in img_path.rglob('*.png'):
    name = img.stem
    cam_id, frame_id = int(name.split('_')[0]), int(name.split('_')[1])
    dest = out_path.joinpath(f'{frame_id:04d}', f'{cam_id:06d}.png')
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(img.read_bytes())