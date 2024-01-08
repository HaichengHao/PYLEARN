# editor 百年
# date: 2023/12/31 9:30
# for in 循环
# in 表达从（字符串，序列等）中依次取值，又称为遍历
# for in 遍历的对象必须是可迭代对象
'''
for in 的语法结构
for 自定义的变量 in 可迭代对象
循环体
'''
# for i in range(1,10):
#     print(i)

# for item in 'Python':
#     print(item)
# 如果在循环体中不需要用到自定义变量，可以将变量写为'_'
# for _ in range(5):
#     print('life is short ,you need python')

# 使用for 循环计算一个累加和0-9
'''sum=0
for i in range(10):
    sum+=i
print(sum)'''
# 45

# 高级
sum=0
q=int(input('请输入你要计算0-几的累加和:'))
for i in range(q+1):
    sum+=i
print(sum)
# 请输入你要计算0-几的累加和:9
# 45