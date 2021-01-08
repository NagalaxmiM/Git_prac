from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import hashlib

Base = declarative_base()      

class Shorten_url(Base):
    
    __tablename__='urls'
    id = Column(Integer, primary_key=True)
    url = Column(String(1024))
    short_url = Column(String(1024), unique = True)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url(self.url)

    def generate_short_url(self, url):
        
        short_url = hashlib.sha1(self.url.encode()).hexdigest()
        link = self.query.filter_by(short_url=short_url).first()
        
        if link:
            return self.generate_short_url(self, url)
        
    
    