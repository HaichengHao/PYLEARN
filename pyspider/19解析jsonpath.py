# editor: 百年
# time: 2024/2/6 9:44
# 语法格式
'''
target_file=json.load(xxx.json)
info_lst=jsonpath.jsonpath(obj=target_file,expr='jsonpath语法')
'''
import json

import jsonpath

# 指定要操作的xxx.json文件
obj=json.load(open('./store.json','r',encoding='utf-8'))

# 访问所有book的author节点
author_lst=jsonpath.jsonpath(obj=obj,expr='$.store.book[*].author')
print(author_lst)
# ['六道', '天蚕土豆', '唐家三少', '南派三叔']

# 访问所有author节点
author_all=jsonpath.jsonpath(obj=obj,expr='$..author')
print(author_all)
# ['六道', '天蚕土豆', '唐家三少', '南派三叔']

# store下的所有节点，book数组和bicycle节点
book_bicycle=jsonpath.jsonpath(obj=obj,expr='$.store.*')
print(book_bicycle)
# [[{'category': '修真', 'author': '六道', 'title': '坏蛋是怎样练成的', 'price': 8.95}, {'category': '修改', 'author': '天蚕土豆', 'title': '斗破苍穹', 'price': 12.99}, {'category': '修真', 'author': '唐家三少', 'title': '斗罗大陆', 'isbn': '0-553-21311-3', 'price': 8.99}, {'category': '修真', 'author': '南派三叔', 'title': '星辰变', 'isbn': '0-395-19395-8', 'price': 22.99}], {'color': '黑色', 'price': 19.95}]

# 匹配第三个book节点,索引为2
book_3th=jsonpath.jsonpath(obj=obj,expr='$.store.book[2]')
# 其它写法
# book_3th=jsonpath.jsonpath(obj=obj,expr='$..book[2]')
print(book_3th)
# [{'category': '修真', 'author': '唐家三少', 'title': '斗罗大陆', 'isbn': '0-553-21311-3', 'price': 8.99}]


# 匹配倒数第一个book节点 利用下标运算符[]
# book_last=jsonpath.jsonpath(obj=obj,expr='$..book[(@.length-1)]')
# 另一种写法,利用切片操作
book_last=jsonpath.jsonpath(obj=obj,expr='$..book[-1:]')
print(book_last)

# 匹配前两个book节点 利用切片操作，类似列表的切片
first_2=jsonpath.jsonpath(obj=obj,expr='$..book[:2]')
print(first_2)

# 条件过滤需要在（）前面加一个?
# 过滤含有isbn字段的节点
fter=jsonpath.jsonpath(obj=obj,expr='$..book[?(@.isbn)]')
print(fter)
# [{'category': '修真', 'author': '唐家三少', 'title': '斗罗大陆', 'isbn': '0-553-21311-3', 'price': 8.99}, {'category': '修真', 'author': '南派三叔', 'title': '星辰变', 'isbn': '0-395-19395-8', 'price': 22.99}]


# 哪本书超过了10块钱
book_lst=jsonpath.jsonpath(obj=obj,expr='$..book[?(@.price<10)]')
print(book_lst)