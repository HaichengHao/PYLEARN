# editor 百年
# date: 2023/12/30 17:29
# 反复做一件事叫做循环
# a=1
# while a<10:
#     # 执行条件执行体
#     print(a)
#     a+=1
'''
题目：计算0-4的累加和
'''

# # 初始化变量
# a=0
# b=0
# # 条件执行体
# while a<5:
#     a+=1
#     b+=a
# print(b)

# 高级
a=0
sum=0
b=int(input('请输入一个数'))
while a<b:
    a+=1
    sum+=a
print(str(b)+"的累加和="+str(sum))