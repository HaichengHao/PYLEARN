# editor: 百年
# time: 2024/2/14 18:52
'''
交互
点击 -- .click()
输入 -- .send_keys()
后退 -- .browser.back()
前进 -- .browser.forward()
模拟JS滚动：
    js = 'document.documentElement.scrollTop=100000'
    browser.execute_script(js)  执行js代码
获取网页源码: -- page_source
退出: -- browser.quit()
'''
import time
from selenium import webdriver
path='chromedriver.exe'
browser=webdriver.Chrome(path)
url='https://www.baidu.com'
browser.get(url)
time.sleep(3)

# 获取文本框的对象
input_zoom=browser.find_element_by_id('kw')
# 在文本框中输入周杰伦
input_zoom.send_keys('周杰伦')

time.sleep(2)

button=browser.find_element_by_id('su')
button.click()

time.sleep(2)

# 模拟js滚动,距离顶部100000
js_command_to_bottom='document.documentElement.scrollTop=100000'
browser.execute_script(js_command_to_bottom)
time.sleep(2)

# 点击下一页
# 利用xpath
button_next_page=browser.find_element_by_xpath('//a[@class="n"]')
# 利用bs4
# button_next_page=browser.find_element_by_css_selector('.n')
button_next_page.click()
time.sleep(2)

# 回到上一页
# xpath
# button_forward_page=browser.find_element_by_xpath('//a[@class="n"][1]')
# bs4
# bs4默认是第一个
'''button_forward_page=browser.find_element_by_css_selector('.n')
time.sleep(2)
button_forward_page.click()'''

# 其它语法
time.sleep(3)
# 回到上一页
browser.back()
time.sleep(2)
# 又到下一页
browser.forward()


# 退出
browser.quit()
