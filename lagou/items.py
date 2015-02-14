# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class JobItem(Item):
    # define the fields for your item here like:
    title = Field()
    company = Field()
    request = Field()
    desc = Field()
    respon = Field()
    link = Field()
    pass

class LagouItem(Item):
    title = Field()
    url = Field()
    salary = Field()
    location = Field()
    founded = Field()
    degree_require = Field()
    tag = Field()
    company = Field()
    business_field = Field()
    stage = Field() 
    size = Field()
    job_detail = Field()
    pass
