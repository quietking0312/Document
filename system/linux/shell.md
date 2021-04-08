> 主机名修改
    
    hostname  # 查询主机名
    hostnamectl set-hostname <新主机名>
    reboot    # 重启

> 重启

    reboot

> 查看端口占用

    #查看所有端口
    netstat -aptn
    # 查看所有tcp协议端口
    netstat -ntpl
    #查看指定端口
    netstat -ap |grep -e 80 -e 8080
     
>查看服务状态

    service <服务名> status
    
> 安装rz sz命令

    apt-get install lrzsz

> 修改ssh端口
    
    # 将22端口修改
    sudo vi /etc/ssh/sshd_config
    
    #重启ssh服务
    service sshd restart
    
    #查看更改是否生效
    netstat -tlnp

> 进程查看
    
    // 进程查看
    ps -aux
    // f 查看进程关系
    ps -ef
    
    // 查看启动程序所在路径
    ls -l /proc/{pid}
    
> 查看磁盘占用

    // 查看磁盘挂载详情
    fdisk -l    
    // 查看磁盘总占用
    df -h
    // 查看指定目录占用磁盘
    du -ah {目录}

[返回目录](../../README.md)