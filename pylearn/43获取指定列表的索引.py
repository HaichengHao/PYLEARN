# editor 百年
# date: 2024/1/1 11:25
# 获取指定列表的索引
# .index的方法
lst=list(['你好','hello','aloha'])
print(lst.index('hello'))

lst2=['hello','hello','aloha']
print(lst2.index('hello'))
# 0
# 为什么没有获取到第二个hello
# 如果列表中有相同元素，只返回第一个元素的索引

# 查找一个不存在与列表中的元素
# print(lst2.index('你好'))
# ValueError: '你好' is not in list

#指定start与stop来查找
print(lst2.index('hello',1,3))  #<--索引为1到索引为3但是不包括3
# 观察第二个列表，lst2=['hello','hello','aloha']
# 发现第二个列表中索引为1到2中索引为1的便是hello
print(lst2.index('hello',0,3))
# 0 从索引为0开始查，发现索引0已经匹配
