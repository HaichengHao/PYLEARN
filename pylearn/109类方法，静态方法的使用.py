# editor 百年
# date: 2024/1/12 15:40
'''
类属性：位于类对象内，类方法外的变量称为类属性，被该类的所有对象所共享
类方法: 使用@classmethod修饰的方法，使用类名直接访问的方法
静态方法：使用@staticmethod修饰的方法，使用类名直接访问的方法
类属性可以通过类对象或者是实例对象来访问，实例属性只能通过实例对象来访问
'''
class student:
    # 直接写在类里的变量称为类属性
    native_place='浙江' #类属性

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
        print('我是类方法，我被调用了')
    # 静态方法 static method
    @staticmethod
    def sm(): #<--注意定义静态方法时不需要传入参数
        print('我是静态方法，我被调用了')

# 创建类对象1
stu1=student('jackma',60)
print(stu1.native_place) #输出类属性
# 浙江

# 调用类方法，不需要传入参数
stu1.cm()
# 我是类方法，我被调用了


# 调用静态方法，不需要传入参数
stu1.sm()
# 我是静态方法，我被调用了

stu2=student('小马',20)
print(stu2.native_place)
# 浙江

# 修改类属性
student.native_place='西藏'
print(stu1.native_place,stu2.native_place)
# 西藏 西藏

