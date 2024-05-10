# 编写一个Python程序，该程序能够读取指定文件夹中的所有文件，并将其内容打印出来。
import os


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
    f.close()

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
                    port = int(line_N.replace("\n", "")[8:-4].replace(" ", ""))
                    if port in ports:
                        # print(port)
                        # print(txt_80_8443)
                        write_to_file(port, txt_80_8443.replace(f":{port}", ""))
                    # with open("log.text", "a+") as file: file.write(line.replace("\n", "").__add__(":") +
                    # line_N.replace("\n", "")[8:-4].replace(" ", "")+ "\n") print(line.replace("\n", "").__add__(":") +
                    # line_N.replace("\n", "")[8:-4].replace(" ", ""))
    file.close()
    f.close()


def system(cmd):
    os.system(cmd)


def main():
    print("CF 一键检测IP ")
    print(f"当前目录：")
    system('pwd')

    # ports = [
    #     80, 443, 2053, 2083, 2087, 8083, 2052, 2082, 2086, 2095, 2051, 2081, 2085, 2096, 8880, 8881, 8443
    # ]
    # _80_8443(ports)


if __name__ == '__main__':
    main()
