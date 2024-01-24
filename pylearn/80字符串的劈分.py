# editor 百年
# date: 2024/1/7 14:14
'''
字符串的劈分操作
.split(sep='默认为空格' [,maxsplit=])
从字符串左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
通过参数sep指定劈分字符串的劈分符
通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分后，剩余的串会单独作为一部分不再劈分
劈分的结果是一个列表

.rsplit(sep='默认为空格' [,seq= ,maxsplit=])
与.split()除了改成从右开始劈分，其余都一样

用在爬虫中会比较方便
'''


str1="never say ever!"
# 不指定分割符和最大分割次数则会按照空格来分割，且会自动分割到最后一个空格为止
l1=str1.split()
print(l1)
# ['never', 'say', 'ever!']


str2="this#is#a#pen#"
# 指定分隔符为'#',最大劈分次数为2
l2=str2.split(sep='#',maxsplit=2)
print(l2)
# ['this', 'is', 'a#pen#'] <--按照#劈分字符串

l3=str2.split(sep='#',maxsplit=4)
print(l3)
# ['this', 'is', 'a', 'pen', '']

l4=str2.split(sep='#',maxsplit=3)
print(l4)
# ['this', 'is', 'a', 'pen#']

# 从右侧开始分割

# 不指定分割符
rl1=str1.rsplit()
print(rl1)
# ['never', 'say', 'ever!']

# 指定分割符
rl2=str2.rsplit(sep='#',maxsplit=2)
print(rl2)
# ['this#is#a', 'pen', '']
rl3=str2.rsplit(sep='#',maxsplit=4)
print(rl3)
# ['this', 'is', 'a', 'pen', '']

# 不指定最大分割次数
rl4=str2.rsplit(sep='#')
print(rl4)
# ['this', 'is', 'a', 'pen', '']