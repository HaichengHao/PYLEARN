# editor 百年
# date: 2023/12/31 17:08
# 列表对象的创建
# 列表需要使用中括号[],元素之间使用英文的逗号进行分隔
# 列表的创建方式
# 使用中括号
# 使用内置函数list()
# 元素之间使用逗号分隔
# 创建列表的第一种方式，使用中括号[]
lst=['hello','world',98]
print(lst)
# ['hello', 'world', 98]
# 第二种方式，使用内置函数list()
lst2=list(['hello','world',98])
# 按索引输出，从0开始
print(lst[0])
# hello
#从后往前是负数索引
print(lst[-1])
# 98
print(lst[-3],lst[0])
# hello hello