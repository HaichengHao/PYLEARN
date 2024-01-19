# editor 百年
# date: 2024/1/19 13:14
# 导入创建的包mypkg里的模块A和模块B
'''from mypkg129 import modeA,modeB
print(modeA.a+modeB.b)'''
# 110

# 另一种写法 import 包名.模块名
'''import mypkg129.modeA ,mypkg129.modeB
print(mypkg129.modeA.a+mypkg129.modeB.b)'''
# 110

# 简单书写，利用 as 别名
'''import mypkg129.modeA as A,mypkg129.modeB as B
print(A.a+B.b)'''
# 110

'''from mypkg129 import modeA as A,modeB as B
print(A.a+B.b)'''
# 110

# 使用 from import 方式导入时还可以跟变量
from  mypkg129.modeA import a
from mypkg129.modeB import b
print(a+b)
# 110

