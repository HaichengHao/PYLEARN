# editor 百年
# date: 2024/1/13 17:00
'''
继承
语法格式
class 子类类名(父类1，父类2):
    pass
'''

'''
如果一个类没有继承任何类，则默认继承object
python支持多继承
定义子类时，必须在其构造函数中调用父类的构造函数
super().__init__(要继承父类的属性)
super().父类中的方法名  继承父类中的方法，用在方法重写当中使用'''
# 理解何为子类
# 例如生物可以分为动物和植物，动物又可分为爬行动物、哺乳动物....

# 定义父类
class Person: #也可写为Person(object),若不写则默认继承object
    def __init__(self,name,age): #初始化方法 定义属性name和age
        self.name=name
        self.age=age
    # 定义方法info
    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name,self.age))
# 定义子类Student,继承Person
class Student(Person):
    def __init__(self,name,age,score):
        # 利用super()调用父类的属性
        super().__init__(name,age)
        # 再指定子类拥有的新的属性成绩(score)
        self.score=score
# 定义子类Teacher,继承Person
class Teacher(Person):
    def __init__(self,name,age,teachofyears):
        # 利用super()调用父类的属性
        super().__init__(name,age)
        # 再指定子类Teacher拥有的属性教龄(teachofyears)
        self.teachofyears=teachofyears

# 测试
# 创建实例对象stu
stu=Student('jack-ma',60,'100')
# 调用Person类的info方法
stu.info()
# 姓名:jack-ma,年龄:60
print(stu.score)
# 100

# 创建实例对象teacher
teacher=Teacher('张三丰',88,40)
# 调用父类Person的info方法
teacher.info()
# 姓名:张三丰,年龄:88

# 查看张三丰老师的教龄
print(teacher.teachofyears)
# 40