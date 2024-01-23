# editor: 百年
# time: 2024/1/23 19:17
# 要求输出所有.py文件
import os
# 获取当前文件
path=os.getcwd()
# 创建一个列表，列出当前目录下的所有文件
lst=os.listdir(path)
# 对列表内的元素进行遍历
for item in lst:
    # 分离文件名和扩展名
    # 如果扩展名是.py结尾则输出
    # 写法1
    # if os.path.splitext(item)[1]=='.py':
    #     print(item)
    if item.endswith('.py'):
        print(item)



