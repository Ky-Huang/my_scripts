import numpy as np

# 这里填要读取的文件路径
file_path = r'F:\MyDataF\XDATCAR'
# 这里填要写入的文件路径+文件名
new_file_path = r'F:\MyDataF\result.txt'
# 板块数量
num_block = 176
# 每板块有多少行
num_lines_per_block = 29

with open(file_path, 'r') as f:
    lines = f.readlines()
    result = []
    for i in range(num_block):
        result.append(lines[i * num_lines_per_block + 2].split()[0])
        result.append(lines[i * num_lines_per_block + 3].split()[1])
        result.append(lines[i * num_lines_per_block + 4].split()[2])
print(result)
result = np.array(result, dtype=float)
result.resize(num_block, 3)
np.savetxt(new_file_path, result, delimiter='   ', fmt='%.6f')