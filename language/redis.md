
# redis
    
    redis-cli -h {host} -p {port} -a {password} -n {db}

    // 删除
    redis-cli -h {host} -p 6379 keys {key} | xargs redis-cli -h {host} -p 6379 del    