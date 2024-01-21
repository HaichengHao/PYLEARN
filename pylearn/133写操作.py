# editor: 百年
# time: 2024/1/21 11:51
# fp=open('D:/PYWORK/pylearn/demo133_write.txt','w+',encoding='GBK')
# fp.write('不过是梦一场')
# fp.close()

'''
fp.write操作可以写入列表等可写文件'''
# 先读取一下
'''rfp=open('D:/PYWORK/pylearn/demo133_write.txt','r')
print(rfp.readline())
rfp.close()'''
# 不过是梦一场

#利用w模式,再次操作，观察变化
'''fp=open('D:/PYWORK/pylearn/demo133_write.txt','w',encoding='GBK')
fp.write('什么？你说什么？')
fp.close()'''

# 再次读取，观察变化
'''rfp=open('D:/PYWORK/pylearn/demo133_write.txt','r')
print(rfp.readline())
rfp.close()'''
# 什么？你说什么？ <--发现文件被覆写，原来的那句话没了


# 利用a+模式，默认指针指向最后一位，不会删除已有的内容,注意'+'不能单独使用
'''fp=open('D:/PYWORK/pylearn/demo133_write.txt','a+')
fp.write('haha')
fp.close()
'''
# 读取，观察变化
rfp=open('D:/PYWORK/pylearn/demo133_write.txt','r')
print(rfp.readline())
rfp.close()
# 什么？你说什么？haha <--发现旧的文本没有被删除，未覆写，而是新增了’haha'



# 发现文件被覆写，之前存在的文本被抹除，新的文件出现