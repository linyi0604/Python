from selenium import webdriver
import time
# 获取一个Chrome的驱动
driver = webdriver.Chrome()
'''
发送请求
'''
driver.get('http://www.baidu.com/')

# 设置打开窗口的大小
driver.set_window_size(1024,768)

'''
获取页面内容的常用方式
'''
# 获取元素并输入内容
driver.find_element_by_id('kw').send_keys('苹果')
# 获取元素并点击
driver.find_element_by_id('su').click()
# 利用xpath获取
# div_list = driver.find_element_by_xpath('//div')
#利用页面内容
# next_page = driver.find_element_by_link_text('下一页').get_attribute('href')

# 将浏览器页面截图保存本地
driver.save_screenshot('./百度.png')

# 获得浏览器的页面源码（经过渲染之后)
html = driver.page_source

print('*'*50)

# 获取页面的cookies
cookie_list = driver.get_cookies()
# cookie 转换成字典
cookies = { dict['name']:dict['value'] for dict in cookie_list }
print(cookies)


# 退出当前页面
driver.close()
# 退出浏览器
driver.quit()

