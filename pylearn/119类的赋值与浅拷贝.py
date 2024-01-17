# editor 百年
# date: 2024/1/16 20:32
'''
类的浅拷贝与深拷贝
1变量的赋值操作
只是形成两个变量，实际上还是指向同一个对象
2浅拷贝
Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，
因此，源对象与拷贝对象会引用同一个子对象
3深拷贝
使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象
和拷贝对象所有的子对象也不相同

'''

class CPU:
    pass
class DISK:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
# 变量的赋值
# 创建实例对象
cpu1=CPU()
# 将cpu1的值赋给cpu2
cpu2=cpu1
# 输出cpu1与cpu2
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))
# <__main__.CPU object at 0x000001D846663FD0> 2028405669840
# <__main__.CPU object at 0x000001D846663FD0> 2028405669840

# 发现内存地址相同,也就是说一个对象放在两个变量中进行存储


# 类的浅拷贝
print('-----------------------')

# 创建一个实例对象disk1
disk1=DISK()
print(disk1)
# <__main__.DISK object at 0x000001F570013EB0>


# 创建一个实例对象computer1
computer1=Computer(cpu1,disk1)

# 开始浅拷贝,需要导入包copy
import  copy
# 浅拷贝computer1赋值给computer2
computer2=copy.copy(computer1)
print(computer1,computer1.cpu,computer1.disk)
print(computer2,computer2.cpu,computer2.disk)
'''
<__main__.Computer object at 0x0000025387EA3E80> <__main__.CPU object at 0x0000025387EA3FD0> <__main__.DISK object at 0x0000025387EA3EB0>
<__main__.Computer object at 0x0000025387EA3DC0> <__main__.CPU object at 0x0000025387EA3FD0> <__main__.DISK object at 0x0000025387EA3EB0>

浅拷贝时，对象包含的子对象内容不拷贝，因此，源对象与拷贝对象会引用同一个子对象
'''