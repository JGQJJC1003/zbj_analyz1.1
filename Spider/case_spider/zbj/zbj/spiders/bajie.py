# -*- coding: utf-8 -*-
import scrapy

from zbj.items import ZbjItem
class BajieSpider(scrapy.Spider):
    name = 'bajie'
    allowed_domains = []
    start_urls = ['https://www.zbj.com/anli/']

    def parse(self, response):
        url_list = response.xpath('//div[@class="channel"]//li/a/@href').extract()
        for url in url_list:
            yield scrapy.Request(url=url,callback=self.parse_next,meta={})

    def parse_next(self,response):
        num = response.xpath('//p[@class="pagination-total"]/text()')[0].extract()
        num = int(num[1:-2])
        url = response.url
        page = 1

        while page < num:
            url1 = url[:-5] + 'k' + str((page-1)*60) + url[-5:]
            page += 1
            yield scrapy.Request(url=url1,callback=self.parse_next2)

            # print('*' * 50)
            # print(url1)
            # print(num)
            # print('*' * 50)

    def parse_next2(self,response):
        li_list = response.xpath('.//div[@class="search-case-wrap"]//li')
        for oli in li_list:
            case_name = oli.xpath('.//a[@class="serivce-desc-title"]/span/@title')[0].extract()
            img = oli.xpath('./a/img/@data-original')[0].extract()
            if img[0:5]=='https':
                case_img = img
            else:
                case_img ='https:'+img
            case_price = oli.xpath('.//span[@class="price"]/text()')[0].extract().strip('\n \t￥')
            link = oli.xpath('.//a[@class="item-img"]/@href')[0].extract()
            case_link = 'https:'+link
            company_id = oli.xpath('.//a[@class="shop-desc-box"]/@href')[0].extract().split('/')[-2]
            # print('*' * 50)
            # print(case_name)
            # print(case_img)
            # print(case_price)
            # print(company_id)
            # print(case_link)
            # print('*' * 50)
            item = ZbjItem()
            for field in item.fields.keys():
                item[field]=eval(field)

            yield item

