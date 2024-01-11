# editor 百年
# date: 2024/1/11 14:56
'''
BaseException 捕获所有错误类型
try...except...else结构
如果try..except..结构中没有抛出异常，则执行else块，如果try中出现异常，则执行Except块
简单理解try试错，有错则执行except模块，无错则执行else模块
'''
# try:
#     a=int(input("请输入第1个整数"))
#     b=int(input("请输入第2个整数"))
#     result=a/b
# except BaseException as e:
#     print('出错了',e)
# else:
#     print(str(a)+'/'+str(b)+'=',result)

'''
try...except...else...finally
与try...except...else...的不同之处就是finaly无论是否出现异常，都会执行
不受影响'''


try:
    a=int(input("请输入第1个整数"))
    b=int(input("请输入第2个整数"))
    result=a/b
except BaseException as e:
    print('出错了',e)
else:
    print(str(a)+'/'+str(b)+'=',result)
finally:
    print('无论怎样我照执行不误')
'''
请输入第1个整数e
出错了 invalid literal for int() with base 10: 'e'
无论怎样我照执行不误
'''
# 可见finally的块不受任何影响，无论是否出错，照样执行