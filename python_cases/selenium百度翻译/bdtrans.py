# editor: 百年
# time: 2024/2/16 21:55
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
chrome_options.binary_location=path #指定二进制文件为path
browser=webdriver.Chrome(options=chrome_options)
print('输入汉语将被翻译为英语\n')
s=input('请输入:')
url='https://fanyi.baidu.com/#zh/en/'
browser.get(url)
time.sleep(2)
input_zoom=browser.find_element_by_id('baidu_translate_input')
input_zoom.send_keys(s)
output_zoom=browser.find_element_by_xpath('//p[2]')
content=output_zoom.text
time.sleep(4)
print(content)
# browser.get_screenshot_as_file('./demo.png')
browser.quit()