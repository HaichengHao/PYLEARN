# editor 百年
# date: 2024/1/7 14:52
'''
字符串判断的相关方法
.isidentifier() 判断指定的字符串是不是合法的标识符
.isspace() 判断指定的字符串是否全部由空白字符串组成(回车、换行、水平制表符)
.isalpha() 判断指定的字符串是否全部由字母组成
.isdecimal() 判断指定字符串是否全部由十进制的数字组成
.isnummeric() 判断指定的字符串是否全部由数字组成
.isalnum() 判断指定的字符串是否全部由字母和数字组成
'''


# 合法标识符，字母数字下划线
str1="!!\! hello,earth"
print(str1.isidentifier())
# False
str2="__11hello"  #<--下划线开头，字母数字下划线
print(str2.isidentifier())
# True

str3="1__hello"
print(str3.isidentifier())
# False <--数字开头是不合法的

str4="hello__1"
print(str4.isidentifier())
# True <--字母开头合法的

s1='  '
print(len(s1))
print(s1.isspace())
# 2
# True

s2='\n'
print(s2.isspace(),len(s2))
# True 1 <--换行符也是空白符,同理，如制表符等也是空白符


# 判断字符串是否都是由字母组成.isalpha()
s3='abcdefg'
print(s3.isalpha())
# True

# .isdecimal() 判断指定字符串是否全部由十进制的数字组成,注意罗马数字不是十进制数字
s4='123322'
print(s4.isdecimal())
# True
sr4='ⅨⅨⅣⅣⅢⅢⅡ'
print(sr4.isdecimal())
# False



# .isnummeric() 判断指定的字符串是否全部由数字组成，注意罗马数字是数字
s5='11223344'
print(s5.isnumeric())
# True
sr5='ⅠⅡⅢⅣⅨ'
print(sr5.isnumeric())
# True


# .isalnum() 判断指定的字符串是否全部由字母和数字组成
s6='11aabbq11'
print(s6.isalnum())
# True