
# 参考地址
# https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html

# s3上传文件命令
import hashlib
import os
import time
import asyncio

import urllib3
urllib3.disable_warnings()

bucket_name = "release-byte-city"

s3_put_cmd = "aws s3api put-object --no-verify-ssl --acl public-read --bucket {bucket_name} --key {remote_path} --body {local_path} "
mime_arg = "--content-type {mime}"
local_dir_path = "D:\Desktop\live_AT1"
ExceptionsMime = {
    "js.gz": "application/javascript",
    "wasm.gz": "application/wasm",
    "data.gz symbols.json.gz glb.gz": "text/plain",
}


class Mime(object):
    def __init__(self):
        self.data = {}
        self._get_mime_dict()

    def _get_mime_dict(self):
        with open("mime.types", "r") as f:
            for line in f:
                if "#" in line:
                    continue
                line = line.strip()
                line_list = line.split(" ", 1)
                if len(line_list) > 1:
                    self.data[line_list[1].strip().strip(";")] = line_list[0]
                    print(f"\"{line_list[1].strip().strip(';')}\":\"{line_list[0]}\",")
        return self.data

    def get_mime_by_path(self, path: str):
        for k, v in ExceptionsMime.items():
            k_list = k.split(" ")
            for item in k_list:
                if path.endswith(item):
                    return v
        for k, v in self.data.items():
            k_list = k.split(" ")
            for item in k_list:
                if path.endswith(item):
                    return v
        return "application/octet-stream"


def get_file_data_md5(file):
    """
    获取文件md5
    :param file:
    :return:
    """
    m = hashlib.md5()
    with open(file=file, mode='rb') as f_obj:
        while True:
            data = f_obj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


MIME = Mime()


def upload():
    loop = asyncio.get_event_loop()
    tasks = []
    for root, dirs, files in os.walk(local_dir_path):
        for file_name in files:
            local_file_path = os.path.join(root, file_name)
            remote_file_path = local_file_path.replace(local_dir_path, "", 1).replace("\\", "/", -1).strip().strip("/").strip("\\")
            tasks.append(upload_file(remote_file_path, local_file_path))
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


async def upload_file(remote_path: str, local_path: str):
    temp_cmd = s3_put_cmd.format(bucket_name=bucket_name, remote_path=remote_path, local_path=local_path)
    temp_cmd = " ".join([temp_cmd, mime_arg.format(mime=MIME.get_mime_by_path(path=local_path))])
    file_md5 = get_file_data_md5(local_path)
    result = os.popen(temp_cmd)
    resp = result.read()
    if file_md5 in resp:
        print(f"{local_path} 上传完成...")
    else:
        print(resp)


t = int(time.time())
print(f"开始上传 time:{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))}")
# upload()
print(f"上传结束 耗时：{int(time.time())-t}秒")