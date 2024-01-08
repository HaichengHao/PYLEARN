# editor 百年
# date: 2023/12/31 15:22
# else 语句
'''for i in range(3):
    pwd=input('请输入密码:')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码错误，请重新输入')
else:
    print('三次输入均错误')'''

# 还可以与while一起使用
i=0
while i<3:
    pwd=input('请输入密码:')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码错误，请重新输入')
        i+=1
else:
    print('三次输入均错误')