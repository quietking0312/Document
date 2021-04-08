#!/bin/bash

#redis
src_ip=172.17.100.17
#redis
src_port=6379
#redis
src_db=0
#redis
src_pw=hAEd7xA1Jp9i%7Ii

#redis
dest_ip=172.17.100.11
#redis
dest_port=6379
#redis
dest_db=0
#redis
dest_pw=123

redis-cli -h $src_ip -p $src_port -a $src_pw -n $src_db keys "EPZJFHS12s*" | while read key
do
  redis-cli -h $src_ip -p $src_port -a $src_pw -n $src_db --raw dump $key | head -c-1
	echo "migrate key $key"
done