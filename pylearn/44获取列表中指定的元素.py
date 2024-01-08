# editor 百年
# date: 2024/1/1 11:33
# 正向索引从0开始 [0,1,...]
# 逆向索引从1开-N到-1 [-n,-n+1,-n+2,...-1]
lst=['hello','world','win98','aloha','haha']
print(lst[2])
# win98
print(lst[-3])
# win98
# win98

# 超出范围便会报错
print(lst[10])
#   File "D:\PYWORK\pylearn\44获取列表中指定的元素.py", line 13, in <module>
#     print(lst[10])
# IndexError: list index out of range