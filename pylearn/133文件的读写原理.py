# editor 百年
# date: 2024/1/19 20:52
'''
文件的读写原理
文件的读写俗称"IO操作"
文件读写操作流程
Python操作文件->打开或新建文件->读、写文件->关闭资源

操作原理
.py文件通过解释器将python语言转化为OS"听"得懂的语言然后操作硬盘，进行读写操作
'''
'''
关于’读‘和‘写’
从外存到内存称为读，从内存到外存叫写
'''

'''
文件的读写操作

python程序通过内置函数open()创建文件对象（此对象映射磁盘上的真实文件）来进行文件操作
通过IO将磁盘文件中的内容与程序中的对象中的内容进行同步

语法规则
创建的文件对象名=open(文件名，模式，编码格式，行操作)
file = open(filename,mode[,encoding,newline])

'''
# 示例
lst1=['h','e','l','l','o','中国']
fp=open('D:/PYWORK/pylearn/demo133.txt',mode='a+',encoding='GBK')
for items in lst1:
    fp.write(items)
fp.close()

# hellohello�й� <--如果输入中文不设置编码格式，则会出现乱码，所以要指定为gbk