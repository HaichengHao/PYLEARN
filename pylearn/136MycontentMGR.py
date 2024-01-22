# editor: 百年
# time: 2024/1/21 17:19
# 定义一个类叫做上下文管理器，默认继承Object类，上下文管理器其实就是一个类实现了特殊方法__enter__()和__exit__()
'''
mycontentMGR上下文管理器，默认继承object类
'''
class mycontentMGR:
    # 定义一个特殊方法__enter__
    def __enter__(self):
        print('Enter方法被调用执行了')
        return self
    # 定义一个特殊方法__exit__
    def __exit__(self, exc_type, exc_value,exc_tb):
        print('Exit方法被调用执行了')

    # 定义实例方法show()
    def show(self):
        print('show方法被调用执行了')

with mycontentMGR() as file: #相当于file=mycontentMGR()
    file.show()