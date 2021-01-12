from models import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind = engine)


Base.metadata.create_all(engine)

