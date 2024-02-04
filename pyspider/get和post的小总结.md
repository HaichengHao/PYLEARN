| 方法                       | GET                                                                              | POST |
| ---------------------------- | ---------------------------------------------------------------------------------- | ------ |
| 构造请求头(如果有多个参数) | 需要对参数进行编码利用urlencode()<br />将汉字转化为unicode编码，并将链接进行拼接 |    需要对参数进行编码（二次编码），即urlencode().encode()  |
|                参数位置            |  不需要写入到请求对象定制内                                                                                | 需要写入到请求对象定制的关键字参数     |

### 实例(GET)
```python
# 多个参数
data={
    'q':'周杰伦'
}
# 利用urllib.parse.urlencode()方法来把汉字转化为unicode编码
encode_data=urllib.parse.urlencode(data)
base_url='https://cn.bing.com/search?'
url=base_url+encode_data
# 构造请求头
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
# 请求对象定制
request=urllib.request.Request(url=url,headers=headers)
# 获取响应的内容
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)
```
### 实例(POST) 
```python
data={
    'kw':'spider'
}
# post请求的参数必须要进行编码，即urllib.parse.urlencode()方法，但post请求需要两次编码即urlencode之后还有encode()
encode_data=urllib.parse.urlencode(data).encode('utf-8')
# post请求的参数是不会拼接在url的后面的，而是需要放在请求对象定制的参数中(与get请求不一样的地方)
# post请求的参数必须进行编码，即再利用urlencode()之后再进行.encode编码,否则会报错，

# 构造请求头
request=urllib.request.Request(url=base_url,data=encode_data,headers=headers)

```

