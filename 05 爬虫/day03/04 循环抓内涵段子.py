from time import time,sleep
import requests
from retrying import retry
import json
'''
循环抓取内涵段子

发现爬取内容大量重复，考虑用session 携带每一次的cookie
不携带cookie 对方认为我们是爬虫

并且把headers补充全面 伪装浏览器更真实

'''
class MySpider(object):
    def __init__(self):
        self.base_url = 'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time='
        self.next_time = time() #　获取当前时间戳
        self.url = self.update_url()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Host": "neihanshequ.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,ru;q=0.4,zh-TW;q=0.2"
        }
        self.session = requests.session()

    def update_url(self):
        return self.base_url + str(self.next_time)

    # 获取当前页面所有段子
    @retry(stop_max_attempt_number=3)   # 最多重连次数３
    def _parse_url(self):
        response = self.session.get(self.url,headers = self.headers,timeout=3)
        assert response.status_code == 200
        return response.content.decode()
    def parse_url(self):
        try:
            json_str = self._parse_url()
        except Exception as e:
            print(e)
            json_str = None
        return json_str

    # 传入抓取的json 获取关键参数 段子、下一页时间、是否有下一页
    def get_key_data(self,json_str):
        json_dict = json.loads(json_str)
        has_more = json_dict['data']['has_more']  # 是否有下一页标记
        next_time = json_dict['data']['max_time'] # 下一页的最大时间
        data_list = json_dict['data']['data']
        content_list = [data['group']['content'] for data in data_list ]
        return content_list,next_time,has_more

    def save(self,content_list):
        with open('neihan_keep.txt','a') as f:
            for content in content_list:
                f.write(str(content_list.index(content))+" "+content)
                f.write('\n')
            f.write('\n')


    def run(self):
        has_more = True
        while has_more == True:
            # 1 获取url 抓取内容
            response_str = self.parse_url()
            # 2 提取关键数据
            content_list, next_time, has_more = self.get_key_data(response_str)
            print(next_time,content_list)
            # 3 保存本地
            self.save(content_list)
            #4 循环操作
            self.next_time = next_time
            self.url = self.update_url()    #更新下一次时间
            sleep(2)




if __name__ == '__main__':
    spider = MySpider()
    spider.run()