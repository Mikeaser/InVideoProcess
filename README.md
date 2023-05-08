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

## 运行准备

### 预训练模型下载[下载链接]()

下载预训练模型，解压后将其放入release_model文件夹下，完成后目录结构如下：

```bash
release_model
   |- E2FGVI-CVPR22.pth
   |- E2FGVI-HQ-CVPR22.pth
   |- i3d_rgb_imagenet.pt
```

### 完整训练数据下载[下载链接]()

<table>
<thead>
  <tr>
    <th>数据集</th>
    <th>YouTube-VOS</th>
    <th>DAVIS</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>详情</td>
    <td>训练: 3,471, 验证: 508</td>
    <td>验证: 50 (共90)</td>
  <tr>
    <td>Images</td>
    <td> [<a href="https://competitions.codalab.org/competitions/19544#participate-get-data">官方链接</a>] (下载全部训练测试集) </td>
    <td> [<a href="https://data.vision.ee.ethz.ch/csergi/share/davis/DAVIS-2017-trainval-480p.zip">官方链接</a>] (2017, 480p, TrainVal) </td>
  </tr>
  <tr>
    <td>Masks</td>
    <td colspan="2"> [<a href="https://drive.google.com/file/d/1dFTneS_zaJAHjglxU10gYzr1-xALgHa4/view?usp=sharing">谷歌网盘</a>] [<a href="https://pan.baidu.com/s/1JC-UKmlQfjhVtD81196cxA?pwd=87e3">百度网盘</a>] </td>
  </tr>
</tbody>
</table>
