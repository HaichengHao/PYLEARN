# editor: 百年
# time: 2024/2/6 10:02
# //p/table/tbody/td/code
import csv
import urllib.request
from lxml import etree
url='http://www.cnblogs.com/youring2/p/10942728.html'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
}

request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)
tree=etree.HTML(content)
info_1lst=tree.xpath('//div[1]/table[1]/tbody/tr/td[1]/code/text()')
# info_1lst=info_1lst.append(tree.xpath('//div[1]/table[1]/text'))
info_2lst=tree.xpath('//div[1]/table[1]/tbody/tr/td[2]/code/text()')
info_3lst=tree.xpath('//div[1]/table[1]/tbody/tr/td[3]/text()')
print(len(info_1lst),info_1lst)
print(len(info_2lst),info_2lst)
print(len(info_3lst),info_3lst)
with open('./demo19.csv','a+',encoding='utf-8',newline='') as fp:
    writer=csv.writer(fp)
    for i in range(0,len(info_1lst)):
        infos=[info_1lst[i],info_2lst[i],info_3lst[i]]
        writer.writerow(infos)