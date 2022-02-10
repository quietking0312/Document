import time

import pymysql

DB_CFG = {
    "host": "172.17",
    "port": 3306,
    "user": "root",
    "password": "",
    "database": "BugReport"
}

conn = pymysql.connect(host=DB_CFG["host"], port=DB_CFG["port"], user=DB_CFG["user"], password=DB_CFG["password"],
                       database=DB_CFG["database"], charset="utf8")

cursor = conn.cursor()

sql = "DELETE FROM `clientLog` WHERE `id` < 51100000 LIMIT 30000"
for i in range(100):
    time.sleep(1)
    cursor.execute(sql)
    conn.commit()
    cont = cursor.rowcount
    print(cont, "条记录被删除")
conn.close()

