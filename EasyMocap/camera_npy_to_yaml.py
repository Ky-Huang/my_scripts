import yaml
import numpy

yml_path = r'G:\MyData\EasyMocap\XieData\intri.yml'
with open(yml_path, 'r') as f:
    myyml = yaml.load(f.read(), Loader=yaml.Loader)




file_path = r'G:\MyData\PhySG\CoreView_313\annots.npy'
npy_file = numpy.load(file_path, allow_pickle=True).item()


### 写在EasyMocap1115得apps\calibration\hk_intri_extri里了。目前把这个脚本也复制进EasyMocap0925_version2了
### 另外从new_params里提取vertices写在EasyMocap0925_version2\apps\demo\hk_write_vertices.py里了