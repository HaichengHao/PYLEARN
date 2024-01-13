# editor 百年
# date: 2024/1/12 15:13
'''
对象的创建又称为类的实例化
语法：
    实例名=类名()
例子：
    stu=Student('Jack',20)
    print(stu.name,stu.age) <--实例属性
    stu.info()实例方法

有了实例，就可以调用类中的内容

'''
# 利用之前的代码
class student:
    # 直接写在类里的变量称为类属性
    native_place='山西' #类属性

    # 注意，在类之外定义的称为函数，在类里定义的叫做方法
    # 定义实例方法，但注意和定义函数不同，小括号内必须写self,也可将self换成自己定义的合法词汇，但一般写self
    def __init__(self,name,age): #name,age为实例属性   def __init__(self)叫做初始化方法
        self.name=name
        self.age=age
    # 实例方法
    def info(self):
        print('我的名字叫:',self.name,'年龄是:',self.age)
    # 类方法 class method
    @classmethod
    def cm(cls):
        print('调用了类方法')
    # 静态方法 static method
    @staticmethod
    def sm():
        print('调用了静态方法')

# 创建对象
stu1=student('张三',20)
print(stu1.name,stu1.age)
# 张三 20  <--输出实例属性
stu1.info()  #<--调用实例方法
# 我的名字叫: 张三 年龄是: 20
print(id(stu1))
# 1577160359456
print(stu1)
# <__main__.student object at 0x0000016F36153E20>

# 同样的可以调用类方法和静态方法
stu1.cm()
# 调用了类方法
stu1.sm()
# 调用了静态方法

# 类方法的两种调用形式

stu1.info() #第一种，对象名.方法名()

student.info(stu1) #第二种，类对象.方法名(对象名)