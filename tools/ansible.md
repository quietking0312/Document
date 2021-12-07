## ansible 使用文档


> 安装
    
    // 该工具不支持windows系统
    pip install ansible


> 配置文件

    通过pip 命令安装的 ansible 需要手动创建 /etc/ansible/ansible.cfg 配置文件

    vi /etc/ansible/ansible.cfg
    [defaults]
    forks          = 8           #执行时并发数
    host_key_checking = False    #不检测host key 可以解决报错 Using a SSH password instead of a key is not possible because Host Key checking is enabled and sshpass does not support this

> 命令

    -v, --verbose：               输出更详细的执行过程信息，**-vvv** 可得到所有执行过程信息。
    -i PATH, --inventory=PATH：   指定inventory信息，默认/etc/ansible/hosts。
    -f NUM, --forks=NUM：         并发线程数，默认5个线程。
    --private-key=PRIVATE_KEY_FILE：  指定密钥文件。
    -m NAME, --module-name=NAME：     指定执行使用的模块。
    -M DIRECTORY, --module-path=DIRECTORY：  指定模块存放路径，默认/usr/share/ansible，也可以通过ANSIBLE_LIBRARY设定默认路径。
    -a 'ARGUMENTS', --args='ARGUMENTS'：     模块参数。
    -k, --ask-pass SSH：           认证密码。
    -K, --ask-sudo-pass sudo：     用户的密码（—sudo时使用）。
    -o, --one-line：               标准输出至一行。
    -s, --sudo：                   相当于Linux系统下的sudo命令。
    -t DIRECTORY, --tree=DIRECTORY：  输出信息至DIRECTORY目录下，结果文件以远程主机名命名。
    -T SECONDS, --timeout=SECONDS：   指定连接远程主机的最大超时，单位是：秒。
    -B NUM, --background=NUM：     后台执行命令，超NUM秒后kill正在执行的任务。
    -P NUM, --poll=NUM：           定期返回后台任务进度。
    -u USERNAME, --user=USERNAME： 指定远程主机以USERNAME运行命令。
    -U SUDO_USERNAME, --sudo-user=SUDO_USERNAM：  使用sudo，相当于Linux下的sudo命令。
    -c CONNECTION, --connection=CONNECTION：      指定连接方式，可用选项paramiko (SSH), ssh, local。Local方式常用于crontab 和 kickstarts。
    -l SUBSET, --limit=SUBSET：    指定运行主机。
    -l ~REGEX, --limit=~REGEX：    指定运行主机（正则）。
    --list-hosts：                 列出符合条件的主机列表，不执行任何其他命令


> hosts
    
    [temp]
    temp1 ansible_ssh_host=127.0.0.1 ansible_ssh_user="root" ansible_ssh_pass="123456" ansible_become_pass="123456"
    
    
    ###
    ansible_ssh_sost  目标主机
    ansible_ssh_port                    # 目标主机端口，默认22
    ansible_ssh_user                    # 目标主机用户
    ansible_ssh_pass                    # 目标主机ssh密码
    ansible_sudo_pass                 # sudo密码
    ansible_sudo_exe                    
    ansible_connection               # 与主机的连接类型，比如：local,ssh或者paramiko
    ansible_ssh_private_key_file  # 私钥地址
    ansible_shell_type                 # 目标系统的shell类型
    ansible_python_interpreter   # python版本
    
> yml

```yaml
    ---
    - hosts: temp1  # 指定hosts 文件的主机， 多个 可以使用冒号分割
      remote_user: ubuntu # 指定在远程主机上执行命令的用户
      vars:
          src_path: ../../temp/          # 注意 src为本地时 相对路径的起始路径yaml文件所在位置， 路径最后加 “/” 将拷贝目录内的所有内容, 不加“/” 将拷贝目录本身
          dst_path: /home/quiet/temp
      tasks:
        - name: copy
          become: true
          tags:
            - copy
          copy:
          remote_src: false           # false src是本机目录， true src是远程服务器的目录 
          src: "{{ src_path }}"
          dest: "{{ dst_path }}"
          owner: ubuntu
          group: ubuntu
          backup: yes
          mode: 0755
        - name: stop
          tags:
            - stop
              shell: /bin/bash "{{ dst_path }}"/stop.sh

```
    ansible-playbook -i hosts xx.yaml --tags "copy"

> tags 标签
> 
1.--tags 只会执行带有指定tags 的任务

2.拥有相同的tags 都会被执行

3.名字为 always的 tags 不论是否被指定， 都会强制执行




[返回目录](../README.md)