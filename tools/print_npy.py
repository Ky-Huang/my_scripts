import numpy as np
a = np.load(r'G:\MyData\PhySG\CoreView_313\annots.npy', allow_pickle=True)
a = a.tolist()
b = np.load(r'E:\BaiduNetdiskDownload\MPI\for_texture500\annots.npy', allow_pickle=True)
b = b.tolist()
c = np.load(r'E:\BaiduNetdiskDownload\MPI\annots.npy', allow_pickle=True)
c = c.tolist()
print(a)
print(b)