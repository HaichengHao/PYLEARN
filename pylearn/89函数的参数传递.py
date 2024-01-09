# editor 百年
# date: 2024/1/9 10:20
'''
函数的参数传递
位置实参
根据形参对应的位置进行参数传递

关键字实参
根据参数名称进行实参传递
'''

# 位置实参的例子
def division(a,b): #其中的a,b即为形参
    c=a/b
    return c
# result=division(10,20) #其中的10，20即为对应a,b的位置实参
# print(result)
# 0.5


# 关键字实参的例子
result2=division(b=10,a=20) #其中a,b是关键字实参，指定什么就传入什么
print(result2)
# 2.0
