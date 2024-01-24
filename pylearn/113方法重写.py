# editor 百年
# date: 2024/1/14 15:45
'''
方法重写
如果子类对继承父类的某个属性或方法不满意，可以在子类中对其（方法体）进行重新编写
子类重写后的方法中可以通过super().父类中的方法()调用父类中被重写的方法
'''
# 定义父类Person
class Person:
    # 初始化方法，指定实例属性name,age
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #创建实例方法info()输出姓名和年龄
    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name,self.age),end=' ')
#定义Student类，继承Person类
class Student(Person):
    def __init__(self,name,age,score):

        # 先继承类中的属性
        super().__init__(name,age)
        # 再指定子类Student类才有的属性成绩(score)
        self.score=score
    # 方法重写时如果还想调用父类中的方法，那就用super().方法名()继承
    def info(self): #<--左边框中已有提示重写了Person类中的方法
        # 这样就会先执行父类的输出，再输出子类中特有的方法
        super().info()
        print('学生成绩:{0}'.format(self.score))

# 定义Teacher类，继承Person类
class Teacher(Person):
    # 初始化Teacher
    def __init__(self,name,age,teachofyears): #指定其拥有的属性
        # 继承父类Person的属性
        super().__init__(name,age)
        # 再指定其拥有的属性教龄(teachofyears)
        self.teachofyears=teachofyears
#         方法重写，要求输出父类中所不具备的教龄teachofyears
    def info(self):
#     首先还是得利用info()输出姓名和年龄，所以利用super().info()继承方法
        super().info()
#         再重写新的方法
        print('教龄:{0}'.format(self.teachofyears))

# 创建实例对象stu
stu=Student('小明',20,'100')
# 调用实例方法
stu.info()
# 姓名小明,年龄20

# 创建实例对象teac
teac=Teacher('张麻子',20,'30')
# 调用实例方法
teac.info()
# 姓名张麻子,年龄20

# 方法重写，输出子类自己独有的属性，例如Student类中有成绩score,Teacher类想输出其独有的teachofyears
# 但是，父类Person的info方法已经无法满足它们的需要，这时就需要方法重写
# 重写的位置，应在子类之内，pycharm会有相应的方法重写提示
'''
方法重写后的运行结果
姓名:小明,年龄:20
学生成绩:100
姓名:张麻子,年龄:20
教龄:30
可以单行输出，只需加上end='/t' 或者end=' '
姓名:小明,年龄:20 学生成绩:100
姓名:张麻子,年龄:20 教龄:30
'''



