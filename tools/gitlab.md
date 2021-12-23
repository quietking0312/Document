
# gitlab 安装指北

一、 环境

1、查询系统版本
```shell
 cat /etc/issue
 # Ubuntu 20.04.3 LTS \n \l
 cat /proc/version
 # Linux version 5.10.16.3-microsoft-standard-WSL2 (oe-user@oe-host) (x86_64-msft-linux-gcc (GCC) 9.3.0, GNU ld (GNU Binutils) 2.34.0.20200220) #1 SMP Fri Apr 2 22:23:49 UTC 2021
```

2. gitlab网站
> 官网：https://about.gitlab.com/install/
> 清华大学开源镜像站：https://mirrors.tuna.tsinghua.edu.cn/gitlab-ee/
> ### gitlab-ce 是社区版， gitlab-ee是企业版。 企业版包含社区版所有内容，以及额外需要付费的内容。 可以安装企业版不付费，当社区版使用

二、 安装

```shell
# 安装密钥
curl https://packages.gitlab.com/gpg.key | apt-key add -
# 报错：gnupg, gnupg2 and gnupg1 do not seem to be installed, but one of them is required for this operation 解决方法如下
apt install gnupg2
# gnupg 是一种用于加密，数字签名，生产非对称密钥对的软件
```

```shell
 # ubuntu 配置源
 vi /etc/apt/sources.list.d/gitlab-ee.list
 # 添加以下内容
 deb https://mirrors.tuna.tsinghua.edu.cn/gitlab-ee/ubuntu xenial main
 # 更新源
 apt update
```
1. 安装gitlab
```shell
apt install gitlab-ee
```
>配置文件： /etc/gitlab/gitlab.rb
>配置文件： /opt/gitlab/embedded/service/gitlab-rails/config/gitlab.yml
2. 修改配置
```shell
vi /etc/gitlab/gitlab.rb
external_url 'http://192.168.0.1'  # 修改为ip或者域名

vi /opt/gitlab/embedded/service/gitlab-rails/config/gitlab.yml
```

3. 安装git
```shell
apt install git
```

>docker 安装
```shell
docker pull gitlab/gitlab-ee:latest

docker run -itd -p 9980:80 -p 9922:22 -v /gitlab/etc:/etc/gitlab -v /gitlab/log:/var/log/gitlab -v /gitlab/opt:/var/opt/gitlab --privileged=true --name gitlab-ee gitlab/gitlab-ee
```
