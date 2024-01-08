# editor 百年
# date: 2024/1/1 15:02
# 列表元素的遍历
# 引例
print('p' in 'python')
# True
print('k' in 'kfc')
# True
print('l' not in 'large')
# False


lst=['10',100,'hello','aloha']
print(100 in lst)
# True
print(10 in lst)
# False <--因为我们写的10是字符串类型的
# 验证
print('10' in lst)
# True
# for in 后面跟的是可迭代变量，目前学了字符串和列表
for i in lst:
    print(i,end='\t')
    # 10	100	hello	aloha