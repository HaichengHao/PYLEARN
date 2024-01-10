# editor 百年
# date: 2024/1/10 10:16
def fun(a,b,c): #形式参数a,b,c
    # 函数体
    print(a,b,c)

# 调用
fun(10,20,30)
# 10 20 30

lst=[11,12,13]
# fun(lst)
# Traceback (most recent call last):
#   File "D:\PYWORK\pylearn\94函数的参数总结.py", line 12, in <module>
#     fun(lst)
# TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
# 只传入一个参数，如果想正确，要在lst前加*，表示是可变的实参
fun(*lst)  #在函数调用时，将列表中的每个元素都转化为位置实参传入
# 11 12 13

# 关键字实参
fun(a=10,b=200,c=500)
# 10 200 500

dic1={'a':100,'b':200,'c':500}
# fun(dic1)
'''
Traceback (most recent call last):
  File "D:\PYWORK\pylearn\94函数的参数总结.py", line 26, in <module>
    fun(dic1)
TypeError: fun() missing 2 required positional arguments: 'b' and 'c'

会报错'''

# 而在前面加上**便正确
fun(**dic1)
# 100 200 500
# 所以如果想将字典转化为关键字实参需要在字典前加上**



# 默认值形参
def func1(a,b=10): #默认值形参，如果不传入，就默认b=10
    print(a,b)
func1(10)
# 10 10  <--可见默认b=10如果实参未指定就按默认的10输出

#个数可变的位置形参
def func2(*args):
    print(args)
func2('hello','world','hi','python')
# ('hello', 'world', 'hi', 'python') <--以元组形式输出


# 个数可变的关键字形参
def func3(**kargs):
    print(kargs)
func3(a=0,b=9,c=87)
# {'a': 0, 'b': 9, 'c': 87} <--以字典形式输出

# 关键字形参
def func4(a,b,c,d):
    print(a,b,c,d)
func4(10,20,30,40) #位置实参传递
# 10 20 30 40
# 关键字实参传递
func4(a=40,b=20,c=10,d=0)
func4(c=0,b=3,d=1,a=2)
# 40 20 10 0
# 2 3 0 1
func4(10,20,d=1,c=6) #前两个利用位置实参传递，后面两个按照关键字实参传递

'''问题，若让c,d只能进行关键字传递，该如何定义函数'''

# 答：在第一个要定义的关键字形参前加*
def func5(a,b,*,c,d):
    print(a,b,c,d)

# 测试
# func5(10,20,30,40)
# Traceback (most recent call last):
#   File "D:\PYWORK\pylearn\94函数的参数总结.py", line 80, in <module>
#     func5(10,20,30,40)
# TypeError: func5() takes 2 positional arguments but 4 were given
# 报错提示，只需要两个位置参数，但是给了四个位置参数

func5(10,20,c=30,d=40)
# 10 20 30 40 <--正确了

'''
函数定义时的形参的顺序问题'''
# 以下几种定义顺序都是可以的
def func6(a,b,*,c,d,**args1):
    pass
def func7(*args,**kargs1):
    pass
def func8(a,b=10,*args,**kwargs):
    pass