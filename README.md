# 视频图像“隐形"处理

## 环境搭建

系统:  ubuntu20.04LTS

显存要求:  >8G

首先创建conda环境：(pytorch=2.0.0  cuda=11.8)

```shell
conda env create -f environment.yaml -n video
conda activate video
```

若出现pytorch无法安装的情况，执行如下命令安装pytorch框架

```shell
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```

若出现mmcv库无法安装的情况，执行如下命令安装mmcv库：

```shell
pip install -U openmim
mim install mmcv
```

## 运行准备

### 预训练模型下载[下载链接](https://pan.baidu.com/s/1ahAu_wHrPE8kVbxmXLNFTQ?pwd=e396)

下载预训练模型，解压后将其放入release_model文件夹下，完成后目录结构如下：

```bash
release_model
   |- E2FGVI-CVPR22.pth
   |- E2FGVI-HQ-CVPR22.pth
   |- i3d_rgb_imagenet.pt
```

## 效果展示

模型可以支持mp4与视频帧形式的流输入。

#### 示例1

安装完整依赖后终端运行

```shell
python test.py --model e2fgvi  --video examples/tennis --mask examples/tennis_mask  --ckpt release_model/E2FGVI-CVPR22.pth
```

该命令将示例中的tennis视频帧输入至网络中，将mask参数对应的掩码内容消除得到处理后的视频，结果保存在results文件夹中。

#### 示例2

终端运行

```shell
python test.py --model e2fgvi --video examples/schoolgirls.mp4 --mask examples/schoolgirls_mask  --ckpt release_model/E2FGVI-CVPR22.pth
```

该命令将mp4格式的视频schoolgirls.mp4输入，将mask参数对应的掩码内容消除得到处理后的视频，结果保存在results文件夹中。

## 模型评估

终端运行

```shell
python evaluate.py --model e2fgvi --dataset davis --data_root datasets/ --ckpt release_model/E2FGVI-CVPR22.pth
```

会在终端输出各个评估数据集的PSNR以及SSIM指标。
