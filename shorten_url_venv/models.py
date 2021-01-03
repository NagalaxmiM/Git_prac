from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import bitly_api


Base = declarative_base()      



class Shorten_url(Base):
    
    __tablename__='urls'
    id = Column(Integer, primary_key=True)
    url = Column(String(1024))
    short_url = Column(String(1024), unique = True)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url(self.url)
        #API_USER = "o_63vlrght6t"

    def generate_short_url(self, url):
        API_KEY = "2fa1d905646fe5aab2ef73b3e6338f8e7032eb12" 
        access = bitly_api.Connection(access_token = API_KEY)
        
        shortened_url = access.shorten(url)
        return shortened_url['url']
       
        
    
    