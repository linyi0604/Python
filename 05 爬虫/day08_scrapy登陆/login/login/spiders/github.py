# -*- coding: utf-8 -*-
import scrapy
import re

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
        authenticity_token = response.xpath("//input[@name = 'authenticity_token']/@value").extract_first()

        # 方法1 利用FormRequest方法 将发送post请求的数据携带
        # yield scrapy.FormRequest(
        #     url="https://github.com/session",
        #     formdata={
        #         'commit':commit,
        #         'utf8':utf8,
        #         'authenticity_token':authenticity_token,
        #         'login' : "noobpythoner",
        #         'password' : "zhoudawei123"
        #     },
        #     callback=self.parse_login
        #
        # )

        # 方法2 利用FormRequest.from_response 方法自动寻找form表单帮助我们提交
        yield scrapy.FormRequest.from_response(
            response=response,
            formdata={
                'login' : "noobpythoner",
                'password' : "zhoudawei123"
            },
            callback=self.parse_login
        )

    def parse_login(self,response):
        print(re.findall("noobpythoner|NoobPythoner", response.body.decode()))
