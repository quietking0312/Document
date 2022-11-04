

# ucloud 云服务器数据盘扩容操作
> 线上数据盘 或者数据盘内含有重要数据， 建议先做一个磁盘快照
> 
> 数据盘扩容不需要重启
# 操作步骤
1. 使用后端对磁盘进行扩容
2. lsblk 或者 fdisk -l 确认磁盘大小 是否扩容完成
3. df -Th 确认挂载目录大小
4. sudo apt-get install cloud-initramfs-growroot        // ucloud 工具
5. LANG=en_US.UTF-8
   resize2fs /dev/vdb

6. df -Th查看磁盘