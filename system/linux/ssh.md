
> 修改ssh端口

    # 将22端口修改
    sudo vi /etc/ssh/sshd_config
    
    #重启ssh服务
    service sshd restart
    
    #查看更改是否生效
    netstat -tlnp



> ssh 配置

    sudo vi /etc/ssh/sshd_config
    Port 22               //监听的端口号为22
    Protocol 2            //使用SSH V2协议
    ListenAdderss 0.0.0.0   //监听的地址为所有的地址
    UserDNS no         //禁止DNS反向解析
    PermitRootLogin no              // 禁止root用户登录
    PermitEmptyPasswords no    // 禁止空密码用户登录
    LoginGraceTime 2m             // 登录验证时间为2分钟
    MaxAuthTries 6                   //  最大重试次数6次
    AllowUsers steven               // 只允许steven用户登录
    DenyUsers steven               //  不允许登录用户 steven
    PasswordAuthentication  yes       //启用密码验证
    PubkeyAuthentication    yes         //启用密匙验证
    AuthorsizedKeysFile .ssh/authorized_keys  //指定公钥数据库文件
    #重启ssh服务
    service sshd restart