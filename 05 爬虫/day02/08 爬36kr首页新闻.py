import requests
import json

class MyNewsSpider(object):
    def __init__(self):
        self.url = url = 'http://36kr.com/api/biggie-word?_=1507384747097'


    def parse_url(self):
        response = requests.get(self.url)
        return response.content.decode()

    def get_news(self,json_str):
        json_dict = json.loads(json_str)
        temp = json.dumps(json_dict,ensure_ascii=False,indent=2)
        print(temp)


    def run(self):
        json_str = self.parse_url()
        self.get_news(json_str)


if __name__ == '__main__':
    spider = MyNewsSpider()
    spider.run()