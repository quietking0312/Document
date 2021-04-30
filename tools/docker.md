
> 修改镜像源
    
    1. 指定镜像全部路径
    
    docker pull {地址源无http}/ubuntu
    
    2. 修改
    /etc/docker/daemon.json
    
    {
      "registry-mirrors": ["{地址源有http}"]
    }
    
    3. 配置守护进程
    dockerd --registry-mirror={地址源有http}

> 查询云端镜像

    sudo docker search mongo
    
> 拉取镜像

    sudo docker pull {image_name}:{tag}

> 删除镜像

    sudo docker rmi {image_name}:{tag}
    
> 查看容器信息

    docker inspect {容器名}

> 删除容器

    sudo docker rm {containerid}

> 进入正在运行的docker 容器

    sudo docker exec -it {containerid} /bin/bash

> 导出镜像

    sudo docker save > {file_name}.tar {imageid}

> 导入镜像

    sudo docker load < {file_name}.tar

> 挂载卷
    
    #查询
    sudo docker volume ls
    删除
    sudo docker volume rm {volumename}
    
> 获取容器名称

    docker ps -a --format "{{.Name}}"

>Windows 上使用docker 

    安装好docker后， 务必点击 switch to Linux containers， 否则镜像会安装失败

>容器启动

    docker run -itd --name mongo -p 27017:27017 -v /home/mongo/data:/data/db -v /home/mongo/conf:/data/configdb mongo
    
    docker run -itd --name redis -p 6379:6379 redis:latest
    
    docker run -itd --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD="123456" -e MYSQL_DATABASE="TEST" mysql

> 容器具体信息查看
    
    docker inspect {dockerName}

[返回目录](../README.md)