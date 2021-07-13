
> 启动， 停止， 重启， 查询

    service mysql start
    
    service mysql stop
    
    service mysql restart
    
    service mysql status


> 创建数据库

    CREATE DATABASE  IF NOT EXISTS `db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    
    #修改字段 
    alter table register modify column data text;

> 导出表结构

    mysqldump -hhostname -uusername -ppassword -d databasename > d:\sql\databasename.sql

> 导出数据

    mysqldump -hhostname -uusername -ppassword databasename > d:\sql\databasename.sql

> 导入

    use databasename;
    source databasename.sql

> 查看详细列
    
    show full fields from table;

> 查看支持的字符集
    
    show characher set;
    
     show collation where charset='utf8mb4';

> mysql5.6 报错处理方案

    1.ERROR 1071 (42000): Specified key was too long; max key length is 767 bytes
     指超出索引字节的限制，并不是指字段长度限制
    

[返回目录](../README.md)
