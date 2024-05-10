# 编写一个Python程序，该程序能够读取指定文件夹中的所有文件，并将其内容打印出来。
import os
import time


def write_to_file(port, txt):
    file_name = f"{port}.log"
    with open(file_name, "a+") as file:
        file.write(txt + "\n")


def _80_8443(ports):
    folder_path = os.getcwd()  # 替换为你的文件夹路径
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            if filename.endswith(".txt"):  # 只处理以.txt结尾的文件
                with open("history.text", 'a+') as f:
                    f.write(filename + "\n")
                # 或者使用print()函数打印文件名和内容
                # print(f"文件名: {filename}")

    with open("history.text", "r") as f:
        lines = f.readlines()
        # print(lines)
        for line_N in lines:
            # print(line_N)
            with open(line_N.replace("\n", ""), "r") as file:
                lines = file.readlines()
                # print(lines)
                for line in lines:
                    txt_80_8443 = line.replace("\n", "").__add__(":") + line_N.replace("\n", "")[8:-4].replace(" ", "")
                    port = int(line_N.replace("\n", "")[8:-4].replace("", ""))
                    if port in ports:
                        # print(port)
                        # print(txt_80_8443)
                        write_to_file(port, txt_80_8443.replace(f":{port}", ""))
                    # with open("log.text", "a+") as file: file.write(line.replace("\n", "").__add__(":") +
                    # line_N.replace("\n", "")[8:-4].replace(" ", "")+ "\n") print(line.replace("\n", "").__add__(":") +
                    # line_N.replace("\n", "")[8:-4].replace(" ", ""))


def system(cmd):
    os.system(cmd)


def Download_CloudflareST_darwin_arm64():
    # 正在检测系统版本
    # operating_system = system_name()
    # print(operating_system)
    print("正在下载CloudflareST...")
    os.system(
        "wget https://github.com/XIU2/CloudflareSpeedTest/releases/download/v2.2.5/CloudflareST_darwin_arm64.zip")
    time.sleep(1)
    print("正在解压CloudflareST...")
    os.system("mkdir CloudflareST_darwin_arm64")
    os.system(
        "tar -zxvf CloudflareST_darwin_arm64.zip")
    os.system("chmod +x CloudflareST")
    os.system("mv CloudflareST CloudflareST_darwin_arm64/CloudflareST")
    os.system("mv ip.txt CloudflareST_darwin_arm64/ip.txt")
    os.system("mv ipv6.txt CloudflareST_darwin_arm64/ipv6.txt")
    os.system("mv cfst_hosts.sh CloudflareST_darwin_arm64/cfst_hosts.sh")
    os.system("rm 使用+错误+反馈说明.txt")

    # system('unzip CloudflareST_darwin_arm64.zip')cd
    time.sleep(1)
    print("正在删除CloudflareST_darwin_arm64.zip...")
    os.system(
        "rm CloudflareST_darwin_arm64.zip")
    # system('rm CloudflareST_darwin_arm64.zip')


def system_name():
    # Determine the operating system
    print("正在检测系统版本... Windows Linux Mac")
    operating_system = os.name
    print(operating_system)
    return operating_system


def main():
    # time.sleep(5)
    # print("正在检测IP...")
    # time.sleep(1)
    time.sleep(3)
    print("正在获取当前目录...")
    system('pwd')
    time.sleep(2)
    print("正在获取当前目录下的文件...")
    folder_path = os.getcwd()  # 替换为你的文件夹路径
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            if filename.endswith(".log"):
                with open("debug.text", "a+") as filename_log:
                    print(f"正在检测文件：{filename}")
                    time.sleep(3)
                    filename_log.write(str(os.popen(
                        f"./CloudflareST_darwin_arm64/CloudflareST -n 200 -t 6 -dn 10 -tp {filename[:-4]} -url https://cf.xiu2.xyz/url -tl 200 -p 5 -f {filename}").readlines()) + "\n")
                    time.sleep(3)
                    # filename_log.write(os.popen(f"./CloudflareST -n 200 -t 6 -dn 10 -tp {filename[:-4]} -url https://cf.xiu2.xyz/url -tl 200 -p 5 -f {filename}").readlines())
                # print(filename[:-4])
                # os.system(f"./CloudflareST_darwin_arm64/CloudflareST -n 200 -t 6 -dn 10 -tp {filename[:-4]} -url https://cf.xiu2.xyz/url -tl 200 -p 5 -f {filename}")

    print("检测完成")
    time.sleep(1)
    print("")


def success():
    os.system("open debug.text")


if __name__ == '__main__':
    print("CF 一键检测IP ")
    print("作者：落幕")
    print("版本：1.0")
    print("时间：2024-05-10")
    print("")
    os.system("rm *.log")
    os.system("rm *.text")
    ports = [80, 443, 2053, 2083, 2087, 8083, 2052, 2082, 2086, 2095, 2051, 2081, 2085, 2096, 8880, 8881, 8443]
    _80_8443(ports)
    system_name()
    Download_CloudflareST_darwin_arm64()
    main()
    success()
