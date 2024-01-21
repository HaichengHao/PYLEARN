# editor: 百年
# time: 2024/1/21 16:34
fp=open('D:/PYWORK/pylearn/demo135_2.txt','a+')
fp.write('lovegithub')
# 这里我们直接利用flush将资源写入到文件中
fp.flush()
# 之后查看利用flush是不是真的把'lovegithub'写入了文件
rfp=open('D:/PYWORK/pylearn/demo135_2.txt','r')
print(rfp.read())
# lovegithub <--输出结果表面在fp没有关闭的情况下'lovegithub'已经被写入到文件当中了
rfp.close()
fp.close()

# 注意顺序，文件一旦关闭就无法再进行读写操作了