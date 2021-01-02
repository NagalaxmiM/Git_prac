from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import string

from random import choices
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
        #link = self.query.filter_by(short_url=self.short_url).first()
        
        #self.add(short_url)
        #self.commit()
        return short_url
    
    