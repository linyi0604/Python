'''
import requests

class TiebaSpider(object):
    ''''''
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
    def get_url_list(self): #构造url list
        url_list = []
        for i in range(20):
            url_temp = "https://tieba.baidu.com/f?kw="+self.tieba_name+"&ie=utf-8&pn={}".format(i)
            url_list.append(url_temp)
        return url_list

    def parse_url(self,url): # 发送请求获取响应
        response = requests.get(url,headers=self.headers)
        return response.content.decode()

    def save_html(self,html_str,page_number):
        file_path = './html_page/' + self.tieba_name + "_第"+str(page_number)+"页" + ".html"
        with open(file_path,'w' ,encoding='utf-8' ) as f:
            f.write(html_str)
        print(file_path+'已保存')


    def run(self):
        # 1 找到url规律 构造utl list
        url_list = self.get_url_list()
        # 2 遍历utl list 发送请求 获取响应
        for url in url_list:
            # 3 提取html字符串
            html_str = self.parse_url(url)
            # 4 保存
            page_number = url_list.index(url)+1
            self.save_html(html_str=html_str,page_number=page_number)


if __name__ == '__main__':
    tieba_spider = TiebaSpider('李毅')
    tieba_spider.run()

'''
import requests

class MySpider(object):
    def __init__(self,url,name):
        self.url = url
        self.name = name
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }

    def get_url_list(self):
        url_list = []
        for i in range(50):
            temp_url = self.url + "?kw="+ self.name + "&pn="+str((i-1)*50)
            url_list.append(temp_url)
        return url_list

    def save_html(self,html_str,file_name):
        file_name = './html_page/' + self.name + file_name + '.html'
        with open(file_name , 'w' ,encoding='utf-8') as f:
            f.write(html_str)
        print(file_name+'已保存！')

    def parse_url(self,url):
        response = requests.get(url=url,headers=self.headers)
        return response.content.decode()

    def run(self):
        # 1 获取爬取网页列表
        url_list = self.get_url_list()
        # 2 训话爬取 获取网页
        for url in url_list:
            html_str = self.parse_url(url)
            # 3保存网页到本地文件
            self.save_html( html_str,str( url_list.index(url)+1 ) )

if __name__ == '__main__':
    spider = MySpider('http://tieba.baidu.com/','哈尔滨工业大学' )
    spider.run()