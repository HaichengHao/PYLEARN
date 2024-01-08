# editor 百年
# date: 2024/1/6 17:28
'''
.index() 查找子串substr第一次出现的位置，如果查找的子串不存在时，则抛出ValueError
.rindex() 查找子串substr最后一次出现的位置，如果查找的子串不存在时，则抛出ValueError
.find() 查找子串substr第一次出现的位置，若不存在，则返回-1
.rfind() 查找子串substr最后一次出现的位置，如果不存在，则返回-1
'''
str1='hello,world,hello'
print(str1.index('lo'))
# 3
print(str1.find('lo'))
# 3


# 查找'lo'最后出现的位置
print(str1.rindex('lo'))
# 15
print(str1.rfind('lo'))
# 15


# 如果查找的元素不存在的情况

# .find()与.rfind()查找的元素不存在则会返回-1
print(str1.find('pp'))
# -1
print(str1.rfind('pp'))
# -1

# .index()和.rindex()查找的元素不存在则会报错
# print(str1.index('pp'))
# Traceback (most recent call last):
#   File "D:\PYWORK\pylearn\77字符串的查询操作.py", line 30, in <module>
#     print(str1.index('pp'))
# ValueError: substring not found
# print(str1.rindex('pp'))
# Traceback (most recent call last):
#   File "D:\PYWORK\pylearn\77字符串的查询操作.py", line 35, in <module>
#     print(str1.rindex('pp'))
# ValueError: substring not found
#
