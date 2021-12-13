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
    gzip_buffers 8 16k; # 以16k 为单位 4倍
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

> ubuntu nginx 编译安装

# nginx官网 http://nginx.org/en/download.html

```shell
  # 下载
  wget http://nginx.org/download/nginx-1.21.4.tar.gz
  
  # 解压
  tar zxvf nginx-1.21.4.tar.gz

```
```shell
    # 检测环境
    gcc -v
    g++ -v
    autoconf -h
    make -h
    # 环境安装
    apt-get install build-essential gcc autoconf make
    # centos 使用 gcc-c++ 代替 build-essential
    
    #pcre 库
    apt-get install libpcre3-dev
    
    #openssl 库
    apt-get install libssl-dev
    
    # zlib 库
    apt-get install zlib1g-dev
```

```shell
    cd nginx-1.21.4
    ./configure  --prefix=/usr/local/nginx  --sbin-path=/usr/local/nginx/sbin/nginx --conf-path=/usr/local/nginx/conf/nginx.conf --error-log-path=/var/log/nginx/error.log  --http-log-path=/var/log/nginx/access.log  --pid-path=/var/run/nginx/nginx.pid --lock-path=/var/lock/nginx.lock  --user=nginx --group=nginx --with-http_ssl_module --with-http_stub_status_module --with-http_gzip_static_module --http-client-body-temp-path=/var/tmp/nginx/client/ --http-proxy-temp-path=/var/tmp/nginx/proxy/ --http-fastcgi-temp-path=/var/tmp/nginx/fcgi/ --http-uwsgi-temp-path=/var/tmp/nginx/uwsgi --http-scgi-temp-path=/var/tmp/nginx/scgi --with-pcre
    # 参数说明
    --prefix              nginx安装的基础目录 默认 /usr/local/nginx
    --sbin-path           nginx二进制安装目录 默认 /sbin/nginx
    --conf-path           nginx主配置文件安装位置      默认 /conf/nginx.conf
    --error-log-path      错误日志位置           默认 /logs/error.log
    --http-log-path      访问日志位置      默认 /logs/access.log
    --pid-path         pid文件路径    /logs/nginx.pid
    --lock-path        锁文件位置     /logs/nginx.lock
    --user    指定用户 `useradd nginx`  添加用户 可以解决 getpwnam("nginx") failed 报错
    --group   指定用户组
    
    --with-http_ssl_module 
    --with-http_stub_status_module 
    --with-http_gzip_static_module
    --with-pcre  强制使用pcre, 该库主要用于正则表达式的支持
    
    
    --http-client-body-temp-path   存放由客户端请求生成的临时文件路径 /client-body_temp
    --http-proxy-temp-path         proxy产生的临时文件位置 /proxy_temp
    --http-fastcgi-temp-path      由http, FastCGL, uwsgi scgi模块产生的临时文件位置 / fastcgi_temp, /uwsgi_temp, and/scgi_temp
    --http-uwsgi-temp-path
    --http-scgi-temp-path
    
    # 安装
    make
```
```shell
    # 默认启动模块， 以下参数允许禁用默认启用模块
    --without-http_charset_module
    --without-http_gzip_module
    --without-http_ssi_module
    --without-http_userid_module
    --without-http_access_module
    --without-http_access_module
    --without-http_autoindex_module
    --without-http_geo_module
    --without-http_map_module
    --without-http_referer_module
    --without-http_rewrite_module
    --without-http_proxy_module
    --without-http_fastcgi_module
    --without-http_uwsgi_module
    --without-http_scgi_module
    --without-http_memcached_module
    --without-http_limit_conn_module
    --without-http_limit_req_module
    --without-http_empty_gif_module
    --without-http_browser_module
    --without-http_upstream_ip_hash_module
    --without-http_upstream_least_conn_module
    --without-http_split_clients_module
    
    #默认禁用模块, 以下参数允许启用默认禁用模块
    --with-http_ssl_module
    --with-http_realip_module
    --with-http_addition_module
    --with-http_xslt_module
    --with-http_image_filter_module
    --with-http_geoip_module
    --with-http_sub_module
    --with-http_dav_module
    --with-http_flv_module
    --with-http_mp4_module
    --with-http_gzip_static_module
    --with-http_random_index_module
    --with-http_secure_link_module
    --with-http_stub_status_module
    --with-google_perftools_module
    --with-http_degradation_module
    --with-http_perl_module
    --with-http_spdy_module
    --with-http_gunzip_module
    --with-http_auth_request_module
```
```shell
  # ubuntu apt-get install nginx 默认参数
  --with-cc-opt='-g -O2 -fdebug-prefix-map=/build/nginx-KTLRnK/nginx-1.18.0=. -fstack-protector-strong -Wformat -Werror=format-security -fPIC -Wdate-time -D_FORTIFY_SOURCE=2' 
  --with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-z,now -fPIC'
  --prefix=/usr/share/nginx 
  --conf-path=/etc/nginx/nginx.conf 
  --http-log-path=/var/log/nginx/access.log 
  --error-log-path=/var/log/nginx/error.log 
  --lock-path=/var/lock/nginx.lock 
  --pid-path=/run/nginx.pid 
  --modules-path=/usr/lib/nginx/modules 
  --http-client-body-temp-path=/var/lib/nginx/body 
  --http-fastcgi-temp-path=/var/lib/nginx/fastcgi 
  --http-proxy-temp-path=/var/lib/nginx/proxy 
  --http-scgi-temp-path=/var/lib/nginx/scgi 
  --http-uwsgi-temp-path=/var/lib/nginx/uwsgi 
  --with-debug 
  --with-compat 
  --with-pcre-jit 
  --with-http_ssl_module 
  --with-http_stub_status_module 
  --with-http_realip_module 
  --with-http_auth_request_module 
  --with-http_v2_module 
  --with-http_dav_module 
  --with-http_slice_module 
  --with-threads 
  --with-http_addition_module 
  --with-http_gunzip_module 
  --with-http_gzip_static_module 
  --with-http_image_filter_module=dynamic 
  --with-http_sub_module 
  --with-http_xslt_module=dynamic 
  --with-stream=dynamic 
  --with-stream_ssl_module 
  --with-mail=dynamic 
  --with-mail_ssl_module

```
[返回目录](../README.md)