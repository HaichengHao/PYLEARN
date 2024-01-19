# editor 百年
# date: 2024/1/19 12:18
'''
Python 中的包
-包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下
作用
-代码规范
-避免模块冲突
包与目录的区别
-含有__init__.py文件的目录称为包
-目录里通常不含__init__.py文件

包的导入
import 包名.模块名
from 包名 import 模块名
'''
# 为了书写方便和可读性 还可用as 别名来替代冗长的名称
# 例如 import mypkg.modeA as ma
'''
python程序的层次结构
一个python程序中有n多个包，
每个包里又有n多个模块
每个模块中又有n多个类/语句/函数

如何新建python包
在目录新建Python package
'''

'''
注意，使用import 方式导入时只能跟包名或模块名
而使用 from import 方式导入时还可以导入变量（观察129demo.py即可）'''