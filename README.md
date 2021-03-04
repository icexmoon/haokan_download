# HaokanDownloader使用指南

## 简介

- 本应用的用途为从[**好看视频**](https://haokan.hao123.com/)网站下载指定视频作者的所有视频到本地。
- 本应用支持断点重下。

## 注意事项

1. 本应用基于python3编写，需要安装python3。
2. 本应用为单线程下载，速度较慢，如果同时要下多个视频作者，可以开多个python程序下载，具体多开数目取决于你的电脑性能，作者最多只开了五个。
3. 应用支持Windows和Linux。
4. 本应用需要安装python第三方模块：
   - BeautifulSoup
   - import requests
   - html5lib

> - Windows下安装python3请阅读[**这里**](https://www.cnblogs.com/Moon-Face/p/14440627.html)。
>
> - Linux下安装python3请阅读[**这里**](https://www.cnblogs.com/Moon-Face/p/14469617.html)。
> - python模块安装请阅读[**这里**](https://www.cnblogs.com/Moon-Face/p/14465792.html)，在文件末尾部分。

## 操作指南

### 修改配置

使用前需要先修改存储主目录，具体为用编辑器打开`config.py`文件：

```python
import platform
windowsHomePath = "d:\\download\\好看视频"
LinuxHomePath = "/home/pi/NewmanDisk/haokan"
```

这里有两个预设路径，windows用户修改前一个，Linux用户修改后一个，两个都用的就都修改。

### 使用

在Linux的Bash或者Windows的Cmd命令窗口下使用python执行入口文件`haokan_download.py`后按提示输入好看视频的作者id。程序会进一步检索需要的下载的视频列表，检索速度稍慢，具体视该作者发布了多少视频而定，请耐心等待。

检索好后程序会比对本地已下载的视频，如果已经存在，不会重复下载。

程序对比出未下载视频后会提示有XX个视频未下载，确认后会自动下载。

> 下载的视频会以作者中文昵称（作者id）的形式保存在单独文件夹。

下载完毕后程序会提示`已下载完毕`。

> - 我的博客地址为https://www.cnblogs.com/Moon-Face，可以通过博客联系我。
>
> - 本应用为方便个人使用编写，请不要用于商业用途。



