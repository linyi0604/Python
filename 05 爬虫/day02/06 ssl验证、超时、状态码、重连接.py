import requests
from retrying import retry
'''
发送请求时候：
设置验证证书： verify = False  不验证
设置超时：  timeou = 10  设置10秒超时


重新连接： 用retry(stop_max_attempt_number=5) 设置最多连接5次


'''

# 12306网站的 sll 证书是没有经过验证的，所以 需要设置verify = False
url = 'https://www.12306.cn/mormhweb/'
proxies = {"https":"https:185.89.217.27:55080"}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
}

# 尝试3次连接后再抛异常
@retry(stop_max_attempt_number=3)
def _parse_url():
    response = requests.get(url,proxies=proxies,headers=headers,timeout=3,verify=False)
    assert response.status_code == 200
    print('连接成功！')


def parse_url():
    try:
        _parse_url()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    parse_url()