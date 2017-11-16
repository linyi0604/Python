# -*- coding: utf-8 -*-
import scrapy


class PositionSpider(scrapy.Spider):
    name = 'position'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']
    base_url = 'http://hr.tencent.com/'
    def parse(self, response):
        tr_list = response.xpath('//table[@class="tablelist"]/tr[@class="odd"]|//table[@class="tablelist"]/tr[@class="even"]')
        for tr in tr_list:
            data = {}
            data['title'] = tr.xpath('./td[1]/a/text()').extract_first()
            data['position'] = tr.xpath('./td[2]/text()').extract_first()
            data['number'] = tr.xpath('./td[3]/text()').extract_first()
            data['location'] = tr.xpath('./td[4]/text()').extract_first()
            data['time'] = tr.xpath('./td[5]/text()').extract_first()
            data['href'] = self.base_url + tr.xpath('./td[1]/a/@href').extract_first()
            yield data


        # 下一页地址 继续爬取
        next_page = tr_list.xpath('//a[@id="next"]/@href').extract_first()
        if next_page != 'javascript:;' :
            next_page = self.base_url + next_page
            yield scrapy.Request(url=next_page,callback=self.parse)