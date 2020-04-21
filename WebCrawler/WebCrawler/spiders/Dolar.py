# -*- coding: utf-8 -*-
import scrapy
from WebCrawler.items import CotacoesDolarItem

class DolarSpider(scrapy.Spider):
    name = 'Dolar'
    allowed_domains = ['investing.com']
    start_urls = ['https://www.investing.com/currencies/usd-brl']

    def parse(self, response):
        blocoCotacao = response.css('#quotes_summary_current_data > div.left > div.inlineblock')
        spanSet = blocoCotacao.css('div.top > span')

        currency = spanSet[0].css('::text').get()
        value = spanSet[0].css('::text').get()
        chg = spanSet[1].css('::text').get()
        chgPercentual = spanSet[3].css('::text').get()
        timestamp = blocoCotacao.css('div.bottom > span')[1].css('::text').get()
        
        cotacaoDolarItem = CotacoesDolarItem(currency=currency,
            value=value,
            change=chg,
            perc=chgPercentual,
            timestamp=timestamp)

        yield cotacaoDolarItem