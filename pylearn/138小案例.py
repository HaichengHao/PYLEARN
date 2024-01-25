# editor: 百年
# time: 2024/1/23 19:17
# 要求输出所有.py文件
import os
# 获取当前文件
path=os.getcwd()
# 利用os.listdir()返回的结果是文件列表，并创建一个对象lst接收这个列表
lst=os.listdir(path)
# 对列表内的元素进行遍历
for item in lst:
    # 分离文件名和扩展名
    # 如果扩展名是.py结尾则输出
    # 写法1
    # 遍历每个元素，进行劈分操作，劈分后的每个元素也成为('文件名','拓展名')这样的元组，所以定位第二个元素，判断是否是'.py',如果是则输出
    # if os.path.splitext(item)[1]=='.py':
    #     print(item)
    if item.endswith('.py'):
        print(item)



