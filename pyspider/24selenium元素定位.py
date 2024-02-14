# editor: 百年
# time: 2024/2/14 10:38
'''
1.find_element_by_id
eg:button = browser.find_element_by_id('su')
2.find_elements_by_name
eg:name = browser.find_element_by_name('wd')
3.find_elements_by_xpath
eg:xpath1 = browser.find_elements_by_xpath('//input[@id="su"]')
4.find_elements_by_tag_name
eg:names = browser.find_elements_by_tag_name('input')
5.find_elements_by_css_selector
eg:my_input = browser.find_elements_by_css_selector('#kw')[0]
6.find_elements_by_link_text
eg:browser.find_element_by_link_text("新闻")
2.Phantomjs
3.Chrome handless
Chrome-headless 模式， Google 针对 Chrome 浏览器 59版 新增加的一种模式，可以让你不打开UI界面的情况下
使用 Chrome 浏览器，所以运行效果与 Chrome 保持完美一致。
eg:browser.find_element_by_link_text("新闻")
'''
import time

from selenium import webdriver
# 指定驱动路径
path='chromedriver.exe'
# 创建浏览器操作对象
browser=webdriver.Chrome(path)

url='https://www.baidu.com'
browser.get(url)


# 根据id找到对象
# 元素定位，获取百度一下按钮
# button=browser.find_element_by_id('su')
# print(button)

# 根据标签属性的属性值来获取对象的
# 获取文本框
# text_input=browser.find_element_by_name('wd')
time.sleep(2)
# 根据xpath路径获取对象
# xpath_demo=browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/a[1]')
# 注意，如果使用的是.find_elements_by_xxxx(),那么返回值将会是一个列表
# print(xpath_demo)

# 根据标签名获取对象
# target_name_demo=browser.find_elements_by_tag_name('input')
# print(target_name_demo)


# 根据css获取对象，即bs4的语法来实现
# css_selector_demo=browser.find_element_by_css_selector('#su')
# print(css_selector_demo)

# 根据link_text查找对象
# link_text_demo=browser.find_element_by_link_text('视频')
# print(link_text_demo)