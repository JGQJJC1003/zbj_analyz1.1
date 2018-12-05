# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZbjItem1(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    case_name = scrapy.Field()
    case_img = scrapy.Field()
    case_link = scrapy.Field()
    case_price = scrapy.Field()
    company_id = scrapy.Field()

class ZbjItem(scrapy.Item):
    content = scrapy.Field()
    user_name = scrapy.Field()
    user_case = scrapy.Field()
    price = scrapy.Field()
    comment_time = scrapy.Field()
    impression = scrapy.Field()
    company_id = scrapy.Field()