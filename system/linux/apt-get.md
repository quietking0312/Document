
    # 查询指定的软件是否存在
    apt-cache search all |grep mysql

    -h, --help              // 查看帮助文档
    -v, --version           // 查看 apt-get 的版本
    -y                      // 在需要确认的场景中回应 yes
    -s, --dry-run           // 模拟执行并输出结果
    -d, --download-only     // 把包下载到缓存中而不安装
    --only-upgrade          // 更新当前版本的包而不是安装新的版本
    --no-upgrade            // 在执行 install 命令时，不安装已安装包的更新
    -q, --quiet             // 减少输出
    --purge                 // 配合 remove 命令删除包的配置文件
    --reinstall             // 重新安装已安装的包或其新版本