# editor: 百年
# time: 2024/1/28 12:55
'''
eval()函数用来执行一个字符串表达式，并返回表达式的值
字符串表达式可以包含变量、函数调用、运算符和其他Python语法元素
eval(expression[,globals[,locals]])
参数
expression --表达式
globals --变量作用域，全局命名空间，如果被提供，可以是任何映射对象

'''

# 几个例子
a='7'
print(type(a))

b=eval(a)
print(b,type(b))
'''
<class 'str'>
7 <class 'int'>
'''

s1="{'小明':20,'小红':19}"
print(s1,type(s1))
print(eval(s1),type(eval(s1)))
# {'小明':20,'小红':19} <class 'str'>
# {'小明': 20, '小红': 19} <class 'dict'>