# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    b_cate = scrapy.Field()  #大分类
    s_cate = scrapy.Field()  #小分类
    s_href = scrapy.Field()  #小分类的url地址
    book_name = scrapy.Field()
    book_author = scrapy.Field()
    book_price = scrapy.Field()
    book_desc = scrapy.Field()
    book_publish = scrapy.Field()  #出版社
    book_img = scrapy.Field()
    book_href = scrapy.Field()
    book_list_href = scrapy.Field()
