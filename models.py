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


class Shorten_url(Base):
    
    __tablename__='urls'
    id = Column(Integer, primary_key=True)
    url = Column(String(1024))
    short_url = Column(String(1024), unique = True)
        
    def __init__(self, **kwargs):
        self.url = url
        self.short_url = self.generate_short_url(self.url)
       
    def generate_short_url(self, url):
        s = Session()      
        url = self.url
        short_url = hashlib.sha1(url.encode()).hexdigest()[0:7]
        link = s.query(Shorten_url).filter_by(short_url=short_url).first()
        
        while link!= None:
            characters = string.digits + string.ascii_letters
            adders = ''.join(choices(characters, k=3))
            url = self.url.encode()+adders.encode()
            short_url = hashlib.sha1(url).hexdigest()[0:7]
            link = s.query(Shorten_url).filter_by(short_url=short_url).first()
            if link_!= None:
                url_list = list(url)
                random.shuffle(url_list)
                shuffled_url = ''.join(url_list)
                short_url = hashlib.sha1(shuffled_url.encode()).hexdigest()[0:7]
                link = s.query(Shorten_url).filter_by(short_url=short_url).first()
        s.close()
        return short_url
        
    
    