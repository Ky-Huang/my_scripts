from pathlib import Path
import itertools
p = Path(r'E:\BaiduNetdiskDownload\MPI\for_texture')
for i in itertools.chain.from_iterable([p.rglob("*.json"), p.rglob("*.jpg"), p.rglob("*.png")]):
    if int(i.stem) < 500:
        dest = Path(str(i).replace("for_texture", "for_texture500"))
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(i.read_bytes())