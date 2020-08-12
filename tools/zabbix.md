
>安装


[下载](https://www.zabbix.com/cn/download?zabbix=5.0&os_distribution=ubuntu&os_version=18.04_bionic&db=mysql&ws=nginx)
    
    # 解包
    tar xf zabbix-5.0.2.tar.gz
        
    cd zabbix-5.0.2
    
    ./configure --prefix=/usr/share/zabbix-server --enable-server --enable-agent --with-mysql --with-net-snmp --with-libcurl --with-libxml2  --enable-java

    



> 错误处理
>> error: MySQL library not found
    
    # 查询文件
    find / -name "mysql_config*" 
    # 未找的则 安装
    apt-get install libmysqlclient-dev  

>> error: LIBXML2 library not found

    apt-get install libxml2-dev

>> Invalid Net-SNMP directory - unable to find net-snmp-config
    
    # ubuntu
    apt-get install snmp snmpd libsnmp-dev
    
>> error: Unable to use libevent (libevent check failed)
    
    apt-get install libevent-dev


>> error: Unable to find "javac" executable in path

    apt-get install openjdk-8-jdk
    
>> error: Curl library not found
    
    apt-get install libcurl4-openssl-dev

>>

    默认账号密码
    Admin
    zabbix


>> 解决中文语言问题
    
    apt-get install langpacks-zh_CN.noarch
    dpkg-reconfigure locales
    reboot

[Zabbix官方文档](https://www.zabbix.com/documentation/4.0/zh/manual)

[源码安装教程](https://www.jianshu.com/p/253f3a7dbc90)

[编译报错解决方案](https://www.cnblogs.com/yinzhengjie2020/p/12306882.html)

[使用教程](https://www.cnblogs.com/linyaonie/p/10017089.html)


[返回目录](../README.md)