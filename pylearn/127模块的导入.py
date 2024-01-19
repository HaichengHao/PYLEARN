# editor 百年
# date: 2024/1/18 16:36
'''
创建模块
新建一个.py文件，名称尽量不要与Python自带的标准模块名称相同

导入模块
import 模块名称 as 别名
from 模块名称 import 函数/变量/类

'''
import math
print(id(math))
print(type(math))
print(math)
'''
2796968619888
<class 'module'>
<module 'math' (built-in)>
'''

print(math.pi)
# 3.141592653589793

# 解包，输出math模块所包含的方法
print(dir(math))
'''
['__doc__', '__loader__', '__name__', '__package__',
 '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 
 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 
 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 
 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 
 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 
 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan',
  'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 
  'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
'''

# 调用math模块中的pow()方法
print(pow(2,3))#输出2的3次方
# 8


# 输出高一位整数
print(math.ceil(9.0000001))
# 10

# 输出低一位整数
print(math.floor(9.99999999999))
# 9