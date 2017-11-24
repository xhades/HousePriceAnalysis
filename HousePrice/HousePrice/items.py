# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HousepriceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class EsfItem(scrapy.Item):
    zongjia = scrapy.Field()
    tax = scrapy.Field()
    huxing = scrapy.Field()
    mianji = scrapy.Field()
    danjia = scrapy.Field()
    chaoxiang = scrapy.Field()
    louceng = scrapy.Field()
    zongcengshu = scrapy.Field()
    zhuangxiu = scrapy.Field()
    xiaoqu = scrapy.Field()
    quyu = scrapy.Field()
    school = scrapy.Field()