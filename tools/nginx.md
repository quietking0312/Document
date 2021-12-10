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


    gzip  on;
    gzip_min_length 1k;  #压缩页面最小字节数
    gzip_buffers 4 16k; # 以16k 为单位 4倍
    gzip_http_version 1.1;
    gzip_comp_level 4; # gzip 压缩比 1-9， 1压缩比最小，速度最快， 9压缩比最大，速度最慢， 消耗cpu
    gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;
    gzip_vary on;
    gzip_disable "MSIE [1-6].";

    #限制用户连接数来预防DOS攻击
    limit_conn_zone $binary_remote_addr zone=perip:10m;
    limit_conn_zone $server_name zone=perserver:10m;
    #限制同一客户端ip最大并发连接数
    limit_conn perip 10;
    #限制同一server最大并发连接数
    limit_conn perserver 100;

    location / {
        if ($request_uri ~* .(gz)$){
            add_header 'content-encoding' gzip;
        }
        location ~* ^.*\.(wasm.gz)$ { # 静态压缩解决方案
            gunzip on; # 该条需要插件ngx_http_gunzip_module 支持
            gzip off; # 已经做了静态压缩, nginx 不需要对其进行压缩
            types {}
            default_type application/wasm;
            add_header Content-Encoding gzip;
        }
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

> cors.conf

```
if ($request_method = 'OPTIONS') {
    add_header 'Access-Control-Allow-Origin' '*' always;
    add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, PUT, DELETE' always;
    add_header 'Access-Control-Allow-Headers' 'DNT,X-Mx-ReqToken,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization,Content-Disposition' always;
    add_header 'Access-Control-Max-Age' 1728000 always;

    return 204;
}

if ($request_method ~* "(GET|POST|DELETE|PUT)") {
    add_header 'Access-Control-Allow-Origin' '*' always;
}
```

[返回目录](../README.md)