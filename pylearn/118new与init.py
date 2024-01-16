# editor 百年
# date: 2024/1/16 16:39
'''
__new__() 与__init__()
'''
# 创建类对象
class Person(object):

    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行，cls的id值为:{0}'.format(id(cls)))
        # 调用object的__new__()方法，传入cls，赋值给变量obj
        obj=super().__new__(cls)
        print('创建的对象的id为:{0}'.format(id(obj)))
        return obj


    def __init__(self,name,age):
        print('__init__()被调用,self的id值为{0}'.format(id(self)))
        # 赋予实例变量
        self.name=name
        self.age=age

# 输出object这一类对象的id
print('类对象object的id为{0}'.format(id(object)))
# 输出Person这一类对象的id
print('类对象Person的id为{0}'.format(id(Person)))


# 创建Person类的实例对象
p1=Person('张三',20)
print('p1这一Person类的实例对象的id为:{0}'.format(id(p1)))

'''
D:\python\python.exe D:/PYWORK/pylearn/118new与init.py
类对象object的id为140706926864256
类对象Person的id为2058115098672
__new__被调用执行，cls的id值为:2058115098672
创建的对象的id为:2058116218544
__init__()被调用,self的id值为2058116218544
p1这一Person类的实例对象的id为:2058116218544
'''