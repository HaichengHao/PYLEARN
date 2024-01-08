# editor 百年
# date: 2023/12/30 17:10
# range()函数
# 用于生成一个整数序列
# 创建range对象的三种方式
'''
range(stop) -->创建一个(0,stop)之间的整数序列，步长为1
range(start,stop) -->创建一个(start,stop)之间的整数序列，步长为1
range(start,stop,step) -->创建一个(start,stop,step)之间的整数序列，步长为step
'''
# 返回值是一个迭代对象
r=range(10)
print(r) #<--这样并不能查看到range生成的序列的具体细节
# range(0, 10)
print(list(r)) #<--利用list()将序列r接收
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 第二种方式，给定两个参数
r2=range(3,8) #不包含stop 8
print(list(r2))
# [3, 4, 5, 6, 7]


# 第三种方式，给定三个参数
r3=range(3,12,2) #3-12(不包含12，步长为2)
print(list(r3))
# [3, 5, 7, 9, 11]

print(10 in r3)
# False
print(7 in r2)
# True

r4=range(1,20,1)
print(list(r4))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

