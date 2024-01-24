# editor 百年
# date: 2024/1/2 11:57
# 列表元素的排序
'''
常见的两种方式
1调用sort()方法，列中的所有元素默认按照从大到小的顺序进行排序，可以指定reverse=True,进行降序排序，原列表会发生改变
2 调用内置函数sorted([reverse=True]),可以指定reverse=True,进行降序排序，原列表不发生改变,但是会产生新的列表对象
'''

lst=[1,4,2,3,46,4,6]
print(id(lst))
# 2528474518592
lst.sort()
print(lst)
# [1, 2, 3, 4, 4, 6, 46]
print(id(lst))
# 2528474518592
lst.sort(reverse=True)
print(lst)
# [46, 6, 4, 4, 3, 2, 1] <--lst已经不再是原来的lst,而是排序后的lst,而内置函数sorted()不会改变原有的列表
print(id(lst))
# [46, 6, 4, 4, 3, 2, 1]


# 问题，含有字符串元素的列表可以排序吗？
# lst2=['a',10,'a','c','b']
# lst2.sort()
# print(lst2)
#   File "D:\PYWORK\pylearn\50列表元素的排序.py", line 19, in <module>
#     lst2.sort()
# TypeError: '<' not supported between instances of 'int' and 'str'  <--发现不能


# 利用sorted(列表)来进行排序,不改变原列表，但是会产生新的对象
lst3=[10,20,5,3,11]
print(id(lst3))
# 1501363557952
print(id(sorted(lst3)))
# 1501363383744 <--标识改变，说明产生了新的列表
# print(lst3)
print(sorted(lst3,reverse=True))
# [20, 11, 10, 5, 3]
print(lst3)
# [10, 20, 5, 3, 11] <--原列表并未发生改变
