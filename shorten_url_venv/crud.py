from models import Base
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

