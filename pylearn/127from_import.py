# editor 百年
# date: 2024/1/18 16:54
'''
from 模块名 import 方法/函数/语句
可以只调用一个模块的个别方法，不用导入整个模块
'''
from math import pi
print(pi)
# 3.141592653589793

# 尝试调用math中的其它方法
try:
    print(math.pow(2,3))
except BaseException as e:
    print(e)
    # name 'math' is not defined
    '''
    所以说利用from 模块名 import 方法名 只能使用被调用的方法，而不能调用没被调用的方法
    并不是调用了整个模块，所以并不是模块中的所有方法都能使用'''