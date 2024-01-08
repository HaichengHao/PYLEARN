# editor 百年
# date: 2024/1/1 14:01
# 语法格式
# 列表名[start:stop:step]
# 切片操作
# 切片的结果是原列表的一个拷贝，切片的范围为start到stop（不包含stop）
lst=['hello','world','hi','China']
# print(lst[1:4])
# ['world', 'hi', 'China']
# print(lst[0:4:2])
# ['hello', 'hi']

print(id(lst))
lst2=lst[1:4]
# 步长不写也代表为1--> lst[1:4:]
print(id(lst2))
# 3110169236544
# 3110172165888

lst3=[0,1,2,3,4,5,6,7,8,9,10]
print(lst3[0:9:3])
# [0, 3, 6]

# 如果不写start,则默认按从索引为0开始
print(lst3[:4])
# [0, 1, 2, 3]
# 如果不写stop,则默认从start到最后
print(lst3[0:])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 如果不写start和stop,则默认整个列表
print(lst3[:])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 如果只写step,则只按step来
print(lst3[::3])
# [0, 3, 6, 9]

# 步长若为负数，则默认start为倒数第一个元素，stop为第一个元素
print(lst3[::-3])
# [10, 7, 4, 1]
# 利用负数步长，可以实现倒序输出
print(lst3[::-1])
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


print(lst3[7::-1])
# [7, 6, 5, 4, 3, 2, 1, 0]

print(lst3[5::-1])
# [5, 4, 3, 2, 1, 0]

print(lst3[::-2])
# [10, 8, 6, 4, 2, 0]

print(lst3[6:0:-2]) #<--注意不包含stop
# [6, 4, 2]