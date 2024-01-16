# editor 百年
# date: 2024/1/16 15:07
'''
特殊的属性 两个下划线开始，两个下划线结束
__dict__ 获得类对象或实例对象所绑定的所有属性和方法的字典
__class__ 输出实例对象所属于的类
__bases__ 输出指定类对象的基类元组/父类元组
__base__ 输出指定类对象继承的第一个类
__mro__ 输出指定类对象所属的类，继承的类以及祖先类的层次结构
'''
# 查看object类中的属性和方法，在114中有实例
print(dir(object))
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
# '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__']

# 查看dict的属性
class A:
    pass
class B:
    pass
class C(A,B): #创建类C继承A，B
    # 初始化方法，定义实例属性name
    def __init__(self,name,age):
        self.name=name
        self.age=age
#创建实例对象c,是C类的一个实例对象
# c=C('小白')
# print(c.__dict__)
# {'name': '小白'}

# 再给C类赋一个实例属性age,并调用__dict__输出实例对象的属性字典
c1=C('小红',20)
print(c1.__dict__)
# {'name': '小红', 'age': 20}

# 同样的可以输出类对象的属性字典
print(C.__dict__)
# {'__module__': '__main__', '__init__': <function C.__init__ at 0x000001B29F1FD990>, '__doc__': None}


# 利用.__class__可以输出指定实例对象所属的类
print(c1.__class__)
# <class '__main__.C'>

# 利用.__bases__输出指定类的基类元组
print(C.__bases__)
# (<class '__main__.A'>, <class '__main__.B'>)


# 利用.__base__输出指定类对象继承的第一个类
print(C.__base__)  #输出继承的第一个类

# 利于.__mro__输出指定实例对象所属的类，以及继承的类的结构
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# 可看出C类继承了A，B，祖先类是object类