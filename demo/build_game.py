import hashlib
import json
import os
import re
import shlex
import shutil
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr, formatdate
import subprocess
import sys
import configparser


class _Const(object):
    """
    全局通用常量类
    """

    # 配置文件用
    # section
    PROJECT = "PROJECT"
    COCOS = "COCOS"
    COCOS_CFG = "COCOS_CFG"
    COS = "COS"
    # options
    PROJECT_PATH = "PROJECT_PATH"
    BACK_PATH = "BACK_PATH"
    START_SCENE_PATH = "START_SCENE_PATH"
    COCOS_CREATOR_PATH = "COCOS_CREATOR_PATH"

    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, key, value):
        if self.__dict__.get(key) is not None:
            raise self.ConstError(f'{key} 常量已存在')
        elif not key.isupper():
            raise self.ConstCaseError(f"{key} 常量需要全部大写")
        else:
            self.__dict__[key] = value


const = _Const()


class Command(object):
    """
    通用
    """

    @staticmethod
    def exec_command(cmd: str, shell: bool = False):
        """
        启用一个子进程执行命令
        :param cmd:
        :param shell:
        :return:
        """
        end_line = ""
        try:
            print(cmd)
            sub_obj = subprocess.Popen(shlex.split(cmd), shell=shell, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                       universal_newlines=True)
            while sub_obj.poll() is None:
                line = sub_obj.stdout.readline()
                line = line.strip()
                if line:
                    end_line = line
                    print(line)
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
    def load_json_file(file):
        """
        读取json
        :param file:
        :return:
        """
        with open(file=file, mode='r') as f_obj:
            data = json.load(fp=f_obj)
        return data

    @staticmethod
    def write_json_file(file: str, data: dict, indent: int = 4, mode: str = 'w'):
        """
        写json
        :param file:
        :param data:
        :param indent:
        :param mode:
        :return:
        """
        with open(file=file, mode=mode) as f_obj:
            json.dump(data, f_obj, indent=indent)

    @staticmethod
    def copy_dir_file(src: str, dst: str, exclude_file_name=None):
        """
        拷贝文件 或目录内的文件 到指定目录内
        :param exclude_file_name: 排除文件
        :param src: 目录或文件
        :param dst: 目录
        :return:
        """

        if exclude_file_name is None:
            exclude_file_name = [".DS_Store", ".git"]
        if not os.path.isdir(dst):
            os.makedirs(dst)
        if os.path.isfile(src):
            print(f"copy: {src} -> {os.path.join(dst, os.path.basename(src))}")
            shutil.copyfile(src, os.path.join(dst, os.path.basename(src)))
        if os.path.isdir(src):
            print(f"copy: {src} -> {dst}")
            for root, dirs, files in os.walk(src):
                for file_name in files:
                    if file_name not in exclude_file_name:
                        file_path = os.path.join(root, file_name)
                        dst_file_path = file_path.replace(src, dst)
                        Command.copy_file_file(src_file=file_path, dst_file=dst_file_path, is_print=False)

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

    @staticmethod
    def get_dir_file_path(dir_path: str):
        """
        获取指定目录下的所有文件的路径
        :param dir_path:
        :return:
        """
        file_list = []
        if os.path.isdir(dir_path):
            for root, dirs, files in os.walk(dir_path):
                for file_name in files:
                    if file_name not in [".DS_Store", ".git"]:
                        file_path = os.path.join(root, file_name)
                        file_list.append(file_path.replace(dir_path, "").lstrip("/").lstrip("\\"))
        return file_list

    @staticmethod
    def send_email(email_host: str, email_port: int, email_user: str, email_pass: str, from_addr: str, to_addr: list,
                   message: str, title: str = "jenkins自动化编译报告", is_ssl: bool = True):
        """
        发送邮件
        :param title:
        :param is_ssl:
        :param email_host: smtp 服务ip
        :param email_port: smtp 服务端口
        :param email_user: 邮箱账号
        :param email_pass: 邮箱密码
        :param from_addr: 发件人地址
        :param to_addr: 接收人地址，数组
        :param message: 发件信息
        :return:
        """
        if is_ssl:
            smtp_obj = smtplib.SMTP_SSL(host=email_host, port=email_port)
        else:
            smtp_obj = smtplib.SMTP()
            smtp_obj.connect(email_host, email_port)
        try:
            smtp_obj.login(email_user, email_pass)

            msg = MIMEText(message, 'plain', 'utf-8')
            msg['From'] = formataddr(('jenkins', from_addr))
            msg['To'] = ",".join(to_addr)
            msg['Subject'] = title
            msg['Date'] = formatdate()
            smtp_obj.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=msg.as_string())
            print("邮件发送成功")
        except Exception as err:
            print(f"邮件发送失败：{err}")
        finally:
            smtp_obj.close()

    @staticmethod
    def check_str_chinese(check_str):
        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

    @staticmethod
    def check_file_path(root_path: str):
        check = True
        path_comp = re.compile(r"[^\w./\\:-]")
        name_comp = re.compile(r"[^\w.-]")
        for root, dirs, files in os.walk(root_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if len(name_comp.findall(file_name)) > 0:
                    check = False
                    print(file_path.encode("utf-8"))
                if len(path_comp.findall(root)) > 0:
                    check = False
                    print(file_path.encode("utf-8"))
        return check


class MyConfigParser(configparser.ConfigParser):
    """
    configParser 默认不识别大小写
    继承重写后的 MyConfigParser 可以识别大小写
    """

    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr: str) -> str:
        return optionstr


