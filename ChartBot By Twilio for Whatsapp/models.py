from sqlalchemy import create_engine, Column, Integer,String
from  sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
import decouple

url = URL.create(drivername="postgresql", username="postgres",password="1234", host="localhost", port=5432)

engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Conversation(Base):
    __tablename__ = 'conversations'
    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String)
    message = Column(String)
    response = Column(String)

Base.metadata.create_all(engine)

