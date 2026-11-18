from database import Base
from sqlalchemy import Column, String, Integer
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)