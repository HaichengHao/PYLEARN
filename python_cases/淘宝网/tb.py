# editor: 百年
# time: 2024/2/23 15:58
import requests  # 导入第三方库
import re
import os


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)  # timeout超时响应参数，这里是30秒
        r.raise_for_status()  # 判断是否异常，200为正常
        r.encoding = r.apparent_encoding  # 编码方式
        return r.text  # 返回内容
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)  # *？前一个字符0次获无限次扩展，这里是.(任何单个字符)无限扩展，知道 “ 结束
        img = re.findall(r'\"pic_url\"\:\".*?\"', html)
        sal = re.findall(r'\"view_sales\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])  # 使用.split以 : 为界限分割，[1]取分割后的第二部分， eval函数去掉双引号
            title = eval(tlt[i].split(":")[1])
            image = eval(img[i].split(":")[1])
            sales = eval(sal[i].split(":")[1])
            ilt.append([price, title, image, sales])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}\t{:128}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称", "图片链接", "销量"))
    count = 0  # 序号
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1], "http:" + g[2], g[3]))  # "http:" + g[2]  补全图片链接
        root = "/Users/ljf/Desktop/爬虫学习/爬取的图片//"  # 保存图片的根目录（根据个人情况填写）
        path = root + str(count) + ".jpg"  # 图片的名称
        try:
            if not os.path.exists(root):  # 判断文件夹是否存在
                os.mkdir(root)  # 不存在则创建文件夹
            r = requests.get("http:" + g[2])  # 获取图片的内容
            with open(path, 'wb') as f:
                f.write(r.content)  # 保存
                f.close()
        except:
            print("爬取失败")
            # print("文件保存成功")
    print("")


def main():
    goods = "笔记本电脑"  # 要搜索的商品名称
    depth = 1  # 页数
    start_url = "https://s.taobao.com/search?q=" + goods  # 接口 + 商品名称
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44 * i)  # 44表示翻页
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                "cookie": "isg=BOnpzZFsrYGGUpH39-VzSEJW-pNDtt3oqodoP4veklAPUg1kyAc4uJmAFHbkUXUg; l=eBNeqQCVju9HU_wsBO5anurza77tWIRcGkPzaNbMiInca1xRwFtBINCCCGCWkdtfgtCbM3-PHw1aeRnw8GUZw2HvCbKrCyConxvO.; tfstk=c7fPB3YsZBjb-jR9ZQOEPvELFpPRaKCG9m8BEt-fa6-Kvuvw7see9TuL1PM8FvC..; mt=ci=1_1; uc1=cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&pas=0&cookie14=Uoe2zXwcputqGQ%3D%3D&cookie21=W5iHLLyFeYZ1WM9hVnmS&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D; enc=9Y%2FMSeHapmbZeG6XlvgC0Oc50OvRn5xdM4NeHN0HYeek34jmgMphPmVwAIcXh0NdbH6PjHVamvYGzLQ4TedObw%3D%3D; JSESSIONID=4E454F22121952F877F6A1410E151A0A; alitrackid=login.taobao.com; lastalitrackid=login.taobao.com; _cc_=VT5L2FSpdA%3D%3D; _l_g_=Ug%3D%3D; _nk_=tb144967843; _tb_token_=3eee331efe136; cookie1=UUtLcQJdn1hJFYRew1usFmKmezYbMs1fAYqooiRlRcI%3D; cookie17=Vy0T4dzZRxBIkw%3D%3D; cookie2=1bf4e35f5ffca24ca53818ddbc8719b6; csg=732c7bb3; dnk=tb144967843; existShop=MTYyMDY1MjA5Ng%3D%3D; lgc=tb144967843; sg=364; sgcookie=E1003%2FUEY9wGmTMDOeZkjQQinX56Zs2O%2FCbD02GdpJBV1ymGeEqBl%2BGdklOQBKGXFkc61ayAW3n66TmMS2jJ3V5i4Q%3D%3D; skt=2efc87efd3d4ad05; t=68244622a071e32615a09150a6129bb6; tracknick=tb144967843; uc3=nk2=F5REOtROM2Cp5EQ%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&id2=Vy0T4dzZRxBIkw%3D%3D&vt3=F8dCuwgsuF2ycxNk97A%3D; uc4=id4=0%40VXqdEk6gqB3vwrSDD4ExDn%2BuTkyu&nk4=0%40FY4PaJQ8hS13HmYHjEKTa3sEipEqVw%3D%3D; unb=4104558176; _samesite_flag_=true; xlly_s=1; cna=bPrhGNbpuEMCAd9oFHI1Y8o4; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156"
            }  # 登陆淘宝后，填写自己浏览器中的cookie，否则会无法爬取
            html = requests.get(url, headers=headers)
            # print(html.text) #打印HTML内容
            parsePage(infoList, html.text)  # 调用函数，提取信息
        except:
            continue
    printGoodsList(infoList)  # 调用函数，输出信息


main()
