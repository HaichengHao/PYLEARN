# editor 百年
# date: 2024/1/1 15:11
# .append()在列表末尾添加一个元素
# .extend()在列表的末尾至少添加一个元素
# .insert()在列表的任意位置添加一个元素
# 切片，在列表的任意位置至少添加一个元素
lst=[10,'hello']
lst.append('hi')
print(lst)
# [10, 'hello', 'hi']

# 查看标识
print(id(lst))
# 2648938337344
lst.extend(['hihi','nikofox'])
print(lst)
# [10, 'hello', 'hi', 'hihi', 'nikofox']
# 查看标识
print(id(lst))
# 2648938337344  <--标识并没有发生变化
# 利用insert在索引为2（即'hi')所在的位置增加一个列表元素
lst.insert(2,['hi2','hi3'])
print(lst)
# [10, 'hello', ['hi2', 'hi3'], 'hi', 'hihi', 'nikofox']
# 查看索引位置
print(lst.index(['hi2','hi3']))
# 2
# 在索引为1的位置增加两个元素
lst.insert(1,'ix1')
print(lst)
# [10, 'ix1', 'hello', ['hi2', 'hi3'], 'hi', 'hihi', 'nikofox']
#查看索引位置
print(lst.index('ix1'))
# 1

# 还可利用extend操作直接将列表元素扩展到旧的列表
lst1=['life','is','short','you']
lst2=['need','python']
lst1.extend(lst2)
print(lst1)
# ['life', 'is', 'short', 'you', 'need', 'python'] <--可以发现，与insert不同，extend可以将列表元素'去皮',但是要注意，extend并不可以在指定位置添加


# 在列表的任意位置添加n多个元素
# 例如，在列表lst1的索引为1的位置上添加lst2的整个列表元素
# lst1[1:]=lst2
# print(lst1)
# ['life', 'need', 'python']

# 又如
lst1[2:]=lst2[1:]
print(lst1)
# ['life', 'is', 'python']