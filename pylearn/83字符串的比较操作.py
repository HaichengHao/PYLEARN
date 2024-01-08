# editor 百年
# date: 2024/1/8 15:13
'''
字符串的比较操作
运算符: > < = ;>= <= == !=
比较规则：首先比较两个字符串中的第一个字符，如果相同，则继续比较下一个字符，依次比较下去，直到两个字符串中的字符不再相等时，其比较结果就是两个字符串的比较结果，两个字符串中的所有后续字符将不再比较
比较原理：两个字符进行比较时，比较的是其ordinal value(原始值),调用内置函数ord可以得到指定字符的原始值；
与ord对应的是内置函数chr,调用内置函数chr时指定ordinal value可以得到其对应的字符
'''

str1='hello world hello python'
str2='hello world'
print(str2>str1)
# False
print(str1>=str2)
# True

str3='melon'

str4='apple'
print(str3>=str4)
# True

print(ord('m'),ord('a'))
# 109 97

str5='water'
str6='flame'
print(ord('w'),ord('f'))
# 119 102
print(str5>=str6)
# True

chr1='1'
chr2='a'
chr3='A'
print(ord(chr1))
print(ord(chr2))
print(ord(chr3))
# 49
# 97
# 65

print(chr(50))
# 2 ascii码中2的码值为50
print(chr(28023))
# 海


'''
== 与 is的区别，之前已经提到过
==比较的是值，而is判断的是地址标识
例如，小明有一个和小红一样的苹果
但是不能说小明的苹果就是小红的苹果
'''

a='apple'
b='apple'
print(a==b)
print(a is b)
# True
# True
# 为什么会出现这种情况，因为这是pycharm自带的机制
# 实际上在交互模式下会出现字符串的驻留机制
'''
驻留机制的几种情况(交互模式cmd)
字符串长度为0或为1时
符合标识符的字符串
字符串只在编译时进行驻留，而非运行时驻留
[-5,256]之间的整数数字'''
