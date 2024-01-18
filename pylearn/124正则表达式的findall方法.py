# editor 百年
# date: 2024/1/17 16:48
'''
re.findall(pattern,string,flag=0)
用在整个字符串中搜索所有符合正则表达式的值，结果为列表,若不匹配，返回的是空列表
'''
# 待检验的字符串
str1="1.1 just like a little cat,0.0 is more funny,just like a little boy who is staring you,7.7 like a boy who is crying "
str2="hello world"
# 定义正则表达式规则

ptn=r'\w\.\w+'
# 导入re模块
import re
# 创建匹配对象matchlst,调用findall方法查找所有匹配的字符串，返回结果是一个列表
matchlst=re.findall(ptn,str1)
matchlst2=re.findall(ptn,str2)
try:
    print(matchlst)
except BaseException as e:
    print(e)

# ['1.1', '0.0', '7.7'] <--成功匹配，结果为列表，列表元素为匹配值

try:
    print(matchlst2)
except BaseException as e:
    print(e)
    # [] <--无匹配内容，返回空列表