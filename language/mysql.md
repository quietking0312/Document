
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
    
[返回目录](../README.md)
