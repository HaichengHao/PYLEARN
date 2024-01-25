# editor: 百年
# time: 2024/1/22 20:54
'''
对照137os模块操作目录相关函数.md进行学习
'''
# 导入os模块
import os

# 获取当前工作目录
print(os.getcwd())
# D:\PYWORK\pylearn

# 返回指定路径下的文件信息(这里选择的指定路径是我们获取的路径)
print(os.listdir(os.getcwd()))
# ['100try_except的使用.py', '101try_except_else与try_except_else_finally结构.py', '102python中常见的异常类型.py', '103traceback模块的使用.py', '104程序的调试.py', '105编程的两大思想.md', '106类与对象.py', '107python中类的创建.py', '108对象的创建.py', '109类方法，静态方法的使用.py', '10bool类型.py', '110动态绑定属性和方法.py', '111封装.py', '112继承.py', '113方法重写.py', '114object类.py', '115多态.py', '116特殊属性.py', '117特殊方法.py', '118new与init.py', '119类的赋值与浅拷贝.py', '11字符串类型.py', '120深拷贝.py', '121其它字符.png', '121其它字符_copy.png', '121初识正则表达式.py', '121常用元字符.png', '121常用限定符.png', '122正则表达式的match方法.py', '123正则表达式的search方法.py', '124正则表达式的findall方法.py', '125正则表达式的sub方法和split方法.py', '126mod1.py', '126什么是模块.py', '127from_import.py', '127使用from_import调用自己的模块.py', '127使用自己的模块.py', '127模块的导入.py', '128以主程序形式运行.py', '129demo.py', '129python中的包.py', '12数据类型转换.py', '130python中常用的内置模块.md', '130python中常用的内置模块.py', '131第三方模块的安装与使用.py', '132编码格式的介绍.py', '133写操作.py', '133复制图片的操作.py', '133文件的读写原理.py', '133读操作.py', '134常用的文件打开模式.md', '135flush和close.py', '135文件对象的常用方法.md', '135文件对象的常用方法.py', '136copy.png', '136MycontentMGR.py', '136with语句.py', '136with语句实现复制.py', '137os模块操作目录的相关函数.py', '137os模块操作目录相关函数.md', '137os模块的常用函数.py', '13数据类型转换,float().py', '14python中的注释.py', '15输入函数input().py', '16input()练习.py', '17python中的运算符.py', '18赋值运算符.py', '19比较运算符.py', '1输出函数.py', '20布尔运算符.py', '21位运算符.py', '22运算符的优先级.py', '23顺序结构.py', '24对象的布尔值.py', '25单分支结构.py', '26双分支结构.py', '27多分支结构.py', '28嵌套if的使用.py', '29条件表达式.py', '2转义字符.py', '30pass语句.py', '31range函数的使用.py', '32while循环.py', '33while练习题，1-100之间的偶数和.py', '34for_in循环.py', '35for_in练习1-100的水仙花数.py', '36流程控制语句break.py', '37流程控制语句continue.py', '38else语句.py', '39嵌套循环.py', '3二进制与字符编码.py', '40二重循环中的break与continue.py', '41列表.py', '42列表对象的创建.py', '43获取指定列表的索引.py', '44获取列表中指定的元素.py', '45获取列表中的多个元素.py', '46列表元素的判断及遍历.py', '47列表元素的添加操作.py', '48列表元素的删除操作.py', '49列表元素的修改操作.py', '4python中的保留字.py', '50列表元素的排序.py', '51列表生成式.py', '52字典(引).py', '53字典的实现原理.py', '54字典的创建.py', '56字典元素的获取.py', '57字典元素的增删改操作.py', '58字典的视图操作.py', '59字典元素的遍历.py', '5变量.py', '60字典的特点.py', '61字典生成式.py', '62元组(引).py', '63元组的创建.py', '64元组精讲.py', '6变量的多次赋值.py', '70元组的遍历.py', '71集合(引).py', '72集合的相关操作.py', '73集合的关系.py', '74集合的数学操作.py', '75集合生成式.py', '76字符串的创建与驻留机制.py', '77字符串的查询操作.py', '78字符串的大小写转换操作.py', '79字符串的对齐操作.py', '7常见的数据类型.py', '80字符串的劈分.py', '81字符串判断的相关方法.py', '82字符串的替换与合并.py', '83字符串的比较操作.py', '84字符串的切片操作.py', '85格式化字符串.py', '86格式化字符串的引申.py', '87字符串的编码转换.py', '88函数的定义与调用.py', '89函数的参数传递.py', '8整数类型.py', '90函数参数传递的内存分析.py', '91函数的返回值.py', '92参数定义（默认值参数）.py', '93个数可变的位置形参与关键字形参.py', '94函数的参数总结.md', '94函数的参数总结.py', '95变量的作用域.py', '96递归函数.py', '96递归函数示意.png', '97斐波那契数列.py', '98bug的由来.py', '99bug常见类型1.py', '99bug常见类型2（错误点不清晰）.py', '99bug常见类型3（思路不清晰）.py', '9浮点类型.py', 'calc.py', 'demo131.py', 'demo133.txt', 'demo133_write.txt', 'demo135.txt', 'demo135_2.txt', 'demo136.txt', 'mymod127.py', 'mypkg129', '__pycache__']
# 输出的是列表形式
# 这次放回pylearn1下的文件信息,结果为列表
print(os.listdir('D:/PYWORK/pylearn1'))
# ['pylearn1'] <--输出成功

# 尝试输出不存在的路径
try:
    print(os.listdir('D:/PYWORK/PL'))
except BaseException as e:
    print(e)
    # [WinError 3] 系统找不到指定的路径。: 'D:/PYWORK/PL'
    # 可以发现，如果不存在，则会抛出异常显示指定路径不存在

# 利用os模块创建目录os.mkdir(path)
# os.mkdir('D:/PYWORK/MachineLearning')
# 创建成功，将为下一阶段的python学习埋下伏笔

# 利用os模块的os.mkdirs()可以创建多级目录
'''try:
    os.makedirs('D:/MYSQLLEARN/demodir')
# 创建mysql学习目录，方便后续的mysql学习
    print('创建成功')
except BaseException as e:
    print(e)'''
#  创建成功 观察发现d盘也创建有了

# 利用os.remove()可以删除目录
# 删除pylearn2
'''try:
    os.rmdir('D:/PYWORK/pylearn2')
    print('删除成功')
except BaseException as e:
    print(e)'''
#     [WinError 5] 拒绝访问。: 'D:/PYWORK/pylearn2' <--被拒接访问了

# 利用os.removedirs()可以删除多级目录
# 删除操作一定要谨慎,尤其是移除多级目录操作


# chdir(dirname) change directory 改当前目录为工作目录
'''os.chdir('D:/PYWORK/pylearn1')
print(os.getcwd())'''
# D:\PYWORK\pylearn1 <--工作目录改变
# 注意,涉及文件的操作一定要谨慎
# 再把工作目录设置回去
os.chdir('D:/PYWORK/pylearn')
print(os.getcwd())
# D:\PYWORK\pylearn <--设置回去了
