import requests
import re
'''
需要模拟浏览器发送cookies 的时候 
可以 传入参数 cookies字典
也可以在headers中加入cookie


'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #'Cookie':'anonymid=j8hatdp1-xq9t5n; depovince=BJ; jebecookies=1bac0a6a-f252-4a69-9174-5fb7a617500b|||||; _r01_=1; JSESSIONID=abcNpo3-zstHg6cNv027v; ick_login=dab76dce-4893-4846-b3e2-ea37f52cd48a; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=5da7009deea77717429ab4302872b07a9; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20170923/2100/main_S2vJ_10a800000de6195a.jpg; t=a56073826020b532430012cc440b109c9; societyguester=a56073826020b532430012cc440b109c9; id=327550029; xnsid=92b19bc; loginfrom=syshome; wp_fold=0'
}

cookie_string = 'anonymid=j8hatdp1-xq9t5n; depovince=BJ; jebecookies=1bac0a6a-f252-4a69-9174-5fb7a617500b|||||; _r01_=1; JSESSIONID=abcNpo3-zstHg6cNv027v; ick_login=dab76dce-4893-4846-b3e2-ea37f52cd48a; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=5da7009deea77717429ab4302872b07a9; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20170923/2100/main_S2vJ_10a800000de6195a.jpg; t=a56073826020b532430012cc440b109c9; societyguester=a56073826020b532430012cc440b109c9; id=327550029; xnsid=92b19bc; loginfrom=syshome; wp_fold=0'

cookies = { str.split('=')[0]:str.split('=')[1]  for str in cookie_string.split('; ') }
response = requests.get('http://www.renren.com/327550029/profile',cookies=cookies,headers=headers)


# 判断是否登录成功
ret = re.findall('毛兆军',response.content.decode())


print(ret)