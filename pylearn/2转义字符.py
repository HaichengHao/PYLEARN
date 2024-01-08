# editor 百年
# date: 2023/12/28 16:11
# 利用反斜杠加上转义功能的首字母
# 例如\n(new line) \r (return) \b (back) \t(table占四个空格)
print('hello \n world')
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')#return 退格到之前
print('hello\b')#back
print('\\\\')
# \\输出的是双反斜杠
print('老师说:\'大家好\'')
# 老师说:'大家好'
# 原义字符：不希望转义字符起作用，就是在字符串之前加上r
print(r'hello \n world')
# hello \n world
