# editor 百年
# date: 2023/12/31 15:12
# continue用于结束当前循环，进入下一个循环，通常与分支结构中的if一起使用
# 比较 break 结束循环  continue 结束当前循环进入下一个循环
# 题目：要求输出0-50中5的倍数
# for i in range(51):
#     if i%5==0:
#         print(i)
#

# 利用continue的解法
for i in range(51):
    # 如果不能被5整除
    if i%5!=0:
        # 结束当前循环，进入下一循环
        continue
    # 若能被5整除
    else:
        # 打印输出
        print(i)