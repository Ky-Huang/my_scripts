# 新和成数据用的，去掉000_0000.png前面的000_
from pathlib import Path

# -----------------------------------修改---------------------------------------------------
p = Path(r'F:\MyDataF\DataSet\synth\smpl1_dance\easymocap_mistyfarmroad')
# -------------------------------------------------------------------------------------------
for img_path in p.rglob("*.png"):
    basename = img_path.name
    dirname = img_path.parent
    newname = basename.split('_')[-1]
    img_path.rename(dirname.joinpath(newname))