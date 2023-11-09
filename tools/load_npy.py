import numpy as np
a = np.load(r'C:\Users\Administrator\Desktop\temp\annots.npy', allow_pickle=True)
a = a.tolist()
b = np.load(r'F:\MyDataF\DataSet\synth\megan_dance_02\megan_dance_02\eaymocap\annots1.npy', allow_pickle=True)
b = b.tolist()
c = np.load(r'E:\BaiduNetdiskDownload\MPI\annots.npy', allow_pickle=True)
c = c.tolist()
print(a)
print(b)