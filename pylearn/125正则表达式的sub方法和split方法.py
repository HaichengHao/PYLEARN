# editor 百年
# date: 2024/1/18 10:30

'''
-re.sub()方法
用于实现字符串的替换
pattern -匹配规则
repl -替换字符
string -待匹配字符串
cont -替换计数（替换多少次）
re.sub(pattern,repl,string[,count,flags=0])


-re.split()方法把字符串劈分
功能与字符串的split方法相同
pattern -替换规则
string -待检验字符串
maxsplit -最大切分次数，不指定则劈分到最后
re.split(pattern,string[,maxsplit,flags=0])
'''

import  re
# 定义格式
ptn='黑客|破解|反爬'
str1='我想学python，破解反爬机制，成为一名黑客'
match1=re.sub(ptn,'X',str1)
print(match1)
# 我想学python，XX机制，成为一名X

str2='https://www.baidu.com/s?wd=ngzk&ie=utf-8&tn=baidu'
ptn2='[?|&]' #[]为区间字符，表示匹配[]之内的内容
matchlst2=re.split(ptn2,str2)
print(matchlst2)
# ['https://www.baidu.com/s', 'wd=ngzk', 'ie=utf-8', 'tn=baidu']