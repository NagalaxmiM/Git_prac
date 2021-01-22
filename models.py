from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import hashlib
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import DATABASE_URI
import string
from random import choices

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
        self.shortUrl = self.generateShortUrl(self.url)
       
    def generateShortUrl(self, url):
        s = Session()      
        url = self.url
        shortUrl = hashlib.sha1(url.encode()).hexdigest()[0:7]
        link = s.query(ShortenUrl).filter_by(shortUrl=shortUrl).first()
        
        while link!= None:
            characters = string.digits + string.ascii_letters
            adders = ''.join(choices(characters, k=3))
            url = self.url.encode()+adders.encode()
            shortUrl = hashlib.sha1(url).hexdigest()[0:7]
            link = s.query(ShortenUrl).filter_by(shortUrl=shortUrl).first()
            if link_!= None:
                url_list = list(url)
                random.shuffle(url_list)
                shuffled_url = ''.join(url_list)
                shortUrl = hashlib.sha1(shuffled_url.encode()).hexdigest()[0:7]
                link = s.query(ShortenUrl).filter_by(shortUrl=shortUrl).first()
        s.close()
        return shortUrl
        
    
    