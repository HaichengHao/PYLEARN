# editor: 百年
# time: 2024/2/15 10:23
'''
chrome-headless模式，谷歌针对Chrome浏览器增加的一种模式，
可以在不打开ui界面的情况下使用Chrome浏览器，所以运行效果与
chrome基本一致
'''
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# # 设置配置参数
# chrome_options=Options()
# chrome_options.add_argument('--headless') #无头模式
# chrome_options.add_argument('--disable-gpu')#禁用gpu,无界面
# # 配置自己chrome浏览器的路径
# path=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# chrome_options.binary_location=path
# # 创建浏览器对象
# browser=webdriver.Chrome(options=chrome_options)
# url='https://www.baidu.com'
# browser.get(url)
# input_zoom=browser.find_element_by_id('kw')
# input_zoom.send_keys('乃木坂46')
# browser.get_screenshot_as_file('./28_1.png')
# bdyx_button=browser.find_element_by_id('su')
# bdyx_button.click()
# time.sleep(3)
# browser.get_screenshot_as_file('./28_2.png')
# browser.quit()
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless') #无头模式
    chrome_options.add_argument('--disable-gpu')#禁用gpu,无界面
    # 配置自己chrome浏览器的路径
    path=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location=path
    # 创建浏览器对象
    browser=webdriver.Chrome(options=chrome_options)
    return browser

browser=share_browser()
url='https://www.baidu.com'
browser.get(url)
input_zoom=browser.find_element_by_id('kw')
input_zoom.send_keys('颛顼')
time.sleep(1)
bdyx_button=browser.find_element_by_id('su')
bdyx_button.click()
time.sleep(2)
browser.get_screenshot_as_file('./kw_zx.png')
time.sleep(3)
browser.quit()
