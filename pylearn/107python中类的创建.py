# editor 百年
# date: 2024/1/12 14:52
'''
类的创建语法
class 类名:
    内容（一般为类属性和实例方法）
'''
'''
类的组成
1.类属性
2.实例方法
3.静态方法
4.类方法
'''

# 例子
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
        print('类方法')
    # 静态方法 static method
    @staticmethod
    def sm():
        print('静态方法')

print(type(student),id(student),end='\t')
# <class 'type'> 2696396236048	 <-- student 已经是类对象且开辟了内存空间