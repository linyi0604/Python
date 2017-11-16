# -*- coding: utf-8 -*-
import scrapy
from book.items import BookItem
from copy import deepcopy
import re

class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['http://snbook.suning.com/web/trd-fl/999999/0.htm']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="ulwrap"]/li')
        for li in li_list:
            item = BookItem()
            item['b_cate'] = li.xpath('./div[1]/a/text()').extract_first()  # 大分类 名称
            a_list = li.xpath('./div[2]/a')
            for a in a_list:
                item['s_href'] = a.xpath("./@href").extract_first() # 小分类 链接
                item["s_cate"] = a.xpath('./text()').extract_first()    # 小分类名称
                if item["s_href"] is not None:
                    item["s_href"] = "http://snbook.suning.com"+item["s_href"]  # 补全链接
                    yield scrapy.Request(
                        url=item['s_href'],
                        callback=self.parse_book_list,
                        meta=deepcopy(item)
                    )


    def parse_book_list(self,response):
        item = response.meta    # 获取到保存数据的对象
        li_list = response.xpath('//div[@class="filtrate-books list-filtrate-books"]/ul/li')
        for li in li_list:
            item["book_img"] = li.xpath("./div[@class='book-img']//img/@src").extract_first()
            if item["book_img"] is None:  # 不是所有的图片都包含在src中 有的在src2 当中
                item["book_img"] = li.xpath("./div[@class='book-img']//img/@src2").extract_first()
            item['book_name'] = li.xpath('.//div[@class="book-title"]/a/@title').extract_first()    # 图书名称
            item['book_href'] = li.xpath('.//div[@class="book-title"]/a/@href').extract_first() # 图书链接
            item['book_author'] = li.xpath('.//div[@class="book-author"]/a/text()').extract_first() # 图书作者
            item['book_publish'] = li.xpath('.//div[@class="book-publish"]/a/text()').extract_first()   #出版社
            item["book_desc"] = li.xpath(".//div[contains(@class,'book-descrip')]/text()").extract_first()  #描述
            if item['book_href'] is not None:
                # 发送给下一个parse 去获取价格
                yield scrapy.Request(
                    url = item['book_href'],
                    callback = self.parse_book_detail,
                    meta = item
                )

        # 下一页 继续爬取数据 "http://snbook.suning.com/web/trd-fl/100301/46.htm?pageNumber="+pageNum+"&sort=0"
        html_str = response.body.decode()
        page_count = re.findall(r'var pagecount=(.*?);',html_str)[0]
        current_page = re.findall(r'var currentPage=(.*?);',html_str)[0]
        if current_page < page_count:
            next_url = response.url+"?pageNumber={}&sort=0".format( str(int(current_page)+1) )
            yield scrapy.Request(
                url = next_url ,
                callback= self.parse_book_list,
                meta = response.meta
            )



    # 获取图书价格
    def parse_book_detail(self,response):
        item = response.meta
        item['book_price'] = re.findall(r'\"bp\":\'(.*?)\',',response.body.decode())
        item['book_price'] = item['book_price'][0] if item['book_price'] else re.findall(r'\"bookPrice\":\'(.*?)\',',response.body.decode())[0]
        yield item
