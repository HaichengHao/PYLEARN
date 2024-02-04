# editor: 百年
# time: 2024/2/2 11:09
'''
使用urllib来获取百度首页的源码
'''
# 导入urllib包的request
import urllib.request

# 定义一个url
base_url='http://www.baidu.com'

# 模拟浏览器向服务器发送请求

# 定义变量response接收浏览器返回的数据
response=urllib.request.urlopen(base_url)

# 获取响应中的页面的源码
# 注意.read()返回的是字节形式的数据
# 我们要将二进制的数据转换为字符串
# 二进制-->字符串 为解码 ，利用.decode('编码格式')
bytes_content=response.read()
content=bytes_content.decode('utf-8')
# 输出查看
print(content)
