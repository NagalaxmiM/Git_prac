from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from models import Base, Shorten_url
from contextlib import contextmanager


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
        
#def addData_post(url_dict):
    


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
if __name__=='__main__':
    recreate_database()
    
    
