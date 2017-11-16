# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CsdnSpiderSpider(CrawlSpider):
    name = 'csdn_spider'
    allowed_domains = ['csdn.net']
    start_urls = ['http://blog.csdn.net/peoplelist.html?channelid=0&page=1']

    rules = (
        # 专家页列表翻页
        Rule(LinkExtractor(allow=r'http://blog\.csdn\.net/peoplelist\.html\?channelid=0&page=\d+$'), follow=True),
        # 进入专家的文章列表首页
        Rule(LinkExtractor(allow=r'http://blog\.csdn\.net/\w+$'), follow=True),
        # 专家文章列表翻页
        Rule(LinkExtractor(allow=r'/\w+?/article/list/=d+$'), follow=True),
        # 进入专家的文章页面
        Rule(LinkExtractor(allow=r'/\w+?/article/details/\d+$'), callback='parse_detail', follow=True),


    )

    def parse_detail(self, response):
        print(response.request.headers['User-Agent'])
        item = {}
        item["article_title"] = response.xpath("(//h1)[1]//text()").extract()
        item["author_name"] = response.xpath("//a[@class='user_name']/text()").extract_first()
        # item["article_content"] = response.xpath("//div[@id='article_content']/div[1]").extract()
        item["blog_rank"] = response.xpath("//ul[@id='blog_rank']/li[1]/span/text()").extract_first()
        yield item