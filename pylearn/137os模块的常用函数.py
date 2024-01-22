# editor: 百年
# time: 2024/1/22 20:08
'''
目录操作
os模块是Python内置的与操作系统功能和文件系统相关的模块，该模块中的语句的执行结果通常与操作系统有关，
在不同的操作系统上运行，得到的结果可能不太一样
os模块与os.path模块用于对目录或文件进行操作
'''
# 导入os模块
import os

# 语法os.system('命令')

# 打开notepad
# os.system('notepad.exe')

# 打开计算机
# os.system('calc.exe')

# 可以直接调用可执行文件os.startfile(path,operation)
# 例如利用os.startfile打开qq
os.startfile('D:/qq/Bin/QQScLauncher.exe')