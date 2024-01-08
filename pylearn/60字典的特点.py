# editor 百年
# date: 2024/1/3 13:34
# 字典中的所有元素都是键值对，键不允许重复，值可以重复
# 字典中的元素是无序的
# 字典中的key必须是不可变对象
# 字典也可以根据需要动态地伸缩
# 字典会浪费较大的内存，是一种使用空间换时间的数据结构
# 列表不可以作为字典的对象
lst1=[100,200,300]
lst1.extend([100,200])
print(lst1)
# [100, 200, 300, 100, 200]
lst1.insert(1,40)
print(lst1)
# [100, 40, 200, 300, 100, 200]


dic1={'张三':45,'李四':48,'王五':89}
dic2=dict(name="张四",age=78)
# 可变对象不能够做键(key)
# 例如
dic3={lst1:100}
print(dic3)
# TypeError: unhashable type: 'list' <--非可哈希化类型，即为非可变类型，不可作为字典的key