class Config(object):
    """
    配置类
    """

    def __init__(self, project_path: str = "", back_path: str = "",
                 cocos_creator_path: str = "",
                 start_scene_path: str = ""):
        self.project_path = project_path
        self.back_path = back_path
        self.cocos_creator_path = cocos_creator_path
        self.start_scene_path = start_scene_path
        self.creator_build_cfg = []
        self.cos_cfg = []

    def set_start_scene_uuid(self, start_scene_path: str):
        """
        根据 项目 scene 路径 设置 项目打包 起始页 scene uuid
        :param start_scene_path:
        :return:
        """
        try:
            meta_path = os.path.join(self.project_path, start_scene_path)
            data = Command.load_json_file(meta_path)
        except Exception as err:
            print(err)
            sys.exit(1)
        else:
            return data["uuid"]

    def read_cfg(self, cfg_path: str):
        """
        读取配置文件内指定字段到对象内
        :param cfg_path:
        :return:
        """
        cf = MyConfigParser()
        cf.read(cfg_path)

        for section in cf.sections():

            if section == const.PROJECT:
                for option in cf.options(section):
                    if option == const.PROJECT_PATH:
                        self.project_path = cf.get(section, option)
                    if option == const.BACK_PATH:
                        self.back_path = cf.get(section, option)
                    if option == const.START_SCENE_PATH:
                        self.start_scene_path = cf.get(section, option)

            # cocos
            if section == const.COCOS:
                for option in cf.options(section):
                    if option == const.COCOS_CREATOR_PATH:
                        self.cocos_creator_path = cf.get(section, option)

            # cocos_cfg
            if section == const.COCOS_CFG:
                self.creator_build_cfg = cf.items(const.COCOS_CFG)
                if len(self.creator_build_cfg) > 0 and self.start_scene_path != "":
                    self.creator_build_cfg.append(("startScene", self.set_start_scene_uuid(self.start_scene_path)))

            # cos
            if section == const.COS:
                self.cos_cfg = cf.items(const.COS)

    def get_cocos_cmd(self, **kwargs):
        """
        构造cocos build 执行命令
        :return:
        """
        build_cfg = ""
        for item in self.creator_build_cfg:
            build_cfg += f"{item[0]}={item[1]};"
        for key, value in kwargs.items():
            build_cfg += f"{key}={value};"

        if build_cfg != "":
            build_cfg = f"\"{build_cfg}\""

        return f"{self.cocos_creator_path} --path {self.project_path} --build {build_cfg}"

    def get_cos_cmd(self, load_path: str, cos_path: str):
        """
        构造cos 上传命令
        :return:
        """
        cos_cfg = ""
        for item in self.cos_cfg:
            cos_cfg += f"-{item[0]} {item[1]} "
        return f"coscmd {cos_cfg} upload -rs {load_path} {cos_path}"
