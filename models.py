from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import hashlib
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import DATABASE_URI
import string
from random import choices
from urllib.parse import urlencode

Base = declarative_base()      

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)


class ShortenUrl(Base):
    
    __tablename__='urls'
    id = Column(Integer, primary_key=True)
    url = Column(String(1024))
    shortUrl = Column(String(1024), unique = True)
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shortUrl = self.generate_shortUrl(self.url)
       
    def generate_shortUrl(self, url):
        s = Session()      
        url = self.url
        shortUrl = "http://"+hashlib.sha1(url.encode()).hexdigest()[0:7]
        link = s.query(ShortenUrl).filter_by(shortUrl=shortUrl).first()
        
        while link!= None:
            characters = string.digits + string.ascii_letters
            adders = ''.join(choices(characters, k=3))
            url = self.url.encode()+adders.encode()
            shortUrl = "http://"+hashlib.sha1(url).hexdigest()[0:7]
            link = s.query(ShortenUrl).filter_by(shortUrl=shortUrl).first()
            if link_!= None:
                url_list = list(url)
                random.shuffle(url_list)
                shuffledUrl = ''.join(url_list)
                shortUrl = "http://"+hashlib.sha1(shuffledUrl.encode()).hexdigest()[0:7]
                link = s.query(ShortenUrl).filter_by(shortUrl=shortUrl).first()
        s.close()
        return shortUrl
        
    
    