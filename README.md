# CGZZT
A dirty deal between three beautiful sister and an uncle

## 工具准备

- [Mxnet](https://github.com/dmlc/mxnet/releases)
- Anaconda2
- cv2 (conda install -c https://conda.binstar.org/menpo opencv)

## 使用说明

先确定mxnet以及cv2正确安装

```
python predictone.py pic.png
```

![image](https://github.com/tsstss123/CGZZT/raw/master/screenshot.png)

## 代码说明

### inception-bn-28.py

我们采用一个小型的28*28的inception-bn网络

### conv.py

进行训练的代码，参数在文件里面调（改成参数怕更不直观...）

### predict.py

用模型文件进行预测

### predictone.py

对单张图片进行预测

### im2rec.py

进过简单修改的mxnet提供的将图片制作成二进制格式训练集的工具，原版有些问题

### showRec.py

提取二进制格式训练集中的图片的工具，查看训练集是否制作正确

### cal.py

统计当前目录下的中文文件信息，并输出整个list的二进制存档

### pull.py

在指定网址循环下载图片

### char.pki

中文字符表的list的二进制文件

### status.txt

中文训练集统计信息

### *.rec

二进制格式训练集

### *-symbol.json

网络的json格式

### *.params

网络的参数权重

## Git使用说明

先本地设置好,fork一份到自己的仓库,用https方法clone一份到本机

### 添加我的仓库为远程源

```
git remote -v
git remote add upstream https://github.com/tsstss123/CGZZT/
```

### 从主仓库拉更新

```
git fetch upstream
git merge upstream/master
```

[在github网页上更新的方法](https://www.zhihu.com/question/20393785/answer/30725725)

[fork后如何同步源的新更新](https://segmentfault.com/q/1010000002590371)

向我提交代码,向我发起pull request即可

### git学习参考

[史上最浅显易懂的Git教程！ 廖雪峰](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)

[Pro Git（中文版）](http://git.oschina.net/progit/)

[Git远程操作详解 阮一峰](http://www.ruanyifeng.com/blog/2014/06/git_remote.html)

[fork后如何跟上源repo的变化](https://segmentfault.com/q/1010000002590371)

### Markdown学习参考

[Markdown入门指南](http://www.jianshu.com/p/1e402922ee32)
