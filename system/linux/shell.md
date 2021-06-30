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

    du -h --max-depth=1 {目录}

> 创建磁盘分区
    
    fdisk /dev/sdb

    mkfs.ext4 /dev/sdb

    vim /etc/fstab 
        /dev/sdb                /home/sdb               ext4    defaults        0 0
    mount -a


> 查看并发
    
    netstat -antp | grep 80 | grep ESTABLSED -c


> 查看之前的命令
    
    history

>动态查看 cpu 内存
    
    top
    // 查看详细命令
    -c


    %us：表示用户空间程序的cpu使用率（没有通过nice调度）

    %sy：表示系统空间的cpu使用率，主要是内核程序。
    
    %ni：表示用户空间且通过nice调度过的程序的cpu使用率。
    
    %id：空闲cpu
    
    %wa：cpu运行时在等待io的时间
    
    %hi：cpu处理硬中断的数量
    
    %si：cpu处理软中断的数量
    
    %st：被虚拟机偷走的cpu

> 软连接

    ln -s 源文件 目标文件

    -f : 链结时先将与 dist 同档名的档案删除
    -d : 允许系统管理者硬链结自己的目录
    -i : 在删除与 dist 同档名的档案时先进行询问
    -n : 在进行软连结时，将 dist 视为一般的档案
    -s : 进行软链结(symbolic link)
    -v : 在连结之前显示其档名
    -b : 将在链结时会被覆写或删除的档案进行备份
    -S SUFFIX : 将备份的档案都加上 SUFFIX 的字尾
    -V METHOD : 指定备份的方式
    --help : 显示辅助说明
    --version : 显示版本

> ls 命令

    # 只显示目录
    ls -F | grep "/$"
    # 只显示文件
    ls -al | grep "^-"

> rsync 文件同步

    rsync -av 源目录 目标目录
    
    -a：归档模式，相当于递归、保留权限等多个选项的组合
    -r：将数据递归（但不保存时间戳和权限，同时传输数据
    -v：显示同步过程详细信息
    -z：传输过程中启用压缩
    -A：保留文件的ACL属性信息
    -n：测试同步过程，不做实际修改
    –delete：删除目标文件夹内多余的文档
    -e: 协议

    # 远程同步
    rsync -ae ssh /home/data root@127.0.0.2:/home/data



[返回目录](../../README.md)