pkill -9 locust
nohup /root/.local/bin/locust -f myLocust.py --master >master.log 2>&1 & 
nohup /root/.local/bin/locust -f myLocust.py --worker >slave1.log 2>&1 &
nohup /root/.local/bin/locust -f myLocust.py --worker >slave2.log 2>&1 &
nohup /root/.local/bin/locust -f myLocust.py --worker >slave3.log 2>&1 &
nohup /root/.local/bin/locust -f myLocust.py --worker >slave4.log 2>&1 &
