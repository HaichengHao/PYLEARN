# editor 百年
# date: 2024/1/6 10:59
#
'''
集合元素的判断操作
类比之前了解过的in 和 not in 可以判断集合中是否有指定的元素
eg:
s1={1,2,3,4}
print(1 not in s1)


集合元素的新增操作
调用.add()方法，一次添加一个元素
调用.append()方法，一次至少添加一个元素


集合元素的删除操作
调用.remove()方法，一次删除一个指定元素，如果指定的元素不存在就抛出KeyError
调用.discard()方法，一次删除一个指定元素，如果指定的的元素不存在不抛出异常
调用.pop()方法，一次删除一个任意元素
调用.clear()方法，清空集合

'''

# 判断操作
s1={1,2,3,4}
print(1 not in s1)
# False
print(10 not in s1)
# True



# 集合元素的新增操作

# .add()的示例
s1.add(20)
print(s1)
# {1, 2, 3, 4, 20}

# 错误示例
# s1.add(30,40,50)
# TypeError: set.add() takes exactly one argument (3 given)


# .update()方式的两种示例
s1.update({30, 40, 50})
print(s1)
# {1, 2, 3, 4, 40, 50, 20, 30}

s2={9,8,7,6}
s1.update(s2)
s1.update([1,2,3])
print(s1)
# {1, 2, 3, 4, 6, 7, 40, 8, 9, 50, 20, 30}
s1.update([98,3,42,123])
print(s1)
# {1, 2, 3, 4, 98, 6, 7, 40, 8, 9, 42, 50, 20, 123, 30}
s1.update((13,24,57,66))
print(s1)
# {1, 2, 3, 4, 6, 7, 8, 9, 13, 20, 24, 30, 40, 42, 50, 57, 66, 98, 123}

# 集合元素的删除操作

# .remove()
s1.remove(1)
print(s1)
# {2, 3, 4, 6, 7, 8, 9, 13, 20, 24, 30, 40, 42, 50, 57, 66, 98, 123}

# 如果移除不存在的元素会报错
# s1.remove(111)
# print(s1)
'''
Traceback (most recent call last):
  File "D:\PYWORK\pylearn\72集合的相关操作.py", line 69, in <module>
    s1.remove(111)
KeyError: 111

进程已结束，退出代码为 1
'''

# discard()
# .discard()删除不存在的元素不会报错
s1.discard(111)
print(s1)
# {2, 3, 4, 6, 7, 8, 9, 13, 20, 24, 30, 40, 42, 50, 57, 66, 98, 123} <--并没有因为111不存在就报错

s1.discard(2)
print(s1)
# {3, 4, 6, 7, 8, 9, 13, 20, 24, 30, 40, 42, 50, 57, 66, 98, 123}


# .pop()随机删除 ,括号内不能指定参数
s1.pop()
print(s1)
# {4, 6, 7, 8, 9, 13, 20, 24, 30, 40, 42, 50, 57, 66, 98, 123}
s1.pop()
print(s1)

# 错误示例， .pop() 括号内指定参数后会报错
s1.pop(123)
print('删除指定元素后',s1)
#     s1.pop(123)
# TypeError: set.pop() takes no arguments (1 given)

# .clear() 清空集合
s1.clear()
print(s1)
# set()