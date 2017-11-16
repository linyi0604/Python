import requests
from lxml import etree
import re

class TiebaSpider(object):
    def __init__(self,name):
        self.url = 'http://tieba.baidu.com/f?ie=utf-8&kw=' + name
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        }

    def parse_url(self):
        response = requests.get(url=self.url,headers=self.headers)
        html_str = response.content.decode()
        html_str = re.sub(r'<!--|-->|\n', '', html_str)
        return html_str

    def get_node_list(self,html_str):
        element = etree.HTML(html_str)
        element_list = element.xpath('//div[@class="col2_right j_threadlist_li_right "]')
        return element_list

    def get_data_list(self,element_list):
        data_list = []
        for element in element_list:
            data = {
                'title' : element.xpath('.//a/text()')[0] if element.xpath('.//a/text()') else None ,
                'url' : element.xpath('.//a/@href')[0] if element.xpath('.//a/@href') else None ,
                'content' : element.xpath('.//div[@class="threadlist_abs threadlist_abs_onlyline "]/text()')[0] if element.xpath('.//div[@class="threadlist_abs threadlist_abs_onlyline "]/text()') else None
            }
            data_list.append(data)
        return data_list

    def run(self):
        # 1 获取地址爬取内容
        html_str = self.parse_url()
        # 2 数据截取
        element_list = self.get_node_list(html_str)
        data_list = self.get_data_list(element_list)
        print(data_list)
        # 3 保存本地

        # 4 循环


if __name__ == '__main__':
    spider = TiebaSpider('哈尔滨工业大学')
    spider.run()