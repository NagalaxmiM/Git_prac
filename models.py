from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import hashlib
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import DATABASE_URI

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
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url(self.url)
       
    def generate_short_url(self, url):
        s = Session()
        short_url = hashlib.sha1(self.url.encode()).hexdigest().......
        link = s.query(Shorten_url).filter_by(short_url=short_url).first()
        
        if link:
            s.close()
            return self.generate_short_url(self, url)
        s.close()
        return short_url
    
    