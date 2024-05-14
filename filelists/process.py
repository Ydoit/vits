import os
import glob

# 遍历当前目录下所有以vctk开头的文件
for filename in glob.glob("vctk*"):
    with open(filename, "r") as file:
        lines = file.readlines()

    # 按行读取文件
    new_lines = []
    for line in lines:
        # 每行被|符号分为3个部分，第一部分为一个文件路径
        filepath = line.split("|")[0]
        # 判断该路径文件是否存在
        if os.path.exists(filepath):
            # 如果存在，则保留该行
            new_lines.append(line)

    # 每个文件处理完写回原文件
    with open(filename, "w") as file:
        file.writelines(new_lines)
