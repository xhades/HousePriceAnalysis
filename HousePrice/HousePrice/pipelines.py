# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time


class HousepricePipeline(object):
    def process_item(self, item, spider):
        return item


class ErshoufangPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y-%m-%d', time.localtime())
        filename = today +"南京二手房房价.txt"
        with open(filename,'a',encoding='utf8') as fp:
            fp.write(item['quyu'] +'\t')
            fp.write(item['xiaoqu'] + '\t')
            fp.write(item['huxing'] + '\t')
            fp.write(item['mianji'] + '\t')
            fp.write(item['zhuangxiu'] + '\t')
            fp.write(item['chaoxiang'] + '\t')
            fp.write(item['louceng'] + '\t')
            fp.write(item['zongcengshu'] + '\t')
            fp.write(item['school'] + '\t')
            fp.write(item['tax'] + '\t')
            fp.write(item['danjia'] + '\t')
            fp.write(item['zongjia'] + '\n\n')
            time.sleep(1)

        # with open(filename, 'a') as fp:
        #     fp.write(esf_item['quyu'].encode('utf8') + '\t')
        #     fp.write(esf_item['xiaoqu'].encode('utf8') + '\t')
        #     fp.write(esf_item['huxing'].encode('utf8') + '\t')
        #     fp.write(esf_item['mianji'].encode('utf8') + '\t')
        #     fp.write(esf_item['zhuangxiu'].encode('utf8') + '\t')
        #     fp.write(esf_item['chaoxiang'].encode('utf8') + '\t')
        #     fp.write(esf_item['louceng'].encode('utf8') + '\t')
        #     fp.write(esf_item['zongcengshu'].encode('utf8') + '\t')
        #     fp.write(esf_item['school'].encode('utf8') + '\t')
        #     fp.write(esf_item['tax'].encode('utf8') + '\t')
        #     fp.write(esf_item['danjia'].encode('utf8') + '\t')
        #     fp.write(esf_item['zongjia'].encode('utf8') + '\n\n')
        #     time.sleep(1)
        return item

