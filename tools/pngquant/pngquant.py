import json
import os
import re
import sys
import subprocess
import shlex
import hashlib
import imghdr
import shutil

SCRIPT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

# 源图目录
SOURCE_PATH = "F:/svn_data/brainhole/assets/Tools/edit/GitBrainstormEdit_Data/StreamingAssets/BrainStorm"
# 生成目录
OUT_PATH = "F:/svn_data/brainhole/assets/BrainStorm_tmp"
# 配置文件，压缩过的图片会被记录
CONFIG_PATH = "metadata.json"

ENV = {"PATH": os.environ.get("PATH")}


class Command(object):
    @staticmethod
    def exec_command(cmd, shell: bool = False, cwd: str = SCRIPT_DIR_PATH):
        """
        启用一个子进程执行命令
        :param cwd:
        :param cmd:
        :param shell:
        :return:
        """
        end_line = ""
        try:
            cmd_list = cmd
            if shell and type(cmd_list) == str:
                cmd_list = shlex.split(cmd_list)
            # print(cmd_list, flush=True)
            sub_obj = subprocess.Popen(cmd_list, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                       universal_newlines=True, env=ENV, cwd=cwd)
            while sub_obj.poll() is None:
                line = sub_obj.stdout.readline()
                line = line.strip()
                if line:
                    end_line += line + "\n"
        except Exception as err:
            print(err)
            sys.exit(1)
        return end_line

    @staticmethod
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

    @staticmethod
    def copy_file_file(src_file: str, dst_file: str, is_print: bool = False):
        """
        拷贝文件 到指定位置
        :param src_file: 文件路径
        :param dst_file: 文件路径
        :param is_print: 是否打印拷贝信息
        :return:
        """
        if not os.path.isdir(os.path.dirname(dst_file)):
            os.makedirs(os.path.dirname(dst_file))
        if os.path.isfile(dst_file):
            os.remove(dst_file)
        if is_print:
            print(f"copy: {src_file} -> {dst_file}")
        shutil.copyfile(src_file, dst_file)


def load_config():
    with open(CONFIG_PATH, "r") as f:
        data = json.load(f)
    return data


def write_config(data: dict):
    with open(CONFIG_PATH, "w") as f:
        json.dump(data, f, indent=4)


def pngquant(source_file_path: str, out_file_path: str):
    cmd_str = ["./pngquant.exe", "-o", f"{out_file_path}", "--speed", "4", f'{source_file_path}']
    result = Command.exec_command(cmd_str, False)
    if result != "":
        print(result, flush=True)
    return


def svn_up():
    cmd_add = ["svn", "add", "."]
    result = Command.exec_command(cmd_add, False, cwd=OUT_PATH)
    if result != "":
        print(result, flush=True)
    cmd_str = ["svn", "commit", "-m", "'BrainStorm update'"]
    result = Command.exec_command(cmd_str, False, cwd=OUT_PATH)
    if result != "":
        print(result, flush=True)

def main():
    pattern = re.compile(u'[\u4e00-\u9fa5]+')
    config_data = load_config()
    for root, dirs, files in os.walk(SOURCE_PATH):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            out_path = file_path.replace(SOURCE_PATH, OUT_PATH)
            if not os.path.isdir(os.path.dirname(out_path)):
                os.makedirs(os.path.dirname(out_path))
            if imghdr.what(file_path) == "png" and pattern.search(file_path) is None:
                file_key = file_path.replace(SOURCE_PATH, "").strip("/").strip("\\")
                file_info = config_data[file_key] if file_key in config_data else {"size": 0, "md5": ""}
                size = os.path.getsize(file_path)
                md5str = Command.get_file_data_md5(file_path)
                if file_info["size"] == size and file_info["md5"] == md5str:
                    continue
                else:
                    if os.path.exists(out_path):
                        os.remove(out_path)
                    # 执行压缩
                    pngquant(file_path, out_path)
                    config_data[file_key] = {"size": size, "md5": md5str}
            else:
                # 将文件拷贝到目标目录
                Command.copy_file_file(file_path, out_path)

    write_config(config_data)
    # TODO 执行文件上传操作


if __name__ == '__main__':
    main()
