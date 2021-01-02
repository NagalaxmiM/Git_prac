from models import Base, Shorten_url
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import DATABASE_URI



engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind = engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
        
Base.metadata.create_all(engine)

def Shorten_url_exe(url):
    s = Session()
    short_url = Shorten_url(url=url)
    link = s.query.filter_by(short_url=short_url).first()
    while link:
        link = Shorten_url(url=url)
        link = s.query.filter_by(short_url=link).first()
    
    s.add(short_url)
    s.commit()
    
    
    


    
    
