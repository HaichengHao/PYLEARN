# editor 百年
# date: 2024/1/3 9:26
'''
获取字典视图
.keys() 获取字典中的所有key
.values() 获取字典中所有的value
.items() 获取字典中所有的key,value对
'''
dic1={'张三':12,'李四':17,'王五':12}
keys=dic1.keys()
print(keys)
# dict_keys(['张三', '李四', '王五'])

# print(dic1.keys())
# dict_keys(['张三', '李四', '王五'])


values=dic1.values()
print(values)
print(dic1.values())
# dict_values([12, 17, 12])
# dict_values([12, 17, 12])


items=dic1.items()
print(items)
print(dic1.items())
# dict_items([('张三', 12), ('李四', 17), ('王五', 12)])
# dict_items([('张三', 12), ('李四', 17), ('王五', 12)])

# 可以利用list()将获取到的字典信息转化成列表

key_lst=list(keys)
print(key_lst)
# ['张三', '李四', '王五']

values_lst=list(values)
print(values_lst)
# [12, 17, 12]


item_lst=list(items)
print(item_lst)
#  [('张三', 12), ('李四', 17), ('王五', 12)]  <--转换后的列表元素由元组构成
