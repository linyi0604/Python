from selenium import webdriver
import json
import time
'''
爬取渲染后的斗鱼所有房间信息
'''

class DouyuSpider(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://www.douyu.com/directory/all'

    def get_data_list(self):
        li_list = self.driver.find_elements_by_xpath('//div[@id="live-list-content"]/ul/li')
        data_list = []
        for li in li_list:
            data = {}
            data['title'] = li.find_element_by_xpath('.//h3[@class="ellipsis"]').text
            data['anchor'] = li.find_element_by_xpath('.//span[@class="dy-name ellipsis fl"]').text
            data['image'] = li.find_element_by_xpath('.//span[@class="imgbox"]/img').get_attribute('src')
            data['category'] = li.find_element_by_xpath('.//span[@class="tag ellipsis"]').text
            data_list.append(data)
        return data_list

    def save(self,data_list):
        with open('douyu.txt','a') as f:
            for d in data_list:
                f.write( json.dumps(d,ensure_ascii=False,indent=2) )
        print('保存成功')

    def __del__(self):
        self.driver.close()

    def run(self):
        # 请求网页
        self.driver.get(self.url)
        # 获取数据
        data_list = self.get_data_list()
        # 保存本地
        self.save(data_list)
        # 翻页继续
        while True:
            try:
                self.driver.find_element_by_xpath('//a[@class="shark-pager-next"]').click()
                time.sleep(5)
                # 获取数据
                data_list = self.get_data_list()
                # 保存本地
                self.save(data_list)
                # 翻页继续
            except:
                break



if __name__ == '__main__':
    spider = DouyuSpider()
    spider.run()