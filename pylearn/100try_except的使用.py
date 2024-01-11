# editor 百年
# date: 2024/1/11 14:16
'''
try except 相当于主动指定报错后执行的操作
'''
# 写一个函数，实现除法运算
def divf(a,b):
    c=a/b
    return c
while 1:
    try:
        n1=int(input('请输入第一个整数:'))
        n2=int(input('请输入第二个整数:'))
        res=divf(n1,n2)
        print(res)
    except ZeroDivisionError:
        print('被除数应当大于0，请重新输入')
    except ValueError:
        print('请输入正确的数值')
