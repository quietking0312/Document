> 查询云端镜像

    sudo docker search mongo

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