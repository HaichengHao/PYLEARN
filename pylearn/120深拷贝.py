# editor 百年
# date: 2024/1/17 9:29
'''
深拷贝
使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象
和拷贝对象所有的子对象也不相同
'''
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

# 创建实例对象
disk1=Disk()
cpu1=CPU()

computer1=Computer(cpu1,disk1)
# 输出computer1,以及其对应的实例属性cpu和disk
print(computer1,computer1.cpu,computer1.disk)


print('------------------------------------------------')
# 深拷贝
import  copy
# 利用深拷贝，将拷贝的computer1赋给computer2
computer2=copy.deepcopy(computer1)
# 输出实例对象computer2,以及其对应的实例属性cpu和disk
print(computer2,computer2.cpu,computer2.disk)

'''
<__main__.Computer object at 0x00000257D1303EB0> <__main__.CPU object at 0x00000257D1303EE0> <__main__.Disk object at 0x00000257D1303FD0>
------------------------------------------------
<__main__.Computer object at 0x00000257D1303D30> <__main__.CPU object at 0x00000257D1303190> <__main__.Disk object at 0x00000257D1330DF0>
'''

# 发现深拷贝后，不但实例对象不同，连实例对象的子对象也不同，说明深拷贝是为实例对象以及子对象开辟了新的空间进行存储