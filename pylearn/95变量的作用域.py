# editor 百年
# date: 2024/1/10 15:57
'''
变量的作用域
定义：
程序代码能访问该变量的区域

分类：
根据变量的有效范围可分为
1.局部变量
即在函数内定义并使用的变量，只在函数内部有效，局部变量使用global声明，就会生成全局变量

2.全局变量
函数体外的变量，可作用于函数体内外
'''

def fun(a,b): #a,b为函数的形参，作用在函数内部
    c=a+b
    return c #<--这里的c就是局部变量，在函数体内起作用


# 尝试打印输出a,b,c会报错，因为超出了范围，a,b,c为局部变量
# print(a,b,c)
# NameError: name 'a' is not defined


# 观察以下例子
name='ikun'
def fun2():
    print(name)
# 调用
fun2()
# ikun
# 可以发现，name为全局变量，作用范围为函数内部和外部


# 例2
'''def fun3():
    age=20
    print(age)
# 调用
fun3()'''
# 20

# 尝试输出函数内部的变量age发现报错
# print(age)
# NameError: name 'age' is not defined

# 如果想要函数内部的变量也可以作用于外部，需要将变量声明为全局变量
def fun3():
    global age
    age=20
    print(age)
#调用
fun3()
# 20

# 再次尝试打印输出age
print(age)
# 20 <--成功，因为age已经被声明为全局变量，可以作用与函数体内外