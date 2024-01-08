# editor 百年
# date: 2024/1/8 15:59
'''
字符串的切片操作
字符串是不可变类型
不具备增删改等操作
切片操作将产生新的对象
与列表的切片操作类似
'''

s1='hello,world'
print(len(s1))
# 11
print(s1[:3])
# hel
print(s1[::2])
# hlowrd

s2=s1[:5]
s3=s1+'!'+s2
print(s3)
#hello,world!hello
