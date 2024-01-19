# editor 百年
# date: 2024/1/19 14:39
'''
python中常用的内置函数
'''
import sys
# sys.getsizeof()返回指定类型所占的比特数
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
'''
28
28
28
24'''

# time模块
# 导入
import time
print(time.time())
print(time.localtime(time.time()))
'''
1705647463.4366987
time.struct_time(tm_year=2024, tm_mon=1, tm_mday=19, tm_hour=14, tm_min=57, tm_sec=43, tm_wday=4, tm_yday=19, tm_isdst=0)
构成 年 月 日 时 分 秒 一周的第几天 一个月的第几天 是否是夏令时
'''

# os模块

# urllib包
import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())