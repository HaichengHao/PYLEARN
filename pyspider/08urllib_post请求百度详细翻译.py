# editor: 百年
# time: 2024/2/3 18:53
import urllib.request
import urllib.parse
# 要发去请求的链接
base_url='https://fanyi.baidu.com/v2transapi?'
#模拟浏览器
headers = {
    'Cookie': 'REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=0hETn5PM0liUFhWbVlyaElZUjVFeTlMZmdqUGFQY3oxQVRRcTJDMTZ1QUlmWk5sRVFBQUFBJCQAAAAAAAAAAAEAAABM~SP2zNLPwvXobwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjwa2UI8GtlZ; BDUSS_BFESS=0hETn5PM0liUFhWbVlyaElZUjVFeTlMZmdqUGFQY3oxQVRRcTJDMTZ1QUlmWk5sRVFBQUFBJCQAAAAAAAAAAAEAAABM~SP2zNLPwvXobwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjwa2UI8GtlZ; PSTM=1706843334; BIDUPSID=F2BDCD40C8DDDC65B56CC32AD1D160A6; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=E2F8DB8F78AF62593D904035D2A2BC54:FG=1; H_PS_PSSID=40202_40079_40206_40211_40222; BAIDUID_BFESS=E2F8DB8F78AF62593D904035D2A2BC54:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1706949510; APPGUIDE_10_6_9=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1706957804; ab_sr=1.0.1_ZjY2N2VlNWM1ZjFiMzlhYmI5OGNhMDZlYWYzNGZlMzE1OWQ4MTU0Y2VmZTYzMjUxYWNjNDdmZjJlOWQ0NDRmN2NjMDBlOTk4ZDcyYzU0ZTQ0NDNjNDg3YjY4ODIwZDMxY2JhZTQzMjczZGI1Y2E0ZjBiMjg5YWJmZTNmZmJkOTY0NGUyMzljZThlYzMzMzg4NmEzZjUyYmExMjRiNzc0Zjg4ODRiZWFjOTJlZTI2NTViOTJhYjJlN2UyNzJmOTgx'
}
# 构造请求
data={
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': '95ab86b2b50e41ef4e461f9b29d52059',
    'domain': 'common',

}
# 将data进行编码,注意是post请求是二次编码，即urlencode().encode()
encode_data=urllib.parse.urlencode(data).encode('utf-8')
# 请求对象定制
request=urllib.request.Request(url=base_url,data=encode_data,headers=headers)

# 获取响应数据
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)
# {"errno":997,"errmsg":"\u672a\u77e5\u9519\u8bef","logid":689182079,"query":"love","from":"en","to":"zh","error":997}
# 可见又是json类型

# 导入json模块
import json
content_json=json.loads(content)
print(content_json)