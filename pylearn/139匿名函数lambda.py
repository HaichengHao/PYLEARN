# editor: 百年
# time: 2024/2/1 11:29
'''
Python使用lambda来创建匿名函数
lambda函数是一种小型的、匿名的、内联函数，它可以具有任意数量的参数，但只能有一个表达式
匿名函数不需要使用def关键字定义完整函数
lambda函数通常用于编写简单的、单行的函数，通常在需要函数作为参数传递的情况下使用
'''
'''
其中：
# 语法格式: lambda arguments:expression
lambda 是python中的关键字，用于定义lambda函数
arguments 是参数列表，可以包含零个或多个参数，但必须在冒号前指定
expression 是一个表达式，用于计算并返回函数的结果
'''
# 例子
f = lambda:"hello pyhton"
print(f())
# hello pyhton

x=lambda a: a+10
print(x(2),x(3),x(4))
# 12 13 14

y=lambda b,c:pow(b,c)
print(y(2,1),y(2,2),y(2,3),y(2,4))
# 2 4 8 16

# lambda函数通常与内置函数如map()、filter()和reduce()一起使用，以便在集合上进行操作
num=[1,2,3,4,5]
squared_num=list(map(lambda x:pow(x,2),num))
print(squared_num)
# [1, 4, 9, 16, 25]