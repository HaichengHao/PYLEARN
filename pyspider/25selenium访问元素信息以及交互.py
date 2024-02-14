# editor: 百年
# time: 2024/2/14 18:42
'''
selenium获取元素信息以及交互
'''
import time

from selenium import webdriver
path='chromedriver.exe'
browser=webdriver.Chrome(path)
url='https://www.baidu.com'
browser.get(url)
time.sleep(2)
input=browser.find_element_by_id('su')
# 获取属性的名字
print(input.get_attribute('class'))
# 获取标签名
print(input.tag_name)
'''
bg s_btn
input
'''
# 获取元素文本
# 注意，元素文本获取的是尖括号之间的内容
a=browser.find_element_by_link_text('新闻')
print(a.text)