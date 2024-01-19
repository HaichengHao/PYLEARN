# editor 百年
# date: 2024/1/18 11:13
# 一个模块当中可以包含语句包含n个类,包含n个函数，n多个语句
def func():
    pass
def func2():
    pass
class Student:
    # 类属性
    native_place='吉林'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def cm(cls):
        pass
    @staticmethod
    def sm():
        pass
    pass
a=10
b=20
print(a+b)