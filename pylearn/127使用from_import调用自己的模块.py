# editor 百年
# date: 2024/1/18 17:17

from mymod127 import multi
print(multi(3,9))
# 27
# 尝试调用模块中的其它方法
try:
    print(mymod127.minus(3,6))
except BaseException as e:
    print(e)
# name 'mymod127' is not defined
# 再次说明，from 模块名 import 函数/变量/类 只能用自己调用的，不能用没被调用的