# 把目录下的所有文件都命名成0，用于smpl dance multiView singleFrame

from pathlib import Path

path = Path(r'F:\MyDataF\DataSet\synth\smpl2_dance_multiView_singleFrame\easymocap\mask')

for i in path.rglob('*.png'):
    i.rename(i.parent.joinpath('0000.png'))