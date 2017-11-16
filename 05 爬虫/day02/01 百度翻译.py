import requests
import json
import sys
class Fanyi(object):
    def __init__(self,query_string):
        self.url = "http://fanyi.baidu.com/v2transapi"
        self.query_string = query_string
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
    def get_language(self):
        data = {
            'query':self.query_string
        }
        url = 'http://fanyi.baidu.com/langdetect/'
        response = requests.post(url=url,data=data)
        json_response = response.content.decode()   # 取得json
        dict_response = json.loads(json_response)   # json转换成字典
        language = dict_response['lan'] # 获取语言
        return language

    def get_data(self,language):
        data = {
            'query':self.query_string,
            'transtype':'realtime',
            'simple_means_flag':3
        }
        data['from'] = language
        data['to'] = 'zh'
        if language == 'zh':
            data['to'] = 'en'
        return data

    def parse_url(self,data):
        response = requests.post(url=self.url,data=data,headers=self.headers)
        return response.content.decode()

    def get_result(self,json_response):
        dict_response = json.loads(json_response) # json转换成字典
        ret = dict_response['trans_result']['data'][0]['dst']
        print(self.query_string+'  翻译为：  '+ ret )
        print('-'*50)
        return ret

    def run(self):
        # 1 获取语言类型
        langurage = self.get_language()
        # 2 生成翻译数据
        data = self.get_data(langurage)
        # 3 发起翻译请求 获得响应结果
        json_response = self.parse_url(data)
        # 4 提取翻译结果
        self.get_result(json_response)



if __name__ == '__main__':
    # print(sys.argv) #获取命令行输入
    while True:
        query_string = input('请输入查询的文字：')
        baidu_fanyi = Fanyi( query_string )
        baidu_fanyi.run()
