#!/bin/bash

ulimit -c unlimited
ulimit -n 65535

chmod +x server

stop() {
  pkill server
}

start() {
  nohup server >server_std.log 2>&1 &
}

c=$1

case ${c} in
start)
  start
  ;;
stop)
  stop
  ;;
restart)
  stop
  start
  ;;
esac