>下载

    https://npm.taobao.org/mirrors/


### mac 环境没有自带pip 命令
    sudo easy_install pip   #pip 安装

### 使用国内镜像进行第三方包下载，以下为清华大学镜像源
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ <module>


### 开发阶段 使用virtualenv进行python 环境隔离
    pip install virtualenv

    virtualenv -p python2.7 py2env
    
    source py2env/bin/active
    
### pip 命令
    pip freeze > requirements.txt     #导出第三方库版本
    
    pip install -r requirements.txt   #根据导出的第三方库版本进行下载第三方库
    
    
    
    
[返回目录](../README.md)