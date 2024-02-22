# editor: 百年
# time: 2024/2/22 9:46
import requests
from lxml import etree
import random
proxies_pool=[
    {'http':'42.63.65.37:80'},
    {'http':'42.63.65.13:80'},
    {'http':'42.63.65.15:80'},
    {'http':'42.63.65.7:80'},
    {'http':'42.63.65.8:80'},
    {'http':'42.63.65.9:80'},
    {'http':'39.173.106.248:80'},
    {'http':'39.173.106.249:80'},
    {'http':'39.173.106.250:80'},
    {'http':'39.173.106.251:80'},
    {'http':'39.173.106.230:80'},
    {'http':'39.173.106.235:80'},
    {'http':'39.173.106.239:80'},
    {'http':'39.173.106.240:80'},
    {'http':'39.173.106.241:80'},
    {'http':'39.173.106.243:80'},
    {'http':'39.173.106.244:80'},
    {'http':'39.173.106.245:80'},
    {'http':'39.173.102.114:80'},
    {'http':'39.173.102.123:80'},
    {'http':'39.173.106.133:80'},
    {'http':'159.226.227.117:80'},
    {'http':'159.226.227.122:80'},
    {'http':'159.226.227.120:80'},
    {'http':'159.226.227.118:80'},
    {'http':'159.226.227.115:80'},
    {'http':'159.226.227.113:80'},
    {'http':'159.226.227.112:80'},
    {'http':'159.226.227.111:80'},
    {'http':'159.226.227.110:80'},
    {'http':'159.226.227.108:80'},
    {'http':'159.226.227.107:80'},
    {'http':'159.226.227.97:80'},
    {'http':'159.226.227.92:80'},
    {'http':'159.226.227.98:80'},
    {'http':'159.226.227.96:80'},
    {'http':'159.226.227.95:80'},
    {'http':'159.226.227.86:80'},
    {'http':'159.226.227.78:80'},
    {'http':'140.249.88.250:80'},
]
proxies=random.choice(proxies_pool)
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
}
url='https://car.autohome.com.cn/price/brand-15.html'
response=requests.get(url=url,headers=headers,proxies=proxies)
source_html=response.text
tree=etree.HTML(source_html)
auto_type=tree.xpath('//div[@class="main-title"]/a/text()')
img_src=tree.xpath('//div[@class="list-cont-img"]/a/img/@src')
# print(img_src)
file_name=file='./bmw_pic/'
for i in range(0,len(img_src)):
    auto_pic_src='https:'+img_src[i]
    auto_type_name=auto_type[i]
    # print(auto_pic_src)
    pic_response=requests.get(url=auto_pic_src,headers=headers)
    pic_source=pic_response.content
    file_pic=file_name+auto_type_name+'.jpg'
    print(file_pic)
    with open(file_pic,'wb') as wfp:
        wfp.write(pic_source)