# editor: 百年
# time: 2024/1/21 13:27
'''
利用文件的读写操作实现对图片的复制操作
'''
source_file=open('D:/PYWORK/pylearn/121其它字符.png','rb')
target_file=open('D:/PYWORK/pylearn/121其它字符_copy.png','wb')
# 边读边写，把读取的source_file写入到target_file当中去
# 让target_file写入source_file读取的内容
target_file.write(source_file.read())

# 关闭文件
source_file.close()
target_file.close()