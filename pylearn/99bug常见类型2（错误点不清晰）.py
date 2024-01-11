# editor 百年
# date: 2024/1/11 10:36
'''
错误点不清晰导致的错误
'''
# 例1 索引越界
'''
lst=[11,22,33,44]
print(lst[4]) '''
#这里就出现了索引越界，四个元素的索引分别是01，2，3

# 例2 方法参数值不清晰
'''
lst=[]
lst.append('a','b','c')
print(lst)'''
# TypeError: list.append() takes exactly one argument (3 given)
# 查看append方法的参数值，只能有一个，但是写了三个

#