# editor 百年
# date: 2024/1/2 10:40
# 列表元素的删除操作
'''
(1) .remove() 一次可以移除一个元素，
    重复元素只删除第一个
    元素不存在则抛出ValueError

(2) .pop() 删除一个指定索引位置的元素
    不指定索引则默认删除最后一个元素
    指定索引不存在则抛出ValueError

(3) 切片，一次至少删除一个元素

(4) .clear() 清空列表

(5) .del() 删除列表
'''


lst1=[10,20,30,40,50,10,50,40,20,30]
print(id(lst1))
# 2438876255296

# .remove()操作
lst1.remove(10)
print(lst1)
print(id(lst1))
# [20, 30, 40, 50, 10, 50, 40, 20, 30]
# 1642480358464
# 有重复元素则默认移除第一个
# 不存在则抛出ValueError
# lst1.remove(100)
# ValueError: list.remove(x): x not in list


# .pop(index)
lst1.pop(-1)  #<--移除最后一个元素
print(lst1)
print(id(lst1))
# [20, 30, 40, 50, 10, 50, 40, 20]  <--最后一个元素‘30’被移除
# 1642480358464
# 索引不存在则报错
# lst1.pop(9) #<--移除索引为9的元素,不存在，会报错
'''
  File "D:\PYWORK\pylearn\48列表元素的删除操作.py", line 38, in <module>
    lst1.pop(9) #<--移除索引为9的元素
IndexError: pop index out of range
'''

# 切片 ，注意，切片会产生一个新的列表对象
lst1=lst1[1:3]
print(lst1)
print(id(lst1))
# [30, 40]
# 2438879172160  <--可以发现，经过切片后，产生了新的列表对象，而.remove()和.pop()操作都不会产生新的列表对象

# .clear() 清空列表
print(lst1.clear() ,id(lst1))
# None 2891362326080 #<--.clear()也不会生成新的列表
print(lst1)
# []


# 如何利用切片操作删除列表元素但是不产生新的对象
lst2=['hello','python','hi','pytorch']
print(lst2)
# ['hello', 'python', 'hi', 'pytorch']
print(id(lst2))
# 2014434907200
lst2[1:3]=[] #<--将索引为1-3（不包括3）的元素利用空列表代替
print(lst2)
# ['hello', 'pytorch']
print(id(lst2))
# 2014434907200 <--可以发现，这次利用切片，并没有产生新的列表对象


# del()操作
lst3=['lemon','melon','potato','tomato']
del lst3 #<--删除列表
print(lst3)
'''
  File "D:\PYWORK\pylearn\48列表元素的删除操作.py", line 81, in <module>
    print(lst3)
NameError: name 'lst3' is not defined. Did you mean: 'lst1'?
删除掉了lst3,所以再次打印输出lst3时报错'''