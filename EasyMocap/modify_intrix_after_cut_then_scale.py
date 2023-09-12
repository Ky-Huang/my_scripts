## 裁剪图片后，原图算出来的定标数据需要相应调整

import numpy as np

# data_path = ""
file_path = r"G:\MyData\XieData\intri.yml"
output_path = r"G:\MyData\XieData\new_intri.yml"
with open(file_path) as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith('K_'):
            K_data = lines[i + 8].strip()
            K_data = K_data.split('[')[1]
            K_data = K_data.split(']')[0]
            K_data = K_data.split(',')
            # K_data = np.array(K_data)
            digital_K_data = [float(x) for x in K_data]
            digital_K_data[2] -= 840
            digital_K_data[5] -= 840
            for j in range(6):
                digital_K_data[j] *= 0.5
            print()
            print("digital_K_data:", digital_K_data)

            lines[i + 8] = "  data: [{:.3f}, {:.3f}, {:.3f}, {:.3f}, {:.3f}, {:.3f}, {:.3f}, {:.3f}, {:.3f}]\n".format(
                digital_K_data[0],
                digital_K_data[1],
                digital_K_data[2],
                digital_K_data[3],
                digital_K_data[4],
                digital_K_data[5],
                digital_K_data[6],
                digital_K_data[7],
                digital_K_data[8])
            print("line:", lines[i + 8])
    print("lines:", lines)
    new_file = open(output_path, 'a+')
    for line in lines:
        new_file.write(line)

