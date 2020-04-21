from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings

Base = declarative_base()

def db_connect():
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    Base.metadata.create_all(engine)

class Dolar(Base):
    __tablename__ = "dolar"

    id = Column(Integer, primary_key=True)
    currency = Column('currency', Text())
    value = Column('value', Text())
    change = Column('change', Text())
    perc = Column('perc', Text())
    timestamp = Column('timestamp', Text())

class CotacaoIBovespa(Base):
    __tablename__ = "cotacaoIBovespa"

    id = Column(Integer, primary_key=True)
    name = Column('name', Text())
    last = Column('last', Text())
    high = Column('high', Text())
    low = Column('low', Text())
    chg = Column('chg', Text())
    chgPercentual = Column('chgPercentual', Text())
    vol = Column('vol', Text())
    time = Column('time', Text())

class CotacaoNasdaq(Base):
    __tablename__ = "cotacaoNasdaq"

    id = Column(Integer, primary_key=True)
    name = Column('name', Text())
    last = Column('last', Text())
    high = Column('high', Text())
    low = Column('low', Text())
    chg = Column('chg', Text())
    chgPercentual = Column('chgPercentual', Text())
    vol = Column('vol', Text())
    time = Column('time', Text())