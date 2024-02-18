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
ports=tree.xpath('//td[2]/text()')
print(ips)
print(ports)
my_ip=[]
my_port=[]
for i in range(0,len(ips)):
    new_ips=ips[i].replace('\n\t\t\t','').replace('\t\t','')
    new_ports=ports[i].replace('\n\t\t\t','').replace('\t\t','')
    my_ip.append(new_ips)
    my_port.append(new_ports)
print(my_ip,my_port)

my_proxy=[]
for x,y in zip(my_ip,my_port):
    prox_sock='{\''+'http\''+':'+'\''+x+':'+y+'\''+'}'
    my_proxy.append(prox_sock)

print(my_proxy)
for prox in my_proxy:
    print(prox+',')