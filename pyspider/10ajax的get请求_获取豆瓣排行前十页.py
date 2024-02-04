# editor: 百年
# time: 2024/2/3 20:47
'''
# 版本1
import urllib.request
import urllib.parse
base_url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start='
# start=0&limit=20,观察发现每页+20
# start=20&limit=20
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
page_num=int(input('输入要爬取的页数(每页20部):'))
rel_num=(page_num-1)*20+1
for i in range(0,rel_num,20):
    url=base_url+str(i)+'&limit=20'
    print(url)
    # 构造请求
    request=urllib.request.Request(url=url,headers=headers)
    # 获取响应
    response=urllib.request.urlopen(request)
    # 获取内容
    content=response.read().decode('utf-8')
    with open('./douban_new.json','a+',encoding='utf-8') as wfp:
        wfp.write(content)
'''
import urllib.request
import urllib.parse
# base_url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start='
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


def create_request(page):
    base_url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action='
    data={
        'start':(page-1)*20,
        'limit':20
    }
    encode_data=urllib.parse.urlencode(data)#注意，get请求不需要二次encode
    url=base_url+'&'+encode_data
    request=urllib.request.Request(url=url,headers=headers)
    return request #注意，有Return一定要有接收对象

'''
不分页保存（保存为一个文件）
def save_data(data):
    with open('./rank_movie.json','a+',encoding='utf-8') as wfp:
        wfp.write(data)
'''


def save_data(data,page):
    with open('./rank_movie'+str(page)+'.json','a+',encoding='utf-8') as wfp:
        wfp.write(data)

def get_content(request):
    # request = urllib.request.Request(url=url, headers=headers)
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content
    # save_data(content)



if __name__ == '__main__':
    start_page=int(input('输入起始页:'))
    end_page=int(input('输入终止页:'))
    for page in range(start_page,end_page+1):
        # 请求对象的定制
        request=create_request(page)
        # 获取响应的数据
        content=get_content(request)
        #保存数据
        save_data(content,page) #如果不分页保存就把page去掉




