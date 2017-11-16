# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']
    base_url = 'http://www.itcast.cn'


    def parse(self, response):
        li_list = response.xpath('//div[@class="tea_con"]//li')
        for li in li_list:
            data = {}
            data['name'] = li.xpath('.//h3/text()').extract_first()
            data['image'] = self.base_url + li.xpath('.//img/@data-original').extract_first()
            data['level'] = li.xpath('.//h4/text()').extract_first()
            data['content'] = li.xpath('.//p/text()').extract_first()
            yield data

