# editor 百年
# date: 2023/12/30 9:38
# date:  '2023/12/27',
# 代理池配置
print('Copyright By 百年，转载请声明，侵权必究')
proxies_pool=[
    {'http':'114.233.71.160:9000'},
    {'http':'111.225.153.132:8089'},
    {'http':'180.105.117.139:8089'},
    {'http':'111.225.152.68:8089'},
    {'http':'36.138.56.214:3128'},
    {'http':'175.100.72.95:57938'},
    {'http':'198.199.74.99:59166'},
    {'http':'176.100.216.154:8087'},
    {'http':'4.16.68.158:443'},
    {'http':'161.35.70.249:8080'},
]
# 导入需要的库
from  lxml import etree
import urllib.request
import urllib.parse
import random
proxies=random.choice(proxies_pool)
print('演示：https://movie.douban.com/subject/36188869/comments\n'
      '其中 \'comments\'前面的即为电影编号，不用记忆，\n只需要在豆瓣电影网里找到你要爬取的电影即可知道这个编号，它是唯一的')
# 定义要爬取的页面
movieid=input('请输入你要爬取电影的编号:')
def creat_request(page):
    base_url = 'https://movie.douban.com/subject/'+str(movieid)+'/comments?'
    # base_url='https://movie.douban.com/subject/35267208/comments?' #这里用的流浪地球2的评论
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.56'

    }
    data={
        'start':(page-1)*20,
        'limit':'500',
        'status':'P',
        'sort':'new_score',
    }
    data=urllib.parse.urlencode(data)#<--get请求之后不需要再加encode()方法
    url=base_url+data
    request=urllib.request.Request(url=url,headers=headers)#get请求这里不写data
    return request

def get_content(request):
    handller = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handller)
    response = opener.open(request)
    tree=etree.HTML(response.read().decode('utf-8'))
    result=tree.xpath('//span[@class="short"]/text()')
    return result


def down_load(page,result):
    # fp=open('./realdata.csv','a+',encoding='utf-8',newline='')#文件替换成自己电脑里的路径
    # # fp=open('D:/pylearnV1.0/新链家/cdljdata.csv','a+',encoding='utf-8',newline='')
    # writer=csv.writer(fp)
    with open('./douban'+str(page)+'.txt','a+',encoding='utf-8') as file:
        file.write(str(result))
        print('第'+str(page)+'页爬取结束')
# 主程序运行
if __name__ == '__main__':
    start_page=int(input('请输入起始的页码:'))
    end_page=int(input('请输入结束的页码:'))
    for page in range(start_page,end_page+1):
        request=creat_request(page)# 调用creat_request()方法，每一页都有自己请求对象的定制
        content = get_content(request)#调用get_content方法，获取响应数据
        down_load(page,content)

