# editor 百年
# date: 2023/12/31 10:08
# break用于结束循环结构，通常与分支结构if一起使用
'''
从键盘录入密码，最多三次机会
'''
pwd='3333'
# 写法1
# for i in range(3):
#     s=int(input('请输入密码:'))
#     if str(s)==pwd:
#         print('密码正确')
#         break
#     else:
#         print('密码错误，请重新输入')

# 写法2
i=0
while i<3:
    s=int(input('请输入密码:'))
    if str(s)==pwd:
        print('密码正确')
        break
    else:
        i+=1
        print('密码错误，请重新输入')