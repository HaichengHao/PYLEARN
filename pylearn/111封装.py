# editor 百年
# date: 2024/1/13 13:43
'''
面向对象的三大特征，与语言无关
封装：提高程序的安全性
    将数据（属性）和行为（方法）包装到类对象当中。在方法内部对属性进行操作，在类对象的外部调用方法。
    这样，无需关心方法内部的实现细节，从而隔离了复杂度
    在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前面使用'__'

继承:提高代码复用性
多态:提高程序的可扩展性和可维护性
'''

# 创建一个类对象car
class car:
    def __init__(self,brand,id_info):#初始化方法,定义实例属性brand
        self.brand=brand
    #     定义一个隐藏属性id_info，不希望被类的外部访问，注意要加'__'
        self.__id_info=id_info
    #定义一个实例方法
    #     引擎启动
    def engine(self):
        print(self.brand+'\t'+'engine starting')

    #定义一个方法，输出车辆的id_info，注意，id_info可以在类的内部使用
    def show(self):
        print(self.__id_info)
# 创建实例对象vehicle(汽车)
vh=car('Audi','8888') #品牌，奥迪
# 调用实例方法
vh.engine()
# Audi	engine starting <--奥迪的引擎正在启动
print(vh.brand)
# Audi <--输出车的品牌
print(vh.show)
print(vh.brand)

# 尝试输出只能在类对象内才能访问的__id_info属性
try:
    print(vh.__id_info)
except BaseException as e:
    print(e)
#     'car' object has no attribute 'id_info'
# 发现id_info属性不能被外部访问


# 那么如何使用呢？
# 先输出，查看vh对象有哪些方法
print(dir(vh))
'''
['__class__', '__delattr__', '__dict__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
'_car__id_info', 'brand', 'engine', 'show']

'''
# 发现没有__id_info,但是有_car__id_info ,我们尝试输出
print(vh._car__id_info)
# 8888 <--输出成功，所以要想访问类对象内的属性，需要写上 对象名._类名__属性名