# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HospitalgoItem(scrapy.Item):
    # name 姓名
    name = scrapy.Field()
    # department 部门
    department = scrapy.Field()
    # Hospital level 医院等级
    # Hospital_level = scrapy.Field()
    # pro_title 医院名称
    pro_title = scrapy.Field()
    # resume 简历
    resume = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
