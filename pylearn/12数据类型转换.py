# editor 百年
# date: 2023/12/28 18:33
# 数据类型转换，可以转换类型
name='张三'
age=20
print(type(name),type(age))
# print('我叫'+name+'今年'+age+'岁')
# TypeError: can only concatenate str (not "int") to str
# 运行上面的代码会报错，因为age是整数类型，所以需要类型转换
print('我叫'+name+'今年'+str(age)+'岁')
# 我叫张三今年20岁

# 将其它类型转化成str类型
a=100
b=13.5
c=False
print(str(a),str(b),str(c))
print(type(a),type(b),type(c))
print(type(str(a)),type(str(b)),type(str(c)))

# 使用int()将其它类型转化成int类型
s1='128'
f1=97.77
s2='76.9'
ff=False
s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),int(f1),int(s2),int(ff))
# ValueError: invalid literal for int() with base 10: '76.9'
# 类型转换时出错，也就是说int()转换时不能将字符串为小数串的转化成int类型，而显示为整数串的可以转换
# 注意，非数字串不允许转换，并且浮点数串也不能转换