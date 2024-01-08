# editor 百年
# date: 2024/1/5 10:17
'''
什么是集合(gather、set)
python语言提供的内置数据结构
与列表、字典一样都属于可变类型的序列
集合是没有值(value)的字典
也利用hash table  第一个放在集合中的元素未必是第一位
集合中的元素不能重复
'''

g1={1,3,5,7,9}
g2={i for i in range(0,10,2)}
print(g1,g2)
# 将集合g2的元素赋予g1,
g1.update(g2)
# 打印输出更新后的g1,利用列表接收，逆序排序
print(sorted(g1,reverse=True))
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# 集合的创建方式
# 第一种{}
g3={'you','me','she'}
g4=set({'our', 'their'})
print(g3,g4)
# {'you', 'me', 'she'} {'their', 'our'}
g5=set(range(10))
print(g5)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# 将列表元素转化为集合元素
g6=set([11,22,33])
print(g6)
# {33, 11, 22} <--放的第一个未必是第一个

g7=set('hello')
print(g7)
# {'h', 'e', 'o', 'l'} <--不像列表一样输出重复的元素

# 空集合的创建
empg=set()
print(empg,type(empg))
# set() <class 'set'>

# 集合套元组，将元组元素转化为集合元素，集合中的元素是无序的
tg=set((11,22,33))
print(tg)
# {33, 11, 22}
print(id(33),id(11),id(22))
# 1928369865968 1928369865264 1928369865616

# 补充：不可以利用{}直接定义空集合，python会将其作为字典
s1={}
print(s1,type(s1))
# {} <class 'dict'>