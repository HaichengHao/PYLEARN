# editor: 百年
# time: 2024/1/21 11:27
# 创建文件对象
fp=open('D:/PYWORK/pylearn/demo133.txt',mode='r')
# 读取内容，按行读并输出
print(fp.readlines())
# 关闭文件
fp.close()
# hellohello中国hello中国hello中国hello中国

# 关于readlines,我们可以在demo133.txt中新增一行内容，观察变化
# 新增后重读
# ['hellohello中国hello中国hello中国hello中国\n', 'hellogithub']
# 发现readlines()可以读取多行，且读出的内容输出为列表
# 如果写为readline()则只读第一行，直接输出内容