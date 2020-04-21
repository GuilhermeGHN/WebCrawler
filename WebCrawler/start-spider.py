from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from WebCrawler.spiders.Dolar import DolarSpider
from WebCrawler.spiders.iBovespa import IbovespaSpider
from WebCrawler.spiders.Nasdaq import NasdaqSpider
  
process = CrawlerProcess(get_project_settings())
process.crawl(DolarSpider)
process.crawl(IbovespaSpider)
process.crawl(NasdaqSpider)
process.start()