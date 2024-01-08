# editor 百年
# date: 2023/12/31 9:24
# while练习题：计算1-100之间的偶数和

# 变量初始化
a=0
sum=0#sum用于存储偶数和
# 条件判断语句
while a<=100:
    # 条件执行体
    a+=1
    # 也可以写为 if a%2: <--这样的话为False 计算的是奇数和
    if a%2==0: #<--这样为True
        sum+=a
print(sum)
# 2550
