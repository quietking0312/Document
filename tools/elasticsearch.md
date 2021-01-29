# docker 搭建方法

    docker pull elasticsearch:7.7.1 
    
    docker run -d -e ES_JAVA_POTS="-Xms512m -Xmx512m"  -e "discovery.type=single-node" -p 9200:9200 -p 9300:9300 --name es7.7.1 {镜像id}
    
    
# 实体环境搭建

    1.当机器内存小于64G时，遵循通用的原则，50%给ES，50%留给lucene
    2. 当机器内存大于64G时，遵循以下原则： 
          a. 如果主要的使用场景是全文检索, 那么建议给ES Heap分配 4~32G的内存即可；其它内存留给操作系统, 供lucene使用（segments cache), 以提供更快的查询性能。
          b. 如果主要的使用场景是聚合或排序， 并且大多数是numerics, dates, geo_points 以及not_analyzed的字符类型， 建议分配给ES Heap分配 4~32G的内存即可，其它内存留给操作系统，供lucene使用(doc values cache)，提供快速的基于文档的聚类、排序性能。 
          c. 如果使用场景是聚合或排序，并且都是基于analyzed 字符数据，这时需要更多的 heap size, 建议机器上运行多ES实例，每个实例保持不超过50%的ES heap设置(但不超过32G，堆内存设置32G以下时，JVM使用对象指标压缩技巧节省空间)，50%以上留给lucene。
          d. 当机器内存大于等于64G时，我们都会采用 31 G 设置
              -Xms 31g
              -Xmx 31g
    3.禁止swap，一旦允许内存与磁盘的交换，会引起致命的性能问题。 通过： 在elasticsearch.yml 中 bootstrap.memory_lock: true， 以保持JVM锁定内存，保证ES的性能
    
        threadpool.bulk.type:fixed
        threadpool.bulk.size:8 #(CPU核数)
        threadpool.flush.type:fixed
        threadpool.flush.size:8 #(CPU核数)
        
    