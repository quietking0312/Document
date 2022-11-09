

# ubuntu 添加用户

```shell
 # 添加用户
 sudo useradd -m {username}
 # 添加密码
 sudo passwd {username}
 # 修改默认目录及命令
 sudo vim /etc/passwd
 # 添加sudo权限
 sudo vim /etc/sudoers
      {username} ALL=(ALL:ALL) NOPASSWD: ALL
```

