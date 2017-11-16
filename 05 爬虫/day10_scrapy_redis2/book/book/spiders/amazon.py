# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
import re
import requests

class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    # start_urls = ['http://amazon.com/']
    redis_key = "amazon"

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='categoryRefinementsSection']/ul/li",)), follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//h2/../../a",)),callback="parse_book_detail"),
    )

    def parse_book_detail(self, response):
        item = {}
        item["book_cate"] = response.xpath("//div[@id='wayfinding-breadcrumbs_feature_div']/ul/li//text()").extract()
        item["book_name"] = response.xpath("//meta[@name='title']/@content").extract_first()
        if "Kindle电子书" in item["book_name"]:
            item["is_ebook"] = True
            item["ebook_price"] = response.xpath("//tr[@class='kindle-price']/td[2]/text()").extract_first()
            item["ebook_img"] = response.xpath("//div[@id='ebooks-img-canvas']/img/@src").extract_first()
        else:
            item["is_ebook"] = False
            item["book_price"] = response.xpath("//div[@id='soldByThirdParty']/span[2]/text()").extract_first()
            # item["book_img"] = response.xpath("//div[@id='img-canvas']/img/@src").extract_first()
        item["book_author"]= response.xpath("//span[@class='author notFaded']/a/text()").extract()
        # item["book_info_list"] = response.xpath("//td[@class='bucket']/div[@class='content']/ul/li//text()").extract()
        item["book_press"] = response.xpath("//td[@class='bucket']/div[@class='content']/ul/li/b[text()='出版社:']/../text()").extract_first()
        temp = re.findall(r"bookDescEncodedData = .*?\"(.*?)\",",response.body.decode(),re.S)
        if len(temp)>0:
            item["book_desc"] = requests.utils.unquote(temp[0])
        yield item
