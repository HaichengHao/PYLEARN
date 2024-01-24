# editor 百年
# date: 2024/1/7 10:03
'''
字符串的对齐
.center(width= [,fillchar=]) 居中对齐，第一个参数指定宽度，第二个参数指定填充字符，第二个参数是可选的
，默认是空格填充，如果设置宽度小于实际宽度则返回原字符串

.ljust(width= [,fillchar=]) 即left just 左对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数可选，同上

.rjust(width= [,fillchar=]) 即right just 右对齐，第一个参数指定宽度，第二个参数指定填充字符，同上

.zfill(width= [,fillchar=])  右对齐 zero fill 左边用0填充，该方法只接收一个参数，用于指定字符串的宽度，如果指定的宽度小于等于字符串的长度，则返回字符串本身
'''

str1="i wander how , i wonder why ,yestoday you told me about..."
print(len(str1))
# 58 <--字符串长度为58
# 指定宽度为70，居中显示，填充字符为'$'
print(str1.center(70,'$'))
# $$$$$$i wander how , i wonder why ,yestoday you told me about...$$$$$$
# 如果指定宽度小于原字符串宽度，则返回原字符串
print(str1.center(30,'$'))
# i wander how , i wonder why ,yestoday you told me about...

str2="   hello,world"
print(str2,len(str2))
#    hello,world 14

# 右对齐,设置宽度为16，填充字符为’#‘
print(str2.rjust(16,'#'))
# ##   hello,world

# 左对齐，设置宽度为17，填充字符为’*‘
print(str2.ljust(17,'*'))
#    hello,world***


# 零填充右对齐
print(str2.zfill(18))
# 0000   hello,world

# zfill()可以指定填充字符吗？
# print(str2.zfill(18,'@'))
'''
    print(str2.zfill(18,'@'))
TypeError: str.zfill() takes exactly one argument (2 given) <--很明显，不能指定
'''