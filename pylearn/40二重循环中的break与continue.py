# editor 百年
# date: 2023/12/31 15:39
# 二重循环中的break和continue
# 二重循环中的break和continue用于控制本层循环
# 题目：
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            break
        print(j)