"""
    python locust 压测脚本
"""
import hashlib
import random
import time

from locust import task, TaskSet
from locust.contrib.fasthttp import FastHttpUser


class TaskUser(TaskSet):
    @task
    def index(self):
        appid = 162625357802
        t = int(time.time())
        sign = f"{appid}{t}2E82102FC6491410"
        json_data = {
            "time": t,
            "sign": hashlib.md5(sign.encode("utf-8")).hexdigest(),
            "app_id": appid,
            "data": {
                "data_form": "server",
                "data_app": {
                    "app_code": "local_android",
                    "platform": "Android",
                    "app_version_name": "本地",
                    "app_version_code": "1.1.6.99.9",
                    "server": "1",
                    "region": "1",
                    "data_time": int(time.time()),
                    "channel": "local"
                },
                "data_user": {
                    "user_id": ''.join([random.choice("abcdefghilkmnopqrstuvwxyz") for _ in range(6)]),
                    "account_id": ''.join([random.choice("abcdefghilkmnopqrstuvwxyz") for _ in range(6)]),
                    "birthday": 0,
                    "sex": 2
                },
                "data_role": {
                    "occupation": 0,
                    "race": 0,
                    "fighting": "710",
                    "props": [
                        {"item_id": "11", "item_type": 1, "count": 0}, {"item_id": "41", "item_type": 1, "count": 4},
                        {"item_id": "61", "item_type": 1, "count": 31}, {"item_id": "62", "item_type": 1, "count": 38},
                        {"item_id": "63", "item_type": 1, "count": 39}, {"item_id": "64", "item_type": 1, "count": 33},
                        {"item_id": "121", "item_type": 1, "count": 5}, {"item_id": "122", "item_type": 1, "count": 1},
                        {"item_id": "150", "item_type": 1, "count": 4}, {"item_id": "2", "item_type": 1, "count": 0},
                        {"item_id": "3", "item_type": 1, "count": 59026},
                        {"item_id": "4", "item_type": 1, "count": 49866},
                        {"item_id": "1", "item_type": 1, "count": 11106161},
                        {"item_id": "1", "item_type": 95, "count": 1}, {"item_id": "201", "item_type": 95, "count": 1},
                        {"item_id": "9001", "item_type": 95, "count": 1}, {"item_id": "2", "item_type": 95, "count": 1},
                        {"item_id": "202", "item_type": 95, "count": 1}, {"item_id": "3", "item_type": 95, "count": 1},
                        {"item_id": "4", "item_type": 95, "count": 1}, {"item_id": "5", "item_type": 95, "count": 1},
                        {"item_id": "6", "item_type": 95, "count": 1}, {"item_id": "7", "item_type": 95, "count": 1},
                        {"item_id": "8", "item_type": 95, "count": 1}, {"item_id": "9", "item_type": 95, "count": 1},
                        {"item_id": "203", "item_type": 95, "count": 1},
                        {"item_id": "204", "item_type": 95, "count": 1},
                        {"item_id": "205", "item_type": 95, "count": 1},
                        {"item_id": "206", "item_type": 95, "count": 1},
                        {"item_id": "207", "item_type": 95, "count": 1},
                        {"item_id": "208", "item_type": 95, "count": 1},
                        {"item_id": "209", "item_type": 95, "count": 1}, {"item_id": "1", "item_type": 94, "count": 1},
                        {"item_id": "4", "item_type": 1004, "count": 0},
                        {"item_id": "6", "item_type": 1004, "count": 0},
                        {"item_id": "7", "item_type": 1004, "count": 0},
                        {"item_id": "8", "item_type": 1004, "count": 0},
                        {"item_id": "9", "item_type": 1004, "count": 0},
                        {"item_id": "10", "item_type": 1004, "count": 0},
                        {"item_id": "2", "item_type": 1004, "count": 0},
                        {"item_id": "17", "item_type": 1004, "count": 0}
                    ],
                    "map": "",
                    "custom": {"smap": 35, "bmap": 10},
                    "role_id": ''.join([random.choice("1234567890") for _ in range(6)]),
                    "level": 35,
                    "vip_level": 5,
                    "role_name": "贺兰敏思",
                    "sex": 2
                },
                "data_event": {
                    "sys_status": "TRUE",
                    "event": "login"
                }
            }
        }
        head = {
            "Content-Type": "application/json; charset=utf-8",
            "Connection": "keep-alive"
        }
        self.client.post("/api/v1/game/data", name="setData", json=json_data, headers=head, stream=False)


class WebUser(FastHttpUser):
    tasks = [TaskUser]
    network_timeout = 0.5
