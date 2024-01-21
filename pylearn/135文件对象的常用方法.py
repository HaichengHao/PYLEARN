# editor: 百年
# time: 2024/1/21 15:05
# 文件对象的常用方法
'''file=open('D:/PYWORK/pylearn/demo135.txt','a+')
file.write('文件对象的常用方法示例文件')
file.close()'''

rfp=open('D:/PYWORK/pylearn/demo135.txt','r')
# 读取两个字符
# print(rfp.read(2))

# 文件

#读取一行
# print(rfp.readline())
# 文件对象的常用方法示例文件
# 读取第二行
# print(rfp.readlines()[1])
# 我是新的一行，利用我来测试
# rfp.close()


#将字符串内容写入文件
# wfp=open('D:/PYWORK/pylearn/demo135.txt','a')
# wfp.write('我是追加的，不指定newline就不会换行')
# wfp=open('D:/PYWORK/pylearn/demo135.txt','a')
# 利用\n实现换行
# wfp.write('\n我是追加的')
# wfp.close()


# seek操作
# sfp=open('D:/PYWORK/pylearn/demo135.txt','r')
# 寻找，从第二个字节开始
# sfp.seek(2)
# print(sfp.read())
# sfp.close()
'''
件对象的常用方法示例文件
我是新的一行，利用我来测试
我是追加的
'''
# 可以发现，指针从第二个字节开始，一个汉字在utf-8下占两个字节，也就跳过了一个汉字，如果写1就会报错，
# 因为汉字两个字节，不存在跳过半个汉字这样的情况，如果全是英文则不会出错


# tell输出当前指针的位置
tfp=open("D:/PYWORK/pylearn/demo135_2.txt",'r')
tfp.seek(2)
print(tfp.read())
print(tfp.tell())
tfp.close()
'''
llo
5 <--hello 总共是5
'''

# flush是把缓冲区的资源写入，但不关闭文件，而close()则是关闭文件














