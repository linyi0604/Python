import requests
from retrying import retry
import re

'''
抓取内涵段子 首页上的所有段子

'''

class NeiHan:
    def __init__(self):
        self.url = 'http://neihanshequ.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }


    retry(stop_max_attempt_number = 3)  # 设置超时重新连接3次
    def _parse_url(self):
        response = requests.get(self.url,headers = self.headers,timeout = 3)
        assert response.status_code == 200 # 如果没有正常返回响应就抛出异常
        return response.content.decode()

    def parse_url(self):
        try:
            html = self._parse_url()
        except Exception as e:
            print(e)
            html = None
        return html

    def get_content_list(self,html_str):

        '''
        要抓取的局部：
        <div class="upload-txt  no-mb">
            <h1 class="title">
            <p>有一个盲了的女孩，她一无所有，只剩下她男朋友，男朋友问她，如果你眼睛好了，能和我结婚吗？女孩答应了。很快女孩可以移植眼角膜，也很快恢复视力，但她发现她男朋友也是盲的。男朋友向她求婚，女孩拒绝了，最后男孩直说了一句话:“take care of my eyes,”谁给我翻译下他说的什么话。</p>
            </h1>
        </div>
        '''
        content_list = re.findall( '<div class="upload-txt\s+no-mb">.*?<h1 class="title">.*?<p>(.*?)</p>.*?</h1>.*?</div>',html_str,re.DOTALL )
        print(content_list)
        return content_list

    def save_content_list(self,content_list):
        with open('./neihan.txt','w') as f:
            for content in content_list:
                f.write( str(content_list.index(content)+1) )
                f.write(" "+content)
                f.write('\n')

    def run(self):
        # 1 找到url
        # 2 发送请求 获取响应
        html_str = self.parse_url()
        # 3 提取数据
        content_list = self.get_content_list(html_str)
        # 4 保存
        self.save_content_list(content_list)


if __name__ == '__main__':
    spider = NeiHan()
    spider.run()