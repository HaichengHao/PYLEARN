# editor: 百年
# time: 2024/2/14 23:40
'''
什么是phantomjs?
一个无界面浏览器，支持页面元素查找，js的执行等
由于一些原因，已经寄了

目前使用Chrome headless
'''
import time
from selenium import webdriver
path='phantomjs.exe'
browser=webdriver.PhantomJS(path)
url='https://www.baidu.com'
browser.get(url)
time.sleep(2)
browser.save_screenshot(filename='./demo27.png')
time.sleep(2)

input_zoom=browser.find_element_by_id('kw')
input_zoom.send_keys('翁美玲')
time.sleep(2)
bdyx_button=browser.find_element_by_id('su')
bdyx_button.click()
time.sleep(2)
browser.save_screenshot(filename='./kw_wml.png')
js_command='document.documentElement.scrollTop=100000'
browser.execute_script(js_command)
time.sleep(2)
next_page=browser.find_element_by_css_selector('.n')
next_page.click()
time.sleep(2)
browser.save_screenshot(filename='./2nd_page.png')
time.sleep(2)
browser.quit()


browser.quit()







