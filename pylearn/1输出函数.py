# editor  百年
# date: 2023/12/28 15:42
# 可以打印数字
print(520)
# 可以打印输出字符串
print("hello")
# 可以输出含有运算符的表达式
print(1+1)
# i = input('请输入一个数字')
# 将数据输出到文件当中
# 指定一个变量作为文件
# 如果文件存在就在文件中追加，不存在就创建
fp = open('D:/PYWORK/test.txt','a+')
# fp.write(i)
print('hello',file=fp)
fp.close()

# 不进行换行输出
print('hello','world','python')