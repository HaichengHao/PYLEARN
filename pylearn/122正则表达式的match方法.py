# editor 百年
# date: 2024/1/17 14:17
'''
re.match()方法，用于从字符串的开始位置进行匹配，如果起始位置匹配成功，结果为Match对象，否则为None
'''
# 用法re.match(pattern,string[,flags=0])
# pattern -规则
# string -待检测的字符串
# flag -标志位
# 导入 re模块

import re
# 定义规则
pattern=r'\d\.\d+' #数字0-9\第二个是'.'\之后是匹配前面的字符一次或多次

# 待匹配的字符串
s='I study Python3.10 every day'
# 创建match对象，调用.match方法匹配
match=re.match(pattern,s,re.I) #re.I标识字符串标识忽略大小写
try:
    print(match)
except BaseException as e:
    print(e)

s2='1 hello world'
match2=re.match(pattern,s2,re.I)
try:
    print(match2)
except BaseException as e:
    print(e)

s3="1.2helloworld"
match3=re.match(pattern,s3,re.I)
try:
    print(match3)
except BaseException as e:
    print(e)

# <re.Match object; span=(0, 3), match='1.2'> <--匹配成功

# 输出匹配值的起始位置
print('匹配值的起始位置:',match3.start())
print('匹配值的结束位置:',match3.end())
print('匹配区间:',match3.span())
print('待匹配的字符串:',match3.string)
print('匹配的数据:',match3.group())
'''
匹配值的起始位置: 0
匹配值的结束位置: 3
匹配区间: (0, 3)
待匹配的字符串: 1.2helloworld
匹配的数据: 1.2
'''