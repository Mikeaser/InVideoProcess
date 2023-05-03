# 视频图像“隐形"处理

## 环境搭建

系统： ubuntu20.04LTS

首先创建conda环境：(pytorch=2.0.0  cuda=11.8)

```shell
conda create -n video
conda activate video
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```

根据需求文件安装完整环境

```shell
pip install -r requirements.txt
```

若出现mmcv库或pytorch无法安装的情况，执行如下命令安装mmcv库：

```shell
pip install -U openmim
mim install mmcv
```
