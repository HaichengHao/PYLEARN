# editor: 百年
# time: 2024/1/23 21:26
# 利用walk遍历指定文件的所有文件，包含子文件
import os
# 获取当前文件路径
path=os.getcwd()
# 输出当前路径，包括子路径的所有内容
list_files=os.walk(path)
print(list_files)
# <generator object _walk at 0x0000021954BE03C0>
# 返回的结果是一个迭代器对象

# 遍历迭代器对象
for dirpath,dirname,filename in list_files:
    print(dirpath)
    print(dirname)
    print(filename)