# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import json

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com',"3.cn"]
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath("//div[@class='mc']/dl/dt")
        for dt in dt_list:
            item = {}
            item["b_cate"] = dt.xpath("./a/text()").extract_first()
            em_list = dt.xpath("./following-sibling::*[1]/em")
            for em in em_list:
                item["s_cate"] = em.xpath("./a/text()").extract_first()
                item["s_href"] = em.xpath("./a/@href").extract_first()
                if item["s_href"] is not None:
                    item["s_href"] = "https:" + item["s_href"]
                    yield scrapy.Request(
                        item["s_href"],
                        callback=self.parse_book_list,
                        meta={"item": deepcopy(item)}
                    )

    def parse_book_list(self, response):
        item = response.meta["item"]
        li_list = response.xpath("//ul[@class='gl-warp clearfix']/li")
        for li in li_list:
            item["book_img"] = li.xpath(".//div[@class='p-img']//img/@src").extract_first()
            item["book_name"] = li.xpath(".//div[@class='p-name']//em/text()").extract_first()
            # item["book_desc"] = li.xpath(".//div[@class='p-name']/a/@title").extract()
            item["book_author"] = li.xpath(".//span[@class='p-bi-name']/span/a/@title").extract()
            item["book_press"] = li.xpath(".//span[@class='p-bi-store']/a/@title").extract_first()
            item["book_sku"] = li.xpath("./div/@data-sku").extract_first()
            if item["book_sku"] is not None:
                comment_url = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds={}".format(item["book_sku"])
                yield  scrapy.Request(
                    comment_url,
                    callback=self.parse_book_comments,
                    meta = {"item":deepcopy(item)}
                )
        #发送列表页的下一页的url地址的请求
        next_url = response.xpath("//a[@class='pn-next']").extract_first()
        if next_url is not None:
            next_url = "https://list.jd.com" +next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse_book_list,
                meta = {"item":deepcopy(response.meta["item"])}
            )

    def parse_book_comments(self,response):
        item = response.meta["item"]
        item["book_comments"] = json.loads(response.text)
        price_url = "https://p.3.cn/prices/get?skuid=J_{}".format(item["book_sku"])
        yield scrapy.Request(
            price_url,
            callback=self.parse_book_price,
            meta = {"item":deepcopy(item)}
        )

    def parse_book_price(self,response):
        item = response.meta["item"]
        item["book_price"] = json.loads(response.body.decode())
        print(item)