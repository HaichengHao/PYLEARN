# editor 百年
# date: 2024/1/10 9:42
'''
个数可变的关键字形参
定义函数时，可能无法事先确定传递的位置参数的个数时，使用可变的位置参数
使用'*'定义个数可变的位置形参
结果为一个元组

个数可变的关键字形参
定义函数时，无法事先确定传递的关键字实参个数时，使用可变的关键字形参
使用'**'定义个数可变的关键字形参
结果为一个字典
'''


# 个数可变的位置形参
def fun1(*args):  #<--个数可变，不止一个
    print(args)

# 调用
fun1('hello')
# ('hello',)
fun1('hello','world','hi','python')
# ('hello', 'world', 'hi', 'python')

# 可以看出个数可变的位置形参结果为一个元组


# 个数可变的关键字形参
def fun2(**args2):
    print(args2)
# 调用
fun2(a=10)
# {'a': 10}
fun2(a=40,b=20,c=30)
# {'a': 40, 'b': 20, 'c': 30}
# 个数可变的关键字形参返回的结果是一个字典


# 注意事项，个数可变的位置参数只能定义一个
# def fun3(*args1,*args):
#     pass
#  File "D:\PYWORK\pylearn\93个数可变的位置形参与关键字形参.py", line 41
#     def fun3(*args1,*args):
#                     ^
# SyntaxError: invalid syntax


# def fun4(**args1,**args2):
#     pass
#   File "D:\PYWORK\pylearn\93个数可变的位置形参与关键字形参.py", line 49
#     def fun4(**args1,**args2):
#                      ^^
# SyntaxError: invalid syntax

# 同样的，个数可变的关键字形参也是只能有一个

# 但是，可以指定一个个数可变的位置形参和个数可变的关键字形参
def fun0(*args,**kwargs):
    print(args)
    print(kwargs)

# 调用
fun0(10,20,30,a=3,b=4,c=9)
# (10, 20, 30)
# {'a': 3, 'b': 4, 'c': 9}

# 可见，可以指定一个个数可变的位置形参和一个个数可变的关键字形参
# 并且，它依然会遵循输出的规则，即个数可变的位置形参输出的依旧是元组，个数可变的关键字形参输出的依旧是字典
# 且，分别输出，互不影响,注意，个数可变的位置形参要在个数可变的关键字形参之前