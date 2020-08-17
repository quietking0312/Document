
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
    



[返回目录](../README.md)