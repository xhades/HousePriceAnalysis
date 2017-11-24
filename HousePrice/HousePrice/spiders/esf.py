# -*- coding: utf-8 -*-
import scrapy
import re
import time
from scrapy.http import Request
from urllib import parse
from HousePrice.items import EsfItem

class EsfSpider(scrapy.Spider):
    name = 'esf'
    allowed_domains = ['http://nanjing.fang.com/']
    start_urls = ['http://esf.nanjing.fang.com']

    def parse(self, response):
        post_urls = response.css(".houseList .title > a::attr(href)").extract()
        for post_url in post_urls:
            yield Request(url=parse.urljoin(response.url,post_url),callback=self.parse_details)

        next_url = response.css("#PageControl1_hlk_next::attr(href)").extract_first()
        if next_url:
            yield Request(url=parse.urljoin(response.url,post_url),callback=self.parse)

    def parse_details(self, response):
    # def parse(self,response):
        esf_item = EsfItem()

        parse_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        price1 = response.css("div.trl-item:nth-child(1) > i:nth-child(1)::text").extract_first()
        jldw = response.css("div.trl-item:nth-child(1)::text").extract_first()
        zongjia = price1+jldw
        tax =  response.css(".bqian > span:nth-child(1)::text").extract_first("")
        huxing = response.css("div.tr-line:nth-child(3) > div:nth-child(1) > div:nth-child(1)::text").extract_first().strip()
        mianji = response.css("div.tr-line:nth-child(3) > div:nth-child(2) > div:nth-child(1)::text").extract_first().strip()
        danjia = response.css("div.tr-line:nth-child(3) > div:nth-child(3) > div:nth-child(1)::text").extract_first().strip()
        chaoxiang = response.css("div.tr-line:nth-child(4) > div:nth-child(1) > div:nth-child(1)::text").extract_first().strip()
        louceng = response.css("div.tr-line:nth-child(4) > div:nth-child(2) > div:nth-child(1)::text").extract_first().strip()
        zongcengshu =response.css("div.tr-line:nth-child(4) > div:nth-child(2) > div:nth-child(2)::text").extract_first().strip()
        match_re = re.match(".*?(\d+).*",zongcengshu)
        if match_re:
            zongcengshu = match_re.group(1)
        zhuangxiu = response.css("div.tr-line:nth-child(4) > div:nth-child(3) > div:nth-child(1)::text").extract_first().strip()
        xiaoqu = response.css("#agantesfxq_C03_05::text").extract_first().strip()
        area1 = response.css("#agantesfxq_C03_07::text").extract_first().strip()
        area2 = response.css("#agantesfxq_C03_08::text").extract_first().strip()
        quyu = area1+area2
        school = response.css("#agantesfxq_C03_09::text").extract_first()
        if school:
            school = school
        else:
            school = ""

        esf_item['zongjia'] = zongjia
        esf_item['tax'] = tax
        esf_item['huxing'] = huxing
        esf_item['mianji'] = mianji
        esf_item['danjia'] = danjia
        esf_item['chaoxiang'] = chaoxiang
        esf_item['louceng'] = louceng
        esf_item['zongcengshu'] = zongcengshu
        esf_item['zhuangxiu'] = zhuangxiu
        esf_item['xiaoqu'] = xiaoqu
        esf_item['quyu'] = quyu
        esf_item['school'] = school
#       esf_item[parse_time] = parse_time
        yield  esf_item
        pass