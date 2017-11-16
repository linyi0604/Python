import requests
from lxml import etree
from retrying import retry
import json
'''
循环爬取百度贴吧 手机 极速版
'''

class TiebaSpider(object):
    def __init__(self,name):
        self.url = 'http://tieba.baidu.com/mo/q---FA77541F561680C166FF4B9C2A85CA24%3AFG%3D1--1-3-0--2--wapp_1507619411320_819/m?kw={}'.format(name)
        self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
        self.base_url = 'http://tieba.baidu.com/mo/q---FA77541F561680C166FF4B9C2A85CA24%3AFG%3D1--1-3-0--2--wapp_1507619411320_819/'

    @retry(stop_max_attempt_number=3)
    def parse_url(self,url):
        try:
            response = requests.get(url=url,headers=self.headers,timeout=2)
            html_str = response.content
            return etree.HTML(html_str)
        except:
            return None

    def get_data_list(self,element):
        if element is None:
            return
        div_list = element.xpath('//div[@class="i"]')
        data_list = []
        for div in div_list:
            data={
                'title':div.xpath('./a/text()')[0].replace('\xa0','') if div.xpath('./a/text()') else None,
                'href': self.base_url + div.xpath('./a/@href')[0] if div.xpath('./a/@href') else None
            }
            data_list.append(data)
        next_url = self.base_url + element.xpath('//a[text()="下一页"]/@href')[0] if element.xpath('//a[text()="下一页"]/@href') else None
        print(next_url)
        return data_list,next_url

    def get_content_and_pictures(self,data_list):
        for data in data_list:
            element = self.parse_url(data['href'])
            div = element.xpath('//div[@class="d"]')[0]
            data['content'] = div.xpath('./div[@class="i"]/text()')[0]
            data['pic_list']= [ requests.utils.unquote(i.split('src=')[1]) for i in div.xpath("./div[@class='i']/a/@href") if i.startswith('http') ]

    def save(self,data_list):
        with open('./tieba.txt','a') as f:
            for d in data_list:
                f.write(json.dumps(d,ensure_ascii=False,indent=2))
                f.write('\n')

    def run(self):
        next_url = self.url
        while next_url is not None:
            # 1 获取 首页的url地址
            # 2发送请求获取响应
            element = self.parse_url(next_url)
            # 3 提取title href 下一页的urli地址
            data_list,next_url = self.get_data_list(element)
            # 4 发送帖子href的请求，获取帖子里面的图片
            self.get_content_and_pictures(data_list)
            # 5 保存到本地
            self.save(data_list)
            # 6 请求下一页url  循环
            



if __name__ == '__main__':
    spider = TiebaSpider( '哈尔滨工业大学' )
    spider.run()