# -*- coding: utf-8 -*-
import scrapy
from WebCrawler.items import CotacoesItem

class NasdaqSpider(scrapy.Spider):
    name = 'Nasdaq'
    allowed_domains = ['investing.com']
    start_urls = ['https://www.investing.com/equities/StocksFilter?index_id=20']

    def parse(self, response):
        for linhaGrid in response.css('#cross_rate_markets_stocks_1 > tbody > tr'):
            colunaGridSet = linhaGrid.css('td')

            name = colunaGridSet[1].css('a::text').get()
            last = colunaGridSet[2].css('::text').get()
            high = colunaGridSet[3].css('::text').get()
            low = colunaGridSet[4].css('::text').get()
            chg = colunaGridSet[5].css('::text').get()
            chgPercentual = colunaGridSet[6].css('::text').get()
            vol = colunaGridSet[7].css('::text').get()
            time = colunaGridSet[8].css('::text').get()

            cotacaoItem = CotacoesItem(           
                name=name,
                last=last,
                high=high,
                low=low,
                chg=chg,
                chgPercentual=chgPercentual,
                vol=vol,
                time=time)

            yield cotacaoItem
