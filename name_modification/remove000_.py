# 新和成数据用的，去掉000_0000.png前面的000_
from pathlib import Path

# -----------------------------------修改---------------------------------------------------
p = Path(r'E:\BaiduNetdiskDownload\synth\brain_dance_for_lightgraid_02.blend\brain_dance_for_lightgraid_02_view2\images\02')
# -------------------------------------------------------------------------------------------
for img_path in p.rglob("*.png"):
    basename = img_path.name
    dirname = img_path.parent
    newname = basename.split('_')[-1]
    img_path.rename(dirname.joinpath(newname))