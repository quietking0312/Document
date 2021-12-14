> 安装

```shell
    # 安装add-apt-repository 命令
    apt-get install software-properties-common
    #添加源
    add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe'
    # 安装
    apt update
    apt install mysql-server-5.6
    
    
    # 报错
    
    The following packages have unmet dependencies:
     mysql-server-5.6 : Depends: initscripts but it is not installable
                        Depends: sysv-rc (>= 2.88dsf-24) but it is not installable or
                                 file-rc (>= 0.8.16) but it is not installable
                        Recommends: libhtml-template-perl but it is not going to be installed
    E: Unable to correct problems, you have held broken packages.
    # 原因 ubuntu 17.04 仅支持mysql5.7
    # ubuntu 20.04 支持mysql8.0
    
```

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
    

> 执行计划 查看

    explain {sql}

1. select_type	说明
    SIMPLE	简单查询
    PRIMARY	最外层查询
    SUBQUERY	映射为子查询
    DERIVED	子查询
    UNION	联合
    UNION RESULT	使用联合的结果
2. type	说明
```
   ALL	全数据表扫描
   index	全索引表扫描
   RANGE	对索引列进行范围查找
   INDEX_MERGE	合并索引，使用多个单列索引搜索
   REF	根据索引查找一个或多个值
   EQ_REF	搜索时使用primary key 或 unique类型
   CONST	常量，表最多有一个匹配行,因为仅有一行,在这行的列值可被优化器剩余部分认为是常数,const表很快,因为它们只读取一次。
   SYSTEM	系统，表仅有一行(=系统表)。这是const联接类型的一个特例。
   性能：all < index < range < index_merge < ref_or_null < ref < eq_ref < system/const
```

3. possible_keys : 可能使用的索引

4. key : 真实使用的

5. key_len : MySQL中使用索引字节长度

6. rows : mysql 预估为了找到所需的行而要读取的行数

7. extra	说明
```
    Using index	此值表示mysql将使用覆盖索引，以避免访问表。
    Using where	mysql 将在存储引擎检索行后再进行过滤，许多where条件里涉及索引中的列，当(并且如果)它读取索引时，就能被存储引擎检验，因此不是所有带where子句的查询都会显示“Using where”。有时“Using where”的出现就是一个暗示：查询可受益于不同的索引。
    Using temporary	mysql 对查询结果排序时会使用临时表。
    Using filesort	mysql会对结果使用一个外部索引排序，而不是按索引次序从表里读取行。mysql有两种文件排序算法，这两种排序方式都可以在内存或者磁盘上完成，explain不会告诉你mysql将使用哪一种文件排序，也不会告诉你排序会在内存里还是磁盘上完成。
    Range checked for each record(index map: N)	没有好用的索引，新的索引将在联接的每一行上重新估算，N是显示在possible_keys列中索引的位图，并且是冗余的
```


[返回目录](../README.md)
