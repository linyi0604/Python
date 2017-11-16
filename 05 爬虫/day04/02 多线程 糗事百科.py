from queue import Queue
import requests
from lxml import etree
from retrying import retry
import json
from threading import Thread
'''
利用多线程 实现糗事百科爬取段子
'''

class QiuSpider(object):
    def __init__(self):
        self.start_url = 'https://www.qiushibaike.com/8hr/page/{}/'
        self.base_url = 'https://www.qiushibaike.com'
        self.headers = {
            'Accept' : 'text / html, application / xhtml + xml, application / xml;',
            'Accept - Encoding': 'gzip, deflate, br',
            'Accept - Language': 'zh - CN, zh;',
            'Connection': 'keep - alive',
            'Host': 'www.qiushibaike.com',
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome .3163 .100 Safari / 537.36'
        }
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.data_list_queue = Queue()

    @retry(stop_max_attempt_number=3)
    def parse_url(self):
        while True:
            try:
                url = self.url_queue.get()
                response = requests.get(url=url,headers=self.headers,timeout=2)
                element = etree.HTML(response.content)
                self.html_queue.put(element)
                self.url_queue.task_done() # 引用计数减1
            except:
                pass

    def get_data_list(self):
        while True:
            element = self.html_queue.get()
            data_list = []
            div_list = element.xpath("//div[contains(@class,'article block untagged mb15 ')]")
            for div in div_list:
                data = {
                    'content':div.xpath('.//div[@class="content"]/span/text()')[0].replace('\n','') if div.xpath('.//div[@class="content"]/span/text()') else None,
                    'href': self.base_url+div.xpath('.//a[@class="contentHerf"]/@href')[0] if div.xpath('.//a[@class="contentHerf"]/@href') else None,
                    'pic_list': [ 'https:'+i for i in div.xpath('.//img/@src')] ,
                    'author': [i.replace('\n','') for i in div.xpath('.//a/h2/text()')],
                    'comment_list': [ i.xpath('./text()')[0].replace('\n','') for i in div.xpath('.//div[@class="main-text"]')]
                }

                data_list.append(data)
            self.data_list_queue.put(data_list)
            self.html_queue.task_done()

    def save(self):
        while True:
            data_list = self.data_list_queue.get()
            with open('./qiushi.txt','a') as f:
                for d in data_list:
                    f.write(json.dumps(d,ensure_ascii=False,indent=2))
            self.data_list_queue.task_done()


    def run(self):
        # 初始化爬取页面
        for i in range(1,14):
            self.url_queue.put(self.start_url.format(i))

        threads = []
        # 1 爬取页面
        for i in range(5):
            t=Thread(target=self.parse_url)
            threads.append(t)

        # 2 提取关键数据
        for i in range(3):
            t = Thread(target=self.get_data_list)
            threads.append(t)
        # 3 保存本地
        t = Thread(target=self.save)
        threads.append(t)

        for t in threads:
            t.setDaemon(True)  # 设置守护线程  主线程结束 子线程自动结束
            t.start()

        for i in [self.url_queue,self.html_queue,self.data_list_queue]:
            i.join()


if __name__ == '__main__':
    spider = QiuSpider()
    spider.run()