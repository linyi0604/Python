# -*- coding: utf-8 -*-
import scrapy
import re

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/436281038/profile']

    # 携带cookie进行访问首页
    def parse(self, response):
        cookies = "anonymid=j8vim6hf-drzm1p; depovince=HLJ; _r01_=1; JSESSIONID=abcO45eKI8gd49TCJdQ8v; _de=F2D09237A1B9369BA5CC9EE82B6DB042; ick_login=4f01cb0b-160c-4822-8ccd-65cd0e96f6f1; t=543c432333607770efd13c6edb323dd78; societyguester=543c432333607770efd13c6edb323dd78; id=436281038; xnsid=d5f0c7d5; jebecookies=1d060041-235a-4ebf-90d4-e9381cbe7487|||||; ver=7.0; loginfrom=null; springskin=set; vip=1; wp_fold=0"
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse_login,
                cookies={ i.split('=')[0]:i.split('=')[-1] for i in cookies.split('; ')  }
            )

    # 检验是否登陆成功
    def parse_login(self,response):
        # print(re.findall(r'林奕',response.body.decode()) )
        cookies = "anonymid=j8vim6hf-drzm1p; depovince=HLJ; _r01_=1; JSESSIONID=abcO45eKI8gd49TCJdQ8v; _de=F2D09237A1B9369BA5CC9EE82B6DB042; ick_login=4f01cb0b-160c-4822-8ccd-65cd0e96f6f1; t=543c432333607770efd13c6edb323dd78; societyguester=543c432333607770efd13c6edb323dd78; id=436281038; xnsid=d5f0c7d5; jebecookies=1d060041-235a-4ebf-90d4-e9381cbe7487|||||; ver=7.0; loginfrom=null; springskin=set; vip=1; wp_fold=0"
        for url in self.start_urls:
            yield scrapy.Request(
                url="http://friend.renren.com/managefriends",
                callback=self.parse_temp,
                cookies={i.split('=')[0]: i.split('=')[-1] for i in cookies.split('; ')}
            )
    # 加入的cookie 会贯穿整个爬虫当中,
    def parse_temp(self,response):
        print(re.findall(r'林奕', response.body.decode()))