>@quiet 2021-12-24

# gitlab 安装指北

gitlab 

组件：
AlertManager  报警插件，用于管理报警信息，然后通过email 等方式发送
grafana   开源的数据可视化插件 源码是golang
logrotate   日常切割压缩
redis  
gitaly       git的rpc服务， gitlab-rails 通过该组件与底层的git通信
postgresql     开源的关系型数据库
postgres-exporter 用于监听postgresql
prometheus      系统监控框架 类似 zabbix
nginx    

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
> ### gitlab-ce 是社区版， gitlab-ee是企业版。 企业版包含社区版所有内容，以及额外需要付费的内容。 可以安装企业版不付费，当社区版使用

二、 安装

1. 安装gitlab
> 默认安装[开发机性能不足无法顺利编译,更新中...]
> 
> 清华大学开源镜像站：https://mirrors.tuna.tsinghua.edu.cn/gitlab-ee/
> 
> 官方安装脚本 https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh

>镜像安装方法：
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
```shell
apt install gitlab-ee
```

> 官方脚本安装:
```shell
# 环境
sudo apt-get update
sudo apt-get install -y curl openssh-server ca-certificates tzdata perl
# 邮箱
sudo apt-get install -y postfix
# 配置源
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash
# 安装
sudo EXTERNAL_URL="https://gitlab.example.com" apt-get install gitlab-ee
```

>docker 安装
```shell
docker pull gitlab/gitlab-ee:latest

docker run -itd -p 9980:80 -p 9922:22 -v /gitlab/etc:/etc/gitlab -v /gitlab/log:/var/log/gitlab -v /gitlab/opt:/var/opt/gitlab --privileged=true --name gitlab-ee gitlab/gitlab-ee
```
> docker-compose 安装
```yaml
version: '3'

services:
  gitlab:
    image: 'gitlab/gitlab-ee:14.5.2-ee.0'
    restart: unless-stopped
    environment:
      TZ: 'Asia/Shanghai'
      GENERATED_EXTERNAL_URL: |
        external_url 'http://192.168.92.171:8880'
    ports:
      - '8880:8880'
      - '443:443'
      - '2212:22'
    volumes:
      - './etc:/etc/gitlab'
      - './log:/var/log/gitlab'
      - './opt:/var/opt/gitlab'
```
```shell
docker-compose up -d
```

二、 配置说明
>配置文件： /etc/gitlab/gitlab.rb
>
```shell
vi /etc/gitlab/gitlab.rb
external_url 'http://192.168.0.1'  # 修改为ip或者域名， 指拉取git 的地址

# gitlab.yml gitlab 的功能
# # ssh连接， 页面主题， 邮箱服务器设置等相关


```
