from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import string
Base = declarative_base()

class Shorten_url(Base):
    __tablename__='urls'
    id = Column(Integer, primary_key=True)
    url = Column(String(1024))
    short_url = Column(String(6), unique = True)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()

    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=3))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()
        
        return short_url
   
        #return "<Shorten_url('id' = {},'url'={},'short_url'={},'success'={True})>".format(self.id,self.url,self.short_url)