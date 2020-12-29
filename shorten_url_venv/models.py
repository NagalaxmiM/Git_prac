from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Shorten_url(Base):
    __tablename__='urls'
    id = Column(Integer, primay_key=True)
    url = Column(String, primary_key=True)
    short_url = Column(String)
    
    def __repr__(self):
        return "<Shorten_url('id' = {},'url'={},'short_url'={},'success'={True})>".format(self.id,self.url,self.short_url)