from selenium import webdriver
import time
# 获取一个Chrome的驱动
driver = webdriver.PhantomJS()
'''
发送请求
'''
driver.get('http://www.baidu.com/')
driver.save_screenshot('./phantom.png')
html_string = driver.page_source

print(html_string)

# 退出当前页面
driver.close()
# 退出浏览器
driver.quit()

