# editor 百年
# date: 2024/1/3 9:12
'''
键(key)的判断
in  -->指定的key在字典中则返回True
not in -->指定的key不在字典中则返回True

字典元素的删除
del dic1['张三']

字典元素的新增
dic1['赵六']=20
'''


dic1={'张三':12,'李四':17,'王五':12}

print('张三'in dic1)
print('赵六'not in dic1)
# True
# True

del dic1['张三']
print(dic1)
# {'李四': 17, '王五': 12}

dic1['赵六']=20
print(dic1)
# {'李四': 17, '王五': 12, '赵六': 20}

# 补充,.clear() <--与列表中的clear功能相同
# print(dic1.clear())
# None

# 另一种写法
# dic1.clear()
# print(dic1)
# {} <--字典空了


# 字典元素的修改操作
dic1['李四']=10
print(dic1)
# {'李四': 10, '王五': 12, '赵六': 20}