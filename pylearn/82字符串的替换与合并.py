# editor 百年
# date: 2024/1/8 10:34
'''
字符串的替换与合并
利用.replace(oldstr:  ,newstr: [,count=])方法替换字符串，其中第一个参数表示要替换的旧字符串，第二个表示指定的新字符串，第三个参数数表示最大替换次数，不指定则默认1次
利用 str.join()方法合并字符串，例如'.'.join('ab','cd','pq') 结果为'ab.cd.pq'
'''

s1='hello,world'
# s1.replace('world','python')
# print(s1)
# hello,world <--依旧是那个问题，旧的字符串并未改变，而是产生了新的字符串

# print(id(s1),id(s1.replace('world','python')))
# 2078811039024 2078811082864 <--地址标识不一样

s2=s1.replace('world','python')
print(s2)
# hello,python

s3='hello,hello,world,world,world'
s4=s3.replace('hello','hi',2)
print(s4)
# hi,hi,world,world,world
s5=s3.replace('world','python',2)
print(s5)
# hello,hello,python,python,world

lst=['hello','world','hi','python']
print('|'.join(lst))
print(''.join(lst))
# hello|world|hi|python
# helloworldhipython

t=('hello','world','python')
print(''.join(t))
# helloworldpython
print('*'.join(t))
# hello*world*python

print('%'.join('hello'))
# h%e%l%l%o

print(' '.join(t))
# hello world python


