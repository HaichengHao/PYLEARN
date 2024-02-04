# editor: 百年
# time: 2024/2/4 14:58
import urllib.request
import urllib.parse
url='https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def create_request(page):
    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': '20'
    }
    encode_data=urllib.parse.urlencode(data).encode('utf-8') #注意post请求需要二次编码
    request=urllib.request.Request(url=url,headers=headers,data=encode_data)
    return request

def create_response(request):
    response=urllib.request.urlopen(request)
    return response

def get_content(response):
    content=response.read().decode('utf-8')
    return content

def save_data(content):
    with open('./KFC_info.json','a+',encoding='utf-8') as wfp:
        wfp.write(content)

if __name__ == '__main__':
    start_page=int(input('请输入起始页:'))
    end_page=int(input('请输入终止页:'))
    for page in range(start_page,end_page+1):
        # 构造请求
        request=create_request(page)
        # 获取响应
        response=create_response(request)
        # 解析内容
        content=get_content(response)
        # 保存为文件
        save_data(content)