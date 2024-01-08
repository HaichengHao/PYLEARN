# editor 百年
# date: 2024/1/6 15:44
'''
字符串的相关操作
1字符串的驻留机制
2字符串的常用操作
3字符串的比较
4字符串的切片操作
5格式化字符串
6字符串的编码转换
'''
# 字符串是什么
# 是python中的基本数据类型，是不可变序列

# 何为字符串驻留机制
'''
仅保存一份相同且不可变的字符串的方法，不同的值被存放在字符串的驻留池中，python的驻留机制对相同的
字符串只留一份拷贝，后续创建相同字符串时，不会开辟新空间，而是把该字符串的地址赋给新创建的变量
'''
st1='hello world'
st2="hello world"
st3='''hello world'''
print(st1,st2,st3)
print(id(st1),id(st2),id(st3))
# hello world hello world hello world
# 1974367233648 1974367233648 1974367233648

# 发现三个字符串内存地址相同


# 字符串的驻留机制
'''
驻留机制的几种情况(交互模式cmd)
字符串长度为0或为1时
符合标识符的字符串
字符串只在编译时进行驻留，而非运行时驻留
[-5,256]之间的整数数字'''


# 字符串长度为0或为1时
# 符合标识符的字符串
'''
>>> s1=''
>>> s2=''
>>> s1 is s2
True
>>> s1='%'
>>> s2='%'
>>> s1 is s2
True
>>> s1 ='abc%'
>>> s2 ='abc%'
>>> s1 == s2
True
>>> s1 is s2
False
>>> id(s1)
1992664613616
>>> id(s2)
1992664625392
>>> s1='abcx'
>>> s2='abcx'
>>> s1 is s2
True
>>> id(s1)
1992664662448
>>> id(s2)
1992664662448
>>>'''

#字符串只在编译时进行驻留，而非运行时驻留
'''
>>> a='abc'
>>> b='ab'+'c' <--编译时就已经进行了拼接产生了驻留
>>> c=''.join(['ab','c']) <--在运行时开辟了新的空间
>>> a is b
True
>>> a is c
False
>>> c
'abc'
>>> type(c)
<class 'str'>
>>> a
'abc'
>>> type(a)
<class 'str'>
'''
# [-5,256]之间的整数数字
'''
>>> a=-5
>>> b=-5
>>> a is b
True
>>> a=-6
>>> b=-6
>>> a is b
False
>>>


'''



'''
sys 中的.intern()方法强制2个字符串指向同一对象
PyCharm对字符串进行了优化处理'''

'''
>>> import sys
>>> a='abc%'
>>> b='abc%'
>>> a is b
False
>>> a=sys.intern(b) <--利用sys.intern(b)可以强制将其转化
>>> a is b
True
>>>
'''

'''
字符串驻留机制的优缺点
当需要值相同的字符串时，可以直接从字符串池里拿来使用，
避免频繁的创建和销毁，提升效率和节约内存，因此拼接字符串和修改字符串是会比较影响性能的

在需要进行字符串拼接时建议使用str类型的.join()方法,而非+拼接字符串，因为.join()方法是先计算所有字符
中的长度，然后再拷贝，只new一次对象，效率要比+效率高'''

