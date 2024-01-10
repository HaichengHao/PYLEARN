# editor 百年
# date: 2024/1/10 16:11
'''
什么是递归函数
答：如果在一个函数体内调用了该函数本身，这个函数就是递归函数

递归函数的组成部分:
递归调用与终止条件

递归的调用过程
每递归调用一次函数，都会在栈内存分配一个栈帧
每执行完一次函数，就会释放相应的空间

递归的优缺点
缺点：占内存多，效率低下
优点：思路和代码简单
'''

# # 阶乘计算
# # 定义函数名为func1
# def func1(num): #<--定义形参为num
#     if num>1: #条件判断语句，如果num>1
#         num=num*func1(num-1) #num就等于num乘func1(num-1)
#     return num
#
#
# # 函数调用
# # num1=int(input('请输入一个大于零的整数:'))
# # result=func1(num1)
# # print(str(num1)+'的阶乘为',result)
#
# # 调试用
# print(func1(6))


# 写法2
def func2(num):
    if num==1:
        return 1
    else:
        num=num*func2(num-1)
        return num
# 调用
print(func2(6))
