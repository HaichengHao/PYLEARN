# editor 百年
# date: 2024/1/5 10:03
# 元组的遍历
# 元组是一个可迭代对象，所以可以使用for in 进行遍历
t1=('white','gray','brown')

# 使用for in 遍历
'''for i in t1:
    print(i,end='\t')
    # white	gray	brown'''

# 其它方式，利用索引，但是需要事先知道元组中元素的个数，否则会出现索引越界的问题
print(t1[2])
# brown


# print(t1[3])
#   File "D:\PYWORK\pylearn\70元组的遍历.py", line 14, in <module>
#     print(t1[3])
# IndexError: tuple index out of range

print(t1[0:3])
# ('white', 'gray', 'brown')
