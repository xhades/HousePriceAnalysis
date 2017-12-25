# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import csv, codecs


# 写入csv pipeline
class Write2CSVPipeline(object):
    def __init__(self, filename):
        self.filename = filename

    @classmethod
    def from_settings(cls, settings):
        filename = settings["FILE_SAVED"]

        return cls(filename)

    def process_item(self, item, spider):
        csvFile = open(self.filename, "a+", encoding="gbk")

        fieldnames = ['xiaoqu', 'quyu', 'louceng', 'chaoxiang', 'mianji', 'zongjia', 'danjia']
        data = {key: value for key, value in dict(item).items() if key in fieldnames}

        dict_writer = csv.DictWriter(csvFile,
                                     fieldnames)
        dict_writer.writerow(data)
        csvFile.close()
        return item

