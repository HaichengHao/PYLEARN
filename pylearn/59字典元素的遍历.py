# editor 百年
# date: 2024/1/3 10:50
# 字典元素的遍历
dic1={'张三':12,'李四':17,'王五':12}
# for item in dic1:
#     print(item)
    # 张三
    # 李四
    # 王五
    # 获取的实际上是字典的键，注意区分，最好写成key，这样方便理解


# []取值法
# 例如: dic['张三']
#
# get()取值法
# 例如: dic.get('张三')

#[]取值法
# for item in dic1:
#     print(item,dic1[item])
#  张三 12
# 李四 17
# 王五 12

# .get()取值法,这里把item写为key方便理解记忆
for key in dic1:
    print(key,dic1.get(key))
    # 张三 12
    # 李四 17
    # 王五 12