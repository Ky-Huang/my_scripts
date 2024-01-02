# 谢子玄的曝光数据
from pathlib import Path
import json

dir = Path(r'F:\MyDataF\xzx\23.12.20\dwzx\LR2')
txt = r'F:\MyDataF\xzx\23.12.20\dwzx\LR\删掉的图.txt'
with open(txt) as f:
    img_names = f.read().splitlines()
print(img_names)
for img_name in img_names:
    img_path = dir.joinpath(img_name + '.jpg')
    img_path.unlink(missing_ok=True)


# 再把相机参数的文件改了
json_path = r'F:\MyDataF\xzx\23.12.20\dwzx\colmap2\sparse\0\transforms.json'
new_json_path = r'F:\MyDataF\xzx\23.12.20\dwzx\LR2\transforms.json'
with open(json_path) as f:
    camera_data = json.load(f)
for ele in camera_data['frames'][:]:
    ele_name = Path(ele['file_path']).stem
    if ele_name in img_names:
        camera_data['frames'].remove(ele)
json.dump(camera_data, open(new_json_path, 'w'))