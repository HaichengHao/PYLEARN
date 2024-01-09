# editor 百年
# date: 2024/1/9 19:11
'''
形参与实参名称可以不相同

'''
# 定义函数名和形参arg1,arg2
def fun(arg1,arg2):
    # 写函数体
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1', arg1)
    print('arg2', arg2)
    return #没有要返回的东西时可以不写返回值，甚至不用写return

# 函数调用
n1=11
n2=[22,33,44] #列表是可变序列
print('n1',n1)
print('n2',n2)
fun(n1,n2)  #位置实参，实参名称与形参名称可以不一样
print('n1',n1)
print('n2',n2)
'''
在函数的调用中，进行参数的传递，如果是不可变对象，在函数体中的修改不会影响实参的值
如果是可变对象，在函数体中的修改会影响实参的值'''
