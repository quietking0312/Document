
### 修改环境变量添加阿里云镜像
    # windows
    go env -w GO111MODULE=on
    go env -w GOPROXY=https://mirrors.aliyun.com/goproxy/
    
    # mac
    export GOPROXY=https://mirrors.aliyun.com/goproxy/

### go mod 命令
    go mod init <module>  # 初始化
    go mod tidy           # 添加未被收录的模块， 删除不使用的引用
    
### 发布编译
    go build




[返回目录](../README.md)