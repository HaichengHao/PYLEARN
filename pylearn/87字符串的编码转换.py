# editor 百年
# date: 2024/1/8 20:36
'''
编码：将字符串转换为二进制数据 gbk(一个中文俩字节) utf-8(一个中文占三个字节)
解码：将二进制数据转化为字符串
'''
s1='海内存知己'

# 编码
print(s1.encode(encoding='GBK'))
# b'\xba\xa3\xc4\xda\xb4\xe6\xd6\xaa\xbc\xba'
# 一个汉字占两个字节，前面的b代表转化成二进制
print(s1.encode(encoding='utf-8'))
# b'\xe6\xb5\xb7\xe5\x86\x85\xe5\xad\x98\xe7\x9f\xa5\xe5\xb7\xb1'

#解码
byte_data=s1.encode(encoding='gbk')
print(byte_data.decode(encoding='gbk'))
# 海内存知己
# 注意，解码要用编码的encoding，不能乱用，例如解码gbk格式不能用utf-8格式