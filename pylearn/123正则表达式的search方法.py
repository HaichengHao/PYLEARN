# editor 百年
# date: 2024/1/17 16:45
'''
re.search(pattern,string,flags=0)
常用的正则处理方法
-re.search()方法
用于在整个字符串中搜索第一个匹配的值，如果匹配成功，输出match对象，否则为None
'''
import re
str1="This is Python3.10 version ,before this version is Python3.9"
str2="4.10 ver"
str3="let`s study python"
# 写匹配规则
ptn=r'\d\.\w'

# 写re.search()赋予变量match1,match2,match3
match1=re.search(ptn,str1,re.I)
match2=re.search(ptn,str2,re.I)
match3=re.search(ptn,str3,re.I)
try:
    print(match1)
except BaseException as e:
    print(e)
# <re.Match object; span=(0, 5), match='1.The'>

try:
    print(match2)
except BaseException as e:
    print(e)
# <re.Match object; span=(0, 3), match='4.1'>

try:
    print(match3)
except BaseException as e:
    print(e)
# None