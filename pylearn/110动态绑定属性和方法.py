# editor 百年
# date: 2024/1/12 20:02
'''
python是动态语言，在创建对象之后，可以动态地绑定属性和方法

'''
# 创建类
class Student:
    def __init__(self,name,age): #初始化方法，name,age为实例属性
        self.name=name
        self.age=age
    def eat(self): #定义实例方法
        print(self.name+'在吃饭')

# 创建对象=类名(参数)
stu1=Student('张三',20)
stu2=Student('李四',30)

#动态绑定，使stu1加上性别gender,stu2不动
stu1.gender='女'
print(stu1.name,stu1.age,stu1.gender)
# 张三 20 女

# 尝试输出stu2.gender，查看是否真的只是指定了实例对象stu1有实例属性gender
try:
    print(stu2.gender)
except BaseException as e:
    print(e)
    # 'Student' object has no attribute 'gender'
    '''
    发现报错了，因为Student没有gender实例属性，也说明了动态绑定的细节
    stu1动态绑定了一个实例属性叫gender，但是Student类本身的实例属性
    (name,age)并没有发生变化，也并未新增gender,好像是特地为stu1指定了gender实例属性一样'''



# 除了动态绑定属性以外，还可以动态绑定方法
# 让stu1，stu2都调用eat()方法
print(stu1.eat,stu2.eat)   #<--问题：为什么不写成stu1.eat() 因为不带括号调用的是整体，带括号调用的是结果
# 张三在吃饭
# 李四在吃饭
# 发现两个实例对象都可以调用实例方法
print(stu1.eat())
# None

stu3=Student('李武',20)
print(Student.eat(stu3))
print(stu3.eat())


# 但是如何单独指定一个实例对象拥有另一个实例对象所不具有的方法发呢?
# 如下
# 定义在类之外的，叫做函数
def show():
    print('我将被绑定在stu2上，成为动态指定的方法')
stu2.show=show #<--语法格式 : 实例对象.动态指定的方法名=写好的备选函数
# （相当于让只能蹲在外边吃饭的人当了小弟，可以进院子里吃饭)

# 调用动态指定的实例方法
print(stu2.show)
# 我将被绑定在stu2上，成为动态指定的方法


# 尝试让stu1实例对象也去调用show方法
try:
    print(stu1.show)
except BaseException as e:
    print(e)
# 'Student' object has no attribute 'show'
# 发现情况与动态绑定实例对象的属性一样，Student并没有这个show方法，
# 就像单独给stu2开小灶一样，只有它可以调用这个show实例方法
