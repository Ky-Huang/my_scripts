## 把删了几帧的文件重新排成连续的

from pathlib import Path

path = Path(r'E:\BaiduNetdiskDownload\synth\megan_dance_04_xie\megan_dance_04_cqf\physg\depth')
ext = 'png'

for i, file in enumerate(sorted(path.glob(f'*.{ext}'), key=lambda path : int(path.stem))):
    dirname = file.parent
    newname = f'{i:06}.{ext}'                                      # 记得修改这里的有效位数
    file.rename(dirname.joinpath(newname))
