# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from WebCrawler.models import Dolar, CotacaoIBovespa, CotacaoNasdaq, db_connect, create_table
from decimal import Decimal

class DolarPipeline(object):

    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        if spider.name != 'Dolar':
            return item

        session = self.Session()
        dolar = Dolar()
        dolar.currency = item["currency"]
        dolar.value = item["value"]
        dolar.change = item["change"]
        dolar.perc = item["perc"]
        dolar.timestamp = item["timestamp"]

        try:
            session.add(dolar)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item

class IbovespaPipeline(object):

    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        if spider.name != 'iBovespa':
            return item

        session = self.Session()
        cotacaoIBovespa = CotacaoIBovespa()
        cotacaoIBovespa.name = item['name']
        cotacaoIBovespa.last = item['last']
        cotacaoIBovespa.high = item['high']
        cotacaoIBovespa.low = item['low']
        cotacaoIBovespa.chg = item['chg']
        cotacaoIBovespa.chgPercentual = item['chgPercentual']
        cotacaoIBovespa.vol = item['vol']
        cotacaoIBovespa.time = item['time']

        try:
            session.add(cotacaoIBovespa)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item

class NasdaqPipeline(object):

    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        if spider.name != 'Nasdaq':
            return item

        session = self.Session()

        dolarMax = session.query(Dolar).order_by(Dolar.id.desc()).first()

        cotacaoNasdaq = CotacaoNasdaq()
        cotacaoNasdaq.name = item['name']
        cotacaoNasdaq.last = str(Decimal(item['last']) * Decimal(dolarMax.currency))
        cotacaoNasdaq.high = str(Decimal(item['high']) * Decimal(dolarMax.currency))
        cotacaoNasdaq.low = str(Decimal(item['low']) * Decimal(dolarMax.currency))
        cotacaoNasdaq.chg = item['chg']
        cotacaoNasdaq.chgPercentual = item['chgPercentual']
        cotacaoNasdaq.vol = item['vol']
        cotacaoNasdaq.time = item['time']

        try:
            session.add(cotacaoNasdaq)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item
