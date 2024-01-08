# editor 百年
# date: 2023/12/28 18:56
# float()数据类型转换
# 文字类无法转换成浮点型
# 整数类转化成浮点型会在后边加上’.0‘
s1='128'
f1=97.77
s2='76.9'
ff=False
s3='hello'
print(float(s1))
print(float(f1))
print(float(ff))
print(float(s3))
# ValueError: could not convert string to float: 'hello'
# 可以看到，字符串类型确实不能转换成浮点型，但数字串可以