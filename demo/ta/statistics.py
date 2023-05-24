import os
import re
import wcwidth
data_list = []


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if "VerificationToken" not in line:
                continue
            match = re.search(r"VerificationToken\s+mid\s+:(\d+)", line)
            if match:
                data_list.append(match.group(1))


class UserTable:
    # k 时间
    # v { "list": [当日活跃用户mid], "new": [单日新增用户] "r1"：[一日后还活跃的用户], "r2": [2日后还活跃的用户] }

    def __init__(self):
        self.data = {}
        self.keys = []
        # 初始化数据
        self._init_data()

    def _init_data(self):
        root_path = "./"
        for file_name in os.listdir(root_path):
            if "mid" in file_name and ".txt" in file_name:
                file_path = os.path.join(root_path, file_name)
                t = int(file_name.replace("mid", "").split("-")[0])
                if t not in self.data.keys():
                    self.data[t] = {
                        "time": t,
                        "list": [],
                        "new": [],
                        "r": {},  # 新增用户在 第 n 天后是否有登录
                        "a": {}  # 新增用户 在第 n-2 ~ n 天是否有登录
                    }
                with open(file_path, "r") as f:
                    for i in f:
                        self.data[t]["list"].append(i)
        # 去重
        for k, v in self.data.items():
            ls = v["list"]
            self.data[k]["list"] = list(set([i for i in ls]))
        # 排序
        self.keys = [i for i in self.data.keys()]
        self.keys.sort()

    def statistics_add(self):
        for k, v in self.data.items():
            for mid in v["list"]:
                is_new = True
                for value in self.data.values():
                    if value["time"] < k and mid in value["list"]:
                        is_new = False
                        break
                if is_new:
                    v["new"].append(mid)

    def statistics_survive(self):
        for k in self.keys:
            n = 0
            r = {}
            while n < len(self.keys):
                n += 1
                r_key = "r" + str(n)
                new_k_list = [k + n]
                r[r_key] = []
                li = []
                for new_k in new_k_list:
                    if new_k in self.keys:
                        for mid in self.data[k]["new"]:
                            if mid in self.data[new_k]["list"]:
                                li.append(mid)
                r[r_key] = list(set(i for i in li))
            self.data[k]["r"] = r

    def statistics_survive3(self, x=3):
        for k in self.keys:
            a = {}
            for a_key in self.keys:
                if a_key < k:
                    continue
                li = []
                new_k_list = [a_key - i for i in range(x)]
                for new_k in new_k_list:
                    if new_k in self.keys and new_k >= k:
                        for mid in self.data[k]["new"]:
                            if mid in self.data[new_k]["list"]:
                                li.append(mid)
                a[a_key] = list(set(i for i in li))
            self.data[k]["a"] = a

    @staticmethod
    def format(s: str, le: int):
        while wcwidth.wcswidth(s) < le:
            s = s + " "*(le - wcwidth.wcswidth(s))
        return s

    # 以单日为一个标准进行打印
    def print(self):
        self.statistics_add()
        self.statistics_survive()
        max_len = 16
        title = UserTable.format("", max_len)
        i = 0
        while i < len(self.keys):
            if i == 0:
                title += UserTable.format("|当日活跃", max_len) + " " * 2
                title += UserTable.format("|当日新增", max_len) + " " * 2
            else:
                title += UserTable.format("|" + str(i) + "日存", max_len)
            i += 1
        print(title)
        for rk in self.keys:
            n_n = 0
            row = UserTable.format(str(rk), max_len) + UserTable.format("|" + str(len(self.data[rk]["list"])), max_len)
            row += UserTable.format("|" + str(len(self.data[rk]["new"])), max_len)
            while n_n < len(self.data[rk]["r"].keys()):
                n_n += 1
                r_n = "r" + str(n_n)
                r_n_num = len(self.data[rk]["r"][r_n])
                if r_n_num > 0:
                    row += UserTable.format("|" + str(r_n_num) + "(" + "{:.2%}".format(r_n_num / len(self.data[rk]["new"])) + ")", max_len)
                else:
                    row + UserTable.format("|", max_len)
            print(row)

    # 以3日为一个标准进行打印
    def print2(self):
        self.statistics_add()
        self.statistics_survive3(3)
        max_len = 16
        title = ["", "当日活跃", "当日新增"]
        i = 0
        while i < len(self.keys):
            title.append(20230518 + i)
            i += 1
        print(" ".join([UserTable.format("|" + str(i), max_len) for i in title]))
        for rk in self.keys:
            row = [rk, len(self.data[rk]["list"]), len(self.data[rk]["new"])]
            while len(row) < len(title):
                row.append("")
            for r_n in self.data[rk]["a"]:
                r_n_num = len(self.data[rk]["a"][r_n])
                index = title.index(r_n)
                if r_n_num > 0:
                    row[index] = str(r_n_num) + "(" + "{:.2%}".format(r_n_num / len(self.data[rk]["new"])) + ")"
            print(" ".join(UserTable.format("|" + str(i), max_len) for i in row))


def statistics():
    user_table = UserTable()

    # user_table.print()
    user_table.print2()


def main():
    for root, dirs, files in os.walk("/mnt/datadisk0/logs/20230518"):
        for file_name in files:
            if "logic" in file_name:
                file_path = os.path.join(root, file_name)
                read_file(file_path)

    if len(data_list) > 0:
        l = list(set(data_list))
        with open("mid20230518.txt", "w") as f:
            f.write("\n".join(l))


if __name__ == '__main__':
    #main()
    statistics()
