# 数据预处理
## 目录说明：
--rendering
1. fbx动画导出obj脚本
2. rrengine绘制脚本

--dataprocess
采集的图像数据集或者绘制的图像数据集的处理脚本
1. deepcap目录下主要是mpi数据的处理脚本，包括deepcap和realtime
2. diy和diy2主要是创艺小镇数据和传媒学院数据处理脚本
3. simulate1为UE4的合成数据的处理脚本
4. simulate2为rrengine的合成数据的处理脚本
5. snapshot 数据的处理脚本（部分依赖没有迁移，故需要在relighting4d的tools目录下跑）


## 1. 数据处理流程（这里以deep_mocap路径为例）
### 1) 图片数据准备
cd到工程目录，运行以下脚本，本步骤主要做图片格式的转换，将二进制图像、exr图像、高分辨率图像转换为指定格式和分辨率。其中为文件名填充0的操作是为了保证图像的文件名在文件系统中的排序和图像时序一致，方便后续easymocap进行smpl参数估计， 如果图像准备时文件名已经用0填充则不需要fill_zero_image.py。
```
python preprocess/deep_mocap/prepare_images.py
python preprocess/deep_mocap/fill_zero_image.py
```

### 2) 分割数据准备
运行以下脚本，准备掩码数据，目前尚不包含调用第三方商用spi的脚本。数据来源不同这里的脚本内容不同，可能包含exr转png或者mask估计算法等。
```
python preprocess/deep_mocap/prepare_masks.py
```
    

### 3) 处理easymocap输入的相机参数
运行以下脚本，input是各种不同格式的相机参数（数据来源不同），output是extri.yml和intri.yml格式的相机参数，为easymocap的input相机格式。
```
python preprocess/deep_mocap/easymocap/prepare_camera_params.py
```

### 4) 提取2D关键点
cd到openpose目录，运行以下目录，得到输入图像的关键点，
```
bin/OpenPoseDemo --hand --face --image_dir your_image_path --write_json output_json_path -display 0 -render_pose 0
```
    
*注：如果easymocap工程里已有openpose配置完成，则此步骤可跳过*
### 5) 进行人体SMPL参数估计
cd到easymocap目录下，运行以下脚本

a. 输入数据是video或者images都要跑这行，out和openpose选项可以省略,主要作用是将video转成图像同时把openpose的输出转为annots文件夹

```bash
data=path/to/data
out=path/to/output
python3 scripts/preprocess/extract_video.py ${data} --openpose <openpose_path> --handface

- `--openpose`: specify the openpose path
- `--handface`: detect hands and face keypoints

```
b.根据前面a步骤得到的annots关键点文件夹，进行smpl参数的估计，输出包括smpl姿态参数、形态参数、二维及三维关键点的投影结果、姿态下的mesh的顶点等。
```
python apps\demo\mv1p.py --out output_path --vis_det --vis_repro --undis --sub_vis selected_sub_vis --vis_smpl --model smpl --body body25 --write_vertices
```
The input flags:

- `--undis`: use to undistort the images
- `--start, --end`: control the begin and end number of frames.

The output flags:

- `--vis_det`: visualize the detection
- `--vis_repro`: visualize the reprojection
- `--sub_vis`: use to specify the views to visualize. If not set, the code will use all views
- `--vis_smpl`: use to render the SMPL mesh to images.
- `--write_smpl_full`: use to write the full poses of the SMPL 
    

### 6) 预处理easymocap生成的smpl参数和vertice
cd到工程目录，运行以下脚本, 将上一步的得到的smpl估计参数和顶点参数转换为anerf对应格式，得到new_params、new_vertices目录
```
python preprocess/deep_mocap/anerf/prepare_smpl.py

python preprocess/deep_mocap/anerf/prepare_vertices.py
```
    
### 7) 预处理得到相机数据annots.npy
读入相机参数的表示文件、输出anerf需要的相机文件格式annots.npy
```
python preprocess/deep_mocap/anerf/prepare_camera_parameter.py
```
    
### 8) 预处理得到lbs数据
cd到工程目录，运行以下脚本, 准备各个pose下的蒙皮权重数据，注意该脚本要求安装 https://github.com/MPI-IS/mesh 输出为lbs目录
```
python tools/prepare_blend_weights.py
```
    
### 9)处理图像文件名
运行以下脚本，去掉前序步骤文件名中为了保持文件顺序添加的0值
```
python preprocess/deep_mocap/anerf/unfill_zero_image.py
```
    