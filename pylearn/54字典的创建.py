# editor 百年
# date: 2024/1/3 8:35
'''
1,使用花括号创建{key:value}
2,使用内置函数dict(key=value)
'''
dic1={'小王':12,'小张':16,'小花':'狗子'}
print(dic1)
# {'小王': 12, '小张': 16, '小花': '狗子'}


# 使用dict(key=value)
dic2=dict(name='小王',age=12)
print(dic2)

print(type(dic1))
# <class 'dict'>

# 创建空字典
dic3={}
print(dic3)
print(type(dic3))
# {}
# <class 'dict'>