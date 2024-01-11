# editor 百年
# date: 2024/1/11 20:06
'''
常见错误
1 ZeroDivisionError  除（或取模）零
2 IndexError 序列中没有此索引
3 KeyError   映射中没有这个键
4 NameError  未声明/初始化对象（没有属性）
5 SyntaxError  Python语法错误
6 ValueError  传入无效的参数
'''

# 1 数学运算错误，除数为0
# print(1/0)
# ZeroDivisionError: division by zero

# 2 IndexError索引错误，索引越界
# lst=[1,2,3,4]
# try:
#     print(lst[4])
# except IndexError as e:
#     print('出错了',e)
#     # 出错了 list index out of range

# 3 KeyError
# dic1={'张三':20,'李四':16,'王五':22}
# print(dic1['赵六'])
# # KeyError: '赵六'

# 4 NameError
# print(a)
# # NameError: name 'a' is not defined

# 5 SyntaxError
# print(001+2)
# SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers


# 6 ValueError
a=int(input('请输入第一个整数:'))
b=int(input('请输入第二个整数:'))
print(a/b)
'''
请输入第一个整数:5.3
Traceback (most recent call last):
  File "D:\PYWORK\pylearn\102python中常见的异常类型.py", line 40, in <module>
    a=int(input('请输入第一个整数:'))
ValueError: invalid literal for int() with base 10: '5.3'

进程已结束，退出代码为 1
'''