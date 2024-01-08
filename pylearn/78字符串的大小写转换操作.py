# editor 百年
# date: 2024/1/7 9:31
'''
字符串的大小写转化操作
1 .upper() 将指定字符串中出现的英文字母全转化为大写
2 .lower() 将指定字符串中出现的英文字母全转化为小写
3 .swapcase() 把大写转化为小写，小写转化为大写
4 .capitalize() 首字符大写，其余小写
5 .title() 把单词的第一个字母大写，其余字母小写
'''

str1='''The wind and the sun were disputing who was the stronger.

　　Suddenly they saw a traveler coming down the road. The sun said, "Whoever can make the traveler take off his coat will be the stronger."

　　So the sun hid behind a cloud, and the wind began to blow as hard as it could. As the wind blew harder, the traveler wrapped his coat more closely around himself.

　　Then the sun came out. He shone on the traveler. The traveler soon felt quite hot, and took off his coat.'''
str2='heLLo,WoRlD'
print(id(str1),id(str2))
print(str1.upper(),id(str1.upper()))
print(str2.upper(),id(str2.upper()))
'''
1936187642720 1936186137904
THE WIND AND THE SUN WERE DISPUTING WHO WAS THE STRONGER.

　　SUDDENLY THEY SAW A TRAVELER COMING DOWN THE ROAD. THE SUN SAID, "WHOEVER CAN MAKE THE TRAVELER TAKE OFF HIS COAT WILL BE THE STRONGER."

　　SO THE SUN HID BEHIND A CLOUD, AND THE WIND BEGAN TO BLOW AS HARD AS IT COULD. AS THE WIND BLEW HARDER, THE TRAVELER WRAPPED HIS COAT MORE CLOSELY AROUND HIMSELF.

　　THEN THE SUN CAME OUT. HE SHONE ON THE TRAVELER. THE TRAVELER SOON FELT QUITE HOT, AND TOOK OFF HIS COAT. 1936179232832<--str1标识改变
HELLO,WORLD 1936186137328 <--str2标识改变
'''
# 错误示例:
'''
str1.upper()
print(str1)

这样看似是对的，但是.upper()操作会产生新的字符串，旧的字符串并未发生改变，还是旧的字符串，打印输出的依然是旧的串'''

# 小写操作.lower()
print(str2.lower(),id(str2.lower()))
# hello,world 1651672338544 <--也是产生新的串

# 大小写转化.swapcase()操作
print(str2.swapcase(),id(str2.swapcase()))
# HEllO,wOrLd 1885865892656 <--产生新的串

# 整个串的首字符大写，其余小写 .capitalize()
print(str2.capitalize(),id(str2.capitalize()))
# Hello,world 2142690594928 <--产生新的串

# 每个单词的首字符大写，其余字符转化为小写 .title()
print(str2.title(),id(str2.title()))
# Hello,World 1478372023088

