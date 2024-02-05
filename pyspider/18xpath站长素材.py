# editor: 百年
# time: 2024/2/5 17:28
import urllib.request
from lxml import etree

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
}
# 请求对象定制
def create_request(page):
    if page==1:
        url='http://sc.chinaz.com/tupian/fengjing.html'
    else:
        url='http://sc.chinaz.com/tupian/fengjing_'+str(page)+'.html'
    # print(url) 测试
    request=urllib.request.Request(url=url,headers=headers)
    return request

# 响应对象的接收
def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content



# 下载
def down_load(content):
    tree=etree.HTML(content)
    title_lst=tree.xpath('//a[@class="name"]/text()')
    # for title in title_lst:
    #     print(title)
    #     一般涉及到图片的网站都会进行懒加载
    pic_src_lst=tree.xpath('//div[@class="tupian-list com-img-txt-list"]/div[@class="item"]/img/@data-original')
    # for pic_src in pic_src_lst:
    #     print(pic_src)
    # print(len(title_lst),len(pic_src_lst))
    for i in range(len(title_lst)):
        title=title_lst[i]
        src=pic_src_lst[i]
        url='https:'+src
        # print(title,url)
        urllib.request.urlretrieve(url=url,filename='./demopic/'+title+'.jpg')

if __name__ == '__main__':
    start_page=int(input('请输入起始页码:'))
    end_page=int(input('请输入终止页码:'))
    for page in range(start_page,end_page+1):
        # 请求对象的定制
        request=create_request(page)
        # 响应对象的接收
        content=get_content(request)
        # 利用etree解析
        # tree=etree.HTML(content)

        # 下载图片
        down_load(content)