# editor 百年
# date: 2024/1/9 20:04
'''
函数返回多个值时，结果为元组
'''
# 定义一个函数，可以返回列表中的奇数和偶数
def jo_fun(num):
    odd=[] #定义奇数列表的接收
    even=[] #定义偶数列表的接收
    # 遍历列表中的元素
    for i in num:
        # 如果可以被2整除，则为偶数，则偶数列表增加这个元素
        if i%2==0:
            even.append(i)
        else:
            # 否则奇数列表增加这个元素
            odd.append(i)
            # 返回偶数列表和奇数列表
    return odd,even

# 函数调用
lst1=[120,534,112,357,666,555] #实参lst1
print(jo_fun(lst1))  #<--注意返回多个值时，结果为元组
# ([357, 555], [120, 534, 112, 666])

# 函数的返回值
'''
1.如果函数没有返回值，则return 可以省略不写
2.函数的返回值，如果是1个，则直接返回
3.函数的返回值，如果是多个，则返回的结果是元组类型'''

def hw(): #无形参
    print('hello world')
    # 无返回值
# 调用
hw()
# hello world


# 定义
def hi():
    return 'hi'
# 调用
result=hi() #定义参数接收返回值
print(result) #输出返回值
# hi

# 定义
def hp():
    return 'hello','world','python' #有两个或多个返回值
print(hp()) #返回的类型是一个元组
# ('hello', 'world', 'python') <--观察，是元组类型


'''函数是否需要返回值要视情况而定'''