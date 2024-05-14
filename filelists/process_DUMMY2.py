import os
import fileinput

# 遍历当前目录及其所有子目录中的所有文件
for root, dirs, files in os.walk("."):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        # 使用fileinput模块来逐行读取和替换文件内容
        with fileinput.FileInput(file_path, inplace=True, backup=".bak") as file:
            for line in file:
                # 将每一行中的"/home/ydoit/AIGC/Raw-EN/wav48_silence_trimmed"替换为"/home/ydoit/AIGC/Raw-EN/wav48_silence_trimmed"
                print(
                    line.replace(
                        "/home/ydoit/AIGC/Raw-EN/wav48_silence_trimmed", "/home/ydoit/AIGC/Raw-EN/wav48_silence_trimmed"
                    ),
                    end="",
                )
