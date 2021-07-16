> 检查
    # 检查配置文件
    nginx -t
> 启动
> 
    # 启动
    #windows
    start nginx

    # centos
    # 重新加载配置文件, 重新加载配置文件不会关闭长链接
    nginx -s reload
    
    # 停止
    #windows
    nginx.exe -s quit 
    或
    nginx.exe -s stop

    

> 配置
> 
    use epoll;
    # 进程数, 建议设置为cpu 核心数
    worker_processes 4
    # 每个worker 能处理的最大链接数, 不能超过 文件句柄数
    worker_connections
    multi_accept off;


    实际最大链接数计算方法
        nginx作为http服务器的时候：
            max_clients = worker_processes * worker_connections/2
        nginx作为反向代理服务器的时候：
            max_clients = worker_processes * worker_connections/4


    location / {
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }