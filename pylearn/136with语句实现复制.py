# editor: 百年
# time: 2024/1/22 19:58
with open('D:/PYWORK/pylearn/121其它字符.png','rb') as source_file:
    with open('D:/PYWORK/pylearn/136copy.png','wb') as target_file:
        target_file.write(source_file.read())

        # 与133复制图片操作最大的区别就是利用上下文管理器省去了文件关闭的过程