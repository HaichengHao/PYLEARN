# editor: 百年
# time: 2024/2/3 16:35
# post请求
'''
注意与get请求进行区分，不再是get类型的爬虫
'''
import urllib.request
import urllib.parse
base_url='https://fanyi.baidu.com/sug'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
data={
    'kw':'spider'
}
# post请求的参数必须要进行编码，即urllib.parse.urlencode()方法，但post请求需要两次编码即urlencode之后还有encode()
encode_data=urllib.parse.urlencode(data).encode('utf-8')
# url=base_url+encode_data
# post请求的参数是不会拼接在url的后面的，而是需要放在请求对象定制的参数中(与get请求不一样的地方)
# post请求的参数必须进行编码，即再利用urlencode()之后再进行.encode编码,否则会报错，

# 构造请求头
request=urllib.request.Request(url=base_url,data=encode_data,headers=headers)

# 接收响应内容
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
# 打印内容
print(content)
# {"errno":0,"data":[{"k":"spider","v":"n. \u8718\u86db; \u661f\u5f62\u8f6e\uff0c\u5341\u5b57\u53c9; \u5e26\u67c4\u4e09\u811a\u5e73\u5e95\u9505; \u4e09\u811a\u67b6"},{"k":"Spider","v":"[\u7535\u5f71]\u8718\u86db"},{"k":"SPIDER","v":"abbr. SEMATECH process induced damage effect revea"},{"k":"spiders","v":"n. \u8718\u86db( spider\u7684\u540d\u8bcd\u590d\u6570 )"},{"k":"spidery","v":"adj. \u50cf\u8718\u86db\u817f\u4e00\u822c\u7ec6\u957f\u7684; \u8c61\u8718\u86db\u7f51\u7684\uff0c\u5341\u5206\u7cbe\u81f4\u7684"}],"logid":3332165045}
# 可见是一个json对象
# 打印内容类型
print(type(content))
# <class 'str'>

# 利用类型转换，将字符串类型转化为json类型
import json #导入json模块
# 利用loads()方法将json对象content转化为我们可以理解的类型
obj=json.loads(content)
print(obj)
# {'errno': 0, 'data': [{'k': 'spider', 'v': 'n. 蜘蛛; 星形轮，十字叉; 带柄三脚平底锅; 三脚架'}, {'k': 'Spider', 'v': '[电影]蜘蛛'}, {'k': 'SPIDER', 'v': 'abbr. SEMATECH process induced damage effect revea'}, {'k': 'spiders', 'v': 'n. 蜘蛛( spider的名词复数 )'}, {'k': 'spidery', 'v': 'adj. 像蜘蛛腿一般细长的; 象蜘蛛网的，十分精致的'}], 'logid': 3507673835}



'''
总结
1.post请求的参数必须编码，编码之后，仍需调用encode()方法，encode_data=urllib.parse.urlencode(data).encode('utf-8')
2.参数是放在请求对象定制的方法中 request=urllib.request.Request(url=base_url,data=encode_data,headers=headers)
3.编码之后必须调用encode()'''