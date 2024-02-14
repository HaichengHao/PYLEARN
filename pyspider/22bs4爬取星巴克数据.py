# editor: 百年
# time: 2024/2/8 16:57
import bs4
import urllib.request
url='https://www.4008123123.com/phhs_ios/Drink.htm'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)
soup=bs4.BeautifulSoup(content,'lxml')
# bev_info_lst=soup.find_all('div',class_='title')
# product=bev_info_lst.__str__()
# print(product)
# print(bev_info_lst)
info_lst=soup.select('div[class="title"]')
# print(info_lst)
for info in info_lst:
    print(info.get_text())