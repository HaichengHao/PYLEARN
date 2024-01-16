# editor 百年
# date: 2024/1/16 15:30
'''
特殊方法 以两个下划线开始，两个下划线结束，且记住有小括号
__len__()通过重写__len__()方法，让内置函数len()的参数可以是指定类型
__add__()通过重写__add__()方法，可使用自定义对象具有“+”功能
__new__()用于创建对象
__init__()对创建的对象进行初始化
'''

a=20
b=100
c=a+b
print(c)
# 120

# 执行加法的时候python底层做了什么
'''
其实底层是调用了__add__()方法'''
# 其实是这样的
print(a.__add__(b))
# 120

# 通过观察builtins就可以看出来
'''
    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        '''

# 自定义一个类实现加法操作
class Student:
    #初始化方法，指定一个实例属性name
    def __init__(self,name):
        self.name=name
#         重写__add__()
    def __add__(self, other):
        return self.name+other.name
#     重写__len__()
    def __len__(self):
        # 返回name的长度
        return len(self.name)


# 创建实例对象
stu1=Student('张三')
stu2=Student('李四')
stu3=Student('henrry')
stu4=Student('erika')

# 现在stu1可以加上stu2么？
# 验证猜想
try:
    print(stu1+stu2)
except BaseException as e:
    print(e)
    # unsupported operand type(s) for +: 'Student' and 'Student'
    # 很明显，不支持这样的操作
    # 如果想实现，那么就要重写__add__()

    # 再次运行猜想
    # 张三李四 <--成功

# 换一种写法
try:
    print(stu1.__add__(stu2))
except BaseException as e:
    print(e)
    # 张三李四 <--成功



# __len__()
#注意，这是特殊方法，和内置函数len()是有区别的

try:
    print(len(stu1))
    print(len(stu3))
#     另一种写法
#     print(stu1.__len__())
    print(stu4.__len__())
except BaseException as e:
    print(e)
    # object of type 'Student' has no len()

    # 如何得出stu1的长度
    # 重写特殊方法__len__()
    # 再次输出
    # 2    即'张三'两个字符长度
    # 6    'henrry'6个字符长度
    # 5    'erika'5个字符长度

