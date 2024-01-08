# editor 百年
# date: 2023/12/29 20:16
# 比较运算符
# 结果是布尔类型
a,b=10,20
print('a>b么？',a>b)
print('a<b么',a<b)
# 高级一点的
# if a>b:
#     print('a>b')
# else:
#     print('a<b')

print(a>=b)
# False
print(a<=b)
# True
print(a!=b)
# True

# 一个等号是赋值运算符
# ‘==’是赋值运算符
# ==比较的是两个对象的value（值）
# 那么如何比较两个对象的标识？
# 答:is
a=10
b=10
print(a==b)
print(a is b)
# True
# True
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1 == lst2)
print(lst1 is lst2)
# True  <--两个列表值相同
# False  <--两个对象的标识不同
print(id(lst1))
print(id(lst2))
# 1911554135104
# 1911557457664

print(lst1 is not  lst2)
# True <--lst1与lst2标识不同