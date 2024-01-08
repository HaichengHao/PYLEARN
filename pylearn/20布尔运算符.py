# editor 百年
# date: 2023/12/30 13:26
# 布尔运算符
a,b=1,2
print(a==1 and b==2) #True True and True --> True
print(a==1 and b<2) #False True and False -->False
print(a!=1 and b==2) #False and True -->False
print(a!=1 and b!=2) #False and False -->False

# or
print(a==1 or b==2)#False or True -->True
print(a==2 or b==1) #False or False -->False
print(a!=1 or b==2) #False or True -->True
print(a!=1 or b!=2) #False or False -->False

# in not in
str1='hello world'
print('w' in str1)
# True
print('k' in str1)
print('k' not in str1)
# False
# True