# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CotacoesItem(scrapy.Item):
    name = scrapy.Field()
    last = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    chg = scrapy.Field()
    chgPercentual = scrapy.Field()
    vol = scrapy.Field()
    time = scrapy.Field()

class CotacoesDolarItem(scrapy.Item):
    currency = scrapy.Field()
    value = scrapy.Field()
    change = scrapy.Field()
    perc = scrapy.Field()
    timestamp = scrapy.Field()