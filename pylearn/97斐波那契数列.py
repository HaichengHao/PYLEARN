# editor 百年
# date: 2024/1/10 17:27
'''
斐波那契数列是什么？
一个数等于前面的数的加和
[1,1,2,3,5,8]
'''
# 定义一个数n表示是第n位的数
def fib(n): #传入第n位
    if n==1: #如果n为1
        return 1 #返回1
    elif n==2: #如果n为2
        return 1 #返回1
    else: #否则开始递归
        return fib(n-1)+fib(n-2) #新的位数等于第n-1位元素加上第n-2位元素
# 斐波那契数列第六位的数字
# print(fib(6))

'''输出斐波那契数列'''
fiblst=[]
for i in range(1,7):
    fiblst.append(fib(i))
    # print(lst.append(fib(i)))
print(fiblst)
# [1, 1, 2, 3, 5, 8]