# editor: 百年
# time: 2024/1/21 17:05
'''
with语句之后as语句之前的称为上下文表达式
with语句（上下文管理器）
with语句可以自动管理上下文资源，不论什么原因跳出with模块，都能确保文件正确地关闭，以此来达到释放资源的目的
例如
with open('D:/PYWORK/pylearn/demo135_2.txt','a+') as src_file:
上下文表达式结果为上下文管理器，同时创建一个运行时上下文，自动调用__enter__()方法，并将返回值赋值给src_file
实现了__enter__()方法和__exit__()方法
遵守了上下文管理协议
离开运行时上下文，自动调用上下文管理器的特殊方法__exit__()

好处：不用非得写close()语句了，也避免了忘记关闭而造成的资源浪费
'''
with open('D:/PYWORK/pylearn/demo136.txt','a+') as fp:
    fp.write('我不过就是个小文件罢了')
