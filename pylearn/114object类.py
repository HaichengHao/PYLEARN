# editor 百年
# date: 2024/1/15 10:09
'''
object类
object是所有类的父类(万类之源)，因此所有类都有object类的属性和方法
内置函数dir()可以查看指定对象所有属性
object有一个__str__()方法，用于返回一个对于"对象的描述"，对应于内置函数str()经常用于print()方法，
帮我们查看对象的信息，所以我们经常会对__str__()进行重写
'''
# 创建Student类
class Student:
    # # 旧
    # def __init__(self):
    #     pass

    # 新
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '姓名:{0}，年龄:{1}'.format(self.name,self.age)


# 旧
# stu0=Student()
# print(stu0)
# <__main__.Student object at 0x00000255926232B0> <--如果未重写__str__()则会输出内存地址
# 查看stu的所有属性
# print(dir(stu))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']






# 新
stu=Student('张三',20)
# 查看stu的所有属性
print(dir(stu))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
# '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name']
# 多了两个我们创建的属性name,age

# 这些都并不是Student类中所有的，而是从object类中继承过来的
print(stu)
#姓名:张三，年龄:20 <--一旦重写__str__()后，他将不再输出对象的内存地址
