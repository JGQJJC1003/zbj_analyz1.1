# -*- coding: utf-8 -*-
import scrapy

from zbj.items import ZbjItem
class BajieSpider(scrapy.Spider):
    name = 'cbajie'
    allowed_domains = []
    start_urls = ['https://www.zbj.com/']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="main-content clearfix"]/li')
        # 拿到首页的url，生成请求对象
        for i in range(1,3):
            url_list = li_list[i].xpath('.//div[@class="cate-item"]//a/@href').extract()
            for url in url_list:
                yield scrapy.Request(url=url,callback=self.parse_next,meta={})


    # https://shop.zbj.com/evaluation/evallist-uid-18168939-type-1-page-2.html
    # https://shop.zbj.com/evaluation/evallist-uid-18168939-type-3-page-2.html
    def parse_next(self,response):
        # 拿到shop_id以及type，用来拼接ajax接口的url
        shop_id = response.xpath('//div[@class="item-wrap j-sp-item-wrap"]/@data-shop-id').extract()
        for id in shop_id:
            for i in range(1,4):
                url = 'https://shop.zbj.com/evaluation/evallist-uid-{}-type-{}-page-1.html'
                url = url.format(id,i)
                # print('#'*50)
                # print(url)
                yield scrapy.Request(url=url,callback=self.parse_next2,meta={'id':id,'type':i})

    def parse_next2(self,response):

        id = response.meta['id']
        type = response.meta['type']
        # 每一个url的最大页数
        num = response.xpath('//li/a/text()').extract()
        try:
            page = 1
            num =int(num[-2])
            while page <= num:
                # 拼接url
                url = 'https://shop.zbj.com/evaluation/evallist-uid-{}-type-{}-page-{}.html'
                url = url.format(id,type,page)
                page += 1
                yield scrapy.Request(url=url, callback=self.parse_next3)
        except Exception as e:
            pass

    # 解析ajax接口函数
    def parse_next3(self,response):
        dl_list = response.xpath('//div[@id="userlist"]//dl')
        for odl in dl_list:
            user_name = odl.xpath('.//p[@class="name-tit"]/text()')[0].extract()
            price = odl.xpath('.//p[@class="name-tit"]/text()')[1].extract().strip('\n \t').split('：')[-1]
            comment_time = odl.xpath('.//dd[@class="mint"]/p/text()')[0].extract()
            content = odl.xpath('//span[@class="gray3"]/text()')[0].extract()
            company_ids = odl.xpath('//p[@class="name-tit"]/a/@href')[0].extract()
            company_idt = company_ids.split('/')
            company_id = company_idt[-2]
            try:
                user_case = odl.xpath('.//a/img/@src')[0].extract()
                user_case = 'https:'+user_case
            except:
                user_case = odl.xpath('.//p[@class="name-tit"]/a/text()')[0].extract().strip('\n \t')

            try:
                impressions =odl.xpath('.//p[@class="yingx"]//u/text()').extract()
                if impressions:
                    impression = ','.join(impressions)
                else:
                    impression = '无'
            except:
                print(1)
            finally:
                item = ZbjItem()
                for field in item.fields.keys():
                    item[field]=eval(field)

                yield item
