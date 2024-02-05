# editor: 百年
# time: 2024/2/5 14:29
# 请求对象的定制
# 获取网页源码
# 下载
'''
https://sc.chinaz.com/tupian/fengjing.html
https://sc.chinaz.com/tupian/fengjing_2.html
//div[@class="item masonry-brick"]/img/@src
'''
import urllib.parse
import urllib.request
from lxml import etree
base_url='https://sc.chinaz.com/tupian/fengjing_'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    # 'Cookie':'__bid_n=186977a04ed8f572da4207; FPTOKEN=4bYVFYxnA+TD3mD56oDVNbdkOYL4PIFTKmVNfT6ND/gdDBUh8t8KxIVnNhu5a/rM3nnUWdU4rSfJA+1p33ziduLXJtnfTqlnDhGqWaZYwefw2QkiKD9d7P/CRt0t1QFODJ1VOFjxxbYiL4Iiij9n5S7WYDGTbi1xL4icoi2Ki/0eoJNHVYvuBkYQWAfGGBCXWMcTvisLBXRrTR0Z8A99VHAAs1eqhMiAtntiqwCsuDyN/Dd449BJjFwXDR+PY1ErN1TrCDVqXcOnwdHQe+1T4OKdHXn+9n7VGx3LV0tC4vb9c89+/PAeAqSGousORR0CNrlyegv1D15X8uPTnJA+HyXCvaBQI8rk2hMHk2h/uv4p7lUMAmu7sVxX1C4UAkLn4j8OhX1l+IwtNM4OvJTbgw==|ML6eCDbQt7DlpT968ntidEbS4b1irvKESjd5OaXzMTA=|10|4c6ab5380b589a56dfb6aafc6911257f; qHistory=aHR0cDovL2lwLnRvb2wuY2hpbmF6LmNvbV9JUC9JUHY25p+l6K+i77yM5pyN5Yqh5Zmo5Zyw5Z2A5p+l6K+i; cz_statistics_visitor=1a2797e0-54cd-49f6-0367-a61cf7b81254; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1707114447; _clck=18dui5t%7C2%7Cfj0%7C0%7C1495; _clsk=inr27j%7C1707114447940%7C1%7C1%7Cl.clarity.ms%2Fcollect; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1707114782'
    }
# for i in range(1,3):
#     if i>=2:
#         url=base_url+str(i)+'.html'
#         print(url)
#     else:
#         url='https://sc.chinaz.com/tupian/fengjing.html'
#     request=urllib.request.Request(url=url,headers=headers)
#     response=urllib.request.urlopen(request)
#     content=response.read().decode('utf-8')
#     tree=etree.HTML(content)
#     sub_urls=tree.xpath('//div[@class="item masonry-brick"]/img/@src')
#     print(sub_urls)

def create_request(page):
    if page==1:
        url='https://sc.chinaz.com/tupian/fengjing.html'
    else:
        url=base_url+str(page)+'.html'
    request=urllib.request.Request(url=url,headers=headers)
    return request

def get_response(request):
    response=urllib.request.urlopen(request)
    return response


def get_content(response):
    content=response.read().decode('utf-8')
    return content
def create_tree(content):
    tree=etree.HTML(content)
    return tree

def get_need(tree):
    pic_src=tree.xpath('//div[@class="item masonry-brick"]/img/@src')
    print(pic_src)
    return pic_src

def download_pic(need):
    for item in need:
        relitem='https:'+item
        file_name='D:\PYWORK\pyspider\demopic'+str(need)+".jpg"
        urllib.request.urlretrieve(relitem,file_name)


if __name__ == '__main__':
    start_page=int(input('请输入如起始页:'))
    end_page=int(input('请输入终止页:'))
    for page in range(start_page,end_page+1):
        request=create_request(page)
        response=get_response(request)
        content=get_content(response)
        tree=create_tree(content)
        pic_src=get_need(tree)
        print(pic_src)
        download_pic(pic_src)
