import numpy as np
a = np.load(r'F:\MyDataF\DataSet\zju-mocap\CoreView_313\new_vertices\2.npy', allow_pickle=True)
a = a.tolist()
b = np.load(r'F:\MyDataF\DataSet\synth\megan_dance_02\megan_dance_02\eaymocap\annots1.npy', allow_pickle=True)
b = b.tolist()
c = np.load(r'E:\BaiduNetdiskDownload\MPI\annots.npy', allow_pickle=True)
c = c.tolist()
print(a)
print(b)