/usr/lib/systemd/system/server.service


[Unit]
Description=server     # 服务描述
After=network.target # 服务依赖 启动这些服务后在启动本服务

[Service]
Type=simple
ExecStart=/root/bin/server server -c xxx.toml  #启动服务命令     
ExecReload=/bin/kill -s USR1 $MAINPID # 重新加载配置文件命令
PrivateTmp=true 

TimeoutSec=600 # 自动重启间隔描述

Restart=always # 何种情况systemd 会自动重启当前服务

[Install]
WantedBy=multi-user.target       # 服务所在服务组





systemctl start 服务名            开启服务

systemctl stop 服务名            关闭服务

systemctl status 服务名    　显示状态

systemctl restart 服务名    　重启服务

systemctl enable 服务名    　开机启动服务

systemctl disable 服务名    　禁止开机启动

systemctl reload　重新加载服务

systemctl is-enabled 服务名　查询是否自启动服务




