# editor 百年
# date: 2024/1/11 20:35
'''
traceback模块
可以使用traceback模块打印异常信息
'''
import traceback
try:
    print('1.-----')
    num=10/0
except:
    traceback.print_exc()