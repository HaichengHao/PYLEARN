# editor 百年
# date: 2024/1/15 10:56
'''
多态
简单来说，多态就是“具有多种形态”，它指的是:即便不知道一个变量所引用的对象到底是什么类型
，仍然可以通过这个变量调用方法，在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法
'''
# 创建类对象Animal,默认继承object类
class Animal():
    # 创建实例方法
    def eat(self):
        print('动物吃')
# 创建类对象dog,继承Animal类
class Dog(Animal):
#     重写eat()方法
    def eat(self):
        print('狗会吃骨头')
# 创建类对象Cat,继承Animal类
class Cat(Animal):
#     重写eat()方法
    def eat(self):
        print('猫吃鱼')

# 创建类对象Human,不继承Animal类
class Human():
#     定义eat()方法
    def eat(self):
        print('人吃五谷杂粮')


# 定义一个函数fun(),要求能够任意调用eat方法
def fun(obj):
    obj.eat()

# 调用函数fun()
fun(Animal())
# 相当于Animal().eat()
fun(Cat())
# 相当于Cat().eat()
fun(Dog())
# 相当于Dog().eat()
fun(Human())
# 相当于Human().eat()
# 动物吃
# 猫吃鱼
# 狗会吃骨头
# 人吃五谷杂粮
# 发现即使Human没有继承Animal类也可以使用其自身的eat方法

'''
Python是一门动态语言，崇尚"鸭子类型"，当看到一只鸟走起来像鸭子，游起泳来像鸭子，那么这只鸟就可以被称为鸭子
，在鸭子类型中，不需要关心对象是什么类型，到底是不是鸭子，只关心对象的行为。


静态语言(如Java)要想实现多态必须明确继承关系，而动态语言只关心是否有这个方法
'''
