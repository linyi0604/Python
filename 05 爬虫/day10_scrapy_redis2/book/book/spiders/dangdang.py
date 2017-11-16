# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from copy import  deepcopy


class DangdangSpider(RedisSpider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    # start_urls = ['http://dangdang.com/']
    redis_key = "dangdang:start_url"

    def parse(self, response):
        div_list = response.xpath("//div[@class='con flq_body']/div")[1:]
        for div in div_list:
            item = {}
            item["b_cate"] = div.xpath("./dl/dt//text()").extract()
            dl_list = div.xpath("./div//dl[@class='inner_dl']")
            for dl in dl_list:
                item["m_cate"] = dl.xpath("./dt/a/@title").extract_first()
                a_list = dl.xpath("./dd/a")
                for a in a_list:
                    item["s_cate"] = a.xpath("./@title").extract_first()
                    item["s_cate_href"] = a.xpath("./@href").extract_first()
                    if item["s_cate_href"] is not None:
                        yield scrapy.Request(
                            item["s_cate_href"],
                            callback = self.parse_book_list,
                            meta = {"item":deepcopy(item)}
                        )

    def parse_book_list(self,resposne):
        item = resposne.meta["item"]
        li_list = resposne.xpath("//ul[@class='bigimg']/li")
        for li in li_list:
            item["book_title"] = li.xpath("./a/@title").extract_first()
            item["book_desc"] = li.xpath("./p[@class='detail']/text()").extract_first()
            item["book_price"] = li.xpath(".//span[@class='search_now_price']/text()").extract_first()
            item["book_pre_price"] = li.xpath(".//span[@class='search_pre_price']/text()").extract_first()
            item["book_comment_num"] = li.xpath("./p[@class='search_star_line']/a/text()").extract_first()
            item["book_press"] = li.xpath("./p[@class='search_book_author']/span[last()]/a/text()").extract_first()
            yield item


