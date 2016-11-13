# CGZZT
A dirty deal between three beautiful sister and an uncle

## 工具准备

- [Mxnet](https://github.com/dmlc/mxnet/releases) (win7-64版本见目录内附使用方法)
- Anaconda2
- cv2 (conda install -c https://conda.binstar.org/menpo opencv)

## 代码说明

### wind.py

启动一个GUI展示预测功能(需要网络，自动从网站上下载并预测，人工统计正确率）

### -symbol.json

网络结构

### .params

网络参数

### char.pki

字符编号

## Mxnet Build tutorials

```
# Clone mxnet repository. In terminal, run the commands WITHOUT "sudo"
git clone https://github.com/dmlc/mxnet.git ~/MXNet/mxnet --recursive

# Install MXNet dependencies
cd ~/MXNet/mxnet/setup-utils
bash install-mxnet-ubuntu.sh

# We have added MXNet Python package path in your ~/.bashrc. 
# Run below command to refresh environment variables.
$ source ~/.bashrc
```

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
