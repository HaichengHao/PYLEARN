# editor: 百年
# time: 2024/1/23 11:39
# 导入os模块的path方法
import os.path

# os.path.abspath()输出指定文件的绝对路径
print(os.path.abspath('138os.path模块的常用方法.py'))
# D:\PYWORK\pylearn\138os.path模块的常用方法.py

# os.path.exists()查看文件是否存在,如果存在则返回True，不存在则返回False
print(os.path.exists('calc.py'))
# True
print(os.path.exists('calc2.py'))
# False

# os.path.join()将目录与目录或者文件名拼接起来
print(os.path.join('D:\PYWORK\pylearn','demo138.txt'))
# D:\PYWORK\pylearn\demo138.txt <--只是拼接，不会产生新的文件

# os.path.splitext()分离文件名和扩展名
print(os.path.splitext('138os.path模块的常用方法.py'))
# ('138os.path模块的常用方法', '.py') <--返回的是一个文件名和扩展名组成的元组

# os.path.basename()从一个目录中提取文件名
print(os.path.basename('D:/PYWORK/pylearn/138os.path模块的常用方法.py'))
# 138os.path模块的常用方法.py

# os.path.dirname()获取文件路径，不包括文件
print(os.path.dirname('D:/PYWORK/pylearn/138os.path模块的常用方法.py'))
# D:/PYWORK/pylearn

# os.path.isdir()用于判断是否为路径，正确则返回True,否则返回False
print(os.path.isdir('D:/PYWORK/pylearns'))
# False

print(os.path.isdir('D:/PYWORK/pylearn'))
# True

