# -*- coding: utf-8 -*-
import scrapy
import re
import time
import logging
from urllib import parse
from HousePrice.items import EsfItem

class EsfSpider(scrapy.Spider):
    name = 'esf'
    allowed_domains = ['http://esf.nanjing.fang.com/']
    start_urls = ['http://esf.nanjing.fang.com']

    def parse(self, response):
        logging.info("Getted Success!!")
        # 翻页
        for i in range(1, 101):  # 共有100页 每页30条
            get_url = "http://esf.nanjing.fang.com/house/i3{}/".format(i)
            logging.info("Getting page-{}".format(i))
            yield scrapy.Request(get_url, callback=self.parse_page, dont_filter=True)

    def parse_page(self, response):
        post_urls = response.css(".houseList .title > a::attr(href)").extract()
        for post_url in post_urls:
            yield scrapy.Request(url=parse.urljoin(response.url,post_url),callback=self.parse_details, dont_filter=True)

    def parse_details(self, response):
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
            school = "暂无"

        esf_item['zongjia'] = zongjia.strip()
        esf_item['tax'] = tax.strip()
        esf_item['huxing'] = huxing.strip()
        esf_item['mianji'] = mianji.strip()
        esf_item['danjia'] = danjia.strip()
        esf_item['chaoxiang'] = chaoxiang.strip()
        esf_item['louceng'] = louceng.strip()
        esf_item['zongcengshu'] = zongcengshu.strip()
        esf_item['zhuangxiu'] = zhuangxiu.strip()
        esf_item['xiaoqu'] = xiaoqu.strip()
        esf_item['quyu'] = quyu.strip()
        esf_item['school'] = school.strip()
#       esf_item[parse_time] = parse_time
        yield  esf_item
