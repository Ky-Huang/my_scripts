# MPI real太大了，选一些数据
from pathlib import Path
import itertools
p = Path(r'E:\BaiduNetdiskDownload\MPI\Vlad500')
for i in itertools.chain.from_iterable([p.rglob("*.json"), p.rglob("*.jpg"), p.rglob("*.png")]):
    if 200 <= int(str(i.stem).replace('_keypoints', '')) < 300:
        dest = Path(str(i).replace("Vlad500", "Vlad100"))
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(i.read_bytes())