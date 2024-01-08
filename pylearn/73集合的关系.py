# editor 百年
# date: 2024/1/6 14:31
# 集合间的关系
'''
1判断两个集合是否相等
 可以用运算符==或!=进行判断
2一个集合是否是另一个集合的子集
 可以调用方法.issubset()( is sub(副的，子级别的) set集合)进行判断
 eg:B是A的子集 B.issubset(A)
3一个集合是否是另一个集合的超集
可以调用方法.issuperset(is super(超级，高级) set)进行判断
eg: A是B的超集 A.issuperset(B)
4两个集合是否没有交集
可以调用方法.isdisjoint进行判断
A.isdisjoint(B)


'''

A={1,2,3,4,5,6,7,8,9}
B={1,2,4,5,6,9,0,12}
C={1,2,3,5,7}

# 判断暖集合A，B是否相等
print(A==B)
# False

print(A!=B)
# True

# 判断C是不是A的子集
print(C.issubset(A))
# True
# 判断B是不是A的子集
print(B.issubset(A))
# False

# 判断A是不是C的超集
print(A.issuperset(C))
# True


# 判断A和B没有交集正确与否
print(A.isdisjoint(B))
# False <--A、B是有交集的

# 输出A与B的交集
print(A & B)
# {1, 2, 4, 5, 6, 9}
# 输出A与C的交集
print(A&C)
# {1, 2, 3, 5, 7}

# 输出三个集合的并集
print(A|B|C)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12}