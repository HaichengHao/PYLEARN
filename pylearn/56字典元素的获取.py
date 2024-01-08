# editor 百年
# date: 2024/1/3 8:42
# 字典元素的获取，即以键取值
'''
[]取值法
例如: dic['张三']

get()取值法
例如: dic.get('张三')

区别：
    []如果字典中不存在指定的key,抛出KeyError异常
    .get()方法取值，如果字典中不存在指定的key,则不会抛出KeyError,而是返回None，
    可以通过参数设置默认的Value,以便指定的Key不存在时返回

'''

dic1={'张三':12,'李四':17,'王五':12}

print(dic1['张三'])
# 12
print(dic1['李四'],dic1['王五'])
# 17 12

# .get()方法
print(dic1.get('张三'))
# 12

# 取值不存在的情况

# 1[]
# print(dic1['赵六'])
#   File "D:\PYWORK\pylearn\56字典元素的获取.py", line 30, in <module>
#     print(dic1['赵六'])
# KeyError: '赵六'

# 2.get()
print(dic1.get('赵六'))
# None

# 指定返回的值
print(dic1.get('赵六','未查找到相关信息'))
# 未查找到相关信息