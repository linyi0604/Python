# -*- coding: utf-8 -*-
import requests
import scrapy
from tieba.items import TiebaItem


class TiebaSpiderSpider(scrapy.Spider):
    name = 'tieba_spider'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw=%E7%8C%AB&lp=5011&lm=&pn=0']
    base_url = 'http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2'

    def parse(self, response):
        item = TiebaItem()
        div_list = response.xpath('//div[contains(@class,"i")]')
        for div in div_list:
            item['title']= div.xpath('./a/text()').extract_first()
            item['href'] = self.base_url + div.xpath('./a/@href').extract_first()
            item['img_list'] = []
            yield scrapy.Request(url=item['href'],callback=self.parse_detail,meta=item)
        next_page = response.xpath('//a[text()="下一页"]/@href').extract_first()
        if next_page is not None:
            next_page = self.base_url + next_page
            yield scrapy.Request(url=next_page,callback=self.parse)


    def parse_detail(self,response):
        item = response.meta
        item['img_list'] += [ requests.utils.unquote(p.extract().split('src=')[-1]) for p in response.xpath('//img[@class="BDE_Image"]/@src') ]
        next_page = response.xpath('//a[text()="下一页"]/@href').extract_first()
        if next_page is not None:
            next_page = self.base_url + next_page
            yield scrapy.Request(url=next_page, callback=self.parse_detail,meta=item)
        else :
            yield item



