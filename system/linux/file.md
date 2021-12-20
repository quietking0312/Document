
# 文件操作

sed
```shell
    sed [option]
    -a #新增
    -c 取代
    -d 删除
    -i 插入
```
示例：
```shell
  sed -i 's/;extension=mysqli/extension=mysqli/g' /etc/php7/php.ini
```
