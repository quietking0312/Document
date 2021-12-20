

# 安装

```shell
    # 安装add-apt-repository 命令
    apt install software-properties-common
    
    # 添加php源
    add-apt-repository ppa:ondrej/php && sudo apt-get update
  
    apt install php7.2-fpm php7.2-mysql
    
    # 修改
    vim /etc/php/7.2/fpm/pool.d/www.conf
    ;listen = /run/php/php7.2-fpm.sock
    listen = 127.0.0.1:9000
    
    # 添加扩展
    vim /etc/php/7.2/fpm/php.ini
    extension=mysqli
    extension=pdo_mysql
    extension=pdo_odbc
```

# php-nginx

```shell
server {
    listen      80;
    server_name 127.0.0.1;
    index        index.php index.html;
    root         /data/www/;
    client_max_body_size 50M;
    #include /etc/nginx/default.d/*.conf;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }


    location ~ \.php$ {
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  /$document_root$fastcgi_script_name;
        #fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        include        fastcgi_params;
        fastcgi_param  PROJECT_ENVIRONMENT      production;
    }

}
```
docker 集群部署注意事项
1. nginx-php-fpm工作流程如下
```shell
  用户请求 -> nginx ->转发php解析器 -> php-fpm -> 读取代码 执行函数 -> 返回 -> nginx -> 返回 -> 用户页面展示
```
2. 读取php代码的工作由php-fpm 进程完成，读取js,css代码由nginx完成， 因此需要将代码目录同时挂载到php-fpm 容器和nginx容器相同的路径下
