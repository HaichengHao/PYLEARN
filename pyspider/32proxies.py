from lxml import etree
from bs4 import BeautifulSoup
import requests
import random
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',

}
proxies_pool=[
    {'http':'114.231.42.16	: 8089'},
    {'http':'183.164.242.175: 8089'},
    {'http':'114.231.42.244	: 8089'},
]
proxies=random.choice(proxies_pool)
url='https://www.89ip.cn/index_1.html'
response=requests.get(url=url,headers=headers,proxies=proxies)
content=response.text
tree=etree.HTML(content)
ips=tree.xpath('//td[1]/text()')
print(ips)
soup=BeautifulSoup(content,'lxml')
td=soup.find_all('td')
print(td)
