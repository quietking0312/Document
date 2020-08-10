
> 启动， 停止， 重启， 查询

    service mysql start
    
    service mysql stop
    
    service mysql restart
    
    service mysql status



> 初始密码未知，密码忘记解决方案
    
    # 设置免密码登陆
    cat /etc/mysql/debian.cnf
    
    mysql -u <username> -p
    <password>
    
    use mysql;                   #连接到mysql数据库
    
    update mysql.user set authentication_string=password('123456') where user='root' and Host ='localhost';    #修改密码123456是密码
    
    update user set  plugin="mysql_native_password";     
    
    flush privileges;
    
    quit; 