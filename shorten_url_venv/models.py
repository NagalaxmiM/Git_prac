from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import bitlyapi


Base = declarative_base()      



class Shorten_url(Base):
    
    __tablename__='urls'
    id = Column(Integer, primary_key=True)
    url = Column(String(1024))
    short_url = Column(String(6), unique = True)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        API_USER = "nagalaxmim"
        API_KEY = "68c406d2d411218d2d18ea39f1a3bd3cfce520bf" 
        access = bitlyapi.BitLy(API_USER,API_KEY)
        
        shortened_url = access.shorten(longurl = self.url)
        self.short_url = shortened_url['url']
       
        
    
    