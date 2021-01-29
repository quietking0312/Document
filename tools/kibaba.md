
 # docker 搭建方法
 
    docker pull kibana:7.7.1
    
    docker run --link {es容器id}:elasticsearch -p 5601:5601 -d  --name kibana7.7.1 {镜像名称} 
    
    docker exec -it kibana7.7.1 /bin/bash
    
    vi config/kibana.yml
 
    ```
    server.name: kibana
    server.host: "0"
    elasticsearch.hosts: [ "http://elasticsearch:9200" ] // es地址
    monitoring.ui.container.elasticsearch.enabled: true
    i18n.locale: "zh-CN" // 中文
    ```
    