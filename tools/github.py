import os
import re
import shutil


hosts_file = "C:\Windows\System32\drivers\etc\hosts"

result = os.popen("nslookup -d github.com")

result_list = [args.strip() for args in result.readlines()]

index = result_list.index("名称:    github.com")
ip_str = result_list[index + 1]
ip_search = re.search(r"([0-9]{1,3}\.){3}[0-9]{1,3}$", ip_str)
ip = ip_search.group()


with open(hosts_file, "r", encoding="utf-8") as f:
    hosts_data = f.read()

if re.search(r"([0-9]{1,3}\.){3}[0-9]{1,3} github.com", hosts_data):
    new_data = re.sub(r"([0-9]{1,3}\.){3}[0-9]{1,3} github.com", f"{ip} github.com", hosts_data)
else:
    new_data = hosts_data + "\n" + f"{ip} github.com"

i = 1
while True:
    try:
        shutil.copy(hosts_file, hosts_file + f"_temp{i}")
    except Exception as err:
        i += 1
        if i == 100:
            print(err)
            exit(1)
    else:
        break

with open(hosts_file, "w", encoding="utf-8") as n_f:
    n_f.write(new_data)
